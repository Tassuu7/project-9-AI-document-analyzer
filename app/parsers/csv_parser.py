"""CSV Structured Data Parser."""
import csv
import io
from typing import Dict, Any, List

class CSVParser:
    @classmethod
    def parse(cls, content: str) -> Dict[str, Any]:
        if not content or not content.strip():
            return {"clean_text": "", "headers": [], "rows": [], "row_count": 0, "column_count": 0, "column_types": {}, "null_counts": {}, "tables": []}

        try:
            reader = csv.reader(io.StringIO(content.strip()))
            rows = list(reader)
            if not rows:
                return {"clean_text": "", "headers": [], "rows": [], "row_count": 0, "column_count": 0, "column_types": {}, "null_counts": {}, "tables": []}
            
            headers = [h.strip() for h in rows[0]]
            data_rows = rows[1:] if len(rows) > 1 else []
            
            col_types = {}
            null_counts = {h: 0 for h in headers}
            
            for col_idx, h in enumerate(headers):
                types_seen = set()
                for r in data_rows:
                    val = r[col_idx].strip() if col_idx < len(r) else ""
                    if not val or val.lower() in ["null", "none", "nan", "na", "-", ""]:
                        null_counts[h] += 1
                        continue
                    try:
                        float(val.replace("$", "").replace(",", "").replace("%", ""))
                        types_seen.add("numeric")
                    except ValueError:
                        types_seen.add("text")
                col_types[h] = "numeric" if types_seen == {"numeric"} else "mixed" if len(types_seen) > 1 else "text"

            text_repr = "\n".join([", ".join(r) for r in rows[:100]])
            return {
                "clean_text": text_repr,
                "headers": headers,
                "rows": data_rows,
                "row_count": len(data_rows),
                "column_count": len(headers),
                "column_types": col_types,
                "null_counts": null_counts,
                "word_count": sum(len(r) for r in rows),
                "page_count": max(1, len(data_rows) // 50),
                "tables": [{"name": "CSV Data Table", "headers": headers, "rows": data_rows[:200]}]
            }
        except Exception as e:
            return {"clean_text": content, "headers": [], "rows": [], "row_count": 0, "column_count": 0, "column_types": {}, "null_counts": {}, "error": str(e), "tables": []}
