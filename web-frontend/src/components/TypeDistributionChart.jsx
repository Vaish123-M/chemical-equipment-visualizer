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
        backgroundColor: [
          "rgba(0, 82, 204, 0.7)",
          "rgba(0, 184, 148, 0.7)",
          "rgba(255, 107, 107, 0.7)",
          "rgba(255, 159, 64, 0.7)",
          "rgba(54, 162, 235, 0.7)",
        ],
        borderColor: [
          "rgba(0, 52, 153, 1)",
          "rgba(0, 130, 105, 1)",
          "rgba(230, 30, 30, 1)",
          "rgba(230, 126, 34, 1)",
          "rgba(41, 128, 185, 1)",
        ],
        borderWidth: 2,
        borderRadius: 8,
      },
    ],
  };

  const options = {
    responsive: true,
    maintainAspectRatio: true,
    plugins: {
      legend: { display: false },
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
      <h2>📦 Type Distribution</h2>
      <Bar data={data} options={options} />
    </div>
  );
}
