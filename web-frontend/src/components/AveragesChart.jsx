import { Line } from "react-chartjs-2";

export default function AveragesChart({ summary }) {
  const data = {
    labels: ["Flowrate", "Pressure", "Temperature"],
    datasets: [
      {
        label: "Averages",
        data: summary
          ? [summary.avg_flowrate, summary.avg_pressure, summary.avg_temperature]
          : [0, 0, 0],
        borderColor: "rgba(15, 23, 42, 0.9)",
        backgroundColor: "rgba(15, 23, 42, 0.15)",
        tension: 0.35,
        fill: true,
      },
    ],
  };

  const options = {
    responsive: true,
    plugins: {
      legend: { display: false },
    },
    scales: {
      y: { beginAtZero: true },
    },
  };

  return (
    <div className="chart-card">
      <h2>Averages</h2>
      <Line data={data} options={options} />
    </div>
  );
}
