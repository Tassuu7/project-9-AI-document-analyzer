"""Document-Grounded Non-Hallucinating Q&A Engine."""
import re
from typing import Dict, Any, List

class ChatEngine:
    @classmethod
    def answer_question(cls, query: str, doc_text: str, analysis_data: Dict[str, Any]) -> Dict[str, Any]:
        if not query or not doc_text:
            return {
                "answer": "I couldn't find enough information in this document to answer that.",
                "citations": []
            }

        q_low = query.lower().strip()
        citations = []

        # 1. Biggest Problems / Summary of Errors
        if any(w in q_low for w in ["biggest problem", "top issue", "main error", "critical issue", "summary of error"]):
            issues = analysis_data.get("issues", [])
            criticals = [i for i in issues if i.get("severity") in ["CRITICAL", "HIGH"]]
            if criticals:
                ans = f"I identified {len(criticals)} critical/high-severity issues in this document:\n\n"
                for idx, c in enumerate(criticals[:4], 1):
                    ans += f"{idx}. **[{c.get('category')}] {c.get('title')}** ({c.get('severity')}): {c.get('explanation')} *Recommendation:* {c.get('recommendation')}\n"
                    citations.append(c.get("location", "Document"))
                return {"answer": ans, "citations": citations}
            else:
                return {
                    "answer": "No critical or high-severity issues were detected. The document passed major validation checks.",
                    "citations": ["Inspection Findings"]
                }

        # 2. Inconsistent Dates / Contradictions
        if any(w in q_low for w in ["inconsistent date", "contradict", "conflict", "different date", "duration"]):
            issues = [i for i in analysis_data.get("issues", []) if i.get("category") == "CONSISTENCY"]
            if issues:
                ans = "Here are the inconsistencies detected in the document:\n\n"
                for idx, iss in enumerate(issues, 1):
                    ans += f"{idx}. **{iss.get('title')}**: {iss.get('evidence')} ({iss.get('explanation')})\n"
                    citations.append(iss.get("location", "Consistency Matrix"))
                return {"answer": ans, "citations": citations}
            else:
                return {
                    "answer": "No cross-section contradictions or conflicting dates were detected in this document.",
                    "citations": []
                }

        # 3. Financial / Calculation Errors
        if any(w in q_low for w in ["financial error", "calculation", "math", "total mismatch", "subtotal"]):
            issues = [i for i in analysis_data.get("issues", []) if i.get("category") == "CALCULATION"]
            if issues:
                ans = "Financial and calculation discrepancies detected:\n\n"
                for idx, iss in enumerate(issues, 1):
                    ans += f"{idx}. **{iss.get('title')}**: Document states {iss.get('value')}, but expected {iss.get('expected_value')}. {iss.get('explanation')}\n"
                    citations.append(iss.get("location", "Calculation Engine"))
                return {"answer": ans, "citations": citations}
            else:
                return {
                    "answer": "All arithmetic formulas (Quantity × Price, Subtotal + Tax = Total) verified with zero calculation errors.",
                    "citations": ["Calculation Validator"]
                }

        # 4. Risks & Termination Clauses
        if any(w in q_low for w in ["risk", "termination", "liability", "indemnif", "auto-renew"]):
            issues = [i for i in analysis_data.get("issues", []) if i.get("category") in ["CONTRACT_RISK", "SECURITY_RISK", "PRIVACY_RISK"]]
            if issues:
                ans = "Key legal and operational risks identified:\n\n"
                for idx, iss in enumerate(issues, 1):
                    ans += f"{idx}. **[{iss.get('severity')}] {iss.get('title')}**: {iss.get('explanation')} *Impact:* {iss.get('impact')}\n"
                    citations.append(iss.get("location", "Risk Analyzer"))
                return {"answer": ans, "citations": citations}

        # 5. PII & Privacy
        if any(w in q_low for w in ["pii", "privacy", "personal data", "email", "phone", "ssn"]):
            issues = [i for i in analysis_data.get("issues", []) if i.get("category") == "PII"]
            if issues:
                ans = f"Detected {len(issues)} sensitive PII identifiers:\n\n"
                for idx, iss in enumerate(issues[:5], 1):
                    ans += f"{idx}. **{iss.get('title')}**: `{iss.get('expected_value')}` at {iss.get('location')}\n"
                return {"answer": ans, "citations": ["PII Inspector"]}

        # 6. Direct Keyword / Clause Search in Document Text
        paragraphs = [p.strip() for p in re.split(r'\n\s*\n+', doc_text) if p.strip()]
        matching_paras = []
        words = [w for w in re.findall(r'\b\w+\b', q_low) if len(w) > 3 and w not in ["what", "where", "when", "show", "tell", "find", "this", "that", "with", "from"]]
        
        for p_idx, p in enumerate(paragraphs):
            p_low = p.lower()
            match_score = sum(1 for w in words if w in p_low)
            if match_score >= max(1, len(words) // 2):
                matching_paras.append((match_score, p_idx + 1, p))

        matching_paras.sort(key=lambda x: x[0], reverse=True)
        if matching_paras:
            best = matching_paras[0]
            ans = f"Based on Paragraph {best[1]}:\n\n\"{best[2][:300]}...\""
            return {"answer": ans, "citations": [f"Paragraph {best[1]}"]}

        return {
            "answer": "I couldn't find enough information in this document to answer that question accurately.",
            "citations": []
        }
