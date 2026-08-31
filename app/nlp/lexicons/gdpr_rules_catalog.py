"""GDPR Statutory Rules Registry (Articles 1 to 99)."""
from typing import Dict, Any

GDPR_REGISTRY: Dict[str, Dict[str, Any]] = {
    "GDPR_ARTICLE_001": {
        "article_id": 1,
        "title": "GDPR Article 1 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 1.",
            "Ensure transparent data subject disclosure pursuant to Article 1.",
            "Validate records of processing activities under Article 1 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_002": {
        "article_id": 2,
        "title": "GDPR Article 2 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 2.",
            "Ensure transparent data subject disclosure pursuant to Article 2.",
            "Validate records of processing activities under Article 2 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_003": {
        "article_id": 3,
        "title": "GDPR Article 3 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 3.",
            "Ensure transparent data subject disclosure pursuant to Article 3.",
            "Validate records of processing activities under Article 3 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_004": {
        "article_id": 4,
        "title": "GDPR Article 4 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 4.",
            "Ensure transparent data subject disclosure pursuant to Article 4.",
            "Validate records of processing activities under Article 4 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_005": {
        "article_id": 5,
        "title": "GDPR Article 5 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 5.",
            "Ensure transparent data subject disclosure pursuant to Article 5.",
            "Validate records of processing activities under Article 5 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_006": {
        "article_id": 6,
        "title": "GDPR Article 6 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 6.",
            "Ensure transparent data subject disclosure pursuant to Article 6.",
            "Validate records of processing activities under Article 6 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_007": {
        "article_id": 7,
        "title": "GDPR Article 7 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 7.",
            "Ensure transparent data subject disclosure pursuant to Article 7.",
            "Validate records of processing activities under Article 7 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_008": {
        "article_id": 8,
        "title": "GDPR Article 8 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 8.",
            "Ensure transparent data subject disclosure pursuant to Article 8.",
            "Validate records of processing activities under Article 8 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_009": {
        "article_id": 9,
        "title": "GDPR Article 9 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 9.",
            "Ensure transparent data subject disclosure pursuant to Article 9.",
            "Validate records of processing activities under Article 9 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_010": {
        "article_id": 10,
        "title": "GDPR Article 10 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 10.",
            "Ensure transparent data subject disclosure pursuant to Article 10.",
            "Validate records of processing activities under Article 10 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_011": {
        "article_id": 11,
        "title": "GDPR Article 11 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 11.",
            "Ensure transparent data subject disclosure pursuant to Article 11.",
            "Validate records of processing activities under Article 11 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_012": {
        "article_id": 12,
        "title": "GDPR Article 12 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 12.",
            "Ensure transparent data subject disclosure pursuant to Article 12.",
            "Validate records of processing activities under Article 12 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_013": {
        "article_id": 13,
        "title": "GDPR Article 13 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 13.",
            "Ensure transparent data subject disclosure pursuant to Article 13.",
            "Validate records of processing activities under Article 13 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_014": {
        "article_id": 14,
        "title": "GDPR Article 14 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 14.",
            "Ensure transparent data subject disclosure pursuant to Article 14.",
            "Validate records of processing activities under Article 14 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_015": {
        "article_id": 15,
        "title": "GDPR Article 15 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 15.",
            "Ensure transparent data subject disclosure pursuant to Article 15.",
            "Validate records of processing activities under Article 15 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_016": {
        "article_id": 16,
        "title": "GDPR Article 16 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 16.",
            "Ensure transparent data subject disclosure pursuant to Article 16.",
            "Validate records of processing activities under Article 16 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_017": {
        "article_id": 17,
        "title": "GDPR Article 17 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 17.",
            "Ensure transparent data subject disclosure pursuant to Article 17.",
            "Validate records of processing activities under Article 17 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_018": {
        "article_id": 18,
        "title": "GDPR Article 18 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 18.",
            "Ensure transparent data subject disclosure pursuant to Article 18.",
            "Validate records of processing activities under Article 18 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_019": {
        "article_id": 19,
        "title": "GDPR Article 19 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 19.",
            "Ensure transparent data subject disclosure pursuant to Article 19.",
            "Validate records of processing activities under Article 19 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_020": {
        "article_id": 20,
        "title": "GDPR Article 20 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 20.",
            "Ensure transparent data subject disclosure pursuant to Article 20.",
            "Validate records of processing activities under Article 20 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_021": {
        "article_id": 21,
        "title": "GDPR Article 21 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 21.",
            "Ensure transparent data subject disclosure pursuant to Article 21.",
            "Validate records of processing activities under Article 21 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_022": {
        "article_id": 22,
        "title": "GDPR Article 22 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 22.",
            "Ensure transparent data subject disclosure pursuant to Article 22.",
            "Validate records of processing activities under Article 22 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_023": {
        "article_id": 23,
        "title": "GDPR Article 23 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 23.",
            "Ensure transparent data subject disclosure pursuant to Article 23.",
            "Validate records of processing activities under Article 23 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_024": {
        "article_id": 24,
        "title": "GDPR Article 24 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 24.",
            "Ensure transparent data subject disclosure pursuant to Article 24.",
            "Validate records of processing activities under Article 24 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_025": {
        "article_id": 25,
        "title": "GDPR Article 25 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 25.",
            "Ensure transparent data subject disclosure pursuant to Article 25.",
            "Validate records of processing activities under Article 25 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_026": {
        "article_id": 26,
        "title": "GDPR Article 26 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 26.",
            "Ensure transparent data subject disclosure pursuant to Article 26.",
            "Validate records of processing activities under Article 26 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_027": {
        "article_id": 27,
        "title": "GDPR Article 27 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 27.",
            "Ensure transparent data subject disclosure pursuant to Article 27.",
            "Validate records of processing activities under Article 27 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_028": {
        "article_id": 28,
        "title": "GDPR Article 28 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 28.",
            "Ensure transparent data subject disclosure pursuant to Article 28.",
            "Validate records of processing activities under Article 28 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_029": {
        "article_id": 29,
        "title": "GDPR Article 29 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 29.",
            "Ensure transparent data subject disclosure pursuant to Article 29.",
            "Validate records of processing activities under Article 29 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_030": {
        "article_id": 30,
        "title": "GDPR Article 30 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 30.",
            "Ensure transparent data subject disclosure pursuant to Article 30.",
            "Validate records of processing activities under Article 30 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_031": {
        "article_id": 31,
        "title": "GDPR Article 31 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 31.",
            "Ensure transparent data subject disclosure pursuant to Article 31.",
            "Validate records of processing activities under Article 31 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_032": {
        "article_id": 32,
        "title": "GDPR Article 32 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 32.",
            "Ensure transparent data subject disclosure pursuant to Article 32.",
            "Validate records of processing activities under Article 32 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_033": {
        "article_id": 33,
        "title": "GDPR Article 33 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 33.",
            "Ensure transparent data subject disclosure pursuant to Article 33.",
            "Validate records of processing activities under Article 33 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_034": {
        "article_id": 34,
        "title": "GDPR Article 34 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 34.",
            "Ensure transparent data subject disclosure pursuant to Article 34.",
            "Validate records of processing activities under Article 34 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_035": {
        "article_id": 35,
        "title": "GDPR Article 35 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 35.",
            "Ensure transparent data subject disclosure pursuant to Article 35.",
            "Validate records of processing activities under Article 35 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_036": {
        "article_id": 36,
        "title": "GDPR Article 36 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 36.",
            "Ensure transparent data subject disclosure pursuant to Article 36.",
            "Validate records of processing activities under Article 36 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_037": {
        "article_id": 37,
        "title": "GDPR Article 37 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 37.",
            "Ensure transparent data subject disclosure pursuant to Article 37.",
            "Validate records of processing activities under Article 37 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_038": {
        "article_id": 38,
        "title": "GDPR Article 38 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 38.",
            "Ensure transparent data subject disclosure pursuant to Article 38.",
            "Validate records of processing activities under Article 38 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_039": {
        "article_id": 39,
        "title": "GDPR Article 39 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 39.",
            "Ensure transparent data subject disclosure pursuant to Article 39.",
            "Validate records of processing activities under Article 39 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_040": {
        "article_id": 40,
        "title": "GDPR Article 40 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 40.",
            "Ensure transparent data subject disclosure pursuant to Article 40.",
            "Validate records of processing activities under Article 40 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_041": {
        "article_id": 41,
        "title": "GDPR Article 41 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 41.",
            "Ensure transparent data subject disclosure pursuant to Article 41.",
            "Validate records of processing activities under Article 41 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_042": {
        "article_id": 42,
        "title": "GDPR Article 42 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 42.",
            "Ensure transparent data subject disclosure pursuant to Article 42.",
            "Validate records of processing activities under Article 42 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_043": {
        "article_id": 43,
        "title": "GDPR Article 43 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 43.",
            "Ensure transparent data subject disclosure pursuant to Article 43.",
            "Validate records of processing activities under Article 43 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_044": {
        "article_id": 44,
        "title": "GDPR Article 44 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 44.",
            "Ensure transparent data subject disclosure pursuant to Article 44.",
            "Validate records of processing activities under Article 44 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_045": {
        "article_id": 45,
        "title": "GDPR Article 45 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 45.",
            "Ensure transparent data subject disclosure pursuant to Article 45.",
            "Validate records of processing activities under Article 45 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_046": {
        "article_id": 46,
        "title": "GDPR Article 46 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 46.",
            "Ensure transparent data subject disclosure pursuant to Article 46.",
            "Validate records of processing activities under Article 46 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_047": {
        "article_id": 47,
        "title": "GDPR Article 47 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 47.",
            "Ensure transparent data subject disclosure pursuant to Article 47.",
            "Validate records of processing activities under Article 47 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_048": {
        "article_id": 48,
        "title": "GDPR Article 48 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 48.",
            "Ensure transparent data subject disclosure pursuant to Article 48.",
            "Validate records of processing activities under Article 48 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_049": {
        "article_id": 49,
        "title": "GDPR Article 49 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 49.",
            "Ensure transparent data subject disclosure pursuant to Article 49.",
            "Validate records of processing activities under Article 49 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_050": {
        "article_id": 50,
        "title": "GDPR Article 50 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 50.",
            "Ensure transparent data subject disclosure pursuant to Article 50.",
            "Validate records of processing activities under Article 50 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_051": {
        "article_id": 51,
        "title": "GDPR Article 51 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 51.",
            "Ensure transparent data subject disclosure pursuant to Article 51.",
            "Validate records of processing activities under Article 51 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_052": {
        "article_id": 52,
        "title": "GDPR Article 52 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 52.",
            "Ensure transparent data subject disclosure pursuant to Article 52.",
            "Validate records of processing activities under Article 52 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_053": {
        "article_id": 53,
        "title": "GDPR Article 53 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 53.",
            "Ensure transparent data subject disclosure pursuant to Article 53.",
            "Validate records of processing activities under Article 53 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_054": {
        "article_id": 54,
        "title": "GDPR Article 54 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 54.",
            "Ensure transparent data subject disclosure pursuant to Article 54.",
            "Validate records of processing activities under Article 54 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_055": {
        "article_id": 55,
        "title": "GDPR Article 55 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 55.",
            "Ensure transparent data subject disclosure pursuant to Article 55.",
            "Validate records of processing activities under Article 55 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_056": {
        "article_id": 56,
        "title": "GDPR Article 56 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 56.",
            "Ensure transparent data subject disclosure pursuant to Article 56.",
            "Validate records of processing activities under Article 56 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_057": {
        "article_id": 57,
        "title": "GDPR Article 57 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 57.",
            "Ensure transparent data subject disclosure pursuant to Article 57.",
            "Validate records of processing activities under Article 57 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_058": {
        "article_id": 58,
        "title": "GDPR Article 58 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 58.",
            "Ensure transparent data subject disclosure pursuant to Article 58.",
            "Validate records of processing activities under Article 58 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_059": {
        "article_id": 59,
        "title": "GDPR Article 59 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 59.",
            "Ensure transparent data subject disclosure pursuant to Article 59.",
            "Validate records of processing activities under Article 59 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_060": {
        "article_id": 60,
        "title": "GDPR Article 60 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 60.",
            "Ensure transparent data subject disclosure pursuant to Article 60.",
            "Validate records of processing activities under Article 60 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_061": {
        "article_id": 61,
        "title": "GDPR Article 61 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 61.",
            "Ensure transparent data subject disclosure pursuant to Article 61.",
            "Validate records of processing activities under Article 61 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_062": {
        "article_id": 62,
        "title": "GDPR Article 62 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 62.",
            "Ensure transparent data subject disclosure pursuant to Article 62.",
            "Validate records of processing activities under Article 62 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_063": {
        "article_id": 63,
        "title": "GDPR Article 63 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 63.",
            "Ensure transparent data subject disclosure pursuant to Article 63.",
            "Validate records of processing activities under Article 63 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_064": {
        "article_id": 64,
        "title": "GDPR Article 64 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 64.",
            "Ensure transparent data subject disclosure pursuant to Article 64.",
            "Validate records of processing activities under Article 64 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_065": {
        "article_id": 65,
        "title": "GDPR Article 65 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 65.",
            "Ensure transparent data subject disclosure pursuant to Article 65.",
            "Validate records of processing activities under Article 65 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_066": {
        "article_id": 66,
        "title": "GDPR Article 66 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 66.",
            "Ensure transparent data subject disclosure pursuant to Article 66.",
            "Validate records of processing activities under Article 66 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_067": {
        "article_id": 67,
        "title": "GDPR Article 67 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 67.",
            "Ensure transparent data subject disclosure pursuant to Article 67.",
            "Validate records of processing activities under Article 67 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_068": {
        "article_id": 68,
        "title": "GDPR Article 68 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 68.",
            "Ensure transparent data subject disclosure pursuant to Article 68.",
            "Validate records of processing activities under Article 68 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_069": {
        "article_id": 69,
        "title": "GDPR Article 69 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 69.",
            "Ensure transparent data subject disclosure pursuant to Article 69.",
            "Validate records of processing activities under Article 69 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_070": {
        "article_id": 70,
        "title": "GDPR Article 70 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 70.",
            "Ensure transparent data subject disclosure pursuant to Article 70.",
            "Validate records of processing activities under Article 70 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_071": {
        "article_id": 71,
        "title": "GDPR Article 71 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 71.",
            "Ensure transparent data subject disclosure pursuant to Article 71.",
            "Validate records of processing activities under Article 71 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_072": {
        "article_id": 72,
        "title": "GDPR Article 72 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 72.",
            "Ensure transparent data subject disclosure pursuant to Article 72.",
            "Validate records of processing activities under Article 72 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_073": {
        "article_id": 73,
        "title": "GDPR Article 73 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 73.",
            "Ensure transparent data subject disclosure pursuant to Article 73.",
            "Validate records of processing activities under Article 73 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_074": {
        "article_id": 74,
        "title": "GDPR Article 74 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 74.",
            "Ensure transparent data subject disclosure pursuant to Article 74.",
            "Validate records of processing activities under Article 74 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_075": {
        "article_id": 75,
        "title": "GDPR Article 75 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 75.",
            "Ensure transparent data subject disclosure pursuant to Article 75.",
            "Validate records of processing activities under Article 75 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_076": {
        "article_id": 76,
        "title": "GDPR Article 76 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 76.",
            "Ensure transparent data subject disclosure pursuant to Article 76.",
            "Validate records of processing activities under Article 76 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_077": {
        "article_id": 77,
        "title": "GDPR Article 77 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 77.",
            "Ensure transparent data subject disclosure pursuant to Article 77.",
            "Validate records of processing activities under Article 77 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_078": {
        "article_id": 78,
        "title": "GDPR Article 78 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 78.",
            "Ensure transparent data subject disclosure pursuant to Article 78.",
            "Validate records of processing activities under Article 78 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_079": {
        "article_id": 79,
        "title": "GDPR Article 79 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 79.",
            "Ensure transparent data subject disclosure pursuant to Article 79.",
            "Validate records of processing activities under Article 79 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_080": {
        "article_id": 80,
        "title": "GDPR Article 80 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 80.",
            "Ensure transparent data subject disclosure pursuant to Article 80.",
            "Validate records of processing activities under Article 80 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_081": {
        "article_id": 81,
        "title": "GDPR Article 81 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 81.",
            "Ensure transparent data subject disclosure pursuant to Article 81.",
            "Validate records of processing activities under Article 81 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_082": {
        "article_id": 82,
        "title": "GDPR Article 82 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 82.",
            "Ensure transparent data subject disclosure pursuant to Article 82.",
            "Validate records of processing activities under Article 82 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_083": {
        "article_id": 83,
        "title": "GDPR Article 83 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 83.",
            "Ensure transparent data subject disclosure pursuant to Article 83.",
            "Validate records of processing activities under Article 83 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_084": {
        "article_id": 84,
        "title": "GDPR Article 84 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 84.",
            "Ensure transparent data subject disclosure pursuant to Article 84.",
            "Validate records of processing activities under Article 84 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_085": {
        "article_id": 85,
        "title": "GDPR Article 85 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 85.",
            "Ensure transparent data subject disclosure pursuant to Article 85.",
            "Validate records of processing activities under Article 85 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_086": {
        "article_id": 86,
        "title": "GDPR Article 86 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 86.",
            "Ensure transparent data subject disclosure pursuant to Article 86.",
            "Validate records of processing activities under Article 86 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_087": {
        "article_id": 87,
        "title": "GDPR Article 87 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 87.",
            "Ensure transparent data subject disclosure pursuant to Article 87.",
            "Validate records of processing activities under Article 87 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_088": {
        "article_id": 88,
        "title": "GDPR Article 88 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 88.",
            "Ensure transparent data subject disclosure pursuant to Article 88.",
            "Validate records of processing activities under Article 88 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_089": {
        "article_id": 89,
        "title": "GDPR Article 89 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 89.",
            "Ensure transparent data subject disclosure pursuant to Article 89.",
            "Validate records of processing activities under Article 89 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_090": {
        "article_id": 90,
        "title": "GDPR Article 90 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 90.",
            "Ensure transparent data subject disclosure pursuant to Article 90.",
            "Validate records of processing activities under Article 90 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_091": {
        "article_id": 91,
        "title": "GDPR Article 91 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 91.",
            "Ensure transparent data subject disclosure pursuant to Article 91.",
            "Validate records of processing activities under Article 91 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_092": {
        "article_id": 92,
        "title": "GDPR Article 92 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 92.",
            "Ensure transparent data subject disclosure pursuant to Article 92.",
            "Validate records of processing activities under Article 92 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_093": {
        "article_id": 93,
        "title": "GDPR Article 93 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 93.",
            "Ensure transparent data subject disclosure pursuant to Article 93.",
            "Validate records of processing activities under Article 93 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_094": {
        "article_id": 94,
        "title": "GDPR Article 94 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 94.",
            "Ensure transparent data subject disclosure pursuant to Article 94.",
            "Validate records of processing activities under Article 94 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_095": {
        "article_id": 95,
        "title": "GDPR Article 95 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 95.",
            "Ensure transparent data subject disclosure pursuant to Article 95.",
            "Validate records of processing activities under Article 95 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_096": {
        "article_id": 96,
        "title": "GDPR Article 96 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 96.",
            "Ensure transparent data subject disclosure pursuant to Article 96.",
            "Validate records of processing activities under Article 96 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_097": {
        "article_id": 97,
        "title": "GDPR Article 97 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 97.",
            "Ensure transparent data subject disclosure pursuant to Article 97.",
            "Validate records of processing activities under Article 97 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_098": {
        "article_id": 98,
        "title": "GDPR Article 98 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 98.",
            "Ensure transparent data subject disclosure pursuant to Article 98.",
            "Validate records of processing activities under Article 98 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
    "GDPR_ARTICLE_099": {
        "article_id": 99,
        "title": "GDPR Article 99 - Data Protection Operational Requirement",
        "category": "Data Governance & Rights",
        "mandatory_checks": [
            "Verify lawful basis of processing according to Article 99.",
            "Ensure transparent data subject disclosure pursuant to Article 99.",
            "Validate records of processing activities under Article 99 mandates.",
            "Confirm retention limitations comply with European Data Protection Board rules.",
            "Verify international transfer adequacy mechanisms if cross-border flow occurs."
        ],
        "severity": "CRITICAL" if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else "HIGH",
        "penalty_weight": 25.0 if art in [5, 6, 9, 12, 13, 17, 25, 32, 33, 44] else 15.0,
        "remediation_clause": "Contracting parties shall establish formal data processing addendums (DPA) incorporating standard contractual clauses (SCC) and privacy notices.",
        "audit_frequency": "Annual External Audit",
        "enforcement_authority": "European Data Protection Board (EDPB)"
    },
}
