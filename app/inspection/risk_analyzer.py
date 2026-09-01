"""Enterprise Risk Scoring, Liability Detection, and Vulnerability Engine."""
import re
from typing import Dict, Any, List

class RiskAnalyzer:
    RISK_RULES = [
        # 1. Contract Risks
        {
            "category": "CONTRACT_RISK",
            "severity": "HIGH",
            "title": "Automatic Renewal Trap",
            "pattern": r'\b(automatically\s+renew|auto-renew|successive\s+terms?\s+of|renew\s+automatically)\b',
            "explanation": "Contract automatically renews without explicit proactive re-authorization.",
            "impact": "Unintended long-term financial commitments and vendor lock-in.",
            "recommendation": "Require explicit affirmative written consent for renewal or establish a 60-day advance cancellation notice.",
            "confidence": 0.95
        },
        {
            "category": "CONTRACT_RISK",
            "severity": "CRITICAL",
            "title": "Unilateral Termination Rights",
            "pattern": r'\b(terminate\s+(?:immediately\s+)?without\s+cause|terminate\s+at\s+any\s+time\s+without\s+notice|sole\s+discretion\s+terminate)\b',
            "explanation": "One party possesses unilateral termination rights without cause or advance notice.",
            "impact": "Operational disruption if services are terminated abruptly.",
            "recommendation": "Establish a mandatory reciprocal 30-day written cure period prior to termination.",
            "confidence": 0.97
        },
        {
            "category": "CONTRACT_RISK",
            "severity": "HIGH",
            "title": "Unlimited Indemnification & Liability Exposure",
            "pattern": r'\b(indemnify\s+and\s+hold\s+harmless|unlimited\s+liability|indemnification\s+shall\s+not\s+be\s+limited|no\s+cap\s+on\s+liability)\b',
            "explanation": "Broad indemnification language with potential absence of reasonable liability caps.",
            "impact": "Unbounded financial exposure in third-party claims or dispute litigation.",
            "recommendation": "Cap indemnification liability to total fees paid in the preceding 12 months.",
            "confidence": 0.94
        },
        {
            "category": "CONTRACT_RISK",
            "severity": "MEDIUM",
            "title": "Unilateral Contract Modification Clause",
            "pattern": r'\b(reserve\s+the\s+right\s+to\s+modify|modify\s+these\s+terms\s+at\s+any\s+time|without\s+prior\s+notice\s+modify)\b',
            "explanation": "Allows one party to unilaterally modify contract terms, pricing, or service levels.",
            "impact": "Unpredictable price increases or altered obligation scope.",
            "recommendation": "Require mutual bilateral written agreement for any contractual amendments.",
            "confidence": 0.92
        },

        # 2. Security & Credential Risks
        {
            "category": "SECURITY_RISK",
            "severity": "CRITICAL",
            "title": "Plain Text Credentials or Security Key Leak",
            "pattern": r'(password\s*=\s*[\'"][^\'"]+[\'"]|api_key\s*=\s*[\'"][^\'"]+[\'"]|sk-[a-zA-Z0-9]{20,}|ghp_[a-zA-Z0-9]{30,})',
            "explanation": "Hardcoded plain-text credentials, API keys, or security secrets exposed in document.",
            "impact": "Direct credential leakage, unauthorized access, and compliance violations.",
            "recommendation": "Immediately revoke and rotate leaked keys; replace with environment variable secret vaults.",
            "confidence": 0.99
        },
        {
            "category": "SECURITY_RISK",
            "severity": "HIGH",
            "title": "Unencrypted Sensitive Storage or Transmission",
            "pattern": r'\b(stored\s+in\s+plain\s*text|unencrypted\s+database|without\s+encryption|plain\s*text\s+log\s+files)\b',
            "explanation": "References to unencrypted sensitive information, databases, or log files.",
            "impact": "Major regulatory violation under GDPR Art. 32 and PCI-DSS Req 3.4.",
            "recommendation": "Enforce AES-256 encryption at rest and TLS 1.3 in transit across all data stores.",
            "confidence": 0.96
        },

        # 3. Privacy & Compliance Risks
        {
            "category": "PRIVACY_RISK",
            "severity": "HIGH",
            "title": "Indefinite Data Retention Policy",
            "pattern": r'\b(retain\s+data\s+indefinitely|unlimited\s+retention|no\s+deletion\s+timeline|store\s+personal\s+data\s+permanently)\b',
            "explanation": "Policy lacks definitive data retention schedule for personal identifiers.",
            "impact": "Breach of GDPR Article 5(1)(e) storage limitation principle.",
            "recommendation": "Specify explicit retention schedules and automated deletion mechanisms upon contract expiry.",
            "confidence": 0.93
        }
    ]

    @classmethod
    def evaluate_risks(cls, text: str) -> Dict[str, Any]:
        findings: List[Dict[str, Any]] = []
        if not text:
            return {"overall_risk_score": 0.0, "risk_level": "LOW", "findings": []}

        severity_weights = {"CRITICAL": 70.0, "HIGH": 30.0, "MEDIUM": 15.0, "LOW": 5.0}
        total_risk_score = 0.0

        for rule in cls.RISK_RULES:
            matches = list(re.finditer(rule["pattern"], text, re.IGNORECASE))
            for m in matches:
                total_risk_score += severity_weights.get(rule["severity"], 10.0)
                findings.append({
                    "category": rule["category"],
                    "severity": rule["severity"],
                    "title": rule["title"],
                    "location": f"Position {m.start()}-{m.end()}",
                    "value": m.group(0),
                    "expected_value": "Compliant risk-mitigated clause",
                    "evidence": f"Found pattern: '{m.group(0)}'.",
                    "explanation": rule["explanation"],
                    "impact": rule["impact"],
                    "recommendation": rule["recommendation"],
                    "confidence": rule["confidence"],
                    "status": "OPEN"
                })

        normalized_score = min(100.0, round(total_risk_score, 1))
        risk_level = "CRITICAL" if normalized_score >= 65 else "HIGH" if normalized_score >= 40 else "MEDIUM" if normalized_score >= 20 else "LOW"

        return {
            "overall_risk_score": normalized_score,
            "risk_level": risk_level,
            "findings": findings
        }
