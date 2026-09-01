"""Filler Word, Fluff, and Redundancy Detection Engine."""
import re
from typing import List, Dict, Any
from app.nlp.lexicons.filler_words_database import FILLER_PHRASES, REDUNDANT_PAIRS, SINGLE_FILLER_WORDS

class FillerDetector:
    """Detects conversational fluff, wordy phrases, and tautologies."""

    @classmethod
    def detect_fillers(cls, text: str) -> List[Dict[str, Any]]:
        findings = []
        idx = 1

        # 1. Multi-word wordy phrases
        for phrase, concise in FILLER_PHRASES.items():
            matches = list(re.finditer(r'\b' + re.escape(phrase) + r'\b', text, re.IGNORECASE))
            for m in matches:
                findings.append({
                    "id": f"filler_phrase_{idx}",
                    "title": f"Wordy Phrase: '{m.group(0)}'",
                    "category": "FILLER_WORD",
                    "severity": "LOW",
                    "location": f"Position {m.start()}-{m.end()}",
                    "value": m.group(0),
                    "expected_value": concise or "Omit phrase",
                    "evidence": text[max(0, m.start()-20):min(len(text), m.end()+20)].strip(),
                    "explanation": f"The phrase '{m.group(0)}' is wordy and can be replaced with a more direct formulation.",
                    "impact": "Adds unnecessary length without adding information.",
                    "recommendation": f"Replace with '{concise}'" if concise else "Omit this phrase to streamline sentence.",
                    "confidence": 0.94,
                    "status": "OPEN",
                    "suggested_correction": concise
                })
                idx += 1

        # 2. Redundant word pairs (Tautologies)
        for rp, concise in REDUNDANT_PAIRS.items():
            matches = list(re.finditer(r'\b' + re.escape(rp) + r'\b', text, re.IGNORECASE))
            for m in matches:
                findings.append({
                    "id": f"redundancy_{idx}",
                    "title": f"Redundant Expression: '{m.group(0)}'",
                    "category": "REDUNDANCY",
                    "severity": "LOW",
                    "location": f"Position {m.start()}-{m.end()}",
                    "value": m.group(0),
                    "expected_value": concise,
                    "evidence": text[max(0, m.start()-20):min(len(text), m.end()+20)].strip(),
                    "explanation": f"'{m.group(0)}' is a tautology (the modifier repeats the noun's meaning).",
                    "impact": "Reduces prose precision.",
                    "recommendation": f"Simplify to '{concise}'.",
                    "confidence": 0.96,
                    "status": "OPEN",
                    "suggested_correction": concise
                })
                idx += 1

        # 3. Single filler words
        for sfw in SINGLE_FILLER_WORDS:
            matches = list(re.finditer(r'\b' + re.escape(sfw) + r'\b', text, re.IGNORECASE))
            for m in matches:
                findings.append({
                    "id": f"single_filler_{idx}",
                    "title": f"Conversational Filler: '{m.group(0)}'",
                    "category": "FILLER_WORD",
                    "severity": "INFO",
                    "location": f"Position {m.start()}-{m.end()}",
                    "value": m.group(0),
                    "expected_value": "Omit word",
                    "evidence": text[max(0, m.start()-20):min(len(text), m.end()+20)].strip(),
                    "explanation": f"The word '{m.group(0)}' is a weak modifier or conversational filler in formal documents.",
                    "impact": "Dilutes the assertiveness of the statement.",
                    "recommendation": "Remove this word to achieve a more authoritative tone.",
                    "confidence": 0.88,
                    "status": "OPEN",
                    "suggested_correction": ""
                })
                idx += 1

        return findings
