"""Thread-Safe Relational Database Engine with WAL Mode."""
import sqlite3
import threading
import time
from typing import Dict, Any, List
from app.core.config import settings

class Database:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(Database, cls).__new__(cls)
                cls._instance._init_db()
            return cls._instance

    def _init_db(self):
        self.db_path = settings.DB_FILE
        self._local = threading.local()
        self._create_tables()

    def get_connection(self) -> sqlite3.Connection:
        if not hasattr(self._local, "conn") or self._local.conn is None:
            self._local.conn = sqlite3.connect(self.db_path, timeout=30.0)
            self._local.conn.row_factory = sqlite3.Row
            self._local.conn.execute("PRAGMA journal_mode=WAL;")
            self._local.conn.execute("PRAGMA synchronous=NORMAL;")
            self._local.conn.execute("PRAGMA foreign_keys=ON;")
        return self._local.conn

    def _create_tables(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # 1. Users & Roles
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id TEXT PRIMARY KEY,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                role TEXT NOT NULL DEFAULT 'ANALYST',
                full_name TEXT NOT NULL,
                created_at REAL NOT NULL,
                last_login REAL,
                is_active INTEGER NOT NULL DEFAULT 1
            )
        """)

        # 2. Documents
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS documents (
                id TEXT PRIMARY KEY,
                user_id TEXT NOT NULL,
                filename TEXT NOT NULL,
                original_name TEXT NOT NULL,
                file_type TEXT NOT NULL,
                file_size INTEGER NOT NULL,
                checksum TEXT NOT NULL,
                upload_timestamp REAL NOT NULL,
                word_count INTEGER DEFAULT 0,
                character_count INTEGER DEFAULT 0,
                page_count INTEGER DEFAULT 1,
                row_count INTEGER DEFAULT 0,
                column_count INTEGER DEFAULT 0,
                status TEXT NOT NULL DEFAULT 'COMPLETED',
                storage_path TEXT NOT NULL,
                folder TEXT DEFAULT 'General',
                tags TEXT DEFAULT '',
                is_favorite INTEGER DEFAULT 0,
                is_archived INTEGER DEFAULT 0,
                version INTEGER DEFAULT 1,
                health_score REAL DEFAULT 0,
                risk_level TEXT DEFAULT 'LOW',
                FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
            )
        """)

        # 3. Document Versions
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS document_versions (
                id TEXT PRIMARY KEY,
                document_id TEXT NOT NULL,
                version_num INTEGER NOT NULL,
                file_size INTEGER NOT NULL,
                upload_timestamp REAL NOT NULL,
                changes_summary TEXT NOT NULL,
                health_score REAL NOT NULL,
                issue_count INTEGER NOT NULL,
                risk_score REAL NOT NULL,
                storage_path TEXT NOT NULL,
                FOREIGN KEY (document_id) REFERENCES documents (id) ON DELETE CASCADE
            )
        """)

        # 4. Document Chunks & Pages
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS document_chunks (
                id TEXT PRIMARY KEY,
                document_id TEXT NOT NULL,
                chunk_index INTEGER NOT NULL,
                page_number INTEGER NOT NULL,
                content TEXT NOT NULL,
                metadata_json TEXT DEFAULT '{}',
                FOREIGN KEY (document_id) REFERENCES documents (id) ON DELETE CASCADE
            )
        """)

        # 5. Analyses
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS analyses (
                id TEXT PRIMARY KEY,
                document_id TEXT NOT NULL,
                version_num INTEGER DEFAULT 1,
                classification TEXT NOT NULL,
                classification_confidence REAL NOT NULL,
                health_score REAL NOT NULL,
                text_quality_score REAL NOT NULL,
                data_quality_score REAL NOT NULL,
                consistency_score REAL NOT NULL,
                risk_score REAL NOT NULL,
                compliance_score REAL NOT NULL,
                summary TEXT NOT NULL,
                metrics_json TEXT NOT NULL,
                created_at REAL NOT NULL,
                FOREIGN KEY (document_id) REFERENCES documents (id) ON DELETE CASCADE
            )
        """)

        # 6. Issues & Findings
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS issues (
                id TEXT PRIMARY KEY,
                document_id TEXT NOT NULL,
                analysis_id TEXT NOT NULL,
                category TEXT NOT NULL,
                severity TEXT NOT NULL,
                title TEXT NOT NULL,
                location TEXT NOT NULL,
                value TEXT DEFAULT '',
                expected_value TEXT DEFAULT '',
                evidence TEXT NOT NULL,
                explanation TEXT NOT NULL,
                impact TEXT NOT NULL,
                recommendation TEXT NOT NULL,
                confidence REAL NOT NULL,
                status TEXT NOT NULL DEFAULT 'OPEN',
                assigned_to TEXT DEFAULT '',
                user_comment TEXT DEFAULT '',
                suggested_correction TEXT DEFAULT '',
                created_at REAL NOT NULL,
                updated_at REAL NOT NULL,
                FOREIGN KEY (document_id) REFERENCES documents (id) ON DELETE CASCADE
            )
        """)

        # 7. Data Quality Findings
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS data_quality_findings (
                id TEXT PRIMARY KEY,
                document_id TEXT NOT NULL,
                metric_name TEXT NOT NULL,
                score REAL NOT NULL,
                details_json TEXT NOT NULL,
                created_at REAL NOT NULL,
                FOREIGN KEY (document_id) REFERENCES documents (id) ON DELETE CASCADE
            )
        """)

        # 8. Document Comparisons
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS comparisons (
                id TEXT PRIMARY KEY,
                user_id TEXT NOT NULL,
                doc_a_id TEXT NOT NULL,
                doc_b_id TEXT NOT NULL,
                similarity_score REAL NOT NULL,
                risk_delta REAL NOT NULL,
                diff_summary TEXT NOT NULL,
                diff_json TEXT NOT NULL,
                created_at REAL NOT NULL
            )
        """)

        # 9. Document Chat Messages
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS chat_messages (
                id TEXT PRIMARY KEY,
                document_id TEXT NOT NULL,
                user_id TEXT NOT NULL,
                role TEXT NOT NULL,
                message TEXT NOT NULL,
                citations_json TEXT DEFAULT '[]',
                created_at REAL NOT NULL,
                FOREIGN KEY (document_id) REFERENCES documents (id) ON DELETE CASCADE
            )
        """)

        # 10. Notifications
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS notifications (
                id TEXT PRIMARY KEY,
                user_id TEXT NOT NULL,
                type TEXT NOT NULL,
                title TEXT NOT NULL,
                message TEXT NOT NULL,
                link TEXT DEFAULT '',
                is_read INTEGER DEFAULT 0,
                created_at REAL NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
            )
        """)

        # 11. Audit Logs
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS audit_logs (
                id TEXT PRIMARY KEY,
                user_id TEXT NOT NULL,
                username TEXT NOT NULL,
                action TEXT NOT NULL,
                target TEXT NOT NULL,
                result TEXT NOT NULL,
                details TEXT DEFAULT '',
                timestamp REAL NOT NULL
            )
        """)

        # 12. Settings & Validation Rules
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS settings (
                id TEXT PRIMARY KEY,
                key TEXT UNIQUE NOT NULL,
                value TEXT NOT NULL,
                description TEXT DEFAULT '',
                updated_at REAL NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS validation_rules (
                id TEXT PRIMARY KEY,
                rule_name TEXT NOT NULL,
                rule_type TEXT NOT NULL,
                expression TEXT NOT NULL,
                severity TEXT NOT NULL,
                is_active INTEGER DEFAULT 1,
                created_at REAL NOT NULL
            )
        """)

        conn.commit()
        conn.close()

    def execute_query(self, query: str, params: tuple = ()) -> List[Dict[str, Any]]:
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(query, params)
        rows = cursor.fetchall()
        return [dict(row) for row in rows]

    def execute_non_query(self, query: str, params: tuple = ()) -> int:
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        return cursor.rowcount

db = Database()
