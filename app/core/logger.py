"""Enterprise Structured Logger."""
import time

class Logger:
    def __init__(self, name: str = "DocAnalyzer"):
        self.name = name

    def info(self, msg: str, **kwargs):
        t = time.strftime("%Y-%m-%d %H:%M:%S")
        print(f"{t} [INFO] [{self.name}] {msg}", flush=True)

    def warning(self, msg: str, **kwargs):
        t = time.strftime("%Y-%m-%d %H:%M:%S")
        print(f"{t} [WARN] [{self.name}] {msg}", flush=True)

    def error(self, msg: str, **kwargs):
        t = time.strftime("%Y-%m-%d %H:%M:%S")
        print(f"{t} [ERROR] [{self.name}] {msg}", flush=True)

logger = Logger("DocAnalyzer")
