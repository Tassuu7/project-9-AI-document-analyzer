"""Cryptographic Hashing and Token Security."""
import os
import hmac
import hashlib
import base64
import time
import secrets
import json
from typing import Optional, Dict, Any

class SecurityManager:
    SECRET_SALT = b"doc_analyzer_enterprise_secure_salt_v2_2026"
    ITERATIONS = 100_000

    @classmethod
    def hash_password(cls, password: str) -> str:
        salt = secrets.token_bytes(16)
        pwd_hash = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), cls.SECRET_SALT + salt, cls.ITERATIONS)
        return f"{base64.b64encode(salt).decode('utf-8')}${base64.b64encode(pwd_hash).decode('utf-8')}"

    @classmethod
    def verify_password(cls, password: str, hashed_value: str) -> bool:
        try:
            salt_b64, hash_b64 = hashed_value.split("$")
            salt = base64.b64decode(salt_b64.encode("utf-8"))
            expected_hash = base64.b64decode(hash_b64.encode("utf-8"))
            actual_hash = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), cls.SECRET_SALT + salt, cls.ITERATIONS)
            return hmac.compare_digest(expected_hash, actual_hash)
        except Exception:
            return False

    @classmethod
    def generate_token(cls, payload: Dict[str, Any], expiry_seconds: int = 86400) -> str:
        payload_data = payload.copy()
        payload_data["exp"] = int(time.time()) + expiry_seconds
        payload_data["nonce"] = secrets.token_hex(8)
        encoded_payload = base64.urlsafe_b64encode(json.dumps(payload_data).encode("utf-8")).decode("utf-8").rstrip("=")
        signature = hmac.new(cls.SECRET_SALT, encoded_payload.encode("utf-8"), hashlib.sha256).digest()
        encoded_sig = base64.urlsafe_b64encode(signature).decode("utf-8").rstrip("=")
        return f"{encoded_payload}.{encoded_sig}"

    @classmethod
    def verify_token(cls, token: str) -> Optional[Dict[str, Any]]:
        try:
            parts = token.split(".")
            if len(parts) != 2:
                return None
            encoded_payload, encoded_sig = parts
            expected_sig = hmac.new(cls.SECRET_SALT, encoded_payload.encode("utf-8"), hashlib.sha256).digest()
            expected_sig_b64 = base64.urlsafe_b64encode(expected_sig).decode("utf-8").rstrip("=")
            if not hmac.compare_digest(encoded_sig, expected_sig_b64):
                return None
            pad_len = 4 - (len(encoded_payload) % 4)
            if pad_len != 4:
                encoded_payload += "=" * pad_len
            payload_json = base64.urlsafe_b64decode(encoded_payload.encode("utf-8")).decode("utf-8")
            payload = json.loads(payload_json)
            if payload.get("exp", 0) < int(time.time()):
                return None
            return payload
        except Exception:
            return None

    @classmethod
    def generate_file_checksum(cls, file_bytes: bytes) -> str:
        return hashlib.sha256(file_bytes).hexdigest()
