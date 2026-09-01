"""Immutable Audit Logging Subsystem."""
import time
import uuid
from typing import Dict, Any, List
from app.core.database import db

class AuditService:
    @classmethod
    def log_action(cls, user_id: str, username: str, action: str, target: str, result: str = "SUCCESS", details: str = "") -> str:
        aid = str(uuid.uuid4())
        db.execute_non_query(
            "INSERT INTO audit_logs (id, user_id, username, action, target, result, details, timestamp) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            (aid, user_id, username, action.upper(), target, result.upper(), details, time.time())
        )
        return aid

    @classmethod
    def list_logs(cls, limit: int = 100) -> List[Dict[str, Any]]:
        return db.execute_query("SELECT * FROM audit_logs ORDER BY timestamp DESC LIMIT ?", (limit,))
