"""Document Structure and Heading Progression Analyzer."""
import re
from typing import Dict, Any, List

class StructureAnalyzer:
    """Validates heading hierarchy, paragraph balance, and transition word density."""

    TRANSITION_WORDS = {
        "furthermore", "moreover", "however", "therefore", "consequently",
        "in addition", "nevertheless", "accordingly", "meanwhile", "specifically",
        "for example", "in contrast", "subsequently", "first", "second", "finally"
    }

    @classmethod
    def analyze_structure(cls, text: str) -> Dict[str, Any]:
        paragraphs = [p.strip() for p in text.split("\n") if p.strip()]
        headings = []
        body_paras = []

        for p in paragraphs:
            if p.startswith("#"):
                level = len(re.match(r'^#+', p).group(0))
                headings.append({"level": level, "text": p.lstrip("#").strip()})
            elif len(p.split()) < 10 and (p.isupper() or p.endswith(":")):
                headings.append({"level": 2, "text": p})
            else:
                body_paras.append(p)

        # Heading hierarchy validation
        heading_issues = []
        for i in range(len(headings) - 1):
            h1 = headings[i]["level"]
            h2 = headings[i+1]["level"]
            if h2 - h1 > 1:
                heading_issues.append({
                    "from_level": f"H{h1}",
                    "to_level": f"H{h2}",
                    "text": headings[i+1]["text"],
                    "issue": f"Skipped heading level from H{h1} directly to H{h2}."
                })

        # Transition word density
        text_lower = text.lower()
        transition_count = sum(1 for tw in cls.TRANSITION_WORDS if tw in text_lower)
        transition_score = min(100, int((transition_count / max(1, len(body_paras))) * 100))

        # Paragraph length balance
        para_word_counts = [len(p.split()) for p in body_paras]
        avg_para_len = round(sum(para_word_counts) / max(1, len(para_word_counts)), 1)
        long_paras = sum(1 for w in para_word_counts if w > 150)
        short_paras = sum(1 for w in para_word_counts if w < 20)

        structure_health = 100
        if heading_issues:
            structure_health -= len(heading_issues) * 10
        if long_paras > 0:
            structure_health -= long_paras * 5
        if transition_score < 30:
            structure_health -= 10
        structure_health = max(40, structure_health)

        return {
            "total_headings": len(headings),
            "total_paragraphs": len(body_paras),
            "average_paragraph_words": avg_para_len,
            "long_paragraphs_count": long_paras,
            "short_paragraphs_count": short_paras,
            "transition_density_score": transition_score,
            "heading_hierarchy_issues": heading_issues,
            "structure_health_score": structure_health,
            "headings_map": headings
        }
