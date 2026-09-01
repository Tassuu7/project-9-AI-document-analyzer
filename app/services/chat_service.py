"""Document AI Assistant Conversation Service."""
import time
import uuid
import json
from typing import Dict, Any, List
from app.core.database import db
from app.services.document_service import DocumentService
from app.inspection.chat_engine import ChatEngine

class ChatService:
    @classmethod
    def ask_document_question(cls, document_id: str, user_id: str, query: str) -> Dict[str, Any]:
        # 1. Retrieve document content and analysis findings
        doc_text = DocumentService.get_document_text(document_id)
        
        analyses = db.execute_query("SELECT * FROM analyses WHERE document_id = ? ORDER BY created_at DESC LIMIT 1", (document_id,))
        issues = db.execute_query("SELECT * FROM issues WHERE document_id = ?", (document_id,))
        
        analysis_data = {
            "analysis": analyses[0] if analyses else {},
            "issues": issues
        }

        # 2. Query Grounded Chat Engine
        ans_data = ChatEngine.answer_question(query, doc_text, analysis_data)
        answer = ans_data["answer"]
        citations = ans_data["citations"]

        # 3. Store conversation history
        user_msg_id = str(uuid.uuid4())
        asst_msg_id = str(uuid.uuid4())
        now = time.time()

        db.execute_non_query(
            "INSERT INTO chat_messages (id, document_id, user_id, role, message, citations_json, created_at) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (user_msg_id, document_id, user_id, "user", query, "[]", now)
        )
        db.execute_non_query(
            "INSERT INTO chat_messages (id, document_id, user_id, role, message, citations_json, created_at) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (asst_msg_id, document_id, user_id, "assistant", answer, json.dumps(citations), now + 0.01)
        )

        return {
            "answer": answer,
            "citations": citations,
            "message_id": asst_msg_id,
            "created_at": now
        }

    @classmethod
    def get_conversation_history(cls, document_id: str) -> List[Dict[str, Any]]:
        rows = db.execute_query(
            "SELECT * FROM chat_messages WHERE document_id = ? ORDER BY created_at ASC",
            (document_id,)
        )
        history = []
        for r in rows:
            history.append({
                "id": r["id"],
                "role": r["role"],
                "message": r["message"],
                "citations": json.loads(r["citations_json"]) if r["citations_json"] else [],
                "created_at": r["created_at"]
            })
        return history
