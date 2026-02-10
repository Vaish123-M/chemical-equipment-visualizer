import { Bar } from "react-chartjs-2";

export default function TypeDistributionChart({ distribution }) {
  const labels = distribution ? Object.keys(distribution) : [];
  const values = distribution ? Object.values(distribution) : [];

  const data = {
    labels,
    datasets: [
      {
        label: "Equipment Count",
        data: values,
        backgroundColor: "rgba(34, 94, 87, 0.8)",
        borderRadius: 8,
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
      <h2>Type Distribution</h2>
      <Bar data={data} options={options} />
    </div>
  );
}
