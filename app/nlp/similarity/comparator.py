"""Document Comparator."""
import difflib
from typing import Dict, Any
from app.nlp.similarity.vectorizer import TFIDFVectorizer

class DocumentComparator:
    @classmethod
    def compare(cls, text_a: str, text_b: str) -> Dict[str, Any]:
        v = TFIDFVectorizer()
        vecs = v.fit_transform([text_a, text_b])
        sim = TFIDFVectorizer.cosine_similarity(vecs[0], vecs[1])
        lines_a = text_a.splitlines()
        lines_b = text_b.splitlines()
        matcher = difflib.SequenceMatcher(None, lines_a, lines_b)
        additions, deletions, mods = 0, 0, 0
        for tag, alo, ahi, blo, bhi in matcher.get_opcodes():
            if tag == "insert": additions += (bhi - blo)
            elif tag == "delete": deletions += (ahi - alo)
            elif tag == "replace": mods += max(ahi - alo, bhi - blo)
        return {
            "similarity_score": round(sim * 100.0, 2),
            "semantic_drift_percentage": round((1.0 - sim) * 100.0, 2),
            "lines_added": additions,
            "lines_deleted": deletions,
            "lines_modified": mods
        }
