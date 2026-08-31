"""Thread-Safe Database Engine."""
import sqlite3
import threading
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
        return self._local.conn

    def _create_tables(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id TEXT PRIMARY KEY,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                role TEXT NOT NULL DEFAULT 'Analyst',
                full_name TEXT NOT NULL,
                created_at REAL NOT NULL,
                last_login REAL,
                is_active INTEGER NOT NULL DEFAULT 1
            )
        """)
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
                status TEXT NOT NULL DEFAULT 'uploaded',
                storage_path TEXT NOT NULL
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS analyses (
                id TEXT PRIMARY KEY,
                document_id TEXT NOT NULL,
                classification TEXT NOT NULL,
                classification_confidence REAL NOT NULL,
                summary TEXT NOT NULL,
                risk_score REAL NOT NULL,
                sentiment_polarity REAL NOT NULL,
                sentiment_subjectivity REAL NOT NULL,
                tone TEXT NOT NULL,
                readability_score REAL NOT NULL,
                readability_grade TEXT NOT NULL,
                entities_json TEXT NOT NULL,
                compliance_json TEXT NOT NULL,
                risks_json TEXT NOT NULL,
                metrics_json TEXT NOT NULL,
                created_at REAL NOT NULL,
                FOREIGN KEY (document_id) REFERENCES documents (id) ON DELETE CASCADE
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS comparisons (
                id TEXT PRIMARY KEY,
                user_id TEXT NOT NULL,
                doc_a_id TEXT NOT NULL,
                doc_b_id TEXT NOT NULL,
                similarity_score REAL NOT NULL,
                diff_summary TEXT NOT NULL,
                semantic_drift_json TEXT NOT NULL,
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
