"""Issue and Finding Management Service."""
import time
import uuid
from typing import Dict, Any, List, Optional
from app.core.database import db

class IssueService:
    @classmethod
    def list_issues(cls, document_id: str = None, category: str = None, severity: str = None, status: str = None) -> List[Dict[str, Any]]:
        query = "SELECT * FROM issues WHERE 1=1"
        params = []
        if document_id:
            query += " AND document_id = ?"
            params.append(document_id)
        if category:
            query += " AND category = ?"
            params.append(category.upper())
        if severity:
            query += " AND severity = ?"
            params.append(severity.upper())
        if status:
            query += " AND status = ?"
            params.append(status.upper())
        query += " ORDER BY CASE severity WHEN 'CRITICAL' THEN 1 WHEN 'HIGH' THEN 2 WHEN 'MEDIUM' THEN 3 WHEN 'LOW' THEN 4 ELSE 5 END, created_at DESC"
        return db.execute_query(query, tuple(params))

    @classmethod
    def get_issue(cls, issue_id: str) -> Optional[Dict[str, Any]]:
        rows = db.execute_query("SELECT * FROM issues WHERE id = ?", (issue_id,))
        return rows[0] if rows else None

    @classmethod
    def update_issue_status(cls, issue_id: str, status: str, user_comment: str = "") -> bool:
        valid_statuses = ["OPEN", "CONFIRMED", "RESOLVED", "IGNORED", "FALSE_POSITIVE", "NEEDS_REVIEW"]
        status_norm = status.upper()
        if status_norm not in valid_statuses:
            return False
        
        query = "UPDATE issues SET status = ?, updated_at = ?"
        params = [status_norm, time.time()]
        if user_comment:
            query += ", user_comment = ?"
            params.append(user_comment)
        query += " WHERE id = ?"
        params.append(issue_id)
        return db.execute_non_query(query, tuple(params)) > 0

    @classmethod
    def get_issue_metrics(cls, document_id: str = None) -> Dict[str, Any]:
        issues = cls.list_issues(document_id=document_id)
        total = len(issues)
        by_severity = {"CRITICAL": 0, "HIGH": 0, "MEDIUM": 0, "LOW": 0, "INFO": 0}
        by_category = {}
        by_status = {"OPEN": 0, "CONFIRMED": 0, "RESOLVED": 0, "IGNORED": 0, "FALSE_POSITIVE": 0, "NEEDS_REVIEW": 0}
        
        for iss in issues:
            sev = iss.get("severity", "LOW")
            cat = iss.get("category", "OTHER")
            st = iss.get("status", "OPEN")
            
            by_severity[sev] = by_severity.get(sev, 0) + 1
            by_category[cat] = by_category.get(cat, 0) + 1
            by_status[st] = by_status.get(st, 0) + 1

        return {
            "total_issues": total,
            "by_severity": by_severity,
            "by_category": by_category,
            "by_status": by_status,
            "open_issues_count": total - by_status.get("RESOLVED", 0) - by_status.get("IGNORED", 0)
        }
