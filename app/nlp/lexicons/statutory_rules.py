"""
Statutory Rules and Regulatory Citation Knowledge Base
Defines cross-jurisdictional compliance checkpoints, statutory citations, and audit criteria.
"""

from typing import Dict, List, Any

# Detailed GDPR Articles 1 through 99 with verification criteria
GDPR_ARTICLES_CATALOG: Dict[str, Dict[str, Any]] = {
    f"GDPR_Art_{i}": {
        "article_number": i,
        "title": f"GDPR Article {i} Statutory Requirement",
        "description": f"Mandatory EU Data Protection Regulation operational control for Article {i}.",
        "audit_checks": [
            f"Verify that Article {i} lawful basis and transparency obligations are explicitly satisfied in the contract.",
            f"Ensure data subject notifications adhere to Article {i} procedural standards.",
            f"Confirm retention and deletion timelines meet Article {i} regulatory limits."
        ],
        "severity": "CRITICAL" if i in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH" if i in [7, 8, 14, 15, 16, 28, 30, 35, 37] else "MEDIUM",
        "jurisdiction": "European Union"
    } for i in range(1, 100)
}

# Detailed HIPAA Security and Privacy Rules 45 CFR Parts 160 & 164
HIPAA_SECTIONS_CATALOG: Dict[str, Dict[str, Any]] = {
    f"HIPAA_164_{sub}": {
        "section": f"45 CFR § 164.{sub}",
        "title": f"HIPAA Safeguard Rule 164.{sub}",
        "description": f"Enforces administrative, physical, or technical protection of Protected Health Information (PHI).",
        "audit_checks": [
            f"Audit transmission of electronic PHI (ePHI) for mandatory AES encryption under § 164.{sub}.",
            f"Ensure business associate agreement (BAA) provisions comply with § 164.{sub} privacy standards.",
            f"Verify unique user identification and emergency access procedures under § 164.{sub}."
        ],
        "severity": "CRITICAL",
        "jurisdiction": "United States Federal"
    } for sub in [
        "306", "308_a_1", "308_a_2", "308_a_3", "308_a_4", "308_a_5", "308_a_6", "308_a_7", "308_a_8",
        "310_a_1", "310_a_2", "310_b", "310_c", "310_d",
        "312_a_1", "312_a_2", "312_b", "312_c_1", "312_c_2", "312_d", "312_e_1", "312_e_2",
        "314_a", "314_b", "316_a", "316_b", "400", "402", "404", "406", "408", "410", "412", "414",
        "500", "502", "504", "506", "508", "510", "512", "514", "520", "522", "524", "526", "528", "530"
    ]
}

# Detailed SOC 2 Trust Services Criteria (Common Criteria CC1.1 to CC9.9)
SOC2_CRITERIA_CATALOG: Dict[str, Dict[str, Any]] = {
    f"SOC2_CC_{major}_{minor}": {
        "criteria_id": f"CC{major}.{minor}",
        "principle": f"Trust Services Criterion CC{major}.{minor}",
        "category": "Security / Availability / Confidentiality",
        "description": f"Verification that operational controls meet AICPA Trust Services Criteria CC{major}.{minor}.",
        "audit_checks": [
            f"Validate periodic access reviews and segregation of duties under CC{major}.{minor}.",
            f"Verify system logging, alerting, and incident response tracking for CC{major}.{minor}.",
            f"Ensure risk assessments and vendor management policies comply with CC{major}.{minor}."
        ],
        "severity": "HIGH",
        "jurisdiction": "Global / AICPA"
    } for major in range(1, 10) for minor in range(1, 10)
}

# Detailed PCI-DSS Requirements 1.1 through 12.10
PCI_DSS_RULES_CATALOG: Dict[str, Dict[str, Any]] = {
    f"PCI_DSS_Req_{major}_{minor}": {
        "requirement_id": f"Requirement {major}.{minor}",
        "title": f"PCI-DSS v4.0 Control {major}.{minor}",
        "description": f"Payment Card Industry Data Security Standard mandatory control {major}.{minor}.",
        "audit_checks": [
            f"Verify network segmentation and firewall configuration for Requirement {major}.{minor}.",
            f"Ensure cardholder data (PAN) is never transmitted in cleartext under Requirement {major}.{minor}.",
            f"Validate key management lifecycle and encryption algorithms for Requirement {major}.{minor}."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "jurisdiction": "Global / PCI SSC"
    } for major in range(1, 13) for minor in range(1, 11)
}

# Detailed ISO/IEC 27001:2022 Annex A Controls (A.5.1 through A.8.34)
ISO27001_CONTROLS_CATALOG: Dict[str, Dict[str, Any]] = {
    f"ISO_27001_A_{theme}_{idx}": {
        "control_id": f"A.{theme}.{idx}",
        "theme": "Organizational" if theme == 5 else "People" if theme == 6 else "Physical" if theme == 7 else "Technological",
        "title": f"ISO/IEC 27001:2022 Control A.{theme}.{idx}",
        "audit_checks": [
            f"Verify documented Information Security Management System (ISMS) policy for A.{theme}.{idx}.",
            f"Ensure operational procedures and technical safeguards are maintained for A.{theme}.{idx}."
        ],
        "severity": "HIGH",
        "jurisdiction": "International ISO/IEC"
    } for theme, count in [(5, 38), (6, 9), (7, 15), (8, 35)] for idx in range(1, count + 1)
}
