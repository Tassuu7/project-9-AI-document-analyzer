/**
 * Core Global Application Engine & Universal Auth Manager
 */

const App = {
  tokenKey: "doc_analyzer_jwt_token",
  userKey: "doc_analyzer_user",

  getToken() {
    return localStorage.getItem(this.tokenKey);
  },

  getUser() {
    try {
      const u = localStorage.getItem(this.userKey);
      return u ? JSON.parse(u) : { username: "analyst_guest", role: "Lead Analyst", full_name: "Lead Intelligence Analyst" };
    } catch(e) {
      return { username: "analyst_guest", role: "Lead Analyst", full_name: "Lead Intelligence Analyst" };
    }
  },

  setAuth(user, token) {
    if (token) localStorage.setItem(this.tokenKey, token);
    if (user) localStorage.setItem(this.userKey, JSON.stringify(user));
    this.renderNavAuth();
  },

  logout() {
    localStorage.removeItem(this.tokenKey);
    localStorage.removeItem(this.userKey);
    this.showToast("Signed out successfully", "info");
    this.renderNavAuth();
    if (window.location.pathname === "/dashboard") {
      setTimeout(() => window.location.href = "/auth", 800);
    }
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

    try {
      const res = await fetch(url, { ...options, headers });
      const data = await res.json();
      if (!res.ok) {
        throw new Error(data.error || `Server Error (${res.status})`);
      }
      return data;
    } catch(err) {
      console.error("API Request Error:", err);
      throw err;
    }
  },

  showToast(message, type = "info") {
    const toast = document.createElement("div");
    const badgeType = type === 'error' ? 'badge-danger' : type === 'success' ? 'badge-success' : type === 'warning' ? 'badge-warning' : 'badge-info';
    toast.className = `badge ${badgeType}`;
    toast.style.cssText = "position: fixed; bottom: 24px; right: 24px; z-index: 99999; padding: 12px 24px; font-size: 14px; font-weight: 600; box-shadow: 0 12px 32px rgba(0,0,0,0.6); backdrop-filter: blur(16px); animation: fadeIn 0.3s ease;";
    toast.innerText = message;
    document.body.appendChild(toast);
    setTimeout(() => {
      toast.style.opacity = "0";
      toast.style.transition = "opacity 0.4s ease";
      setTimeout(() => toast.remove(), 400);
    }, 3500);
  },

  downloadFile(filename, content, mimeType = "text/plain") {
    const blob = new Blob([content], { type: mimeType });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = filename;
    document.body.appendChild(a);
    a.click();
    setTimeout(() => {
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
    }, 100);
  },

  renderNavAuth() {
    const container = document.getElementById("navAuthBox");
    if (!container) return;
    const token = this.getToken();
    const user = this.getUser();

    if (token && user) {
      container.innerHTML = `
        <div style="display: flex; align-items: center; gap: 0.6rem;">
          <div class="badge badge-purple" style="padding: 0.4rem 0.75rem; font-size: 0.8rem;">
            👤 ${user.username} <span style="opacity: 0.75; font-size: 11px;">(${user.role || 'Analyst'})</span>
          </div>
          <button class="btn btn-secondary btn-sm" onclick="App.logout()">Sign Out</button>
        </div>
      `;
    } else {
      container.innerHTML = `
        <a href="/auth" class="btn btn-primary btn-sm">Sign In / Portal</a>
      `;
    }
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

document.addEventListener("DOMContentLoaded", () => {
  App.initTheme();
  App.renderNavAuth();
});
