"""HIPAA 45 CFR Parts 160 & 164 Safeguards Catalog."""
from typing import Dict, Any

HIPAA_SAFEGUARDS: Dict[str, Dict[str, Any]] = {
    "HIPAA_SAFEGUARD_001": {
        "id": 1,
        "cfr_section": "45 CFR § 164.301",
        "title": "HIPAA Privacy and Security Standard #1",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_002": {
        "id": 2,
        "cfr_section": "45 CFR § 164.302",
        "title": "HIPAA Privacy and Security Standard #2",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_003": {
        "id": 3,
        "cfr_section": "45 CFR § 164.303",
        "title": "HIPAA Privacy and Security Standard #3",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_004": {
        "id": 4,
        "cfr_section": "45 CFR § 164.304",
        "title": "HIPAA Privacy and Security Standard #4",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_005": {
        "id": 5,
        "cfr_section": "45 CFR § 164.305",
        "title": "HIPAA Privacy and Security Standard #5",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_006": {
        "id": 6,
        "cfr_section": "45 CFR § 164.306",
        "title": "HIPAA Privacy and Security Standard #6",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_007": {
        "id": 7,
        "cfr_section": "45 CFR § 164.307",
        "title": "HIPAA Privacy and Security Standard #7",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_008": {
        "id": 8,
        "cfr_section": "45 CFR § 164.308",
        "title": "HIPAA Privacy and Security Standard #8",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_009": {
        "id": 9,
        "cfr_section": "45 CFR § 164.309",
        "title": "HIPAA Privacy and Security Standard #9",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_010": {
        "id": 10,
        "cfr_section": "45 CFR § 164.310",
        "title": "HIPAA Privacy and Security Standard #10",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_011": {
        "id": 11,
        "cfr_section": "45 CFR § 164.311",
        "title": "HIPAA Privacy and Security Standard #11",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_012": {
        "id": 12,
        "cfr_section": "45 CFR § 164.312",
        "title": "HIPAA Privacy and Security Standard #12",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_013": {
        "id": 13,
        "cfr_section": "45 CFR § 164.313",
        "title": "HIPAA Privacy and Security Standard #13",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_014": {
        "id": 14,
        "cfr_section": "45 CFR § 164.314",
        "title": "HIPAA Privacy and Security Standard #14",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_015": {
        "id": 15,
        "cfr_section": "45 CFR § 164.315",
        "title": "HIPAA Privacy and Security Standard #15",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_016": {
        "id": 16,
        "cfr_section": "45 CFR § 164.316",
        "title": "HIPAA Privacy and Security Standard #16",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_017": {
        "id": 17,
        "cfr_section": "45 CFR § 164.317",
        "title": "HIPAA Privacy and Security Standard #17",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_018": {
        "id": 18,
        "cfr_section": "45 CFR § 164.318",
        "title": "HIPAA Privacy and Security Standard #18",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_019": {
        "id": 19,
        "cfr_section": "45 CFR § 164.319",
        "title": "HIPAA Privacy and Security Standard #19",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_020": {
        "id": 20,
        "cfr_section": "45 CFR § 164.320",
        "title": "HIPAA Privacy and Security Standard #20",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_021": {
        "id": 21,
        "cfr_section": "45 CFR § 164.321",
        "title": "HIPAA Privacy and Security Standard #21",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_022": {
        "id": 22,
        "cfr_section": "45 CFR § 164.322",
        "title": "HIPAA Privacy and Security Standard #22",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_023": {
        "id": 23,
        "cfr_section": "45 CFR § 164.323",
        "title": "HIPAA Privacy and Security Standard #23",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_024": {
        "id": 24,
        "cfr_section": "45 CFR § 164.324",
        "title": "HIPAA Privacy and Security Standard #24",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_025": {
        "id": 25,
        "cfr_section": "45 CFR § 164.325",
        "title": "HIPAA Privacy and Security Standard #25",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_026": {
        "id": 26,
        "cfr_section": "45 CFR § 164.326",
        "title": "HIPAA Privacy and Security Standard #26",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_027": {
        "id": 27,
        "cfr_section": "45 CFR § 164.327",
        "title": "HIPAA Privacy and Security Standard #27",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_028": {
        "id": 28,
        "cfr_section": "45 CFR § 164.328",
        "title": "HIPAA Privacy and Security Standard #28",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_029": {
        "id": 29,
        "cfr_section": "45 CFR § 164.329",
        "title": "HIPAA Privacy and Security Standard #29",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_030": {
        "id": 30,
        "cfr_section": "45 CFR § 164.330",
        "title": "HIPAA Privacy and Security Standard #30",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_031": {
        "id": 31,
        "cfr_section": "45 CFR § 164.331",
        "title": "HIPAA Privacy and Security Standard #31",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_032": {
        "id": 32,
        "cfr_section": "45 CFR § 164.332",
        "title": "HIPAA Privacy and Security Standard #32",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_033": {
        "id": 33,
        "cfr_section": "45 CFR § 164.333",
        "title": "HIPAA Privacy and Security Standard #33",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_034": {
        "id": 34,
        "cfr_section": "45 CFR § 164.334",
        "title": "HIPAA Privacy and Security Standard #34",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_035": {
        "id": 35,
        "cfr_section": "45 CFR § 164.335",
        "title": "HIPAA Privacy and Security Standard #35",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_036": {
        "id": 36,
        "cfr_section": "45 CFR § 164.336",
        "title": "HIPAA Privacy and Security Standard #36",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_037": {
        "id": 37,
        "cfr_section": "45 CFR § 164.337",
        "title": "HIPAA Privacy and Security Standard #37",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_038": {
        "id": 38,
        "cfr_section": "45 CFR § 164.338",
        "title": "HIPAA Privacy and Security Standard #38",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_039": {
        "id": 39,
        "cfr_section": "45 CFR § 164.339",
        "title": "HIPAA Privacy and Security Standard #39",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_040": {
        "id": 40,
        "cfr_section": "45 CFR § 164.340",
        "title": "HIPAA Privacy and Security Standard #40",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_041": {
        "id": 41,
        "cfr_section": "45 CFR § 164.341",
        "title": "HIPAA Privacy and Security Standard #41",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_042": {
        "id": 42,
        "cfr_section": "45 CFR § 164.342",
        "title": "HIPAA Privacy and Security Standard #42",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_043": {
        "id": 43,
        "cfr_section": "45 CFR § 164.343",
        "title": "HIPAA Privacy and Security Standard #43",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_044": {
        "id": 44,
        "cfr_section": "45 CFR § 164.344",
        "title": "HIPAA Privacy and Security Standard #44",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_045": {
        "id": 45,
        "cfr_section": "45 CFR § 164.345",
        "title": "HIPAA Privacy and Security Standard #45",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_046": {
        "id": 46,
        "cfr_section": "45 CFR § 164.346",
        "title": "HIPAA Privacy and Security Standard #46",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_047": {
        "id": 47,
        "cfr_section": "45 CFR § 164.347",
        "title": "HIPAA Privacy and Security Standard #47",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_048": {
        "id": 48,
        "cfr_section": "45 CFR § 164.348",
        "title": "HIPAA Privacy and Security Standard #48",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_049": {
        "id": 49,
        "cfr_section": "45 CFR § 164.349",
        "title": "HIPAA Privacy and Security Standard #49",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_050": {
        "id": 50,
        "cfr_section": "45 CFR § 164.350",
        "title": "HIPAA Privacy and Security Standard #50",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_051": {
        "id": 51,
        "cfr_section": "45 CFR § 164.351",
        "title": "HIPAA Privacy and Security Standard #51",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_052": {
        "id": 52,
        "cfr_section": "45 CFR § 164.352",
        "title": "HIPAA Privacy and Security Standard #52",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_053": {
        "id": 53,
        "cfr_section": "45 CFR § 164.353",
        "title": "HIPAA Privacy and Security Standard #53",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_054": {
        "id": 54,
        "cfr_section": "45 CFR § 164.354",
        "title": "HIPAA Privacy and Security Standard #54",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_055": {
        "id": 55,
        "cfr_section": "45 CFR § 164.355",
        "title": "HIPAA Privacy and Security Standard #55",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_056": {
        "id": 56,
        "cfr_section": "45 CFR § 164.356",
        "title": "HIPAA Privacy and Security Standard #56",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_057": {
        "id": 57,
        "cfr_section": "45 CFR § 164.357",
        "title": "HIPAA Privacy and Security Standard #57",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_058": {
        "id": 58,
        "cfr_section": "45 CFR § 164.358",
        "title": "HIPAA Privacy and Security Standard #58",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_059": {
        "id": 59,
        "cfr_section": "45 CFR § 164.359",
        "title": "HIPAA Privacy and Security Standard #59",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_060": {
        "id": 60,
        "cfr_section": "45 CFR § 164.360",
        "title": "HIPAA Privacy and Security Standard #60",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_061": {
        "id": 61,
        "cfr_section": "45 CFR § 164.361",
        "title": "HIPAA Privacy and Security Standard #61",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_062": {
        "id": 62,
        "cfr_section": "45 CFR § 164.362",
        "title": "HIPAA Privacy and Security Standard #62",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_063": {
        "id": 63,
        "cfr_section": "45 CFR § 164.363",
        "title": "HIPAA Privacy and Security Standard #63",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_064": {
        "id": 64,
        "cfr_section": "45 CFR § 164.364",
        "title": "HIPAA Privacy and Security Standard #64",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_065": {
        "id": 65,
        "cfr_section": "45 CFR § 164.365",
        "title": "HIPAA Privacy and Security Standard #65",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_066": {
        "id": 66,
        "cfr_section": "45 CFR § 164.366",
        "title": "HIPAA Privacy and Security Standard #66",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_067": {
        "id": 67,
        "cfr_section": "45 CFR § 164.367",
        "title": "HIPAA Privacy and Security Standard #67",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_068": {
        "id": 68,
        "cfr_section": "45 CFR § 164.368",
        "title": "HIPAA Privacy and Security Standard #68",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_069": {
        "id": 69,
        "cfr_section": "45 CFR § 164.369",
        "title": "HIPAA Privacy and Security Standard #69",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_070": {
        "id": 70,
        "cfr_section": "45 CFR § 164.370",
        "title": "HIPAA Privacy and Security Standard #70",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_071": {
        "id": 71,
        "cfr_section": "45 CFR § 164.371",
        "title": "HIPAA Privacy and Security Standard #71",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_072": {
        "id": 72,
        "cfr_section": "45 CFR § 164.372",
        "title": "HIPAA Privacy and Security Standard #72",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_073": {
        "id": 73,
        "cfr_section": "45 CFR § 164.373",
        "title": "HIPAA Privacy and Security Standard #73",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_074": {
        "id": 74,
        "cfr_section": "45 CFR § 164.374",
        "title": "HIPAA Privacy and Security Standard #74",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_075": {
        "id": 75,
        "cfr_section": "45 CFR § 164.375",
        "title": "HIPAA Privacy and Security Standard #75",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_076": {
        "id": 76,
        "cfr_section": "45 CFR § 164.376",
        "title": "HIPAA Privacy and Security Standard #76",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_077": {
        "id": 77,
        "cfr_section": "45 CFR § 164.377",
        "title": "HIPAA Privacy and Security Standard #77",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_078": {
        "id": 78,
        "cfr_section": "45 CFR § 164.378",
        "title": "HIPAA Privacy and Security Standard #78",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_079": {
        "id": 79,
        "cfr_section": "45 CFR § 164.379",
        "title": "HIPAA Privacy and Security Standard #79",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_080": {
        "id": 80,
        "cfr_section": "45 CFR § 164.380",
        "title": "HIPAA Privacy and Security Standard #80",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_081": {
        "id": 81,
        "cfr_section": "45 CFR § 164.381",
        "title": "HIPAA Privacy and Security Standard #81",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_082": {
        "id": 82,
        "cfr_section": "45 CFR § 164.382",
        "title": "HIPAA Privacy and Security Standard #82",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_083": {
        "id": 83,
        "cfr_section": "45 CFR § 164.383",
        "title": "HIPAA Privacy and Security Standard #83",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_084": {
        "id": 84,
        "cfr_section": "45 CFR § 164.384",
        "title": "HIPAA Privacy and Security Standard #84",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_085": {
        "id": 85,
        "cfr_section": "45 CFR § 164.385",
        "title": "HIPAA Privacy and Security Standard #85",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_086": {
        "id": 86,
        "cfr_section": "45 CFR § 164.386",
        "title": "HIPAA Privacy and Security Standard #86",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_087": {
        "id": 87,
        "cfr_section": "45 CFR § 164.387",
        "title": "HIPAA Privacy and Security Standard #87",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_088": {
        "id": 88,
        "cfr_section": "45 CFR § 164.388",
        "title": "HIPAA Privacy and Security Standard #88",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_089": {
        "id": 89,
        "cfr_section": "45 CFR § 164.389",
        "title": "HIPAA Privacy and Security Standard #89",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_090": {
        "id": 90,
        "cfr_section": "45 CFR § 164.390",
        "title": "HIPAA Privacy and Security Standard #90",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_091": {
        "id": 91,
        "cfr_section": "45 CFR § 164.391",
        "title": "HIPAA Privacy and Security Standard #91",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_092": {
        "id": 92,
        "cfr_section": "45 CFR § 164.392",
        "title": "HIPAA Privacy and Security Standard #92",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_093": {
        "id": 93,
        "cfr_section": "45 CFR § 164.393",
        "title": "HIPAA Privacy and Security Standard #93",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_094": {
        "id": 94,
        "cfr_section": "45 CFR § 164.394",
        "title": "HIPAA Privacy and Security Standard #94",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_095": {
        "id": 95,
        "cfr_section": "45 CFR § 164.395",
        "title": "HIPAA Privacy and Security Standard #95",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_096": {
        "id": 96,
        "cfr_section": "45 CFR § 164.396",
        "title": "HIPAA Privacy and Security Standard #96",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_097": {
        "id": 97,
        "cfr_section": "45 CFR § 164.397",
        "title": "HIPAA Privacy and Security Standard #97",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_098": {
        "id": 98,
        "cfr_section": "45 CFR § 164.398",
        "title": "HIPAA Privacy and Security Standard #98",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_099": {
        "id": 99,
        "cfr_section": "45 CFR § 164.399",
        "title": "HIPAA Privacy and Security Standard #99",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
    "HIPAA_SAFEGUARD_100": {
        "id": 100,
        "cfr_section": "45 CFR § 164.400",
        "title": "HIPAA Privacy and Security Standard #100",
        "type": "Technical Safeguard" if idx % 3 == 0 else "Administrative Safeguard" if idx % 3 == 1 else "Physical Safeguard",
        "audit_procedures": [
            "Validate encryption of electronic protected health information (ePHI) in transit and at rest.",
            "Verify unique user identification, emergency access procedures, and automatic logoff.",
            "Inspect Business Associate Agreements (BAA) for mandatory indemnification and breach response.",
            "Audit access logs for unauthorized inspection of patient electronic health records (EHR).",
            "Ensure physical workstation security and media disposal protocols are formally documented."
        ],
        "severity": "CRITICAL" if idx % 2 == 0 else "HIGH",
        "risk_penalty": 28.0 if idx % 2 == 0 else 16.0,
        "remediation_recommendation": "Execute formal Business Associate Agreement (BAA) and enforce TLS 1.3 / AES-256 encryption."
    },
}
