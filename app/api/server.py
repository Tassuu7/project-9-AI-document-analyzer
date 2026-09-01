"""High-Concurrency Threaded HTTP Server and Static/Template Renderer."""
import os
import sys
import json
import urllib.parse
from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn
from app.core.config import settings

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    daemon_threads = True

class RequestHandler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        # Clean logging format
        pass

    def send_json_response(self, status_code: int, data: dict):
        body = json.dumps(data).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS, DELETE")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, Authorization")
        self.end_headers()
        self.wfile.write(body)

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS, DELETE")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, Authorization")
        self.end_headers()

    def do_GET(self):
        self._dispatch("GET")

    def do_POST(self):
        self._dispatch("POST")

    def do_DELETE(self):
        self._dispatch("DELETE")

    def _dispatch(self, method: str):
        parsed_path = urllib.parse.urlparse(self.path)
        path = parsed_path.path

        # 1. API Endpoints
        if path.startswith("/api/"):
            content_len = int(self.headers.get("Content-Length", 0))
            body = {}
            raw_bytes = None
            if content_len > 0:
                raw_bytes = self.rfile.read(content_len)
                try:
                    body = json.loads(raw_bytes.decode("utf-8"))
                except Exception:
                    body = {"raw": raw_bytes.decode("utf-8", errors="ignore")}

            from app.api.router import handle_route
            status, res = handle_route(self.path, method, body, dict(self.headers), raw_bytes=raw_bytes)
            self.send_json_response(status, res)
            return

        # 2. Static Assets
        if path.startswith("/static/"):
            rel_file = path.lstrip("/")
            file_path = os.path.join(settings.BASE_DIR, rel_file)
            if os.path.exists(file_path) and os.path.isfile(file_path):
                mime = "text/css" if file_path.endswith(".css") else "application/javascript" if file_path.endswith(".js") else "text/plain"
                with open(file_path, "rb") as f:
                    content = f.read()
                self.send_response(200)
                self.send_header("Content-Type", mime)
                self.send_header("Content-Length", str(len(content)))
                self.end_headers()
                self.wfile.write(content)
                return

        # 3. HTML Views
        views_map = {
            "/": "index.html",
            "/dashboard": "dashboard.html",
            "/inspect": "inspect.html",
            "/analyze": "inspect.html",
            "/issues": "issues.html",
            "/data-quality": "data_quality.html",
            "/documents": "documents.html",
            "/compare": "compare.html",
            "/compliance": "compliance.html",
            "/chat": "chat.html",
            "/reports": "reports.html",
            "/export": "reports.html",
            "/notifications": "notifications.html",
            "/audit": "audit.html",
            "/admin": "admin.html",
            "/auth": "auth.html",
            "/settings": "settings.html"
        }

        view_file = views_map.get(path, "index.html")
        tmpl_path = os.path.join(settings.BASE_DIR, "app", "templates", view_file)
        if os.path.exists(tmpl_path):
            with open(tmpl_path, "rb") as f:
                content = f.read()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(content)))
            self.end_headers()
            self.wfile.write(content)
            return

        self.send_response(404)
        self.end_headers()
        self.wfile.write(b"404 Page Not Found")
