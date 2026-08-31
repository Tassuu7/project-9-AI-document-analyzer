"""PII Masker."""
import hashlib
from typing import Dict, Any
from app.nlp.ner.entity_extractor import EntityExtractor

class PIIMasker:
    @classmethod
    def mask_document(cls, text: str, mode: str = "tag") -> Dict[str, Any]:
        entities = EntityExtractor.extract_entities(text)
        pii = [e for e in entities if e["category"] in ["PII", "FINANCIAL_PII"] or e["type"] in ["EMAIL", "PHONE_NUMBER", "SSN"]]
        pii.sort(key=lambda x: x["start"], reverse=True)
        masked_text = text
        counts = {}
        for e in pii:
            etype = e["type"]
            counts[etype] = counts.get(etype, 0) + 1
            idx = counts[etype]
            rep = f"[{etype}_{idx}]" if mode == "tag" else "[REDACTED]"
            masked_text = masked_text[:e["start"]] + rep + masked_text[e["end"]:]
        return {"masked_text": masked_text, "entities_masked": len(pii)}
