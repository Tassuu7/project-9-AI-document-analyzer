"""Authentication, Cryptography & Role-Based Authorization Engine."""
import hashlib
import hmac
import base64
import json
import time
import uuid
import secrets
from typing import Dict, Any, Optional

SECRET_KEY = "enterprise-doc-inspector-secure-key-2026-strict-signature"

class Security:
    ROLES = ["ADMIN", "ANALYST", "VIEWER"]

    @classmethod
    def hash_password(cls, password: str, salt: str = None) -> str:
        if not salt:
            salt = secrets.token_hex(16)
        key = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt.encode("utf-8"), 100000)
        return f"{salt}:{key.hex()}"

    @classmethod
    def verify_password(cls, password: str, password_hash: str) -> bool:
        try:
            salt, stored_key = password_hash.split(":", 1)
            calculated_key = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt.encode("utf-8"), 100000).hex()
            return hmac.compare_digest(calculated_key, stored_key)
        except Exception:
            return False

    @classmethod
    def generate_token(cls, user_id: str, username: str, role: str) -> str:
        payload = {
            "sub": user_id,
            "username": username,
            "role": role.upper(),
            "iat": time.time(),
            "exp": time.time() + (24 * 3600),
            "jti": str(uuid.uuid4())
        }
        data = base64.urlsafe_b64encode(json.dumps(payload).encode("utf-8")).decode("utf-8").rstrip("=")
        signature = hmac.new(SECRET_KEY.encode("utf-8"), data.encode("utf-8"), hashlib.sha256).hexdigest()
        return f"{data}.{signature}"

    @classmethod
    def decode_token(cls, token: str) -> Optional[Dict[str, Any]]:
        try:
            if not token or "." not in token:
                return None
            data_str, sig = token.split(".", 1)
            expected_sig = hmac.new(SECRET_KEY.encode("utf-8"), data_str.encode("utf-8"), hashlib.sha256).hexdigest()
            if not hmac.compare_digest(sig, expected_sig):
                return None
            padded = data_str + "=" * (-len(data_str) % 4)
            payload = json.loads(base64.urlsafe_b64decode(padded.encode("utf-8")).decode("utf-8"))
            if payload.get("exp", 0) < time.time():
                return None
            return payload
        except Exception:
            return None

    @classmethod
    def check_permission(cls, user_role: str, required_role: str) -> bool:
        role_hierarchy = {"ADMIN": 3, "ANALYST": 2, "VIEWER": 1}
        user_level = role_hierarchy.get(user_role.upper(), 0)
        req_level = role_hierarchy.get(required_role.upper(), 99)
        return user_level >= req_level

    @classmethod
    def calculate_checksum(cls, content: bytes) -> str:
        return hashlib.sha256(content).hexdigest()
