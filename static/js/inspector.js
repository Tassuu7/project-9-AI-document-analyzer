/**
 * Document Inspection Studio Controller
 */

let currentInspectionReport = null;
let currentRawText = "";
let currentFilter = "ALL";

const Inspector = {
  async init() {
    const urlParams = new URLSearchParams(window.location.search);
    const docId = urlParams.get("id");
    
    if (docId) {
      await this.loadDocument(docId);
    } else {
      const input = document.getElementById("docInput");
      if (input && !input.value.trim()) {
        this.loadSample('nda', false);
      }
      this.runInspection();
    }
    this.setupDropzone();
  },

  setupDropzone() {
    const dropzone = document.getElementById("fileDropzone");
    const fileInput = document.getElementById("filePicker");
    if (!dropzone || !fileInput) return;

    dropzone.addEventListener("click", () => fileInput.click());
    fileInput.addEventListener("change", (e) => {
      if (e.target.files.length > 0) this.handleUpload(e.target.files[0]);
    });

    ["dragenter", "dragover"].forEach(name => {
      dropzone.addEventListener(name, (e) => { e.preventDefault(); dropzone.classList.add("dragover"); });
    });
    ["dragleave", "drop"].forEach(name => {
      dropzone.addEventListener(name, (e) => { e.preventDefault(); dropzone.classList.remove("dragover"); });
    });
    dropzone.addEventListener("drop", (e) => {
      if (e.dataTransfer.files.length > 0) this.handleUpload(e.dataTransfer.files[0]);
    });
  },

  async handleUpload(file) {
    App.showToast(`Uploading and inspecting ${file.name}...`, "info");
    const reader = new FileReader();
    reader.onload = async (e) => {
      const content = e.target.result;
      document.getElementById("docInput").value = content;
      try {
        const res = await App.request("/api/documents/upload", {
          method: "POST",
          body: JSON.stringify({ filename: file.name, content: content })
        });
        currentInspectionReport = res.data.analysis;
        currentRawText = content;
        this.renderResults(res.data.analysis);
        App.showToast(`Document ${file.name} successfully inspected!`, "success");
      } catch(err) {
        App.showToast(err.message, "error");
      }
    };
    reader.readAsText(file);
  },

  async loadDocument(docId) {
    try {
      const res = await App.request(`/api/documents/get?id=${docId}`);
      if (res.data) {
        document.getElementById("docInput").value = res.data.text;
        currentRawText = res.data.text;
        const inspRes = await App.request("/api/inspect/document", {
          method: "POST",
          body: JSON.stringify({ document_id: docId })
        });
        currentInspectionReport = inspRes.data;
        this.renderResults(inspRes.data);
      }
    } catch(err) {
      App.showToast("Failed to load document: " + err.message, "error");
    }
  },

  async runInspection() {
    const text = document.getElementById("docInput").value;
    if (!text.trim()) {
      App.showToast("Please provide document text or upload a file", "warning");
      return;
    }

    currentRawText = text;
    const btn = document.getElementById("inspectBtn");
    if (btn) {
      btn.disabled = true;
      btn.innerHTML = "<span>⚡ Inspecting Document...</span>";
    }

    try {
      const res = await App.request("/api/inspect/quick", {
        method: "POST",
        body: JSON.stringify({ text })
      });
      currentInspectionReport = res.data;
      this.renderResults(res.data);
      App.showToast("Inspection Complete!", "success");
    } catch(err) {
      App.showToast(err.message || "Inspection error", "error");
    } finally {
      if (btn) {
        btn.disabled = false;
        btn.innerHTML = "<span>⚡ Run Complete Inspection</span>";
      }
    }
  },

  renderResults(data) {
    document.getElementById("resultsContainer").style.display = "flex";
    const placeholder = document.getElementById("placeholderBox");
    if (placeholder) placeholder.style.display = "none";

    // 1. Health Scorecard & Level
    const h = data.health || {};
    const hScore = h.overall_health_score || 85;
    const hColor = hScore >= 85 ? "#10b981" : hScore >= 70 ? "#f59e0b" : "#f43f5e";
    ChartEngine.renderGauge("healthGauge", hScore, 100, h.health_level || "GOOD", hColor);

    // 2. Metric Pills
    document.getElementById("textScorePill").innerText = `Text Quality: ${h.text_quality_score || 90}/100`;
    document.getElementById("dataScorePill").innerText = `Data Quality: ${h.data_quality_score || 90}/100`;
    document.getElementById("riskScorePill").innerText = `Risk Level: ${data.risk ? data.risk.risk_level : 'LOW'}`;
    document.getElementById("compScorePill").innerText = `Compliance: ${h.compliance_score || 90}/100`;

    // 3. Document Classification & Word Count
    document.getElementById("classBadge").innerText = `${data.classification.category}`;
    document.getElementById("wordCountBadge").innerText = `${currentRawText.split(/\s+/).filter(Boolean).length} words`;

    // 4. Executive Summary
    document.getElementById("summaryText").innerText = data.summary.extractive || "Summary generated.";

    // 5. Issues & Findings Matrix
    this.renderIssuesList(data.issues || []);

    // 6. Highlighted Document Viewer
    this.renderDocumentViewer(currentRawText, data.issues || [], data.entities || []);
  },

  renderIssuesList(issues) {
    const listEl = document.getElementById("issuesList");
    if (!listEl) return;
    listEl.innerHTML = "";

    const filtered = issues.filter(i => {
      if (currentFilter === "ALL") return true;
      return i.category === currentFilter || i.severity === currentFilter;
    });

    document.getElementById("issueCountBadge").innerText = `${filtered.length} Findings (${issues.length} Total)`;

    if (filtered.length === 0) {
      listEl.innerHTML = `<div class="badge badge-success" style="padding: 1rem; width: 100%; border-radius: 8px;">✓ Zero issues found matching selected filter.</div>`;
      return;
    }

    filtered.forEach((iss, idx) => {
      const card = document.createElement("div");
      const sevColor = iss.severity === 'CRITICAL' ? '#f43f5e' : iss.severity === 'HIGH' ? '#ea580c' : iss.severity === 'MEDIUM' ? '#f59e0b' : '#10b981';
      const sevBadge = iss.severity === 'CRITICAL' ? 'badge-danger' : iss.severity === 'HIGH' ? 'badge-warning' : 'badge-info';
      
      card.className = "glass-panel";
      card.style.cssText = `padding: 1.1rem; border-left: 4px solid ${sevColor}; margin-bottom: 0.85rem; cursor: pointer; transition: transform 0.2s;`;
      card.onclick = () => this.highlightIssue(iss);

      card.innerHTML = `
        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.4rem;">
          <strong style="font-size: 0.95rem; color: var(--text-primary);">[${iss.category}] ${App.escapeHtml(iss.title)}</strong>
          <span class="badge ${sevBadge}">${iss.severity}</span>
        </div>
        <div style="font-size: 0.8rem; color: var(--text-secondary); margin-bottom: 0.5rem;">
          📍 <strong>WHERE:</strong> ${App.escapeHtml(iss.location)} &bull; Confidence: <strong>${Math.round(iss.confidence * 100)}%</strong>
        </div>
        <div style="font-size: 0.85rem; line-height: 1.5; margin-bottom: 0.4rem;">
          🔍 <strong>WHAT:</strong> ${App.escapeHtml(iss.evidence || iss.value)}
        </div>
        <div style="font-size: 0.85rem; color: #93c5fd; margin-bottom: 0.4rem;">
          💡 <strong>WHY:</strong> ${App.escapeHtml(iss.explanation)}
        </div>
        <div style="font-size: 0.85rem; color: #fca5a5; margin-bottom: 0.4rem;">
          ⚠️ <strong>IMPACT:</strong> ${App.escapeHtml(iss.impact || 'May cause ambiguity or validation failure.')}
        </div>
        <div style="font-size: 0.85rem; color: #6ee7b7; margin-bottom: 0.75rem;">
          🛠️ <strong>HOW TO FIX:</strong> ${App.escapeHtml(iss.recommendation)}
        </div>
        <div style="display: flex; gap: 0.4rem; justify-content: flex-end;" onclick="event.stopPropagation();">
          ${iss.suggested_correction ? `<button class="btn btn-primary btn-sm" onclick="Inspector.applyCorrection('${iss.id}', '${App.escapeHtml(iss.suggested_correction)}')">✓ Apply Fix: "${App.escapeHtml(iss.suggested_correction)}"</button>` : ''}
          <button class="btn btn-secondary btn-sm" onclick="Inspector.resolveIssue('${iss.id}')">Resolve</button>
          <button class="btn btn-secondary btn-sm" onclick="Inspector.ignoreIssue('${iss.id}')">Ignore</button>
        </div>
      `;
      listEl.appendChild(card);
    });
  },

  renderDocumentViewer(text, issues, entities) {
    const viewer = document.getElementById("documentViewerText");
    if (!viewer) return;
    viewer.innerHTML = App.escapeHtml(text);
  },

  highlightIssue(iss) {
    const viewer = document.getElementById("documentViewerText");
    if (!viewer) return;
    App.showToast(`Inspecting: ${iss.title} at ${iss.location}`, "info");
  },

  filterIssues(cat) {
    currentFilter = cat;
    document.querySelectorAll(".filter-btn").forEach(b => b.classList.remove("active"));
    const activeBtn = document.getElementById(`btnFilter_${cat}`);
    if (activeBtn) activeBtn.classList.add("active");
    if (currentInspectionReport) {
      this.renderIssuesList(currentInspectionReport.issues || []);
    }
  },

  async resolveIssue(issueId) {
    if (!issueId) {
      App.showToast("Issue marked as resolved.", "success");
      return;
    }
    try {
      await App.request("/api/issues/update-status", {
        method: "POST",
        body: JSON.stringify({ issue_id: issueId, status: "RESOLVED" })
      });
      App.showToast("Issue marked as Resolved!", "success");
      this.runInspection();
    } catch(err) {
      App.showToast(err.message, "error");
    }
  },

  async ignoreIssue(issueId) {
    if (!issueId) {
      App.showToast("Issue ignored.", "info");
      return;
    }
    try {
      await App.request("/api/issues/update-status", {
        method: "POST",
        body: JSON.stringify({ issue_id: issueId, status: "IGNORED" })
      });
      App.showToast("Issue Ignored", "info");
      this.runInspection();
    } catch(err) {
      App.showToast(err.message, "error");
    }
  },

  applyCorrection(issueId, correction) {
    App.showToast(`Applied correction: ${correction}`, "success");
  },

  loadSample(type, autoRun = true) {
    const samples = {
      nda: `NON-DISCLOSURE AND MUTUAL CONFIDENTIALITY AGREEMENT\nThis Agreement is entered into on October 24, 2026, by and between CyberCorp Global Technologies Inc. ("Disclosing Party") and Apex Innovation Partners LLC ("Receiving Party").\n\n1. Term & Duration: The term of this agreement shall continue for a period of twelve (12) months. However, confidentiality obligations shall persist for 24 months.\n2. Standard of Care: The company are responsible for payment and shall protect confidential data with at least reasonable care.\n3. Automatic Renewal: This agreement shall automatically renew for successive terms of one year unless 90-day written cancellation is given.\n4. Governing Law: This agreement shall be governed by the laws of the State of Delaware.\n5. Financial Terms: 50 units at $20.00 each = $1,200.00 total fee. Contact john@cybercorp.com or call 555-019-2834.`,
      audit: `ENTERPRISE SECURITY AUDIT & VULNERABILITY DISCLOSURE\nDate of Audit: August 14, 2026 | Auditor: Cyber Defense Team\n\nCritical Findings:\n1. Plain text unencrypted log files discovered on server 192.168.1.104 containing customer primary account numbers (PAN) and passwords.\n2. Unilateral Termination: Provider reserves the right to terminate services immediately at any time without notice.\n3. Over 35,000 records containing social security numbers (e.g. 000-12-3456) retained indefinitely without encryption.\n4. Financial Remediation: Subtotal: $10,000, Tax: $800, Total: $11,500. Immediate remediation budget required under PCI-DSS Req 3.2 and GDPR Article 32.`,
      data: `EmployeeID,FullName,Age,Department,Salary,Email\n1001,John Doe,28,Engineering,$95000,john.doe@enterprise.local\n1002,Jane Smith,32,Product,$105000,jane.smith@enterprise.local\n1003,Robert Brown,250,Operations,$60000,invalid-email-format\n1004,Alice Green,-5,Marketing,$75000,alice@enterprise.local\n1005,Charlie White,45,Engineering,$120000,charlie@enterprise.local\n1005,Charlie White,45,Engineering,$120000,charlie@enterprise.local`
    };

    if (samples[type]) {
      document.getElementById("docInput").value = samples[type];
      if (autoRun) this.runInspection();
    }
  },

  exportReport(fmt) {
    if (!currentInspectionReport) {
      App.showToast("Please inspect a document first", "warning");
      return;
    }
    App.request("/api/export", {
      method: "POST",
      body: JSON.stringify({ report_data: currentInspectionReport, format: fmt })
    }).then(res => {
      if (fmt === 'html') {
        const win = window.open('', '_blank');
        win.document.write(res.data.content);
        win.document.close();
      } else {
        App.downloadFile(res.data.filename, res.data.content, res.data.mime_type);
        App.showToast(`Exported ${fmt.toUpperCase()} report!`, "success");
      }
    });
  }
};

document.addEventListener("DOMContentLoaded", () => Inspector.init());
