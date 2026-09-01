"""Comprehensive REST API Router for AI DOCUMENT INSPECTOR."""
import json
import time
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
            filename = body.get("filename", "uploaded_document.txt")
            content_str = body.get("content", "")
            file_bytes = raw_bytes if raw_bytes else content_str.encode("utf-8")
            
            doc_info = DocumentService.save_and_process_upload(filename, file_bytes, user_id=user_id)
            
            # Automatically run inspection pipeline on uploaded doc
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

        elif path_clean == "/api/documents/favorite" and method == "POST":
            doc_id = body.get("id", "")
            ok = DocumentService.toggle_favorite(doc_id)
            return 200, {"success": ok}

        elif path_clean == "/api/documents/archive" and method == "POST":
            doc_id = body.get("id", "")
            arch = bool(body.get("archive", True))
            ok = DocumentService.archive_document(doc_id, archive=arch)
            return 200, {"success": ok}

        elif path_clean == "/api/documents/delete" and method == "POST":
            if not Security.check_permission(user_role, "ANALYST"):
                return 403, {"success": False, "error": "Permission denied: Viewer cannot delete documents."}
            doc_id = body.get("id", "")
            ok = DocumentService.delete_document(doc_id)
            AuditService.log_action(user_id, username, "DELETE", f"Document ID: {doc_id}")
            return 200, {"success": ok}

        # =========================================================================
        # 3. INSPECTION & QUALITY ANALYSIS
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
        # 4. ISSUES & FINDINGS MANAGEMENT
        # =========================================================================
        elif path_clean == "/api/issues/list" and method == "GET":
            issues = IssueService.list_issues(
                document_id=query_params.get("document_id"),
                category=query_params.get("category"),
                severity=query_params.get("severity"),
                status=query_params.get("status")
            )
            return 200, {"success": True, "data": {"issues": issues}}

        elif path_clean == "/api/issues/metrics" and method == "GET":
            metrics = IssueService.get_issue_metrics(document_id=query_params.get("document_id"))
            return 200, {"success": True, "data": metrics}

        elif path_clean == "/api/issues/update-status" and method == "POST":
            if not Security.check_permission(user_role, "ANALYST"):
                return 403, {"success": False, "error": "Permission denied: Viewer cannot modify findings."}
            iss_id = body.get("issue_id", "")
            st = body.get("status", "RESOLVED")
            comment = body.get("comment", "")
            ok = IssueService.update_issue_status(iss_id, status=st, user_comment=comment)
            AuditService.log_action(user_id, username, "UPDATE_ISSUE", f"Issue {iss_id} -> {st}")
            return 200, {"success": ok}

        # =========================================================================
        # 5. DOCUMENT DIFF & COMPARISON
        # =========================================================================
        elif path_clean == "/api/compare" and method == "POST":
            text_a = body.get("text_a", "")
            text_b = body.get("text_b", "")
            doc_a_id = body.get("doc_a_id", "")
            doc_b_id = body.get("doc_b_id", "")
            res = ComparisonService.compare_documents(text_a, text_b, user_id=user_id, doc_a_id=doc_a_id, doc_b_id=doc_b_id)
            AuditService.log_action(user_id, username, "COMPARE", "Documents Diff Matrix")
            return 200, {"success": True, "data": res}

        # =========================================================================
        # 6. AI DOCUMENT ASSISTANT / CHAT
        # =========================================================================
        elif path_clean == "/api/chat/ask" and method == "POST":
            doc_id = body.get("document_id", "")
            q = body.get("query", "")
            ans = ChatService.ask_document_question(doc_id, user_id, q)
            return 200, {"success": True, "data": ans}

        elif path_clean == "/api/chat/history" and method == "GET":
            doc_id = query_params.get("document_id", "")
            history = ChatService.get_conversation_history(doc_id)
            return 200, {"success": True, "data": {"history": history}}

        # =========================================================================
        # 7. NOTIFICATIONS
        # =========================================================================
        elif path_clean == "/api/notifications/list" and method == "GET":
            notes = NotificationService.list_user_notifications(user_id, unread_only=bool(query_params.get("unread")))
            return 200, {"success": True, "data": {"notifications": notes}}

        elif path_clean == "/api/notifications/read" and method == "POST":
            nid = body.get("id")
            if nid:
                NotificationService.mark_as_read(nid)
            else:
                NotificationService.mark_all_as_read(user_id)
            return 200, {"success": True}

        # =========================================================================
        # 8. REPORTS & EXPORTS
        # =========================================================================
        elif path_clean == "/api/export" and method == "POST":
            report_data = body.get("report_data", {})
            fmt = body.get("format", "json")
            res = ExportService.generate_report(report_data, fmt=fmt)
            AuditService.log_action(user_id, username, "EXPORT", f"Format: {fmt}")
            return 200, {"success": True, "data": res}

        # =========================================================================
        # 9. TELEMETRY & ADMIN DASHBOARD
        # =========================================================================
        elif path_clean in ["/api/stats/dashboard", "/api/admin/stats"] and method == "GET":
            docs_count = len(DocumentService.list_documents(user_id=None))
            analyses_count = len(db.execute_query("SELECT id FROM analyses"))
            users_count = len(AuthService.list_users())
            issues_metrics = IssueService.get_issue_metrics()
            
            avg_health_row = db.execute_query("SELECT AVG(health_score) as avg_h FROM analyses")
            avg_health = round(avg_health_row[0]["avg_h"] or 84.5, 1)

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

        elif path_clean == "/api/audit/logs" and method == "GET":
            if not Security.check_permission(user_role, "ADMIN"):
                return 403, {"success": False, "error": "Permission denied: Admin role required."}
            logs = AuditService.list_logs(limit=100)
            return 200, {"success": True, "data": {"logs": logs}}

        elif path_clean == "/api/admin/users" and method == "GET":
            if not Security.check_permission(user_role, "ADMIN"):
                return 403, {"success": False, "error": "Permission denied: Admin role required."}
            users = AuthService.list_users()
            return 200, {"success": True, "data": {"users": users}}

        return 404, {"success": False, "error": f"Endpoint not found: {method} {path_clean}"}

    except Exception as e:
        return 500, {"success": False, "error": str(e)}
