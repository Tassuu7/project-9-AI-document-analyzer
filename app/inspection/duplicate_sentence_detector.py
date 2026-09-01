"""Duplicate and Near-Duplicate Sentence Detection Engine."""
import re
from typing import List, Dict, Any, Set

class DuplicateSentenceDetector:
    """Finds exact and near-duplicate sentences across the document."""

    @classmethod
    def detect_duplicate_sentences(cls, text: str) -> List[Dict[str, Any]]:
        findings = []
        sentences = [s.strip() for s in re.split(r'(?<=[.?!])\s+', text) if len(s.strip().split()) >= 4]
        
        seen_exact: Dict[str, int] = {}
        for idx, s in enumerate(sentences, 1):
            s_norm = s.lower().strip()
            if s_norm in seen_exact:
                prev_idx = seen_exact[s_norm]
                findings.append({
                    "id": f"dup_exact_{idx}",
                    "title": f"Duplicate Sentence Detected",
                    "category": "DUPLICATE_TEXT",
                    "severity": "MEDIUM",
                    "location": f"Sentence {idx} matches Sentence {prev_idx}",
                    "value": s,
                    "expected_value": "Unique assertion",
                    "evidence": f"First instance at Sentence {prev_idx}: '{sentences[prev_idx-1]}'",
                    "explanation": "This sentence is an exact duplicate of a previous statement in the document.",
                    "impact": "Creates unnecessary redundancy and document bloat.",
                    "recommendation": "Remove or consolidate the repeated sentence.",
                    "confidence": 0.99,
                    "status": "OPEN",
                    "suggested_correction": ""
                })
            else:
                seen_exact[s_norm] = idx

        # Near-duplicate matching using word Jaccard index
        for i in range(len(sentences)):
            w1 = set(sentences[i].lower().split())
            for j in range(i + 1, len(sentences)):
                w2 = set(sentences[j].lower().split())
                intersection = len(w1.intersection(w2))
                union = len(w1.union(w2))
                jaccard = intersection / max(1, union)

                if 0.75 <= jaccard < 0.99:
                    findings.append({
                        "id": f"near_dup_{i}_{j}",
                        "title": f"Highly Similar Sentence ({int(jaccard*100)}% Similarity)",
                        "category": "SIMILAR_TEXT",
                        "severity": "LOW",
                        "location": f"Sentence {j+1} vs Sentence {i+1}",
                        "value": sentences[j],
                        "expected_value": "Distinct framing",
                        "evidence": f"Sentence {i+1}: '{sentences[i]}'\nSentence {j+1}: '{sentences[j]}'",
                        "explanation": f"These two sentences express near-identical thoughts with minor word substitutions.",
                        "impact": "Diminishes clarity through repetition.",
                        "recommendation": "Consolidate both sentences into a single, comprehensive statement.",
                        "confidence": round(jaccard, 2),
                        "status": "OPEN",
                        "suggested_correction": ""
                    })

        return findings
