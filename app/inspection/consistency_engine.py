"""Cross-Section and Cross-Document Consistency & Contradiction Checker."""
import re
from typing import Dict, Any, List

class ConsistencyEngine:
    @classmethod
    def check_consistency(cls, text: str) -> List[Dict[str, Any]]:
        issues: List[Dict[str, Any]] = []
        if not text:
            return issues

        paragraphs = text.split("\n\n")

        # 1. Conflicting Contract Durations (e.g. "12 months" vs "24 months" / "3 years" vs "5 years")
        durations_found = []
        duration_pattern = re.compile(r'\b(\d+)\s*(months?|years?|days?)\b', re.IGNORECASE)
        for p_idx, p in enumerate(paragraphs):
            for match in duration_pattern.finditer(p):
                durations_found.append({
                    "val": match.group(0).lower(),
                    "num": int(match.group(1)),
                    "unit": match.group(2).lower(),
                    "para_idx": p_idx + 1,
                    "snippet": p[:100].strip()
                })

        # Compare found durations with same units
        by_unit = {}
        for d in durations_found:
            unit_norm = "year" if "year" in d["unit"] else "month" if "month" in d["unit"] else "day"
            if unit_norm not in by_unit:
                by_unit[unit_norm] = []
            by_unit[unit_norm].append(d)

        for unit_norm, list_d in by_unit.items():
            distinct_nums = set(d["num"] for d in list_d)
            if len(distinct_nums) > 1 and len(list_d) <= 6:
                # Potential contradiction
                d1 = list_d[0]
                d2 = next(d for d in list_d if d["num"] != d1["num"])
                issues.append({
                    "category": "CONSISTENCY",
                    "severity": "HIGH",
                    "title": f"Conflicting Duration Terms ({unit_norm.capitalize()}s)",
                    "location": f"Paragraph {d1['para_idx']} vs Paragraph {d2['para_idx']}",
                    "value": f"{d1['val']} vs {d2['val']}",
                    "expected_value": "Consistent agreement duration",
                    "evidence": f"Paragraph {d1['para_idx']} states '{d1['val']}' while Paragraph {d2['para_idx']} states '{d2['val']}'.",
                    "explanation": f"Contradictory term lengths detected throughout document sections.",
                    "impact": "Creates legal ambiguity regarding actual term, expiration, and renewal dates.",
                    "recommendation": f"Confirm whether the intended duration is {d1['val']} or {d2['val']}.",
                    "confidence": 0.93,
                    "suggested_correction": ""
                })

        # 2. Conflicting Governing Law / Jurisdiction
        states = ["Delaware", "California", "New York", "Texas", "England and Wales", "Germany", "France", "Ontario", "Singapore"]
        states_found = []
        for p_idx, p in enumerate(paragraphs):
            for s in states:
                if re.search(rf'\b(laws of the state of|governed by the laws of|jurisdiction of)\s+{s}\b', p, re.IGNORECASE):
                    states_found.append({"state": s, "para_idx": p_idx + 1})

        distinct_states = list(set(s["state"] for s in states_found))
        if len(distinct_states) > 1:
            s1 = states_found[0]
            s2 = next(s for s in states_found if s["state"] != s1["state"])
            issues.append({
                "category": "CONSISTENCY",
                "severity": "CRITICAL",
                "title": "Conflicting Governing Law Jurisdictions",
                "location": f"Paragraph {s1['para_idx']} vs Paragraph {s2['para_idx']}",
                "value": f"{s1['state']} vs {s2['state']}",
                "expected_value": "Single governing law jurisdiction",
                "evidence": f"Paragraph {s1['para_idx']} specifies {s1['state']}, but Paragraph {s2['para_idx']} specifies {s2['state']}.",
                "explanation": "Multiple contradictory legal jurisdictions designated in the same agreement.",
                "impact": "May render choice-of-law provisions unenforceable or subject to multi-jurisdictional litigation.",
                "recommendation": "Harmonize the governing law clause to designate a single intended jurisdiction.",
                "confidence": 0.98,
                "suggested_correction": s1["state"]
            })

        # 3. Conflicting Effective Dates
        dates_found = []
        date_pattern = re.compile(r'\b(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+\d{4}\b', re.IGNORECASE)
        for p_idx, p in enumerate(paragraphs):
            for match in date_pattern.finditer(p):
                dates_found.append({"date": match.group(0), "para_idx": p_idx + 1, "context": p[:80]})

        distinct_dates = list(set(d["date"] for d in dates_found))
        if len(distinct_dates) > 1 and any("effective date" in d["context"].lower() for d in dates_found):
            issues.append({
                "category": "CONSISTENCY",
                "severity": "MEDIUM",
                "title": "Multiple Key Dates Referenced",
                "location": "Document Dates Timeline",
                "value": ", ".join(distinct_dates[:3]),
                "expected_value": "Clear chronological sequence",
                "evidence": f"Found multiple distinct formal dates: {', '.join(distinct_dates[:3])}.",
                "explanation": "Document references multiple key dates across paragraphs.",
                "impact": "Potential misalignment between execution date, effective date, and delivery milestone dates.",
                "recommendation": "Verify chronology between execution date, effective date, and performance deadlines.",
                "confidence": 0.89,
                "suggested_correction": ""
            })

        return issues
