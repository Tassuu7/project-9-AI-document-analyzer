"""Document Comparison and Risk Delta Service."""
import json
import time
import uuid
from typing import Dict, Any, List
from app.core.database import db
from app.nlp.similarity.comparator import DocumentComparator
from app.inspection.risk_analyzer import RiskAnalyzer

class ComparisonService:
    @classmethod
    def compare_documents(cls, text_a: str, text_b: str, user_id: str = "user_default", doc_a_id: str = "", doc_b_id: str = "") -> Dict[str, Any]:
        diff_res = DocumentComparator.compare(text_a, text_b)
        
        # Risk Delta Calculation
        risk_a = RiskAnalyzer.evaluate_risks(text_a)
        risk_b = RiskAnalyzer.evaluate_risks(text_b)
        
        score_a = risk_a["overall_risk_score"]
        score_b = risk_b["overall_risk_score"]
        risk_delta = round(score_b - score_a, 1)

        result = {
            "similarity_score": diff_res["similarity_score"],
            "lines_added": diff_res["lines_added"],
            "lines_deleted": diff_res["lines_deleted"],
            "lines_modified": diff_res["lines_modified"],
            "lines_unchanged": diff_res["lines_unchanged"],
            "diff_lines": diff_res["diff_lines"],
            "risk_score_v1": score_a,
            "risk_score_v2": score_b,
            "risk_delta": risk_delta,
            "risk_delta_explanation": f"Risk increased by +{risk_delta} points" if risk_delta > 0 else f"Risk decreased by {risk_delta} points" if risk_delta < 0 else "Risk level unchanged",
            "semantic_drift": diff_res.get("semantic_drift", {}),
            "created_at": time.time()
        }

        if doc_a_id and doc_b_id:
            cid = str(uuid.uuid4())
            db.execute_non_query(
                "INSERT INTO comparisons (id, user_id, doc_a_id, doc_b_id, similarity_score, risk_delta, diff_summary, diff_json, created_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (cid, user_id, doc_a_id, doc_b_id, diff_res["similarity_score"], risk_delta, result["risk_delta_explanation"], json.dumps(result), time.time())
            )
            result["id"] = cid

        return result
