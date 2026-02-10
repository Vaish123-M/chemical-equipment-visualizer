import sys
from pathlib import Path

import requests
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5.QtCore import Qt, QSettings
from PyQt5.QtWidgets import (
    QApplication,
    QFileDialog,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QListWidget,
    QListWidgetItem,
    QMessageBox,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chemical Equipment Visualizer")
        self.settings = QSettings("ChemicalVisualizer", "DesktopApp")

        self.api_input = QLineEdit(self.settings.value("api_base", "http://127.0.0.1:8000"))
        self.token_input = QLineEdit(self.settings.value("api_token", ""))
        self.token_input.setEchoMode(QLineEdit.Password)

        self.upload_button = QPushButton("Upload CSV")
        self.refresh_button = QPushButton("Refresh History")
        self.status_label = QLabel("Ready")

        self.history_list = QListWidget()
        self.history_list.setMinimumWidth(240)

        self.summary_group = QGroupBox("Summary")
        self.count_label = QLabel("Total count: -")
        self.flowrate_label = QLabel("Avg flowrate: -")
        self.pressure_label = QLabel("Avg pressure: -")
        self.temperature_label = QLabel("Avg temperature: -")

        summary_layout = QVBoxLayout()
        summary_layout.addWidget(self.count_label)
        summary_layout.addWidget(self.flowrate_label)
        summary_layout.addWidget(self.pressure_label)
        summary_layout.addWidget(self.temperature_label)
        self.summary_group.setLayout(summary_layout)

        self.distribution_table = QTableWidget(0, 2)
        self.distribution_table.setHorizontalHeaderLabels(["Type", "Count"])
        self.distribution_table.horizontalHeader().setStretchLastSection(True)

        self.figure = Figure(figsize=(6, 4))
        self.canvas = FigureCanvas(self.figure)

        self._build_layout()
        self._connect_signals()

    def _build_layout(self):
        controls_layout = QVBoxLayout()

        controls_layout.addWidget(QLabel("Backend URL"))
        controls_layout.addWidget(self.api_input)
        controls_layout.addWidget(QLabel("API Token"))
        controls_layout.addWidget(self.token_input)

        button_row = QHBoxLayout()
        button_row.addWidget(self.upload_button)
        button_row.addWidget(self.refresh_button)
        controls_layout.addLayout(button_row)

        controls_layout.addWidget(QLabel("History"))
        controls_layout.addWidget(self.history_list)
        controls_layout.addWidget(self.status_label)

        controls_widget = QWidget()
        controls_widget.setLayout(controls_layout)

        data_layout = QVBoxLayout()
        data_layout.addWidget(self.summary_group)
        data_layout.addWidget(QLabel("Type Distribution"))
        data_layout.addWidget(self.distribution_table)
        data_layout.addWidget(self.canvas)

        data_widget = QWidget()
        data_widget.setLayout(data_layout)

        main_layout = QHBoxLayout()
        main_layout.addWidget(controls_widget, 1)
        main_layout.addWidget(data_widget, 2)
        self.setLayout(main_layout)

    def _connect_signals(self):
        self.upload_button.clicked.connect(self.upload_csv)
        self.refresh_button.clicked.connect(self.fetch_history)
        self.history_list.itemClicked.connect(self.handle_history_click)
        self.api_input.textChanged.connect(lambda value: self.settings.setValue("api_base", value))
        self.token_input.textChanged.connect(lambda value: self.settings.setValue("api_token", value))

    def _headers(self):
        token = self.token_input.text().strip()
        return {"Authorization": f"Token {token}"} if token else {}

    def _base_url(self):
        return self.api_input.text().strip().rstrip("/")

    def _request(self, method, path, **kwargs):
        url = f"{self._base_url()}{path}"
        return requests.request(method, url, headers=self._headers(), timeout=30, **kwargs)

    def upload_csv(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select CSV", str(Path.cwd()), "CSV Files (*.csv)")
        if not file_path:
            return

        try:
            with open(file_path, "rb") as handle:
                self.status_label.setText("Uploading...")
                response = self._request("POST", "/api/upload/", files={"file": handle})
            response.raise_for_status()
            self.status_label.setText("Upload complete.")
            summary = response.json()
            self.update_summary(summary)
            self.fetch_history()
        except Exception as exc:
            self.status_label.setText("Upload failed.")
            QMessageBox.critical(self, "Upload error", str(exc))

    def fetch_history(self):
        try:
            self.status_label.setText("Loading history...")
            response = self._request("GET", "/api/history/")
            response.raise_for_status()
            history = response.json()
            self.history_list.clear()
            for item in history:
                label = f"Dataset {item['id']} - {item['upload_time']}"
                list_item = QListWidgetItem(label)
                list_item.setData(Qt.UserRole, item["id"])
                self.history_list.addItem(list_item)
            if history:
                self.update_summary(history[0])
            self.status_label.setText("Ready")
        except Exception as exc:
            self.status_label.setText("History load failed.")
            QMessageBox.critical(self, "History error", str(exc))

    def handle_history_click(self, item):
        dataset_id = item.data(Qt.UserRole)
        self.fetch_summary(dataset_id)

    def fetch_summary(self, dataset_id):
        try:
            self.status_label.setText("Loading summary...")
            response = self._request("GET", f"/api/summary/{dataset_id}/")
            response.raise_for_status()
            summary = response.json()
            self.update_summary(summary)
            self.status_label.setText("Ready")
        except Exception as exc:
            self.status_label.setText("Summary load failed.")
            QMessageBox.critical(self, "Summary error", str(exc))

    def update_summary(self, summary):
        if not summary:
            return

        self.count_label.setText(f"Total count: {summary['total_count']}")
        self.flowrate_label.setText(f"Avg flowrate: {summary['avg_flowrate']:.2f}")
        self.pressure_label.setText(f"Avg pressure: {summary['avg_pressure']:.2f}")
        self.temperature_label.setText(f"Avg temperature: {summary['avg_temperature']:.2f}")

        distribution = summary.get("type_distribution", {})
        self.distribution_table.setRowCount(len(distribution))
        for row, (name, count) in enumerate(distribution.items()):
            self.distribution_table.setItem(row, 0, QTableWidgetItem(str(name)))
            self.distribution_table.setItem(row, 1, QTableWidgetItem(str(count)))

        self._update_chart(summary)

    def _update_chart(self, summary):
        self.figure.clear()
        axes1 = self.figure.add_subplot(1, 2, 1)
        axes2 = self.figure.add_subplot(1, 2, 2)

        distribution = summary.get("type_distribution", {})
        axes1.bar(distribution.keys(), distribution.values(), color="#2f6f64")
        axes1.set_title("Type Distribution")
        axes1.tick_params(axis="x", rotation=45)

        averages = [
            summary.get("avg_flowrate", 0),
            summary.get("avg_pressure", 0),
            summary.get("avg_temperature", 0),
        ]
        axes2.plot(["Flowrate", "Pressure", "Temperature"], averages, marker="o", color="#1e293b")
        axes2.set_title("Averages")
        axes2.set_ylim(bottom=0)

        self.figure.tight_layout()
        self.canvas.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(1200, 720)
    window.show()
    sys.exit(app.exec_())
