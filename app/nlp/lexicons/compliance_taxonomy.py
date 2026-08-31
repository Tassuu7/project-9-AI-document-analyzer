"""Regulatory and Compliance Rules Taxonomy."""
from typing import Dict, Any

COMPLIANCE_STANDARDS: Dict[str, Dict[str, Any]] = {
    "GDPR": {
        "name": "General Data Protection Regulation (EU 2016/679)",
        "mandatory_terms": ["data controller", "data processor", "personal data", "consent", "right to erasure", "breach notification", "gdpr"],
        "prohibited_patterns": ["unlimited retention", "plain text personal data", "retain indefinitely", "without encryption"]
    },
    "HIPAA": {
        "name": "Health Insurance Portability and Accountability Act",
        "mandatory_terms": ["protected health information", "phi", "business associate agreement", "covered entity", "encryption", "hipaa"],
        "prohibited_patterns": ["unencrypted phi", "plain text health data", "unencrypted medical", "plain text"]
    },
    "SOC2": {
        "name": "Service Organization Control 2 (AICPA TSC)",
        "mandatory_terms": ["role-based access control", "multi-factor authentication", "continuous monitoring", "incident response", "soc 2"],
        "prohibited_patterns": ["shared admin credentials", "unencrypted database", "no multi-factor", "plain text"]
    },
    "PCI-DSS": {
        "name": "Payment Card Industry Data Security Standard (v4.0)",
        "mandatory_terms": ["cardholder data", "primary account number", "pan", "masking", "strong cryptography", "pci-dss"],
        "prohibited_patterns": ["store cvv", "retain cvc", "plain text pan", "plain text", "cvv", "unencrypted"]
    }
}
