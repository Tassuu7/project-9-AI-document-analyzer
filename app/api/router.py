"""Comprehensive REST API Router for AI DOCUMENT INSPECTOR."""
import json
import time
import base64
from typing import Dict, Any, Tuple
from app.core.security import Security
from app.services.auth_service import AuthService
from app.services.document_service import DocumentService
from app.services.analyzer_service import AnalyzerService
from app.services.issue_service import IssueService
from app.services.chat_service import ChatService
from app.services.comparison_service import ComparisonService
from app.services.export_service import ExportService
from app.services.notification_service import NotificationService
from app.services.audit_service import AuditService
from app.inspection.paraphrase_engine import ParaphraseEngine
from app.builders.docx_builder import DocxBuilder
from app.core.database import db

def parse_auth_header(headers: Dict[str, str]) -> Dict[str, Any]:
    auth = headers.get("authorization", "") or headers.get("Authorization", "")
    if auth.startswith("Bearer "):
        token = auth[7:].strip()
        decoded = Security.decode_token(token)
        if decoded:
            return decoded
    return {"sub": "user_default", "username": "analyst", "role": "ANALYST"}

def handle_route(path: str, method: str, body: Dict[str, Any], headers: Dict[str, str], raw_bytes: bytes = None) -> Tuple[int, Dict[str, Any]]:
    path_clean = path.split("?")[0].rstrip("/")
    query_params = {}
    if "?" in path:
        qs = path.split("?")[1]
        for pair in qs.split("&"):
            if "=" in pair:
                k, v = pair.split("=", 1)
                query_params[k] = v

    user = parse_auth_header(headers)
    user_id = user.get("sub", "user_default")
    user_role = user.get("role", "ANALYST")
    username = user.get("username", "analyst")

    try:
        # =========================================================================
        # 1. AUTHENTICATION & USERS
        # =========================================================================
        if path_clean == "/api/auth/register" and method == "POST":
            res = AuthService.register_user(
                username=body.get("username", "").strip(),
                email=body.get("email", "").strip(),
                password=body.get("password", ""),
                full_name=body.get("full_name", "").strip(),
                role=body.get("role", "ANALYST")
            )
            AuditService.log_action(res["user"]["id"], res["user"]["username"], "REGISTER", "User Account")
            return 201, {"success": True, "data": res}

        elif path_clean == "/api/auth/login" and method == "POST":
            res = AuthService.authenticate_user(
                username=body.get("username", "").strip(),
                password=body.get("password", "")
            )
            AuditService.log_action(res["user"]["id"], res["user"]["username"], "LOGIN", "Session Token")
            return 200, {"success": True, "data": res}

        elif path_clean == "/api/auth/me" and method == "GET":
            return 200, {"success": True, "data": {"user": user}}

        # =========================================================================
        # 2. DOCUMENT INGESTION & LIBRARY
        # =========================================================================
        elif path_clean == "/api/documents/upload" and method == "POST":
            filename = body.get("filename", "uploaded_document.docx")
            content_str = body.get("content", "")
            file_bytes = raw_bytes if raw_bytes else content_str.encode("utf-8")
            
            doc_info = DocumentService.save_and_process_upload(filename, file_bytes, user_id=user_id)
            report = AnalyzerService.inspect_document_by_id(doc_info["id"], user_id=user_id)
            AuditService.log_action(user_id, username, "UPLOAD", f"Document: {filename}")
            return 201, {"success": True, "data": {"document": doc_info, "analysis": report}}

        elif path_clean == "/api/documents/list" and method == "GET":
            docs = DocumentService.list_documents(
                user_id=user_id,
                search=query_params.get("search", ""),
                folder=query_params.get("folder"),
                tag=query_params.get("tag"),
                is_archived=int(query_params.get("archived", 0))
            )
            return 200, {"success": True, "data": {"documents": docs}}

        elif path_clean == "/api/documents/get" and method == "GET":
            doc_id = query_params.get("id", "")
            doc = DocumentService.get_document(doc_id)
            if not doc:
                return 404, {"success": False, "error": "Document not found"}
            text = DocumentService.get_document_text(doc_id)
            return 200, {"success": True, "data": {"document": doc, "text": text}}

        # =========================================================================
        # 3. PARAPHRASING & DOCX EXPORT ENGINE
        # =========================================================================
        elif path_clean == "/api/paraphrase" and method == "POST":
            text = body.get("text", "")
            mode = body.get("mode", "professional")
            res = ParaphraseEngine.paraphrase_text(text, mode=mode)
            AuditService.log_action(user_id, username, "PARAPHRASE", f"Mode: {mode}")
            return 200, {"success": True, "data": res}

        elif path_clean == "/api/documents/export-docx" and method == "POST":
            text = body.get("text", "")
            title = body.get("title", "Exported Document")
            docx_bytes = DocxBuilder.text_to_docx_bytes(text, title=title)
            b64_content = base64.b64encode(docx_bytes).decode("utf-8")
            AuditService.log_action(user_id, username, "EXPORT_DOCX", f"Title: {title}")
            return 200, {
                "success": True,
                "data": {
                    "filename": "analyzed_document.docx",
                    "mime_type": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                    "base64": b64_content
                }
            }

        # =========================================================================
        # 4. INSPECTION & QUALITY ANALYSIS
        # =========================================================================
        elif path_clean == "/api/inspect/quick" and method == "POST":
            text = body.get("text", "")
            report = AnalyzerService.inspect_document(text, user_id=user_id)
            return 200, {"success": True, "data": report}

        elif path_clean == "/api/inspect/document" and method == "POST":
            doc_id = body.get("document_id", "")
            report = AnalyzerService.inspect_document_by_id(doc_id, user_id=user_id)
            AuditService.log_action(user_id, username, "INSPECT", f"Document ID: {doc_id}")
            return 200, {"success": True, "data": report}

        # =========================================================================
        # 5. ISSUES & FINDINGS MANAGEMENT
        # =========================================================================
        elif path_clean == "/api/issues/list" and method == "GET":
            issues = IssueService.list_issues(
                document_id=query_params.get("document_id"),
                category=query_params.get("category"),
                severity=query_params.get("severity"),
                status=query_params.get("status")
            )
            return 200, {"success": True, "data": {"issues": issues}}

        elif path_clean == "/api/issues/update-status" and method == "POST":
            iss_id = body.get("issue_id", "")
            st = body.get("status", "RESOLVED")
            ok = IssueService.update_issue_status(iss_id, status=st)
            AuditService.log_action(user_id, username, "UPDATE_ISSUE", f"Issue {iss_id} -> {st}")
            return 200, {"success": ok}

        # =========================================================================
        # 6. DIFF & COMPARISON
        # =========================================================================
        elif path_clean == "/api/compare" and method == "POST":
            text_a = body.get("text_a", "")
            text_b = body.get("text_b", "")
            res = ComparisonService.compare_documents(text_a, text_b, user_id=user_id)
            return 200, {"success": True, "data": res}

        # =========================================================================
        # 7. REPORTS & TELEMETRY
        # =========================================================================
        elif path_clean == "/api/export" and method == "POST":
            report_data = body.get("report_data", {})
            fmt = body.get("format", "json")
            res = ExportService.generate_report(report_data, fmt=fmt)
            return 200, {"success": True, "data": res}

        elif path_clean == "/api/stats/dashboard" and method == "GET":
            docs_count = len(DocumentService.list_documents(user_id=None))
            analyses_count = len(db.execute_query("SELECT id FROM analyses"))
            users_count = len(AuthService.list_users())
            issues_metrics = IssueService.get_issue_metrics()
            avg_health_row = db.execute_query("SELECT AVG(health_score) as avg_h FROM analyses")
            avg_health = round(avg_health_row[0]["avg_h"] or 85.4, 1)
            recent_docs = DocumentService.list_documents(user_id=None)[:10]

            return 200, {
                "success": True,
                "data": {
                    "total_documents": docs_count,
                    "total_analyses": analyses_count,
                    "total_users": users_count,
                    "average_health_score": avg_health,
                    "issue_metrics": issues_metrics,
                    "recent_documents": recent_docs
                }
            }

        return 404, {"success": False, "error": f"Endpoint not found: {method} {path_clean}"}

    except Exception as e:
        return 500, {"success": False, "error": str(e)}
