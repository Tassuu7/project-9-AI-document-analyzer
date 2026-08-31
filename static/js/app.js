/**
 * Core Application Engine, Auth Manager, and Global Utilities
 */

const App = {
  tokenKey: "doc_analyzer_jwt_token",
  
  getToken() {
    return localStorage.getItem(this.tokenKey);
  },
  
  setToken(token) {
    localStorage.setItem(this.tokenKey, token);
  },
  
  removeToken() {
    localStorage.removeItem(this.tokenKey);
  },

  async request(url, options = {}) {
    const token = this.getToken();
    const headers = options.headers || {};
    if (token) {
      headers["Authorization"] = `Bearer ${token}`;
    }
    if (!(options.body instanceof FormData) && !headers["Content-Type"]) {
      headers["Content-Type"] = "application/json";
    }
    
    const res = await fetch(url, { ...options, headers });
    const data = await res.json();
    if (!res.ok) {
      throw new Error(data.error || `HTTP Error ${res.status}`);
    }
    return data;
  },

  showToast(message, type = "info") {
    const toast = document.createElement("div");
    toast.className = `badge badge-${type === 'error' ? 'danger' : type === 'success' ? 'success' : 'info'}`;
    toast.style.cssText = "position: fixed; bottom: 24px; right: 24px; z-index: 9999; padding: 12px 20px; font-size: 14px; box-shadow: 0 8px 24px rgba(0,0,0,0.5); backdrop-filter: blur(12px);";
    toast.innerText = message;
    document.body.appendChild(toast);
    setTimeout(() => toast.remove(), 4000);
  },

  initTheme() {
    const saved = localStorage.getItem("doc_theme") || "dark";
    document.documentElement.setAttribute("data-theme", saved);
  },

  toggleTheme() {
    const current = document.documentElement.getAttribute("data-theme") || "dark";
    const next = current === "dark" ? "light" : "dark";
    document.documentElement.setAttribute("data-theme", next);
    localStorage.setItem("doc_theme", next);
  }
};

document.addEventListener("DOMContentLoaded", () => App.initTheme());
