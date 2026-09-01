"""PII & Sensitive Privacy Information Inspector and Redaction Engine."""
import re
from typing import Dict, Any, List

class PIIInspector:
    PII_PATTERNS = [
        ("EMAIL", r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', "PII", 0.99),
        ("PHONE_NUMBER", r'\b(?:\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b', "PII", 0.95),
        ("SSN", r'\b\d{3}-\d{2}-\d{4}\b', "PII", 0.98),
        ("CREDIT_CARD", r'\b(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14}|3[47][0-9]{13}|3(?:0[0-5]|[68][0-9])[0-9]{11}|6(?:011|5[0-9]{2})[0-9]{12})\b', "FINANCIAL", 0.99),
        ("IP_ADDRESS", r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b', "TECHNICAL", 0.97),
        ("DATE_OF_BIRTH", r'\b(?:DOB|Date of Birth|Born)[:\s]+(\d{4}[-/]\d{2}[-/]\d{2}|\d{2}[-/]\d{2}[-/]\d{4})\b', "PII", 0.96),
        ("MEDICAL_RECORD_NUM", r'\b(?:MRN|Medical Record)[:\s]+([A-Z0-9\-]{6,14})\b', "HEALTHCARE", 0.95)
    ]

    @classmethod
    def inspect_pii(cls, text: str) -> Dict[str, Any]:
        findings: List[Dict[str, Any]] = []
        if not text:
            return {"total_pii_count": 0, "breakdown": {}, "findings": [], "redacted_text": ""}

        breakdown: Dict[str, int] = {}
        
        for pii_type, pattern, category, conf in cls.PII_PATTERNS:
            for match in re.finditer(pattern, text, re.IGNORECASE):
                val = match.group(0)
                breakdown[pii_type] = breakdown.get(pii_type, 0) + 1
                
                # Create masked representation
                if pii_type == "EMAIL":
                    parts = val.split("@")
                    masked = parts[0][0] + "***@" + parts[1]
                elif pii_type == "SSN":
                    masked = "***-**-" + val[-4:]
                elif pii_type == "CREDIT_CARD":
                    masked = "****-****-****-" + val[-4:]
                elif pii_type == "PHONE_NUMBER":
                    masked = "***-***-" + val[-4:]
                else:
                    masked = f"[{pii_type}_REDACTED]"

                findings.append({
                    "category": "PII",
                    "severity": "HIGH" if pii_type in ["SSN", "CREDIT_CARD", "MEDICAL_RECORD_NUM"] else "MEDIUM",
                    "title": f"Sensitive {pii_type.replace('_', ' ').title()} Exposed",
                    "location": f"Position {match.start()}-{match.end()}",
                    "value": val,
                    "expected_value": masked,
                    "evidence": f"Detected sensitive {pii_type}: {masked}",
                    "explanation": f"Personal Identifiable Information ({pii_type}) is exposed in plain text.",
                    "impact": "Exposing PII risks privacy compliance breaches under GDPR, HIPAA, or CCPA.",
                    "recommendation": f"Redact or mask value before external sharing.",
                    "confidence": conf,
                    "suggested_correction": masked
                })

        # Generate complete redacted copy
        redacted = text
        # Sort findings descending by start to avoid offset shifts
        for f in findings:
            val = f["value"]
            masked = f["expected_value"]
            redacted = redacted.replace(val, masked)

        return {
            "total_pii_count": len(findings),
            "breakdown": breakdown,
            "findings": findings,
            "redacted_text": redacted
        }
