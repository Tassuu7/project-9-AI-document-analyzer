"""Compliance Engine."""
from typing import List, Dict, Any
from app.nlp.tokenizers.sentence_tokenizer import SentenceTokenizer
from app.nlp.lexicons.compliance_taxonomy import COMPLIANCE_STANDARDS

class ComplianceEngine:
    @classmethod
    def audit_document(cls, text: str) -> Dict[str, Any]:
        sentences = SentenceTokenizer.tokenize(text)
        text_lower = text.lower()
        violations: List[Dict[str, Any]] = []
        framework_scores = {}

        for std, data in COMPLIANCE_STANDARDS.items():
            mandatory = data["mandatory_terms"]
            prohibited = data["prohibited_patterns"]
            present = [m for m in mandatory if m in text_lower]
            
            for s in sentences:
                sl = s.lower()
                for p in prohibited:
                    if p in sl:
                        violations.append({
                            "standard": std,
                            "severity": "CRITICAL" if "cvv" in p or "unencrypted" in p else "HIGH",
                            "clause": s.strip(),
                            "rule": f"{std} Prohibition of '{p}'",
                            "remediation": f"Remediate and enforce standard {std} operational controls."
                        })
            cov = len(present) / max(1, len(mandatory))
            framework_scores[std] = round(max(0.0, (cov * 100.0) - (len(violations) * 15.0)), 1)

        crit = sum(1 for v in violations if v["severity"] == "CRITICAL")
        return {
            "overall_compliance_score": round(sum(framework_scores.values()) / max(1, len(framework_scores)), 1),
            "framework_scores": framework_scores,
            "violations_found": violations,
            "critical_violations": crit
        }
