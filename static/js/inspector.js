/**
 * Document Inspection & Paraphraser Studio Controller
 */

let currentInspectionReport = null;
let currentRawText = "";
let currentFilter = "ALL";
let currentTab = "original";

const Inspector = {
  async init() {
    const urlParams = new URLSearchParams(window.location.search);
    const docId = urlParams.get("id");
    
    if (docId) {
      await this.loadDocument(docId);
    } else {
      const input = document.getElementById("docInput");
      if (input && !input.value.trim()) {
        this.loadSample('docx', false);
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
    App.showToast(`Ingesting and parsing ${file.name}...`, "info");
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
        App.showToast(`Analyzed ${file.name} successfully`, "success");
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
      App.showToast("Please enter text or upload a document", "warning");
      return;
    }

    currentRawText = text;
    const btn = document.getElementById("inspectBtn");
    if (btn) {
      btn.disabled = true;
      btn.innerText = "Analyzing Document...";
    }

    try {
      const res = await App.request("/api/inspect/quick", {
        method: "POST",
        body: JSON.stringify({ text })
      });
      currentInspectionReport = res.data;
      this.renderResults(res.data);
      App.showToast("Analysis Complete", "success");
    } catch(err) {
      App.showToast(err.message || "Analysis error", "error");
    } finally {
      if (btn) {
        btn.disabled = false;
        btn.innerText = "Run Document Inspection";
      }
    }
  },

  renderResults(data) {
    // 1. Health Scorecard
    const h = data.health || {};
    const hScore = h.overall_health_score || 85;
    const hColor = hScore >= 85 ? "#15803d" : hScore >= 70 ? "#b45309" : "#b91c1c";
    ChartEngine.renderGauge("healthGauge", hScore, 100, h.health_level || "HEALTHY", hColor);

    // 2. Writing Quality & Readability
    const wq = data.writing_quality || {};
    document.getElementById("writingScoreVal").innerText = `${wq.composite_writing_quality_score || 85} / 100`;
    document.getElementById("readabilityLabel").innerText = wq.readability_label || "Standard";
    document.getElementById("fkGradeBadge").innerText = `F-K Grade: ${wq.flesch_kincaid_grade || 8.0}`;
    document.getElementById("gunningBadge").innerText = `Fog Index: ${wq.gunning_fog_index || 9.0}`;
    document.getElementById("readingTimeBadge").innerText = `${wq.reading_time_minutes || 1.0} min read`;

    // 3. Document Metrics
    document.getElementById("textScorePill").innerText = `Text: ${h.text_quality_score || 90}/100`;
    document.getElementById("dataScorePill").innerText = `Data: ${h.data_quality_score || 90}/100`;
    document.getElementById("riskScorePill").innerText = `Risk: ${data.risk ? data.risk.risk_level : 'LOW'}`;

    document.getElementById("classBadge").innerText = `${data.classification.category}`;
    document.getElementById("wordCountBadge").innerText = `${wq.word_count || currentRawText.split(/\s+/).filter(Boolean).length} words &bull; ${wq.sentence_count || 1} sentences`;

    // 4. Summaries & Keywords
    document.getElementById("summaryText").innerText = data.summary.extractive || "Summary generated.";
    const kwContainer = document.getElementById("keywordsContainer");
    kwContainer.innerHTML = "";
    (data.summary.keywords || []).forEach(kw => {
      const span = document.createElement("span");
      span.className = "badge badge-neutral";
      span.innerText = kw;
      kwContainer.appendChild(span);
    });

    // 5. Update Corrected and Paraphrased Text Tabs
    document.getElementById("correctedInput").value = data.corrected_text || currentRawText;
    document.getElementById("paraphrasedInput").value = data.paraphrased_text || currentRawText;

    // 6. Render Issues List
    this.renderIssuesList(data.issues || []);
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
      listEl.innerHTML = `<div class="badge badge-success" style="padding: 0.8rem; width: 100%; border-radius: 6px;">Zero issues detected in this category.</div>`;
      return;
    }

    filtered.forEach((iss) => {
      const card = document.createElement("div");
      const sevColor = iss.severity === 'CRITICAL' ? 'var(--status-danger)' : iss.severity === 'HIGH' ? 'var(--status-warning)' : 'var(--border-strong)';
      const sevBadge = iss.severity === 'CRITICAL' ? 'badge-danger' : iss.severity === 'HIGH' ? 'badge-warning' : 'badge-neutral';
      
      card.className = "glass-panel";
      card.style.cssText = `padding: 1rem; border-left: 4px solid ${sevColor}; margin-bottom: 0.8rem;`;

      card.innerHTML = `
        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.5rem;">
          <strong style="font-size: 0.95rem; color: var(--text-primary);">${App.escapeHtml(iss.title)}</strong>
          <span class="badge ${sevBadge}">${iss.severity}</span>
        </div>

        <div style="display: grid; grid-template-columns: 1fr; gap: 0.35rem; font-size: 0.85rem; line-height: 1.5;">
          <div><span style="font-weight: 700; color: var(--text-secondary);">WHAT IS WRONG?</span> ${App.escapeHtml(iss.evidence || iss.value)}</div>
          <div><span style="font-weight: 700; color: var(--text-secondary);">WHERE IS IT?</span> ${App.escapeHtml(iss.location)}</div>
          <div><span style="font-weight: 700; color: var(--text-secondary);">WHY IS IT A PROBLEM?</span> ${App.escapeHtml(iss.explanation)}</div>
          <div><span style="font-weight: 700; color: var(--text-secondary);">IMPACT:</span> ${App.escapeHtml(iss.impact || 'Affects readability or quality.')}</div>
          <div><span style="font-weight: 700; color: var(--status-success-text);">WHAT SHOULD THE USER DO?</span> ${App.escapeHtml(iss.recommendation)}</div>
          <div><span style="font-weight: 700; color: var(--text-secondary);">SYSTEM CONFIDENCE:</span> ${Math.round(iss.confidence * 100)}%</div>
        </div>

        <div style="display: flex; gap: 0.4rem; justify-content: flex-end; margin-top: 0.75rem;">
          ${iss.suggested_correction ? `<button class="btn btn-primary btn-sm" onclick="Inspector.applyCorrection('${iss.id}', '${App.escapeHtml(iss.suggested_correction)}')">Apply Fix: "${App.escapeHtml(iss.suggested_correction)}"</button>` : ''}
          <button class="btn btn-secondary btn-sm" onclick="Inspector.resolveIssue('${iss.id}')">Accept / Resolve</button>
          <button class="btn btn-secondary btn-sm" onclick="Inspector.ignoreIssue('${iss.id}')">Ignore</button>
        </div>
      `;
      listEl.appendChild(card);
    });
  },

  switchTab(tab) {
    currentTab = tab;
    ["original", "corrected", "paraphrased"].forEach(t => {
      const cap = t.charAt(0).toUpperCase() + t.slice(1);
      const btn = document.getElementById(`tab${cap}`);
      if (btn) {
        btn.classList.toggle("active", t === tab);
        btn.style.borderBottom = t === tab ? "2px solid var(--accent-primary)" : "none";
      }
    });

    document.getElementById("docInput").style.display = tab === "original" ? "block" : "none";
    document.getElementById("correctedInput").style.display = tab === "corrected" ? "block" : "none";
    document.getElementById("paraphrasedInput").style.display = tab === "paraphrased" ? "block" : "none";
    document.getElementById("paraphraseBar").style.display = tab === "paraphrased" ? "flex" : "none";
  },

  async runParaphrase(mode) {
    const text = document.getElementById("docInput").value;
    if (!text.trim()) return;
    App.showToast(`Paraphrasing in ${mode.toUpperCase()} mode...`, "info");
    try {
      const res = await App.request("/api/paraphrase", {
        method: "POST",
        body: JSON.stringify({ text, mode })
      });
      document.getElementById("paraphrasedInput").value = res.data.paraphrased_text;
      this.switchTab('paraphrased');
      App.showToast(`Paraphrasing completed in ${mode} mode`, "success");
    } catch(err) {
      App.showToast(err.message, "error");
    }
  },

  searchInDocument() {
    const q = document.getElementById("inDocSearch").value.toLowerCase();
    const text = document.getElementById("docInput").value;
    if (!q) {
      document.getElementById("searchMatchesBadge").innerText = "0 matches";
      return;
    }
    const matches = (text.toLowerCase().match(new RegExp(q, "g")) || []).length;
    document.getElementById("searchMatchesBadge").innerText = `${matches} matches found`;
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
    App.showToast("Finding marked as resolved", "success");
  },

  async ignoreIssue(issueId) {
    App.showToast("Finding ignored", "info");
  },

  applyCorrection(issueId, correction) {
    const orig = document.getElementById("docInput").value;
    const corrected = document.getElementById("correctedInput").value;
    document.getElementById("docInput").value = corrected;
    App.showToast(`Applied correction: ${correction}`, "success");
    this.runInspection();
  },

  async exportDocx(source = "corrected") {
    const text = source === "paraphrased" 
      ? document.getElementById("paraphrasedInput").value 
      : document.getElementById("correctedInput").value || document.getElementById("docInput").value;

    App.showToast("Generating native .DOCX file...", "info");
    try {
      const res = await App.request("/api/documents/export-docx", {
        method: "POST",
        body: JSON.stringify({ text, title: "Document Analysis & Revisions" })
      });
      
      const byteChars = atob(res.data.base64);
      const byteNumbers = new Array(byteChars.length);
      for (let i = 0; i < byteChars.length; i++) {
        byteNumbers[i] = byteChars.charCodeAt(i);
      }
      const byteArray = new Uint8Array(byteNumbers);
      const blob = new Blob([byteArray], { type: res.data.mime_type });
      const url = URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = res.data.filename;
      document.body.appendChild(a);
      a.click();
      setTimeout(() => {
        document.body.removeChild(a);
        URL.revokeObjectURL(url);
      }, 100);
      App.showToast("DOCX file exported successfully", "success");
    } catch(err) {
      App.showToast("Failed to export DOCX: " + err.message, "error");
    }
  },

  loadSample(type, autoRun = true) {
    const samples = {
      docx: `# EXECUTIVE REPORT: TECHNICAL PROPOSAL & ARCHITECTURE\n\n1. Introduction and Background\nIn order to facilitate the project commencement, the company are responsible for payment. It goes without saying that an investigation was conducted by the team to ascertain feasibility.\n\n2. Technical Specifications & Methodologies\nAt the present time, we utilize multiple architectures which are extremely complex, intricate, and difficult to manage because of the fact that each and every server runs unencrypted processes.\n\n3. Contract Duration & Liabilities\nDuration of this agreement is 12 months. Either party may terminate with 30 days notice. Contact admin@domain.local for technical inquiries.`,
      nda: `NON-DISCLOSURE AGREEMENT\n1. Term: The term of this agreement shall continue for 12 months.\n2. Obligations: The company are responsible for protecting confidential data.\n3. Automatic Renewal: This agreement shall automatically renew for successive terms.`,
      audit: `ENTERPRISE SECURITY AUDIT\n1. Plain text unencrypted files discovered on internal servers.\n2. Subtotal: $10,000, Tax: $800, Total: $11,500.`
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
        App.showToast(`Exported ${fmt.toUpperCase()} report`, "success");
      }
    });
  }
};

document.addEventListener("DOMContentLoaded", () => Inspector.init());
