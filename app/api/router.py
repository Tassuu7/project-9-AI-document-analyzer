"""API & UI Router."""
import os
from typing import Dict, Any
from app.core.config import settings
from app.services.auth_service import AuthService
from app.services.document_service import DocumentService
from app.services.analyzer_service import AnalyzerService
from app.services.comparison_service import ComparisonService
from app.services.export_service import ExportService
from app.services.stats_service import StatsService
from app.nlp.compliance.compliance_taxonomy import COMPLIANCE_STANDARDS

def serve_template(handler, name: str):
    p = os.path.join(settings.BASE_DIR, "app", "templates", name)
    if os.path.exists(p):
        with open(p, "r", encoding="utf-8") as f: handler._send_html_response(f.read())
    else: handler.send_error(404)

def handle_route(handler, method: str, path: str, query: Dict[str, Any]):
    if path.startswith("/static/"):
        handler._send_file_response(os.path.join(settings.BASE_DIR, "static", path[8:]))
        return

    if method == "GET":
        if path in ["/", "/index.html"]: serve_template(handler, "index.html"); return
        if path == "/dashboard": serve_template(handler, "dashboard.html"); return
        if path == "/analyze": serve_template(handler, "analyze.html"); return
        if path == "/compare": serve_template(handler, "compare.html"); return
        if path == "/compliance": serve_template(handler, "compliance.html"); return
        if path == "/export": serve_template(handler, "export.html"); return
        if path == "/auth": serve_template(handler, "auth.html"); return

    if path == "/api/auth/register" and method == "POST":
        b = handler.parse_request_body()
        res = AuthService.register(b.get("username",""), b.get("email",""), b.get("password",""), b.get("full_name",""))
        handler._send_json_response({"success": True, "data": res}, 201); return

    if path == "/api/auth/login" and method == "POST":
        b = handler.parse_request_body()
        res = AuthService.login(b.get("username","") or b.get("email",""), b.get("password",""))
        handler._send_json_response({"success": True, "data": res}); return

    if path == "/api/stats/dashboard" and method == "GET":
        handler._send_json_response({"success": True, "data": StatsService.get_dashboard_stats()}); return

    if path == "/api/analyze/quick" and method == "POST":
        b = handler.parse_request_body()
        res = AnalyzerService.run_full_pipeline(b.get("text", ""))
        handler._send_json_response({"success": True, "data": res}); return

    if path == "/api/documents/list" and method == "GET":
        handler._send_json_response({"success": True, "data": DocumentService.list_documents()}); return

    if path == "/api/documents/upload" and method == "POST":
        b = handler.parse_request_body()
        doc = DocumentService.ingest_file("user_1", b.get("filename", "doc.txt"), b.get("content", "").encode("utf-8"))
        res = AnalyzerService.analyze_document_by_id(doc.id)
        handler._send_json_response({"success": True, "document": doc.to_dict(), "analysis": res}, 201); return

    if path == "/api/compare" and method == "POST":
        b = handler.parse_request_body()
        res = ComparisonService.compare_texts(b.get("text_a", ""), b.get("text_b", ""))
        handler._send_json_response({"success": True, "data": res}); return

    if path == "/api/compliance/rules" and method == "GET":
        handler._send_json_response({"success": True, "data": COMPLIANCE_STANDARDS}); return

    if path == "/api/export" and method == "POST":
        b = handler.parse_request_body()
        fmt = b.get("format", "json")
        rep = b.get("report", {})
        out = ExportService.to_json(rep) if fmt == "json" else ExportService.to_csv_entities(rep) if fmt == "csv" else ExportService.to_markdown(rep)
        handler._send_json_response({"success": True, "content": out}); return

    handler._send_json_response({"success": False, "error": "Not Found"}, 404)
