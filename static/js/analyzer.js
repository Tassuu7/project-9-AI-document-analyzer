/**
 * Live Intelligent Document Analyzer Controller
 */

let currentAnalysisReport = null;
let currentRawText = "";
let isMaskedMode = false;

const Analyzer = {
  init() {
    // Check if sample text is in input, if empty, load default NDA and run immediately
    const input = document.getElementById("docInput");
    if (input && !input.value.trim()) {
      this.loadSample('nda', false);
    }
    this.runAnalysis();
    this.setupDropzone();
  },

  setupDropzone() {
    const dropzone = document.getElementById("fileDropzone");
    const fileInput = document.getElementById("filePicker");
    if (!dropzone || !fileInput) return;

    dropzone.addEventListener("click", () => fileInput.click());
    
    fileInput.addEventListener("change", (e) => {
      if (e.target.files.length > 0) {
        this.handleFile(e.target.files[0]);
      }
    });

    ["dragenter", "dragover"].forEach(eventName => {
      dropzone.addEventListener(eventName, (e) => {
        e.preventDefault();
        dropzone.classList.add("dragover");
      }, false);
    });

    ["dragleave", "drop"].forEach(eventName => {
      dropzone.addEventListener(eventName, (e) => {
        e.preventDefault();
        dropzone.classList.remove("dragover");
      }, false);
    });

    dropzone.addEventListener("drop", (e) => {
      if (e.dataTransfer.files.length > 0) {
        this.handleFile(e.dataTransfer.files[0]);
      }
    });
  },

  async handleFile(file) {
    App.showToast(`Reading file: ${file.name}...`, "info");
    const reader = new FileReader();
    reader.onload = async (e) => {
      const text = e.target.result;
      document.getElementById("docInput").value = text;
      App.showToast(`File ${file.name} ingested successfully!`, "success");
      await this.runAnalysis();
    };
    reader.readAsText(file);
  },

  async runAnalysis() {
    const text = document.getElementById("docInput").value;
    if (!text.trim()) {
      App.showToast("Please enter or paste document text", "warning");
      return;
    }

    currentRawText = text;
    const btn = document.getElementById("analyzeBtn");
    if (btn) {
      btn.disabled = true;
      btn.innerHTML = "<span>⚡ Analyzing Pipeline...</span>";
    }

    try {
      const res = await App.request("/api/analyze/quick", {
        method: "POST",
        body: JSON.stringify({ text })
      });
      
      currentAnalysisReport = res.data;
      this.renderReport(res.data, text);
      App.showToast("Analysis Pipeline Complete!", "success");
    } catch (err) {
      console.error(err);
      App.showToast(err.message || "Analysis error", "error");
    } finally {
      if (btn) {
        btn.disabled = false;
        btn.innerHTML = "<span>⚡ Analyze Intelligence</span>";
      }
    }
  },

  renderReport(data, originalText) {
    document.getElementById("resultsContainer").style.display = "flex";
    const placeholder = document.getElementById("placeholderBox");
    if (placeholder) placeholder.style.display = "none";

    // 1. Classification & Summary
    const cls = data.classification;
    const confPct = Math.round(cls.confidence * 100);
    document.getElementById("classBadge").innerText = `${cls.category}`;
    document.getElementById("confBadge").innerText = `${confPct}% Confidence`;
    document.getElementById("summaryText").innerText = data.summary.extractive || "Summary generated.";

    // 2. Word counts
    const words = originalText.split(/\s+/).filter(Boolean).length;
    document.getElementById("docWordCount").innerText = `${words} words`;

    // 3. Structured Key Obligations & Risks
    const obEl = document.getElementById("keyObligationsList");
    if (obEl) {
      obEl.innerHTML = "";
      const obs = data.summary.key_obligations || [];
      if (obs.length === 0) {
        obEl.innerHTML = `<li style="color: var(--text-secondary);">No explicit mandatory obligations detected.</li>`;
      } else {
        obs.forEach(o => {
          const li = document.createElement("li");
          li.style.marginBottom = "6px";
          li.innerText = o;
          obEl.appendChild(li);
        });
      }
    }

    const riskEl = document.getElementById("keyRisksList");
    if (riskEl) {
      riskEl.innerHTML = "";
      const rks = data.summary.critical_risks || [];
      if (rks.length === 0) {
        riskEl.innerHTML = `<li style="color: var(--text-secondary);">No high-exposure liability terms detected.</li>`;
      } else {
        rks.forEach(r => {
          const li = document.createElement("li");
          li.style.marginBottom = "6px";
          li.innerText = r;
          riskEl.appendChild(li);
        });
      }
    }

    // 4. Risk Score & Gauge
    const riskScore = data.risk.overall_risk_score;
    const riskColor = riskScore > 60 ? "#f43f5e" : riskScore > 35 ? "#f59e0b" : "#10b981";
    ChartEngine.renderGauge("riskGauge", riskScore, 100, data.risk.risk_level, riskColor);

    // 5. Sentiment & Readability
    document.getElementById("toneBadge").innerText = `${data.sentiment.tone}`;
    document.getElementById("polarityVal").innerText = `Polarity: ${data.sentiment.polarity}`;
    document.getElementById("readabilityBadge").innerText = `Flesch: ${data.readability.flesch_reading_ease} / 100`;
    document.getElementById("gradeLevelVal").innerText = `Grade Level: ${data.readability.flesch_kincaid_grade} (${data.readability.reading_level})`;

    // 6. Compliance Breakdown
    const compEl = document.getElementById("complianceList");
    if (compEl) {
      compEl.innerHTML = "";
      const violations = data.compliance.violations_found || [];
      if (violations.length === 0) {
        compEl.innerHTML = `
          <div class="badge badge-success" style="padding: 0.75rem 1rem; border-radius: var(--radius-md); width: 100%; display: flex; align-items: center; justify-content: space-between;">
            <span>✓ Clean Document - No Regulatory Violations Detected</span>
            <span style="font-weight: 700;">100% Pass</span>
          </div>
        `;
      } else {
        violations.forEach(v => {
          const item = document.createElement("div");
          const bg = v.severity === 'CRITICAL' ? 'rgba(244,63,94,0.15)' : 'rgba(245,158,11,0.15)';
          const border = v.severity === 'CRITICAL' ? '#f43f5e' : '#f59e0b';
          item.style.cssText = `padding: 10px 12px; border-left: 4px solid ${border}; background: ${bg}; border-radius: 6px; margin-bottom: 8px; font-size: 0.85rem;`;
          item.innerHTML = `
            <div style="display: flex; justify-content: space-between; margin-bottom: 4px;">
              <strong style="color: var(--text-primary);">[${v.standard}] ${v.rule}</strong>
              <span class="badge ${v.severity === 'CRITICAL' ? 'badge-danger' : 'badge-warning'}">${v.severity}</span>
            </div>
            <div style="color: var(--text-secondary); margin-bottom: 4px;"><em>"${App.escapeHtml(v.clause)}"</em></div>
            <div style="color: #6ee7b7; font-size: 0.8rem;"><strong>Remediation:</strong> ${v.remediation}</div>
          `;
          compEl.appendChild(item);
        });
      }
    }

    // 7. Render Entities
    this.renderHighlightedEntities(originalText, data.entities);
  },

  renderHighlightedEntities(text, entities) {
    const viewer = document.getElementById("highlightedText");
    if (!viewer) return;

    if (isMaskedMode) {
      // Show masked text
      let masked = text;
      const sorted = [...entities].sort((a,b) => b.start - a.start);
      sorted.forEach((e, idx) => {
        if (e.category === 'PII' || e.type === 'EMAIL' || e.type === 'PHONE_NUMBER' || e.type === 'SSN') {
          masked = masked.substring(0, e.start) + `[REDACTED_${e.type}]` + masked.substring(e.end);
        }
      });
      viewer.innerHTML = App.escapeHtml(masked);
      return;
    }

    if (!entities || entities.length === 0) {
      viewer.innerText = text;
      return;
    }

    let html = "";
    let lastIdx = 0;
    
    entities.forEach(e => {
      if (e.start >= lastIdx) {
        html += App.escapeHtml(text.substring(lastIdx, e.start));
        html += `<span class="entity-chip entity-${e.category}" title="${e.type} (${Math.round(e.confidence*100)}%)">${App.escapeHtml(e.text)} <small style="font-size:9px; opacity:0.85; margin-left:3px;">${e.type}</small></span>`;
        lastIdx = e.end;
      }
    });
    html += App.escapeHtml(text.substring(lastIdx));
    viewer.innerHTML = html;
  },

  toggleMask() {
    isMaskedMode = !isMaskedMode;
    const btn = document.getElementById("maskToggleBtn");
    if (btn) {
      btn.innerText = isMaskedMode ? "👁️ View Original Tags" : "🛡️ Mask / Redact PII";
      btn.className = isMaskedMode ? "btn btn-danger btn-sm" : "btn btn-secondary btn-sm";
    }
    if (currentAnalysisReport) {
      this.renderHighlightedEntities(currentRawText, currentAnalysisReport.entities);
    }
  },

  clearText() {
    document.getElementById("docInput").value = "";
    document.getElementById("resultsContainer").style.display = "none";
    document.getElementById("placeholderBox").style.display = "flex";
    App.showToast("Editor cleared", "info");
  },

  loadSample(type, autoRun = true) {
    const samples = {
      nda: `NON-DISCLOSURE AND MUTUAL CONFIDENTIALITY AGREEMENT\nThis Agreement is entered into on October 24, 2026, by and between CyberCorp Global Technologies Inc. ("Disclosing Party") and Apex Innovation Partners LLC ("Receiving Party").\n\n1. Confidential Information: Receiving Party agrees not to disclose proprietary trade secrets, customer lists, or source code to any third party without prior written consent.\n2. Standard of Care: Receiving Party shall protect confidential data with at least reasonable care.\n3. Term & Termination: This Agreement shall remain in effect for three (3) years. Upon material breach, Disclosing Party may terminate immediately without notice.\n4. Governing Law: This agreement shall be governed by the laws of the State of Delaware. Total consideration fee: $75,000 USD. Contact legal@cybercorp.com.`,
      breach: `SECURITY AUDIT REPORT - CRITICAL INCIDENT DISCLOSURE\nDate of Inspection: August 14, 2026 | Inspector: Cyber Defense Operations\n\nFindings Summary:\nDuring the internal audit on server 10.200.4.12, auditors discovered that primary cardholder data (PAN) and customer credentials were stored in unencrypted plain text log files. Over 35,000 records containing customer social security numbers (e.g. 000-45-6789) and emails (user@clientcorp.com) were accessible without multi-factor authentication. Immediate remediation is mandatory under PCI-DSS Requirement 3.2 and GDPR Article 32. Total remediation budget: $150,000 USD.`,
      financial: `CONSOLIDATED STATEMENT OF OPERATIONS AND COMPREHENSIVE INCOME\nFiscal Year Ended December 31, 2025 (in thousands, except per share data)\n\nRevenue:\n  Subscription and recurring software services: $485,250\n  Professional services and maintenance: $62,180\n  Total Gross Revenue: $547,430\n\nCost of Revenue: $140,500\nGross Profit: $406,930 (Gross Margin: 74.3%)\nOperating Expenses: $326,500\nOperating Income (EBIT): $80,430\nAdjusted EBITDA: $112,650\nNet Income Attributable to Stockholders: $62,380\nDiluted Earnings Per Share: $1.42. Contact CFO Office: cfo@enterprise.org on March 15, 2026.`,
      medical: `CLINICAL INPATIENT ADMISSION NOTE & DISCHARGE SUMMARY\nPatient Name: Johnathan Doe | MRN: 984-210-4491 | DOB: 1982-04-15\nAdmit Date: 2026-06-10 | Discharge Date: 2026-06-14 | Attending Physician: Dr. Sarah Jenkins, MD\n\nChief Complaint: Acute substernal chest discomfort and dyspnea on exertion.\nDiagnostic Lab Work: Complete Blood Count (CBC) normal, 12-Lead ECG normal sinus rhythm at 72 bpm.\nHospital Course & Plan: Patient monitored in telemetry unit for 72 hours. Symptoms resolved with nitroglycerin. Discharged home in stable condition with outpatient cardiology follow-up on July 02, 2026.`
    };

    if (samples[type]) {
      document.getElementById("docInput").value = samples[type];
      if (autoRun) {
        this.runAnalysis();
      }
    }
  },

  exportCurrent(format) {
    if (!currentAnalysisReport) {
      App.showToast("No analysis to export. Please analyze a document first.", "warning");
      return;
    }

    if (format === 'json') {
      const jsonStr = JSON.stringify(currentAnalysisReport, null, 2);
      App.downloadFile("document_intelligence_report.json", jsonStr, "application/json");
      App.showToast("Exported JSON report!", "success");
    } else if (format === 'csv') {
      let csv = "Entity Text,Type,Category,Confidence\n";
      (currentAnalysisReport.entities || []).forEach(e => {
        csv += `"${(e.text || '').replace(/"/g, '""')}","${e.type}","${e.category}",${e.confidence}\n`;
      });
      App.downloadFile("extracted_entities.csv", csv, "text/csv");
      App.showToast("Exported CSV entities!", "success");
    } else if (format === 'markdown') {
      let md = `# AI Document Intelligence Report\n\n`;
      md += `**Classification:** ${currentAnalysisReport.classification.category} (${Math.round(currentAnalysisReport.classification.confidence*100)}%)\n\n`;
      md += `## Executive Summary\n${currentAnalysisReport.summary.extractive}\n\n`;
      md += `## Risk Score: ${currentAnalysisReport.risk.overall_risk_score}/100 (${currentAnalysisReport.risk.risk_level})\n\n`;
      App.downloadFile("analysis_report.md", md, "text/markdown");
      App.showToast("Exported Markdown report!", "success");
    } else if (format === 'html') {
      const printWin = window.open('', '_blank');
      printWin.document.write(`
        <html><head><title>AI Document Intelligence Report</title>
        <style>body{font-family:sans-serif;padding:30px;line-height:1.6;color:#1e293b;max-width:850px;margin:0 auto;} h1{color:#4338ca;} h2{color:#334155;border-bottom:1px solid #cbd5e1;padding-bottom:6px;} .badge{background:#e0e7ff;color:#3730a3;padding:4px 8px;border-radius:4px;font-weight:bold;font-size:12px;}</style></head>
        <body>
          <h1>AI Document Intelligence Report</h1>
          <p><span class="badge">${currentAnalysisReport.classification.category}</span> &bull; Risk Index: <strong>${currentAnalysisReport.risk.overall_risk_score}/100</strong></p>
          <h2>Executive Summary</h2>
          <p>${currentAnalysisReport.summary.extractive}</p>
          <h2>Risk Assessment</h2>
          <p>Level: <strong>${currentAnalysisReport.risk.risk_level}</strong></p>
          <script>window.print();</script>
        </body></html>
      `);
      printWin.document.close();
      App.showToast("Opened print-ready report!", "success");
    }
  }
};

document.addEventListener("DOMContentLoaded", () => Analyzer.init());
