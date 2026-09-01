"""User Authentication, RBAC, and Demo Accounts Initialization."""
import time
import uuid
from typing import Dict, Any, Optional, List
from app.core.database import db
from app.core.security import Security

class AuthService:
    @classmethod
    def register_user(cls, username: str, email: str, password: str, full_name: str = "", role: str = "ANALYST") -> Dict[str, Any]:
        existing = db.execute_query("SELECT id FROM users WHERE username = ? OR email = ?", (username, email))
        if existing:
            raise ValueError("Username or email already registered.")
        
        user_id = str(uuid.uuid4())
        pwd_hash = Security.hash_password(password)
        now = time.time()
        
        db.execute_non_query(
            "INSERT INTO users (id, username, email, password_hash, role, full_name, created_at, is_active) VALUES (?, ?, ?, ?, ?, ?, ?, 1)",
            (user_id, username, email, pwd_hash, role.upper(), full_name or username, now)
        )
        token = Security.generate_token(user_id, username, role.upper())
        return {
            "token": token,
            "user": {
                "id": user_id,
                "username": username,
                "email": email,
                "role": role.upper(),
                "full_name": full_name
            }
        }

    @classmethod
    def authenticate_user(cls, username: str, password: str) -> Dict[str, Any]:
        rows = db.execute_query("SELECT * FROM users WHERE username = ? OR email = ?", (username, username))
        if not rows:
            raise ValueError("Invalid username or password.")
        user = rows[0]
        if not Security.verify_password(password, user["password_hash"]):
            raise ValueError("Invalid username or password.")
        
        db.execute_non_query("UPDATE users SET last_login = ? WHERE id = ?", (time.time(), user["id"]))
        token = Security.generate_token(user["id"], user["username"], user["role"])
        return {
            "token": token,
            "user": {
                "id": user["id"],
                "username": user["username"],
                "email": user["email"],
                "role": user["role"],
                "full_name": user["full_name"]
            }
        }

    @classmethod
    def init_demo_accounts(cls):
        demo_users = [
            ("admin", "admin@inspector.local", "AdminPass2026!", "ADMIN", "System Administrator"),
            ("analyst", "analyst@inspector.local", "AnalystPass2026!", "ANALYST", "Lead Document Analyst"),
            ("viewer", "viewer@inspector.local", "ViewerPass2026!", "VIEWER", "Audit Reviewer")
        ]
        for u, email, pwd, role, full in demo_users:
            rows = db.execute_query("SELECT id FROM users WHERE username = ?", (u,))
            if not rows:
                user_id = str(uuid.uuid4())
                pwd_hash = Security.hash_password(pwd)
                db.execute_non_query(
                    "INSERT INTO users (id, username, email, password_hash, role, full_name, created_at, is_active) VALUES (?, ?, ?, ?, ?, ?, ?, 1)",
                    (user_id, u, email, pwd_hash, role, full, time.time())
                )
        print("[+] Demo accounts (Admin, Analyst, Viewer) initialized.")

    @classmethod
    def list_users(cls) -> List[Dict[str, Any]]:
        rows = db.execute_query("SELECT id, username, email, role, full_name, created_at, last_login, is_active FROM users ORDER BY created_at ASC")
        return rows

AuthService.register = AuthService.register_user
AuthService.login = AuthService.authenticate_user
