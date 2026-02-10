export default function HistoryList({ history, onSelect }) {
  const formatDate = (dateString) => {
    const date = new Date(dateString);
    return date.toLocaleString("en-US", {
      year: "numeric",
      month: "short",
      day: "numeric",
      hour: "2-digit",
      minute: "2-digit",
    });
  };

  return (
    <section className="history">
      <div className="history-header">
        <h2>📋 Recent Uploads</h2>
      </div>
      <div className="history-list">
        {history.length === 0 ? (
          <p className="muted" style={{ padding: "20px", textAlign: "center" }}>
            No uploads yet. Upload your first dataset to get started!
          </p>
        ) : (
          history.map((item, idx) => (
            <button
              key={item.id}
              className="history-item"
              onClick={() => onSelect(item.id)}
              style={{ background: "none", padding: "0", border: "none" }}
            >
              <div>
                <span style={{ fontWeight: 700 }}>Dataset #{item.id}</span>
              </div>
              <span className="muted">{formatDate(item.upload_time)}</span>
            </button>
          ))
        )}
      </div>
    </section>
  );
}
