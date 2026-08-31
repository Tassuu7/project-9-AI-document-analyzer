"""Export Service."""
import json
import csv
import io
from typing import Dict, Any

class ExportService:
    @classmethod
    def to_json(cls, data: Dict[str, Any]) -> str:
        return json.dumps(data, indent=2)

    @classmethod
    def to_csv_entities(cls, data: Dict[str, Any]) -> str:
        out = io.StringIO()
        w = csv.writer(out)
        w.writerow(["Entity Text", "Type", "Category", "Confidence"])
        for e in data.get("entities", []):
            w.writerow([e.get("text", ""), e.get("type", ""), e.get("category", ""), e.get("confidence", 1.0)])
        return out.getvalue()

    @classmethod
    def to_markdown(cls, data: Dict[str, Any]) -> str:
        c = data.get("classification", {})
        s = data.get("summary", {})
        r = data.get("risk", {})
        lines = [
            "# AI Document Analysis Report",
            f"**Classification:** {c.get('category', 'N/A')} ({int(c.get('confidence', 0)*100)}% confidence)",
            "## Executive Summary",
            s.get("extractive", "N/A"),
            "## Risk Assessment",
            f"- Overall Risk Score: {r.get('overall_risk_score', 0)} / 100 ({r.get('risk_level', 'N/A')})"
        ]
        return "\n\n".join(lines)
