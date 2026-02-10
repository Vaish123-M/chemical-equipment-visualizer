import { useEffect, useMemo, useState } from "react";
import {
  Chart as ChartJS,
  BarElement,
  CategoryScale,
  LinearScale,
  LineElement,
  PointElement,
  Tooltip,
  Legend,
} from "chart.js";

import { buildApiClient } from "./api.js";
import SummaryCards from "./components/SummaryCards.jsx";
import TypeDistributionChart from "./components/TypeDistributionChart.jsx";
import AveragesChart from "./components/AveragesChart.jsx";
import HistoryList from "./components/HistoryList.jsx";

ChartJS.register(
  BarElement,
  CategoryScale,
  LinearScale,
  LineElement,
  PointElement,
  Tooltip,
  Legend
);

export default function App() {
  const [apiBaseUrl, setApiBaseUrl] = useState("http://127.0.0.1:8000");
  const [token, setToken] = useState("");
  const [history, setHistory] = useState([]);
  const [summary, setSummary] = useState(null);
  const [status, setStatus] = useState("Ready");
  const [selectedFile, setSelectedFile] = useState(null);

  const api = useMemo(() => buildApiClient(apiBaseUrl, token), [apiBaseUrl, token]);

  useEffect(() => {
    if (!token) {
      setHistory([]);
      setSummary(null);
      return;
    }

    setStatus("Loading history...");
    api
      .fetchHistory()
      .then((data) => {
        setHistory(data);
        // Don't automatically set summary - only show data after upload
        setSummary(null);
        setStatus("Ready");
      })
      .catch((error) => {
        setStatus(error.message);
      });
  }, [api, token]);

  const handleUpload = async () => {
    if (!selectedFile) {
      setStatus("Choose a CSV file first.");
      return;
    }
    if (!token) {
      setStatus("Token required.");
      return;
    }

    const formData = new FormData();
    formData.append("file", selectedFile);

    setStatus("Uploading...");
    try {
      const data = await api.uploadDataset(formData);
      setSummary(data);
      const updatedHistory = await api.fetchHistory();
      setHistory(updatedHistory);
      setStatus("Upload complete.");
    } catch (error) {
      setStatus(error.message);
    }
  };

  const handleSelectHistory = async (datasetId) => {
    setStatus("Loading summary...");
    try {
      const data = await api.fetchSummary(datasetId);
      setSummary(data);
      setStatus("Ready");
    } catch (error) {
      setStatus(error.message);
    }
  };

  return (
    <div className="app">
      <section className="landing">
        <h1 className="landing-title">Parameter Visualization</h1>
        <p className="landing-description">
          Chemical Equipment Parameter Visualizer is a hybrid web and desktop application that enables users to upload chemical equipment data in CSV format and instantly view key analytics. The platform provides summary statistics, interactive charts, and dataset history through a shared backend, making equipment monitoring and analysis simple and efficient.
        </p>
      </section>

      <header className="hero">
        <div>
          <p className="eyebrow">Chemical Equipment</p>
          <h1>Parameter Visualizer</h1>
          <p className="subtitle">Upload CSV datasets and compare key averages instantly.</p>
        </div>
        <div className="panel">
          <label className="field">
            <span>Backend URL</span>
            <input
              value={apiBaseUrl}
              onChange={(event) => setApiBaseUrl(event.target.value)}
              placeholder="http://127.0.0.1:8000"
            />
          </label>
          <label className="field">
            <span>API Token</span>
            <input
              value={token}
              onChange={(event) => setToken(event.target.value)}
              placeholder="Paste token from /api/token/"
              type="password"
            />
          </label>
          <label className="file-field">
            <span>CSV Dataset</span>
            <input
              type="file"
              accept=".csv"
              onChange={(event) => setSelectedFile(event.target.files[0])}
            />
          </label>
          <button className="primary" onClick={handleUpload}>
            Upload & Analyze
          </button>
          <p className="status">{status}</p>
        </div>
      </header>

      <main>
        <section className="grid">
          <SummaryCards summary={summary} />
          <TypeDistributionChart distribution={summary?.type_distribution} />
          <AveragesChart summary={summary} />
        </section>

        <HistoryList history={history} onSelect={handleSelectHistory} />
      </main>
    </div>
  );
}
