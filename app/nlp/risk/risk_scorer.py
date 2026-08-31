"""Risk Scorer."""
from typing import Dict, Any, List
from app.nlp.tokenizers.sentence_tokenizer import SentenceTokenizer

class RiskScorer:
    @classmethod
    def evaluate_risk(cls, text: str) -> Dict[str, Any]:
        text_lower = text.lower()
        risk_factors: List[Dict[str, Any]] = []
        score = 15.0
        if "unlimited liability" in text_lower:
            risk_factors.append({"category": "Liability", "severity": "CRITICAL", "description": "Unlimited liability clause detected."})
            score += 35.0
        if "terminate immediately without notice" in text_lower:
            risk_factors.append({"category": "Termination", "severity": "HIGH", "description": "Immediate termination without notice."})
            score += 25.0
        if "indemnify" in text_lower:
            risk_factors.append({"category": "Indemnity", "severity": "MEDIUM", "description": "Broad indemnification obligations."})
            score += 15.0
        final_score = min(99.0, max(5.0, score))
        level = "HIGH RISK" if final_score >= 60 else "MODERATE RISK" if final_score >= 35 else "LOW RISK"
        return {
            "overall_risk_score": round(final_score, 2),
            "risk_level": level,
            "risk_factors": risk_factors
        }
