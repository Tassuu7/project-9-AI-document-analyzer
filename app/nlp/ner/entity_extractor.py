"""NER & PII Extractor."""
import re
from typing import List, Dict, Any
from app.nlp.lexicons.entity_lexicons import KNOWN_ORGANIZATIONS, ISO_COUNTRIES

class EntityExtractor:
    EMAIL_PATTERN = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
    PHONE_PATTERN = re.compile(r'(?:\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}')
    SSN_PATTERN = re.compile(r'\b\d{3}-\d{2}-\d{4}\b')
    MONEY_PATTERN = re.compile(r'(?:[\$\€\£\¥\₹]\s*|\b(?:USD|EUR|GBP|INR)\s*)\d+(?:,\d{3})*(?:\.\d{1,2})?(?:\s*(?:million|billion|k|m|b))?\b', re.IGNORECASE)
    DATE_PATTERN = re.compile(r'\b(?:\d{1,2}[/-]\d{1,2}[/-]\d{2,4}|(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember))\s+\d{1,2}(?:st|nd|rd|th)?,?\s+\d{4}|\d{4}-\d{2}-\d{2})\b', re.IGNORECASE)

    @classmethod
    def extract_entities(cls, text: str) -> List[Dict[str, Any]]:
        entities: List[Dict[str, Any]] = []
        if not text: return entities

        for m in cls.EMAIL_PATTERN.finditer(text):
            entities.append({"type": "EMAIL", "text": m.group(0), "start": m.start(), "end": m.end(), "category": "PII", "confidence": 0.99})
        for m in cls.PHONE_PATTERN.finditer(text):
            entities.append({"type": "PHONE_NUMBER", "text": m.group(0), "start": m.start(), "end": m.end(), "category": "PII", "confidence": 0.95})
        for m in cls.SSN_PATTERN.finditer(text):
            entities.append({"type": "SSN", "text": m.group(0), "start": m.start(), "end": m.end(), "category": "PII", "confidence": 0.98})
        for m in cls.MONEY_PATTERN.finditer(text):
            entities.append({"type": "MONETARY_VALUE", "text": m.group(0), "start": m.start(), "end": m.end(), "category": "FINANCIAL", "confidence": 0.95})
        for m in cls.DATE_PATTERN.finditer(text):
            entities.append({"type": "DATE", "text": m.group(0), "start": m.start(), "end": m.end(), "category": "TEMPORAL", "confidence": 0.94})

        for org in KNOWN_ORGANIZATIONS:
            for m in re.finditer(rf'\b{re.escape(org)}\b', text, re.IGNORECASE):
                entities.append({"type": "ORGANIZATION", "text": m.group(0), "start": m.start(), "end": m.end(), "category": "ORGANIZATION", "confidence": 0.92})

        for country in ISO_COUNTRIES:
            for m in re.finditer(rf'\b{re.escape(country)}\b', text, re.IGNORECASE):
                entities.append({"type": "LOCATION", "text": m.group(0), "start": m.start(), "end": m.end(), "category": "GEOPOLITICAL", "confidence": 0.91})

        entities.sort(key=lambda x: (x["start"], -(x["end"] - x["start"])))
        deduped = []
        last_end = -1
        for e in entities:
            if e["start"] >= last_end:
                deduped.append(e)
                last_end = e["end"]
        return deduped
