export default function HistoryList({ history, onSelect }) {
  return (
    <section className="history">
      <div className="history-header">
        <h2>Last 5 Uploads</h2>
      </div>
      <div className="history-list">
        {history.length === 0 ? (
          <p className="muted">No uploads yet.</p>
        ) : (
          history.map((item) => (
            <button
              key={item.id}
              className="history-item"
              onClick={() => onSelect(item.id)}
            >
              <span>Dataset {item.id}</span>
              <span className="muted">
                {new Date(item.upload_time).toLocaleString()}
              </span>
            </button>
          ))
        )}
      </div>
    </section>
  );
}
