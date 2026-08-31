"""JSON Parser."""
import json
from typing import Dict, Any, List

class JSONParser:
    @classmethod
    def parse(cls, content: str) -> Dict[str, Any]:
        try:
            data = json.loads(content)
        except Exception:
            return {"clean_text": content, "word_count": len(content.split()), "valid_json": False}
        lines: List[str] = []
        def _walk(obj, prefix=""):
            if isinstance(obj, dict):
                for k, v in obj.items():
                    key_path = f"{prefix}.{k}" if prefix else k
                    _walk(v, key_path)
            elif isinstance(obj, list):
                for i, item in enumerate(obj):
                    key_path = f"{prefix}[{i}]"
                    _walk(item, key_path)
            else:
                lines.append(f"{prefix}: {obj}")
        _walk(data)
        full_text = "\n".join(lines)
        return {
            "clean_text": full_text,
            "word_count": len(full_text.split()),
            "char_count": len(full_text),
            "valid_json": True
        }
