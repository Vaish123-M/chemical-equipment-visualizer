export default function SummaryCards({ summary }) {
  const cards = [
    {
      label: "Total Count",
      value: summary?.total_count ?? "-",
    },
    {
      label: "Avg Flowrate",
      value: summary ? summary.avg_flowrate.toFixed(2) : "-",
    },
    {
      label: "Avg Pressure",
      value: summary ? summary.avg_pressure.toFixed(2) : "-",
    },
    {
      label: "Avg Temperature",
      value: summary ? summary.avg_temperature.toFixed(2) : "-",
    },
  ];

  return (
    <div className="cards">
      {cards.map((card) => (
        <div className="card" key={card.label}>
          <p className="card-label">{card.label}</p>
          <p className="card-value">{card.value}</p>
        </div>
      ))}
    </div>
  );
}
