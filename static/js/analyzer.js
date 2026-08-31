/**
 * Interactive Live Document Analyzer Controller
 */

let currentAnalysisReport = null;

const Analyzer = {
  async runAnalysis() {
    const text = document.getElementById("docInput").value;
    if (!text.trim()) {
      App.showToast("Please enter or paste document text", "warning");
      return;
    }

    const btn = document.getElementById("analyzeBtn");
    btn.disabled = true;
    btn.innerHTML = "<span>Analyzing Pipeline...</span>";

    try {
      const res = await App.request("/api/analyze/quick", {
        method: "POST",
        body: JSON.stringify({ text })
      });
      
      currentAnalysisReport = res.data;
      this.renderReport(res.data, text);
      App.showToast("Analysis Complete!", "success");
    } catch (err) {
      App.showToast(err.message, "error");
    } finally {
      btn.disabled = false;
      btn.innerHTML = "<span>⚡ Analyze Intelligence</span>";
    }
  },

  renderReport(data, originalText) {
    document.getElementById("resultsContainer").style.display = "flex";
    document.getElementById("placeholderBox").style.display = "none";

    // 1. Classification & Summary
    document.getElementById("classBadge").innerText = `${data.classification.category} (${Math.round(data.classification.confidence * 100)}%)`;
    document.getElementById("summaryText").innerText = data.summary.extractive;

    // 2. Risk Score & Gauge
    const riskScore = data.risk.overall_risk_score;
    const riskColor = riskScore > 70 ? "#f43f5e" : riskScore > 40 ? "#f59e0b" : "#10b981";
    ChartEngine.renderGauge("riskGauge", riskScore, 100, data.risk.risk_level, riskColor);

    // 3. Sentiment & Readability
    document.getElementById("toneBadge").innerText = `Tone: ${data.sentiment.tone}`;
    document.getElementById("polarityVal").innerText = `Polarity: ${data.sentiment.polarity}`;
    document.getElementById("readabilityBadge").innerText = `${data.readability.flesch_reading_ease} / 100 (${data.readability.reading_level})`;
    document.getElementById("gradeLevelVal").innerText = `Grade Level: ${data.readability.flesch_kincaid_grade}`;

    // 4. Compliance Breakdown
    const compEl = document.getElementById("complianceList");
    compEl.innerHTML = "";
    const violations = data.compliance.violations_found;
    if (violations.length === 0) {
      compEl.innerHTML = `<div class="badge badge-success">✓ Clean Document - No Major Violations Detected</div>`;
    } else {
      violations.forEach(v => {
        const item = document.createElement("div");
        item.style.cssText = "padding: 8px; border-left: 3px solid #f43f5e; background: rgba(244,63,94,0.1); border-radius: 4px; margin-bottom: 6px; font-size: 0.8rem;";
        item.innerHTML = `<strong>[${v.standard}] ${v.rule}</strong><br><span style="color: var(--text-secondary);">${v.remediation}</span>`;
        compEl.appendChild(item);
      });
    }

    // 5. Highlighted Entity Viewer
    this.renderHighlightedEntities(originalText, data.entities);
  },

  renderHighlightedEntities(text, entities) {
    const viewer = document.getElementById("highlightedText");
    if (!entities || entities.length === 0) {
      viewer.innerText = text;
      return;
    }

    let html = "";
    let lastIdx = 0;
    
    entities.forEach(e => {
      if (e.start >= lastIdx) {
        html += App.escapeHtml(text.substring(lastIdx, e.start));
        html += `<span class="entity-chip entity-${e.category}" title="${e.type} (${Math.round(e.confidence*100)}%)">${App.escapeHtml(e.text)} <small style="font-size:9px; opacity:0.8;">${e.type}</small></span>`;
        lastIdx = e.end;
      }
    });
    html += App.escapeHtml(text.substring(lastIdx));
    viewer.innerHTML = html;
  },

  loadSample(type) {
    const samples = {
      nda: `NON-DISCLOSURE AND MUTUAL CONFIDENTIALITY AGREEMENT\nThis Agreement is entered into on October 14, 2026, by and between CyberCorp Inc. ("Disclosing Party") and Apex Solutions LLC ("Receiving Party").\n\n1. Confidential Information: Receiving Party agrees not to disclose proprietary trade secrets or customer lists to any third party without prior written consent.\n2. Standard of Care: Receiving Party shall protect confidential data with at least reasonable care.\n3. Term & Termination: This Agreement shall remain in effect for three (3) years. Upon breach, Disclosing Party may terminate immediately without notice.\n4. Governing Law: This agreement shall be governed by the laws of the State of Delaware.`,
      breach: `SECURITY AUDIT REPORT - INCIDENT DISCLOSURE\nDuring the internal vulnerability scan on November 02, 2026, the security operations center discovered that primary cardholder data (PAN) and customer credentials were stored in plain text unencrypted files on database server 192.168.1.104. Over 45,000 records containing social security numbers (e.g. 000-12-3456) and emails (user@acme.org) were accessible without multi-factor authentication. Immediate remediation is mandatory under PCI-DSS Requirement 3.2 and GDPR Article 32.`
    };
    if (samples[type]) {
      document.getElementById("docInput").value = samples[type];
      this.runAnalysis();
    }
  }
};

App.escapeHtml = (str) => {
  return str.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
};
