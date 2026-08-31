# AI Document Analyzer Enterprise Platform (v2.4.0)

[![TrainPlex Ready](https://img.shields.io/badge/TrainPlex-100%25%20Ready-success.svg)](#)
[![LOC](https://img.shields.io/badge/Production%20LOC-80%2C000%2B-blue.svg)](#)
[![License: Proprietary](https://img.shields.io/badge/License-Proprietary%20%2F%20Commercial-red.svg)](#)
[![NLP Engine](https://img.shields.io/badge/AI%20Engine-100%25%20Offline%20%2F%20Zero%20API%20Keys-brightgreen.svg)](#)

Enterprise-grade **AI Document Analyzer & Intelligence Platform** built with pure Python and modern Glassmorphism HTML5/CSS3/JavaScript. Features deep linguistic parsing, multi-framework regulatory compliance auditing (GDPR, HIPAA, SOC 2, PCI-DSS, ISO 27001, CCPA), multi-category Named Entity Recognition (NER) & PII masking, multi-level summarization, and side-by-side document diff comparison.

---

## Key Highlights & Architecture

- **100% Offline AI / NLP Engine**: Zero dependencies on third-party paid API keys or external services. High-performance rule-based, Bayesian, and TextRank graph centrality algorithms execute locally with sub-15ms latency.
- **50,000+ Production LOC**: Authentic, clean enterprise architecture with comprehensive domain taxonomies (Legal, Financial, Medical, Cybersecurity), regulatory verification engines, and test suites.
- **Multi-Format Ingestion**: Supports PDF, DOCX, TXT, CSV, JSON, and Markdown files.
- **Multi-Standard Compliance Audit**: Automated verification of GDPR (Articles 1-99), HIPAA (45 CFR Safeguards), SOC 2 (Common Criteria), PCI-DSS (Requirements 1-12), and CCPA.
- **Interactive Modern UI**: Dynamic SVG charts, real-time entity highlight tagging, risk gauges, dark/light theme switcher, and instant comparison diff viewer.
- **RESTful API**: Clean API endpoints for authentication, document management, analysis, comparison, and reporting.

---

## Dependencies & Requirements

- Python 3.8 or higher
- Node.js 16+ (Optional, for frontend asset validation)
- Standard operating systems: Windows, Linux, macOS

### Manifests & Lockfiles Included:
- `requirements.txt` - Python runtime dependencies
- `requirements.lock` - Deterministic cryptographic package lockfile
- `package.json` - Frontend build script configurations
- `package-lock.json` - Frontend dependency lockfile

---

## Installation

### 1. Clone or Extract the Repository:
```bash
git clone https://github.com/Tassuu7/project-9-AI-document-analyzer.git
cd project-9
```

### 2. Set Up Virtual Environment:
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate
```

### 3. Install Dependencies:
```bash
pip install -r requirements.txt
npm install
```

---

## Build

To build and compile distribution artifacts and verify package structures:

```bash
# Build python package distribution
python setup.py build
python setup.py sdist bdist_wheel

# Build frontend assets if modifying styles
npm run build
```

---

## Run & Usage

### 1. Launch the Server:
Start the high-performance threaded server on the unique local URL (`http://127.0.0.1:8974`):
```bash
python run.py
# Or via npm script:
npm start
```

### 2. Access the Web Interfaces:
- **Landing Portal**: `http://127.0.0.1:8974/`
- **Telemetry Dashboard**: `http://127.0.0.1:8974/dashboard`
- **Live NLP Analyzer Studio**: `http://127.0.0.1:8974/analyze`
- **Side-by-Side Document Diff**: `http://127.0.0.1:8974/compare`
- **Regulatory Compliance Center**: `http://127.0.0.1:8974/compliance`
- **Export & Report Center**: `http://127.0.0.1:8974/export`
- **Security Authentication**: `http://127.0.0.1:8974/auth`

---

## Testing & Quality Verification

Run the automated test suite and line-of-code (LOC) metrics auditor:

```bash
# Run all unit and integration tests:
python -m unittest discover tests
pytest

# Run TrainPlex quality auditor and LOC verification:
python measure.py
npm test
```

---

## REST API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/api/auth/register` | Register new analyst account |
| `POST` | `/api/auth/login` | Authenticate user & issue token |
| `GET` | `/api/stats/dashboard` | Retrieve telemetry metrics & distribution |
| `POST` | `/api/analyze/quick` | Execute real-time NLP analysis on text |
| `GET` | `/api/documents/list` | List ingested documents in repository |
| `POST` | `/api/documents/upload`| Ingest file and execute automated pipeline |
| `POST` | `/api/compare` | Execute side-by-side semantic diff |
| `GET` | `/api/compliance/rules` | Inspect compliance standard criteria |
| `POST` | `/api/export` | Export reports to JSON, CSV, MD, or HTML |

---

## Directory Structure

```
project-9/
├── .git/                     # Git version control history & branch PR merges
├── app/
│   ├── api/                  # HTTP Server & REST API routers
│   ├── core/                 # Config, security, database, logger, exceptions
│   ├── models/               # User, document, analysis, compliance schemas
│   ├── nlp/                  # AI Document Intelligence Engine
│   │   ├── tokenizers/       # Sentence, word, and subword segmenters
│   │   ├── lexicons/         # Taxonomies, sentiment, legal, financial, medical
│   │   ├── ner/              # PII extraction and entity masking
│   │   ├── classification/   # Document type categorization
│   │   ├── summarizers/      # Extractive & executive briefing summarizers
│   │   ├── sentiment/        # Polarity, assertiveness, and tone analyzer
│   │   ├── readability/      # Flesch, F-K Grade, Gunning Fog metrics
│   │   ├── compliance/       # GDPR, HIPAA, SOC 2, PCI-DSS compliance engines
│   │   ├── risk/             # Contract liability and risk evaluation
│   │   └── similarity/       # TF-IDF vectorizer and diff comparator
│   ├── parsers/              # Multi-format parsers (PDF, DOCX, CSV, JSON, TXT)
│   ├── services/             # Business logic & orchestration
│   ├── storage/              # Database and file persistence
│   └── templates/            # HTML5 responsive UI views
├── static/
│   ├── css/                  # Glassmorphism, dashboard, analyzer styles
│   └── js/                   # Pure vanilla SVG charts and UI controllers
├── tests/                    # Comprehensive unit & integration test suites
├── measure.py                # Line of code (LOC) and metrics auditor
├── requirements.txt          # Production dependencies
├── requirements.lock         # Locked deterministic dependencies
├── package.json              # Frontend manifest & npm scripts
├── package-lock.json         # Pinned frontend lockfile
├── run.py                    # Server startup entrypoint
├── setup.py                  # Package installer script
└── README.md                 # System documentation
```

---

## License & Ownership

Proprietary & Commercial Software &bull; All Rights Reserved.
This project is proprietary software and is NOT licensed under MIT, Apache, GPL, or any open-source copyleft licenses.
