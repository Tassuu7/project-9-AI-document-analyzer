"""Document Storage, Versioning, and Library Management Service."""
import os
import uuid
import time
from typing import Dict, Any, List, Optional
from app.core.config import settings
from app.core.database import db
from app.core.security import Security
from app.parsers.text_parser import TextParser
from app.parsers.csv_parser import CSVParser
from app.parsers.xlsx_parser import XLSXParser
from app.parsers.json_parser import JSONParser
from app.parsers.docx_parser import DOCXParser
from app.parsers.pdf_parser import PDFParser

class DocumentService:
    @classmethod
    def save_and_process_upload(cls, filename: str, file_bytes: bytes, user_id: str = "user_default") -> Dict[str, Any]:
        ext = filename.split(".")[-1].lower() if "." in filename else "txt"
        doc_id = str(uuid.uuid4())
        checksum = Security.calculate_checksum(file_bytes)
        now = time.time()
        
        storage_filename = f"{doc_id}_{filename}"
        storage_path = os.path.join(settings.UPLOAD_DIR, storage_filename)
        with open(storage_path, "wb") as f:
            f.write(file_bytes)

        # Parse based on extension
        parsed = {}
        if ext == "pdf":
            parsed = PDFParser.parse_bytes(file_bytes)
        elif ext == "docx":
            parsed = DOCXParser.parse_bytes(file_bytes)
        elif ext == "csv":
            parsed = CSVParser.parse(file_bytes.decode("utf-8", errors="ignore"))
        elif ext == "xlsx":
            parsed = XLSXParser.parse_bytes(file_bytes)
        elif ext == "json":
            parsed = JSONParser.parse(file_bytes.decode("utf-8", errors="ignore"))
        else:
            parsed = TextParser.parse(file_bytes.decode("utf-8", errors="ignore"))

        clean_text = parsed.get("clean_text", "")
        word_count = parsed.get("word_count", len(clean_text.split()))
        char_count = len(clean_text)
        page_count = parsed.get("page_count", 1)
        row_count = parsed.get("row_count", 0)
        col_count = parsed.get("column_count", 0)

        # Save processed text
        processed_path = os.path.join(settings.PROCESSED_DIR, f"{doc_id}.txt")
        with open(processed_path, "w", encoding="utf-8") as f:
            f.write(clean_text)

        # Insert document record
        db.execute_non_query(
            """INSERT INTO documents 
               (id, user_id, filename, original_name, file_type, file_size, checksum, upload_timestamp, word_count, character_count, page_count, row_count, column_count, status, storage_path, folder, tags, version, health_score)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'COMPLETED', ?, 'General', '', 1, 0)""",
            (doc_id, user_id, storage_filename, filename, ext, len(file_bytes), checksum, now, word_count, char_count, page_count, row_count, col_count, storage_path)
        )

        # Insert version 1
        db.execute_non_query(
            """INSERT INTO document_versions 
               (id, document_id, version_num, file_size, upload_timestamp, changes_summary, health_score, issue_count, risk_score, storage_path)
               VALUES (?, ?, 1, ?, ?, 'Initial Upload', 0, 0, 0, ?)""",
            (str(uuid.uuid4()), doc_id, len(file_bytes), now, storage_path)
        )

        return {
            "id": doc_id,
            "filename": filename,
            "file_type": ext,
            "file_size": len(file_bytes),
            "word_count": word_count,
            "page_count": page_count,
            "row_count": row_count,
            "column_count": col_count,
            "clean_text": clean_text,
            "tables": parsed.get("tables", [])
        }

    @classmethod
    def get_document(cls, document_id: str) -> Optional[Dict[str, Any]]:
        rows = db.execute_query("SELECT * FROM documents WHERE id = ?", (document_id,))
        return rows[0] if rows else None

    @classmethod
    def get_document_text(cls, document_id: str) -> str:
        processed_path = os.path.join(settings.PROCESSED_DIR, f"{document_id}.txt")
        if os.path.exists(processed_path):
            with open(processed_path, "r", encoding="utf-8") as f:
                return f.read()
        doc = cls.get_document(document_id)
        if doc and os.path.exists(doc["storage_path"]):
            with open(doc["storage_path"], "rb") as f:
                content = f.read()
                return content.decode("utf-8", errors="ignore")
        return ""

    @classmethod
    def list_documents(cls, user_id: str = None, search: str = "", folder: str = None, tag: str = None, is_archived: int = 0) -> List[Dict[str, Any]]:
        query = "SELECT * FROM documents WHERE is_archived = ?"
        params = [is_archived]
        if user_id and user_id != "admin":
            query += " AND (user_id = ? OR user_id = 'user_default')"
            params.append(user_id)
        if folder:
            query += " AND folder = ?"
            params.append(folder)
        if tag:
            query += " AND tags LIKE ?"
            params.append(f"%{tag}%")
        if search:
            query += " AND (original_name LIKE ? OR filename LIKE ?)"
            params.extend([f"%{search}%", f"%{search}%"])
        query += " ORDER BY upload_timestamp DESC"
        return db.execute_query(query, tuple(params))

    @classmethod
    def toggle_favorite(cls, document_id: str) -> bool:
        doc = cls.get_document(document_id)
        if not doc: return False
        new_fav = 0 if doc.get("is_favorite") == 1 else 1
        return db.execute_non_query("UPDATE documents SET is_favorite = ? WHERE id = ?", (new_fav, document_id)) > 0

    @classmethod
    def archive_document(cls, document_id: str, archive: bool = True) -> bool:
        val = 1 if archive else 0
        return db.execute_non_query("UPDATE documents SET is_archived = ? WHERE id = ?", (val, document_id)) > 0

    @classmethod
    def delete_document(cls, document_id: str) -> bool:
        return db.execute_non_query("DELETE FROM documents WHERE id = ?", (document_id,)) > 0
