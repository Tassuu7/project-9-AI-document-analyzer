"""Comparison Service."""
import json
import time
import uuid
from typing import Dict, Any
from app.core.database import db
from app.nlp.similarity.comparator import DocumentComparator

class ComparisonService:
    @classmethod
    def compare_texts(cls, a: str, b: str, doc_a_id: str = "A", doc_b_id: str = "B") -> Dict[str, Any]:
        res = DocumentComparator.compare(a, b)
        cid = str(uuid.uuid4())
        db.execute_non_query(
            "INSERT INTO comparisons (id, user_id, doc_a_id, doc_b_id, similarity_score, diff_summary, semantic_drift_json, created_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            (cid, "guest", doc_a_id, doc_b_id, res["similarity_score"], f"+{res['lines_added']} -{res['lines_deleted']}", json.dumps(res), time.time())
        )
        res["comparison_id"] = cid
        return res
