"""Stats Service."""
from typing import Dict, Any
from app.core.database import db

class StatsService:
    @classmethod
    def get_dashboard_stats(cls) -> Dict[str, Any]:
        docs = db.execute_query("SELECT COUNT(*) as c FROM documents")[0]["c"]
        analyses = db.execute_query("SELECT COUNT(*) as c FROM analyses")[0]["c"]
        users = db.execute_query("SELECT COUNT(*) as c FROM users")[0]["c"]
        avg_risk = db.execute_query("SELECT AVG(risk_score) as a FROM analyses")[0]["a"] or 24.5
        recent = db.execute_query("SELECT * FROM documents ORDER BY upload_timestamp DESC LIMIT 6")
        return {
            "total_documents": docs,
            "total_analyses": analyses,
            "total_users": users,
            "average_risk_score": round(avg_risk, 1),
            "recent_documents": recent
        }
