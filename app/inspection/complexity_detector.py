"""Long and Complex Sentence Detection Engine."""
import re
from typing import List, Dict, Any

class ComplexityDetector:
    """Identifies excessively long sentences (> 25 words) and complex multi-clause structures."""

    MAX_RECOMMENDED_WORDS = 25
    CRITICAL_RECOMMENDED_WORDS = 40

    @classmethod
    def detect_complex_sentences(cls, text: str) -> List[Dict[str, Any]]:
        findings = []
        sentences = re.split(r'(?<=[.?!])\s+', text)

        for s_idx, s in enumerate(sentences, 1):
            s_clean = s.strip()
            if not s_clean:
                continue
            words = s_clean.split()
            w_count = len(words)

            if w_count >= cls.MAX_RECOMMENDED_WORDS:
                severity = "HIGH" if w_count >= cls.CRITICAL_RECOMMENDED_WORDS else "MEDIUM"
                clauses = len(re.split(r'[,;:]|\b(although|whereas|furthermore|however|nevertheless|consequently)\b', s_clean, flags=re.IGNORECASE))

                findings.append({
                    "id": f"complex_sentence_{s_idx}",
                    "title": f"Complex Sentence Detected ({w_count} words)",
                    "category": "COMPLEXITY",
                    "severity": severity,
                    "location": f"Sentence {s_idx}",
                    "value": f"{w_count} words in single sentence",
                    "expected_value": f"Under {cls.MAX_RECOMMENDED_WORDS} words",
                    "evidence": s_clean,
                    "explanation": f"This sentence contains {w_count} words and multiple nested sub-clauses, which increases cognitive load.",
                    "impact": "Significantly impairs comprehension and readability scores.",
                    "recommendation": "Split this sentence into two or more concise, focused statements.",
                    "confidence": 0.95,
                    "status": "OPEN",
                    "suggested_correction": cls._suggest_split(s_clean)
                })

        return findings

    @classmethod
    def _suggest_split(cls, sentence: str) -> str:
        # Simple splitting at major conjunctions
        match = re.search(r'([,;]\s*(?:and|but|while|whereas|although|however)\s+)', sentence, re.IGNORECASE)
        if match:
            split_pos = match.start()
            s1 = sentence[:split_pos].strip()
            s2 = sentence[match.end():].strip().capitalize()
            return f"{s1}. {s2}"
        return ""
