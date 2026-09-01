"""In-App Notification and Alert Dispatcher."""
import time
import uuid
from typing import Dict, Any, List
from app.core.database import db

class NotificationService:
    @classmethod
    def create_notification(cls, user_id: str, n_type: str, title: str, message: str, link: str = "") -> str:
        nid = str(uuid.uuid4())
        db.execute_non_query(
            "INSERT INTO notifications (id, user_id, type, title, message, link, is_read, created_at) VALUES (?, ?, ?, ?, ?, ?, 0, ?)",
            (nid, user_id, n_type.upper(), title, message, link, time.time())
        )
        return nid

    @classmethod
    def list_user_notifications(cls, user_id: str, unread_only: bool = False) -> List[Dict[str, Any]]:
        query = "SELECT * FROM notifications WHERE user_id = ?"
        params = [user_id]
        if unread_only:
            query += " AND is_read = 0"
        query += " ORDER BY created_at DESC LIMIT 50"
        return db.execute_query(query, tuple(params))

    @classmethod
    def mark_as_read(cls, notification_id: str) -> bool:
        return db.execute_non_query("UPDATE notifications SET is_read = 1 WHERE id = ?", (notification_id,)) > 0

    @classmethod
    def mark_all_as_read(cls, user_id: str) -> bool:
        return db.execute_non_query("UPDATE notifications SET is_read = 1 WHERE user_id = ?", (user_id,)) > 0
