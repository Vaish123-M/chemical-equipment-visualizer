import { Line } from "react-chartjs-2";

export default function AveragesChart({ summary }) {
  const data = {
    labels: ["Flowrate", "Pressure", "Temperature"],
    datasets: [
      {
        label: "Average Values",
        data: summary
          ? [summary.avg_flowrate, summary.avg_pressure, summary.avg_temperature]
          : [0, 0, 0],
        borderColor: "rgba(0, 82, 204, 1)",
        backgroundColor: "rgba(0, 184, 148, 0.15)",
        borderWidth: 3,
        pointRadius: 6,
        pointBackgroundColor: "rgba(0, 82, 204, 1)",
        pointBorderColor: "#ffffff",
        pointBorderWidth: 2,
        tension: 0.4,
        fill: true,
        pointHoverRadius: 8,
        pointHoverBackgroundColor: "rgba(0, 184, 148, 1)",
      },
    ],
  };

  const options = {
    responsive: true,
    maintainAspectRatio: true,
    plugins: {
      legend: { display: true, labels: { padding: 15, font: { size: 12 } } },
    },
    scales: {
      y: { 
        beginAtZero: true,
        grid: {
          color: "rgba(0, 0, 0, 0.05)",
        },
      },
      x: {
        grid: {
          display: false,
        },
      },
    },
  };

  return (
    <div className="chart-card">
      <h2>📈 Trend Analysis</h2>
      <Line data={data} options={options} />
    </div>
  );
}
