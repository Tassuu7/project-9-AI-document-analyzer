"""JSON Structural Data Parser."""
import json
from typing import Dict, Any, List

class JSONParser:
    @classmethod
    def parse(cls, content: str) -> Dict[str, Any]:
        try:
            data = json.loads(content)
            lines = []
            keys_seen = []
            
            def flatten(obj, prefix=""):
                if isinstance(obj, dict):
                    for k, v in obj.items():
                        full_key = f"{prefix}.{k}" if prefix else k
                        keys_seen.append(full_key)
                        if isinstance(v, (dict, list)):
                            flatten(v, full_key)
                        else:
                            lines.append(f"{full_key}: {v}")
                elif isinstance(obj, list):
                    for i, item in enumerate(obj):
                        full_key = f"{prefix}[{i}]"
                        if isinstance(item, (dict, list)):
                            flatten(item, full_key)
                        else:
                            lines.append(f"{full_key}: {item}")

            flatten(data)
            clean_text = "\n".join(lines)
            
            # Extract tabular representation if root or child is list of objects
            tables = []
            if isinstance(data, list) and len(data) > 0 and isinstance(data[0], dict):
                headers = list(data[0].keys())
                rows = [[str(item.get(h, "")) for h in headers] for item in data]
                tables.append({"name": "JSON Root Table", "headers": headers, "rows": rows})
            elif isinstance(data, dict):
                for k, v in data.items():
                    if isinstance(v, list) and len(v) > 0 and isinstance(v[0], dict):
                        headers = list(v[0].keys())
                        rows = [[str(item.get(h, "")) for h in headers] for item in v]
                        tables.append({"name": f"JSON Table: {k}", "headers": headers, "rows": rows})

            return {
                "clean_text": clean_text,
                "parsed_data": data,
                "keys": keys_seen,
                "key_count": len(keys_seen),
                "valid_json": True,
                "word_count": len(clean_text.split()),
                "page_count": max(1, len(lines) // 40),
                "tables": tables
            }
        except Exception as e:
            return {"clean_text": content, "parsed_data": None, "keys": [], "key_count": 0, "valid_json": False, "error": str(e), "tables": []}
