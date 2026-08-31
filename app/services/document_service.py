"""Document Service."""
import os
import time
import uuid
from typing import List, Dict, Any
from app.core.config import settings
from app.core.database import db
from app.core.security import SecurityManager
from app.parsers.text_parser import TextParser
from app.parsers.pdf_parser import PDFParser
from app.parsers.docx_parser import DOCXParser
from app.parsers.csv_parser import CSVParser
from app.parsers.json_parser import JSONParser
from app.models.document import Document

class DocumentService:
    @classmethod
    def ingest_file(cls, user_id: str, original_filename: str, file_bytes: bytes) -> Document:
        doc_id = str(uuid.uuid4())
        ext = original_filename.split(".")[-1].lower() if "." in original_filename else "txt"
        stored_name = f"{doc_id}_{int(time.time())}.{ext}"
        storage_path = os.path.join(settings.UPLOAD_DIR, stored_name)
        with open(storage_path, "wb") as f:
            f.write(file_bytes)
        checksum = SecurityManager.generate_file_checksum(file_bytes)
        if ext in ["txt", "md"]: text = TextParser.parse(file_bytes.decode("utf-8", errors="ignore"))["clean_text"]
        elif ext == "pdf": text = PDFParser.parse_bytes(file_bytes)["clean_text"]
        elif ext == "docx": text = DOCXParser.parse_bytes(file_bytes)["clean_text"]
        elif ext == "csv": text = CSVParser.parse(file_bytes.decode("utf-8", errors="ignore"))["clean_text"]
        elif ext == "json": text = JSONParser.parse(file_bytes.decode("utf-8", errors="ignore"))["clean_text"]
        else: text = file_bytes.decode("utf-8", errors="ignore")

        p_path = os.path.join(settings.PROCESSED_DIR, f"{doc_id}.txt")
        with open(p_path, "w", encoding="utf-8") as f:
            f.write(text)

        doc = Document(id=doc_id, user_id=user_id, filename=stored_name, original_name=original_filename,
                       file_type=ext, file_size=len(file_bytes), checksum=checksum, upload_timestamp=time.time(),
                       word_count=len(text.split()), character_count=len(text), status="uploaded", storage_path=storage_path)

        db.execute_non_query(
            "INSERT INTO documents (id, user_id, filename, original_name, file_type, file_size, checksum, upload_timestamp, word_count, character_count, status, storage_path) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (doc.id, doc.user_id, doc.filename, doc.original_name, doc.file_type, doc.file_size, doc.checksum, doc.upload_timestamp, doc.word_count, doc.character_count, doc.status, doc.storage_path)
        )
        return doc

    @classmethod
    def get_document_text(cls, doc_id: str) -> str:
        p_path = os.path.join(settings.PROCESSED_DIR, f"{doc_id}.txt")
        if os.path.exists(p_path):
            with open(p_path, "r", encoding="utf-8") as f: return f.read()
        rows = db.execute_query("SELECT storage_path FROM documents WHERE id = ?", (doc_id,))
        if rows and os.path.exists(rows[0]["storage_path"]):
            with open(rows[0]["storage_path"], "rb") as f: return f.read().decode("utf-8", errors="ignore")
        return ""

    @classmethod
    def list_documents(cls, user_id: str = None) -> List[Dict[str, Any]]:
        return db.execute_query("SELECT * FROM documents ORDER BY upload_timestamp DESC LIMIT 50")

    @classmethod
    def delete_document(cls, doc_id: str) -> bool:
        db.execute_non_query("DELETE FROM analyses WHERE document_id = ?", (doc_id,))
        db.execute_non_query("DELETE FROM documents WHERE id = ?", (doc_id,))
        return True
