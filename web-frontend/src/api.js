const defaultBaseUrl = "http://127.0.0.1:8000";

export function buildApiClient(baseUrl, token) {
  const apiBase = (baseUrl || defaultBaseUrl).replace(/\/+$/, "");

  const authHeaders = token
    ? {
        Authorization: `Token ${token}`,
      }
    : {};

  async function request(path, options = {}) {
    const response = await fetch(`${apiBase}${path}`, {
      ...options,
      headers: {
        ...(options.headers || {}),
        ...authHeaders,
      },
    });

    if (!response.ok) {
      const message = await response.text();
      throw new Error(message || "Request failed");
    }

    if (response.headers.get("content-type")?.includes("application/json")) {
      return response.json();
    }

    return response;
  }

  return {
    uploadDataset(formData) {
      return request("/api/upload/", {
        method: "POST",
        body: formData,
      });
    },
    fetchSummary(id) {
      return request(`/api/summary/${id}/`);
    },
    fetchHistory() {
      return request("/api/history/");
    },
  };
}
