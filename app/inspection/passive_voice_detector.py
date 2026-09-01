"""Passive Voice Detection and Active Voice Conversion Engine."""
import re
from typing import List, Dict, Any
from app.nlp.lexicons.grammar_rules_database import AUXILIARY_BE_VERBS, PAST_PARTICIPLES, IRREGULAR_VERBS

class PassiveVoiceDetector:
    """Detects passive auxiliary constructions (e.g., 'was conducted by', 'is processed')."""

    REGULAR_PAST_PARTICIPLE_PATTERN = re.compile(r'^[a-z]{3,}(ed|en|t)$', re.IGNORECASE)

    @classmethod
    def detect_passive_voice(cls, text: str) -> List[Dict[str, Any]]:
        findings = []
        sentences = re.split(r'(?<=[.?!])\s+', text)

        for s_idx, sentence in enumerate(sentences, 1):
            if not sentence.strip():
                continue
            words = re.findall(r'\b[a-zA-Z]+\b', sentence)
            for i in range(len(words) - 1):
                w1 = words[i].lower()
                w2 = words[i+1].lower()

                if w1 in AUXILIARY_BE_VERBS and cls._is_past_participle(w2):
                    phrase = f"{words[i]} {words[i+1]}"
                    loc = f"Sentence {s_idx}"
                    active_hint = cls._suggest_active_voice(words, i)

                    findings.append({
                        "id": f"passive_{s_idx}_{i}",
                        "title": f"Passive Voice Construction: '{phrase}'",
                        "category": "PASSIVE_VOICE",
                        "severity": "LOW",
                        "location": loc,
                        "value": phrase,
                        "expected_value": "Active voice equivalent",
                        "evidence": sentence.strip(),
                        "explanation": f"The clause uses passive voice ('{phrase}'), which can make sentence flow less direct.",
                        "impact": "Reduces readability and direct engagement.",
                        "recommendation": active_hint,
                        "confidence": 0.92,
                        "status": "OPEN",
                        "suggested_correction": ""
                    })

        return findings

    @classmethod
    def _is_past_participle(cls, word: str) -> bool:
        if word in PAST_PARTICIPLES:
            return True
        if cls.REGULAR_PAST_PARTICIPLE_PATTERN.match(word):
            # Exclude obvious non-verbs ending in ed/en
            if word not in {"red", "bed", "fed", "then", "when", "ten", "men", "even", "open"}:
                return True
        return False

    @classmethod
    def _suggest_active_voice(cls, words: List[str], aux_idx: int) -> str:
        # Check if agent exists ("... by [agent]")
        by_idx = -1
        for j in range(aux_idx + 1, len(words)):
            if words[j].lower() == "by":
                by_idx = j
                break
        if by_idx != -1 and by_idx + 1 < len(words):
            agent = " ".join(words[by_idx+1:])
            return f"Rephrase with active subject: '{agent} {words[aux_idx+1]}...'"
        return "Convert to active voice by placing the acting subject before the verb."
