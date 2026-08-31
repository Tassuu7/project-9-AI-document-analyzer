"""CSV Parser."""
import csv
import io
from typing import Dict, Any, List

class CSVParser:
    @classmethod
    def parse(cls, content: str) -> Dict[str, Any]:
        reader = csv.reader(io.StringIO(content))
        rows = list(reader)
        if not rows:
            return {"clean_text": "", "row_count": 0, "column_count": 0}
        headers = rows[0]
        data_rows = rows[1:]
        lines = [f"Dataset with {len(headers)} columns: {', '.join(headers)}."]
        for idx, r in enumerate(data_rows[:200]):
            desc = [f"{headers[i] if i < len(headers) else f'Col{i}'}: {val}" for i, val in enumerate(r) if val.strip()]
            if desc:
                lines.append(f"Record {idx+1}: " + "; ".join(desc) + ".")
        full_text = "\n".join(lines)
        return {
            "clean_text": full_text,
            "row_count": len(data_rows),
            "column_count": len(headers),
            "word_count": len(full_text.split()),
            "char_count": len(full_text)
        }
