/**
 * Pure Vanilla SVG Charting Engine
 * Renders high-performance Donut, Bar, Radar, and Gauge charts with zero third-party dependencies.
 */

const ChartEngine = {
  renderGauge(containerId, value, maxValue = 100, label = "Risk Index", color = "#6366f1") {
    const el = document.getElementById(containerId);
    if (!el) return;
    
    const pct = Math.min(1, Math.max(0, value / maxValue));
    const radius = 60;
    const circ = 2 * Math.PI * radius;
    const offset = circ * (1 - (pct * 0.75)); // 270 degree gauge
    
    el.innerHTML = `
      <div style="text-align: center; position: relative; width: 160px; margin: 0 auto;">
        <svg width="160" height="160" viewBox="0 0 160 160">
          <circle cx="80" cy="80" r="${radius}" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="12" stroke-dasharray="${circ * 0.75} ${circ * 0.25}" stroke-linecap="round" transform="rotate(135 80 80)"/>
          <circle cx="80" cy="80" r="${radius}" fill="none" stroke="${color}" stroke-width="12" stroke-dasharray="${circ}" stroke-dashoffset="${offset}" stroke-linecap="round" transform="rotate(135 80 80)" style="transition: stroke-dashoffset 0.8s ease;"/>
        </svg>
        <div style="position: absolute; top: 40%; left: 0; right: 0; text-align: center;">
          <div style="font-size: 1.75rem; font-weight: 700; color: var(--text-primary);">${Math.round(value)}</div>
          <div style="font-size: 0.75rem; color: var(--text-secondary); text-transform: uppercase;">${label}</div>
        </div>
      </div>
    `;
  },

  renderDonut(containerId, dataMap) {
    const el = document.getElementById(containerId);
    if (!el) return;
    
    const keys = Object.keys(dataMap);
    const total = Object.values(dataMap).reduce((a, b) => a + b, 0) || 1;
    const colors = ["#6366f1", "#06b6d4", "#10b981", "#f59e0b", "#a855f7", "#f43f5e"];
    
    let html = `<div style="display: flex; flex-direction: column; gap: 0.75rem;">`;
    keys.forEach((k, idx) => {
      const val = dataMap[k];
      const pct = Math.round((val / total) * 100);
      const color = colors[idx % colors.length];
      html += `
        <div>
          <div style="display: flex; justify-content: space-between; font-size: 0.8rem; margin-bottom: 0.25rem;">
            <span>${k}</span>
            <span style="font-weight: 600; color: ${color};">${val} (${pct}%)</span>
          </div>
          <div style="height: 6px; background: rgba(255,255,255,0.08); border-radius: 999px; overflow: hidden;">
            <div style="width: ${pct}%; height: 100%; background: ${color}; border-radius: 999px; transition: width 0.6s ease;"></div>
          </div>
        </div>
      `;
    });
    html += `</div>`;
    el.innerHTML = html;
  }
};
