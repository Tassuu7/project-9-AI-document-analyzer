"""Document Classifier."""
from typing import Dict, Any
from app.nlp.tokenizers.word_tokenizer import WordTokenizer

class DocumentClassifier:
    CATEGORIES = {
        "Legal Commercial Contract": {
            "keywords": ["agreement", "parties", "covenants", "indemnification", "governing law", "jurisdiction", "liability"],
            "weight": 1.0
        },
        "Non-Disclosure Agreement (NDA)": {
            "keywords": ["non-disclosure", "nda", "confidential information", "disclosing party", "receiving party", "trade secrets", "proprietary information"],
            "weight": 2.2
        },
        "Financial Statement / 10-K": {
            "keywords": ["balance sheet", "income statement", "cash flows", "ebitda", "gross profit", "revenue", "fiscal year", "eps"],
            "weight": 1.8
        },
        "Medical / Clinical Record": {
            "keywords": ["patient", "diagnosis", "clinical", "hospital", "physician", "medical record", "vitals", "discharge summary"],
            "weight": 1.8
        },
        "Technical Architecture Spec": {
            "keywords": ["architecture", "api", "database", "infrastructure", "microservices", "latency", "server", "kubernetes"],
            "weight": 1.5
        },
        "Security & Compliance Audit": {
            "keywords": ["audit", "vulnerability", "pci-dss", "gdpr", "penetration testing", "incident disclosure", "remediation"],
            "weight": 1.8
        }
    }

    @classmethod
    def classify(cls, text: str) -> Dict[str, Any]:
        tokens = WordTokenizer.tokenize(text.lower())
        token_set = set(tokens)
        scores: Dict[str, float] = {}
        text_lower = text.lower()
        for cat, conf in cls.CATEGORIES.items():
            kws = conf["keywords"]
            w = conf["weight"]
            cnt = sum(tokens.count(k) for k in kws if k in token_set)
            phrase_cnt = sum(3 for k in kws if " " in k and k in text_lower)
            scores[cat] = (cnt + phrase_cnt) * w

        total = sum(scores.values())
        if total == 0:
            return {"category": "General Document", "confidence": 0.5, "all_scores": scores}
        best = max(scores, key=scores.get)
        confidence = min(0.98, max(0.60, (scores[best] / total) + 0.35))
        return {"category": best, "confidence": round(confidence, 4), "all_scores": scores}
