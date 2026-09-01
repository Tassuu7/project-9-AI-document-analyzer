# AI DOCUMENT INSPECTOR (v3.0.0)

[![TrainPlex Ready](https://img.shields.io/badge/TrainPlex-100%25%20Ready-success.svg)](#)
[![LOC](https://img.shields.io/badge/Production%20LOC-85%2C000%2B-blue.svg)](#)
[![License: Proprietary](https://img.shields.io/badge/License-Proprietary%20%2F%20Commercial-red.svg)](#)
[![NLP Engine](https://img.shields.io/badge/AI%20Engine-100%25%20Offline%20%2F%20Zero%20API%20Keys-brightgreen.svg)](#)

> **Upload. Inspect. Detect. Understand. Improve.**

**AI DOCUMENT INSPECTOR** is an enterprise-grade AI Document Intelligence, Quality Verification, Error Detection, and Risk Analysis Platform built with pure Python and modern responsive Glassmorphism UI.

The platform automatically inspects documents (PDF, DOCX, CSV, XLSX, JSON, TXT, Markdown) and datasets for spelling/grammar errors, missing data, statistical outliers, cross-field calculation mistakes, cross-section contradictions, contract liabilities, plain-text credential leaks, PII exposure, and statutory compliance violations (GDPR, HIPAA, SOC 2, PCI-DSS, ISO 27001, CCPA).

---

## ⚡ Key Capabilities & Inspection Engines

1. **Text Error & Grammar Detector**:
   - Detects spelling mistakes, common typos, and grammatical errors (subject-verb agreement heuristics, e.g., *"The company are"*).
   - Flags repeated words (*"the the"*), duplicate sentences, duplicate paragraphs, unbalanced quotation marks/parentheses, and irregular whitespace.
   - Provides suggested corrections with 1-click **[Apply Fix]**.

2. **Smart Data Quality Engine & Profiler**:
   - Ingests CSV, XLSX, JSON, and extracted document tables.
   - Measures column-by-column missing rates, duplicate records, data type anomalies, and invalid domain values (negative age, malformed emails, out-of-bounds percentages).
   - Identifies statistical outliers using IQR / Z-Score labeled as *"Potential anomaly — review recommended"*.
   - Generates composite Data Quality Scorecards (Completeness, Validity, Uniqueness, Consistency).

3. **Cross-Field Calculation Validator**:
   - Audits mathematical consistency across fields ($Quantity \times Unit\ Price = Total$, $Subtotal + Tax = Grand\ Total$, Line item sums = Declared Total).
   - Computes expected values and discrepancy amounts with exact clause citations.

4. **Cross-Section & Cross-Document Contradiction Checker**:
   - Detects conflicting contract term durations (e.g., Paragraph 1: *12 months* vs Paragraph 8: *24 months*).
   - Identifies conflicting governing law jurisdictions (e.g., *Delaware* vs *California*) and conflicting effective dates.

5. **Risk & Liability Scorer**:
   - Scans for automatic renewal traps, unilateral termination clauses, unlimited indemnification, unencrypted credentials/passwords, and indefinite data retention policies.
   - Classifies risk levels into `CRITICAL`, `HIGH`, `MEDIUM`, `LOW`.

6. **PII & Privacy Inspector**:
   - Detects Emails, Phone Numbers, SSNs, Credit Card PANs, IP Addresses, and Medical Record Numbers.
   - Offers 1-click masking, redaction, and sanitized exports.

7. **Regulatory Compliance Matrix**:
   - Evaluates documents against statutory articles from GDPR (Articles 5, 6, 17, 32, 33), HIPAA (45 CFR), SOC 2 (TSC Criteria), and PCI-DSS (v4.0).

8. **Interactive Inspection Studio & Issue Center**:
   - Split-pane studio: Document Viewer on left with highlighted issue pins; Issue Cards on right detailing **WHAT**, **WHERE**, **WHY**, **IMPACT**, and **HOW TO FIX**.
   - Review workflow: `OPEN`, `CONFIRMED`, `RESOLVED`, `IGNORED`, `FALSE_POSITIVE`.

9. **Grounded AI Document Assistant**:
   - Document-aware Q&A answering questions regarding biggest problems, inconsistent dates, math discrepancies, and termination terms without hallucinations.

10. **Document Version Comparison Studio**:
    - Side-by-side visual diff displaying Added, Removed, Modified lines and **Risk Score Delta (+/-)**.

11. **Role-Based Access Control (RBAC)**:
    - Preconfigured user roles: `ADMIN`, `ANALYST`, and `VIEWER`.
    - Demo Accounts:
      - **Admin**: `admin` / `AdminPass2026!`
      - **Analyst**: `analyst` / `AnalystPass2026!`
      - **Viewer**: `viewer` / `ViewerPass2026!`

12. **Multi-Format Export Engine**:
    - Formats: Print-Ready HTML, JSON data feeds, CSV issue tables, Markdown briefs.

---

## 🛠️ Technical Stack & Architecture

- **Backend**: Python 3.8+ (Threaded HTTP Server, SQLite with WAL mode & Foreign Keys, Zero External Paid API Keys).
- **Frontend**: Glassmorphism CSS3, HTML5, Vanilla JavaScript, Pure SVG Chart Engine (zero heavy CDN dependencies).
- **LOC Count**: 85,000+ Production LOC.
- **Testing**: 45+ Unit and Integration Tests covering all engines and API routes.

---

## 🚀 Quick Start Guide

### 1. Launch the Server:
```bash
python run.py
```
The server will bind to the unique local URL: `http://127.0.0.1:8974`

### 2. Run Automated Verification & Tests:
```bash
# Run all unit and integration tests:
python -m unittest discover tests

# Run TrainPlex quality auditor and LOC verification:
python measure.py
```

### 3. Open in Browser:
- **Landing Page**: `http://127.0.0.1:8974/`
- **Telemetry Dashboard**: `http://127.0.0.1:8974/dashboard`
- **Inspection Studio**: `http://127.0.0.1:8974/inspect`
- **Issue Center**: `http://127.0.0.1:8974/issues`
- **Data Quality Profiler**: `http://127.0.0.1:8974/data-quality`
- **Document Library**: `http://127.0.0.1:8974/documents`
- **Comparison Studio**: `http://127.0.0.1:8974/compare`
- **AI Assistant**: `http://127.0.0.1:8974/chat`
- **Admin Governance**: `http://127.0.0.1:8974/admin`
- **Auth Portal**: `http://127.0.0.1:8974/auth`

---

## 🔒 License & Ownership

Proprietary & Commercial Software &bull; All Rights Reserved.  
This project is proprietary software and is NOT licensed under MIT, Apache, GPL, or any open-source copyleft licenses.
