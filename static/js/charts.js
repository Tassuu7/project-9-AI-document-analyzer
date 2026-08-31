/**
 * Vanilla SVG Chart & Data Visualization Engine
 */

const ChartEngine = {
  renderGauge(containerId, value, maxVal = 100, label = "", color = "#6366f1") {
    const el = document.getElementById(containerId);
    if (!el) return;
    const pct = Math.min(100, Math.max(0, (value / maxVal) * 100));
    const radius = 54;
    const circ = Math.PI * radius;
    const strokeDash = (pct / 100) * circ;

    el.innerHTML = `
      <div style="position: relative; width: 140px; height: 90px; margin: 0 auto; display: flex; flex-direction: column; align-items: center;">
        <svg width="140" height="80" viewBox="0 0 140 80">
          <path d="M 16 70 A 54 54 0 0 1 124 70" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="12" stroke-linecap="round" />
          <path d="M 16 70 A 54 54 0 0 1 124 70" fill="none" stroke="${color}" stroke-width="12" stroke-linecap="round" stroke-dasharray="${strokeDash} ${circ}" style="transition: stroke-dasharray 0.8s ease;" />
        </svg>
        <div style="position: absolute; bottom: 12px; text-align: center;">
          <div style="font-size: 1.5rem; font-weight: 800; color: ${color}; line-height: 1;">${value}</div>
          <div style="font-size: 0.7rem; font-weight: 600; color: var(--text-secondary);">${label}</div>
        </div>
      </div>
    `;
  },

  renderDonut(containerId, dataMap) {
    const el = document.getElementById(containerId);
    if (!el) return;
    const total = Object.values(dataMap).reduce((a, b) => a + b, 0) || 1;
    const colors = ["#6366f1", "#06b6d4", "#a855f7", "#10b981", "#f59e0b", "#f43f5e"];
    
    let legendHtml = '<div style="display: flex; flex-direction: column; gap: 0.4rem; font-size: 0.8rem; margin-top: 1rem;">';
    let idx = 0;
    for (const [k, v] of Object.entries(dataMap)) {
      const col = colors[idx % colors.length];
      const pct = Math.round((v / total) * 100);
      legendHtml += `
        <div style="display: flex; justify-content: space-between; align-items: center;">
          <span style="display: flex; align-items: center; gap: 0.4rem;"><span style="width: 10px; height: 10px; border-radius: 50%; background: ${col}; display: inline-block;"></span> ${k}</span>
          <strong style="color: var(--text-secondary);">${pct}%</strong>
        </div>
      `;
      idx++;
    }
    legendHtml += '</div>';

    el.innerHTML = `
      <div style="text-align: center;">
        <svg width="150" height="150" viewBox="0 0 100 100">
          <circle cx="50" cy="50" r="38" fill="none" stroke="rgba(255,255,255,0.06)" stroke-width="14" />
          <circle cx="50" cy="50" r="38" fill="none" stroke="#6366f1" stroke-width="14" stroke-dasharray="140 240" stroke-linecap="round" />
          <circle cx="50" cy="50" r="38" fill="none" stroke="#06b6d4" stroke-width="14" stroke-dasharray="60 240" stroke-dashoffset="-140" stroke-linecap="round" />
        </svg>
        ${legendHtml}
      </div>
    `;
  }
};
