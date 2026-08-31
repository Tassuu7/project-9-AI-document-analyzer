"""Auth Service."""
import time
import uuid
from typing import Dict, Any
from app.core.database import db
from app.core.security import SecurityManager
from app.core.exceptions import AuthenticationError, ValidationError

class AuthService:
    @classmethod
    def register(cls, username: str, email: str, password: str, full_name: str = "", role: str = "Analyst") -> Dict[str, Any]:
        if not username or len(username) < 3: raise ValidationError("Invalid username")
        if not password or len(password) < 6: raise ValidationError("Password too short")
        existing = db.execute_query("SELECT id FROM users WHERE username = ? OR email = ?", (username, email))
        if existing: raise ValidationError("User already exists")
        uid = str(uuid.uuid4())
        pwd_hash = SecurityManager.hash_password(password)
        now = time.time()
        db.execute_non_query(
            "INSERT INTO users (id, username, email, password_hash, role, full_name, created_at, is_active) VALUES (?, ?, ?, ?, ?, ?, ?, 1)",
            (uid, username, email, pwd_hash, role, full_name or username, now)
        )
        token = SecurityManager.generate_token({"sub": uid, "username": username, "role": role})
        return {"user": {"id": uid, "username": username, "email": email, "role": role}, "token": token}

    @classmethod
    def login(cls, username_or_email: str, password: str) -> Dict[str, Any]:
        rows = db.execute_query("SELECT * FROM users WHERE username = ? OR email = ?", (username_or_email, username_or_email))
        if not rows or not SecurityManager.verify_password(password, rows[0]["password_hash"]):
            raise AuthenticationError("Invalid username or password")
        u = rows[0]
        token = SecurityManager.generate_token({"sub": u["id"], "username": u["username"], "role": u["role"]})
        return {"user": {"id": u["id"], "username": u["username"], "email": u["email"], "role": u["role"]}, "token": token}
