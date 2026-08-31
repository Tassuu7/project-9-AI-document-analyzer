"""HTTP Server."""
import os
import json
import urllib.parse
from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn
from typing import Dict, Any, Optional
from app.core.config import settings
from app.core.security import SecurityManager

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    daemon_threads = True
    allow_reuse_address = True

class RequestHandler(BaseHTTPRequestHandler):
    def log_message(self, format, *args): pass

    def _send_json_response(self, data: Any, status_code: int = 200):
        body = json.dumps(data).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, Authorization")
        self.end_headers()
        self.wfile.write(body)

    def _send_html_response(self, html_content: str, status_code: int = 200):
        body = html_content.encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _send_file_response(self, file_path: str):
        if not os.path.exists(file_path):
            self.send_error(404, "File Not Found")
            return
        mime = "text/css" if file_path.endswith(".css") else "application/javascript" if file_path.endswith(".js") else "text/html"
        with open(file_path, "rb") as f: content = f.read()
        self.send_response(200)
        self.send_header("Content-Type", mime)
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, Authorization")
        self.end_headers()

    def parse_request_body(self) -> Dict[str, Any]:
        l = int(self.headers.get("Content-Length", 0))
        if l == 0: return {}
        raw = self.rfile.read(l)
        try: return json.loads(raw.decode("utf-8"))
        except Exception: return {"_raw": raw}

    def do_GET(self): self._dispatch("GET")
    def do_POST(self): self._dispatch("POST")
    def do_DELETE(self): self._dispatch("DELETE")

    def _dispatch(self, method: str):
        from app.api.router import handle_route
        parsed = urllib.parse.urlparse(self.path)
        handle_route(self, method, parsed.path, urllib.parse.parse_qs(parsed.query))
