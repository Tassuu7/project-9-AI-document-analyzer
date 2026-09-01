/**
 * Clean SVG Visualizations (Strictly No Blue, Neutral & Semantic Palette)
 */
const ChartEngine = {
  renderGauge(containerId, value, maxVal = 100, label = "Score", strokeColor = "#15803d") {
    const container = document.getElementById(containerId);
    if (!container) return;
    const pct = Math.min(100, Math.max(0, (value / maxVal) * 100));
    const radius = 38;
    const circumference = 2 * Math.PI * radius;
    const strokeDashoffset = circumference - (pct / 100) * circumference;

    container.innerHTML = `
      <svg width="100" height="100" viewBox="0 0 100 100">
        <circle cx="50" cy="50" r="${radius}" fill="none" stroke="var(--border-subtle)" stroke-width="8"></circle>
        <circle cx="50" cy="50" r="${radius}" fill="none" stroke="${strokeColor}" stroke-width="8" stroke-dasharray="${circumference}" stroke-dashoffset="${strokeDashoffset}" stroke-linecap="round" transform="rotate(-90 50 50)" style="transition: stroke-dashoffset 0.6s ease;"></circle>
        <text x="50" y="48" font-size="17" font-weight="bold" fill="var(--text-primary)" text-anchor="middle" dominant-baseline="middle">${Math.round(value)}</text>
        <text x="50" y="65" font-size="9" fill="var(--text-secondary)" text-anchor="middle" dominant-baseline="middle">${label}</text>
      </svg>
    `;
  }
};
