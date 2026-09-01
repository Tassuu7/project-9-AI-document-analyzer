"""Multi-Format Comprehensive Inspection Report Generator (Clean Neutral Styling)."""
import json
from typing import Dict, Any

class ExportService:
    @classmethod
    def generate_report(cls, data: Dict[str, Any], fmt: str = "json") -> Dict[str, Any]:
        fmt = fmt.lower()
        if fmt == "json":
            return {
                "content": json.dumps(data, indent=2),
                "mime_type": "application/json",
                "filename": "inspection_report.json"
            }
        elif fmt == "csv":
            lines = ["Category,Severity,Title,Location,Value,Expected Value,Explanation,Recommendation,Confidence,Status"]
            for iss in data.get("issues", []):
                cat = iss.get("category", "")
                sev = iss.get("severity", "")
                title = f'"{iss.get("title", "")}"'
                loc = f'"{iss.get("location", "")}"'
                val = f'"{str(iss.get("value", "")).replace(chr(34), chr(39))}"'
                exp = f'"{str(iss.get("expected_value", "")).replace(chr(34), chr(39))}"'
                expl = f'"{str(iss.get("explanation", "")).replace(chr(34), chr(39))}"'
                rec = f'"{str(iss.get("recommendation", "")).replace(chr(34), chr(39))}"'
                conf = iss.get("confidence", 0.9)
                st = iss.get("status", "OPEN")
                lines.append(f"{cat},{sev},{title},{loc},{val},{exp},{expl},{rec},{conf},{st}")
            return {
                "content": "\n".join(lines),
                "mime_type": "text/csv",
                "filename": "inspection_issues.csv"
            }
        elif fmt in ["md", "markdown"]:
            h = data.get("health", {})
            md = f"# AI DOCUMENT INSPECTOR - Comprehensive Inspection Report\n\n"
            md += f"**Overall Health Score:** {h.get('overall_health_score', 85)}/100 ({h.get('health_level', 'GOOD')})\n\n"
            md += f"## Health Score Breakdown\n"
            md += f"- **Text Quality:** {h.get('text_quality_score', 90)}/100\n"
            md += f"- **Data Quality:** {h.get('data_quality_score', 90)}/100\n"
            md += f"- **Consistency:** {h.get('consistency_score', 90)}/100\n"
            md += f"- **Risk Health:** {h.get('risk_health_score', 80)}/100\n"
            md += f"- **Compliance Score:** {h.get('compliance_score', 90)}/100\n\n"
            md += f"## Executive Summary\n{data.get('summary', {}).get('extractive', 'Inspection completed.')}\n\n"
            md += f"## Detailed Findings & Issues ({len(data.get('issues', []))} total)\n"
            for idx, iss in enumerate(data.get('issues', []), 1):
                md += f"### {idx}. [{iss.get('severity')}] {iss.get('title')} ({iss.get('category')})\n"
                md += f"- **WHAT IS WRONG:** {iss.get('evidence')}\n"
                md += f"- **WHERE IS IT:** {iss.get('location')}\n"
                md += f"- **WHY IS IT A PROBLEM:** {iss.get('explanation')}\n"
                md += f"- **IMPACT:** {iss.get('impact')}\n"
                md += f"- **WHAT SHOULD THE USER DO:** {iss.get('recommendation')}\n"
                md += f"- **SYSTEM CONFIDENCE:** {int(iss.get('confidence', 0.9)*100)}%\n\n"
            return {
                "content": md,
                "mime_type": "text/markdown",
                "filename": "inspection_report.md"
            }
        else: # Standalone HTML Print-Ready
            h = data.get("health", {})
            html = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>AI Document Inspector - Inspection Report</title>
<style>
body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; line-height: 1.5; color: #0f172a; max-width: 860px; margin: 30px auto; padding: 0 20px; }}
h1 {{ color: #1e293b; border-bottom: 2px solid #334155; padding-bottom: 8px; font-size: 24px; }}
h2 {{ color: #334155; margin-top: 24px; border-bottom: 1px solid #e2e8f0; padding-bottom: 4px; font-size: 18px; }}
.badge {{ display: inline-block; padding: 3px 8px; border-radius: 4px; font-weight: bold; font-size: 11px; text-transform: uppercase; }}
.badge-crit {{ background: #fee2e2; color: #991b1b; }}
.badge-high {{ background: #ffedd5; color: #9a3412; }}
.badge-med {{ background: #fef9c3; color: #854d0e; }}
.badge-low {{ background: #dcfce7; color: #166534; }}
.card {{ border: 1px solid #e2e8f0; border-radius: 6px; padding: 12px; margin-bottom: 10px; background: #f8fafc; font-size: 13px; }}
</style></head><body>
<h1>AI DOCUMENT INSPECTOR - Official Inspection Report</h1>
<p><strong>Overall Health Score:</strong> {h.get('overall_health_score', 85)}/100 ({h.get('health_level', 'GOOD')}) &bull; Total Findings: <strong>{len(data.get('issues', []))}</strong></p>
<h2>Executive Summary</h2>
<p>{data.get('summary', {}).get('extractive', 'Document analyzed.')}</p>
<h2>Inspection Findings Matrix</h2>
"""
            for iss in data.get("issues", []):
                sev_cls = "badge-crit" if iss.get("severity") == "CRITICAL" else "badge-high" if iss.get("severity") == "HIGH" else "badge-med" if iss.get("severity") == "MEDIUM" else "badge-low"
                html += f"""<div class="card">
<div style="display:flex; justify-content:space-between; margin-bottom: 6px;">
  <strong>[{iss.get('category')}] {iss.get('title')}</strong>
  <span class="badge {sev_cls}">{iss.get('severity')}</span>
</div>
<p style="margin: 3px 0;"><strong>WHERE IS IT:</strong> {iss.get('location')} &bull; Confidence: {int(iss.get('confidence', 0.9)*100)}%</p>
<p style="margin: 3px 0;"><strong>WHAT IS WRONG:</strong> {iss.get('evidence')}</p>
<p style="margin: 3px 0;"><strong>WHY IS IT A PROBLEM:</strong> {iss.get('explanation')}</p>
<p style="margin: 3px 0; color: #166534;"><strong>WHAT SHOULD THE USER DO:</strong> {iss.get('recommendation')}</p>
</div>"""
            html += "</body></html>"
            return {
                "content": html,
                "mime_type": "text/html",
                "filename": "inspection_report.html"
            }
