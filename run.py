"""
Enterprise Server Startup Script
Launches the AI Document Analyzer HTTP & REST server on http://127.0.0.1:8974.
"""

import sys
import os
import time

# Ensure UTF-8 stdout encoding on Windows
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

# Ensure project root is in python path
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from app.core.config import settings
from app.core.logger import logger
from app.api.server import ThreadedHTTPServer, RequestHandler

def start_server():
    """Start threaded HTTP server."""
    host = settings.HOST
    port = settings.PORT
    url = settings.UNIQUE_LOCAL_URL
    
    server_address = (host, port)
    httpd = ThreadedHTTPServer(server_address, RequestHandler)
    
    print("=" * 70)
    print("     [+] AI DOCUMENT ANALYZER ENTERPRISE PLATFORM (v2.4.0)")
    print("=" * 70)
    print(f"  [*] Server Engine  : High-Performance Multi-Threaded HTTP/REST")
    print(f"  [*] Local URL      : {url}")
    print(f"  [*] Offline NLP    : Pure Python Built-in (Zero API Keys)")
    print(f"  [*] Telemetry UI   : {url}/dashboard")
    print(f"  [*] Live Analyzer  : {url}/analyze")
    print(f"  [*] Compliance Ctr : {url}/compliance")
    print(f"  [*] Document Diff  : {url}/compare")
    print(f"  [*] Export Center  : {url}/export")
    print("=" * 70)
    print(f"[+] Server listening on {url} ...")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[!] Server shutting down gracefully.")
        httpd.server_close()

if __name__ == "__main__":
    start_server()
