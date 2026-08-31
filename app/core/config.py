"""Central Settings and Configuration."""
import os
from typing import List

class Settings:
    APP_NAME: str = "AI Document Analyzer Enterprise Platform"
    APP_VERSION: str = "2.4.0"
    HOST: str = "127.0.0.1"
    PORT: int = 8974
    UNIQUE_LOCAL_URL: str = "http://127.0.0.1:8974"
    DEBUG: bool = False

    BASE_DIR: str = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    STORAGE_DIR: str = os.path.join(BASE_DIR, "app", "storage", "data")
    UPLOAD_DIR: str = os.path.join(STORAGE_DIR, "uploads")
    PROCESSED_DIR: str = os.path.join(STORAGE_DIR, "processed")
    EXPORTS_DIR: str = os.path.join(STORAGE_DIR, "exports")
    DB_FILE: str = os.path.join(STORAGE_DIR, "analyzer.db")

    SESSION_COOKIE_NAME: str = "doc_analyzer_session"
    TOKEN_EXPIRATION_HOURS: int = 24
    MAX_UPLOAD_SIZE_MB: int = 50
    ALLOWED_EXTENSIONS: List[str] = ["txt", "pdf", "docx", "csv", "json", "md", "html"]

    SUPPORTED_COMPLIANCE_STANDARDS: List[str] = [
        "GDPR", "HIPAA", "SOC2", "PCI-DSS", "CCPA", "ISO27001"
    ]

    @classmethod
    def ensure_directories(cls):
        for path in [cls.STORAGE_DIR, cls.UPLOAD_DIR, cls.PROCESSED_DIR, cls.EXPORTS_DIR]:
            os.makedirs(path, exist_ok=True)

settings = Settings()
settings.ensure_directories()
