"""Cross-Field Formula and Calculation Validator."""
import re
from typing import Dict, Any, List

class CalculationValidator:
    @classmethod
    def validate_calculations(cls, text: str) -> List[Dict[str, Any]]:
        issues: List[Dict[str, Any]] = []
        if not text:
            return issues

        # 1. Quantity * Price = Total pattern
        # e.g. "50 units at $20.00 each = $1,200.00" (Expected $1,000)
        qty_price_pattern = re.compile(
            r'(\d+)\s*(?:units|items|hours|shares|licenses)?\s*(?:at|@)\s*\$?([\d,]+(?:\.\d{2})?)\s*(?:each|per\s+unit)?\s*(?:total|equals|=|\:)\s*\$?([\d,]+(?:\.\d{2})?)',
            re.IGNORECASE
        )
        for match in qty_price_pattern.finditer(text):
            try:
                qty = float(match.group(1).replace(",", ""))
                unit_price = float(match.group(2).replace(",", ""))
                stated_total = float(match.group(3).replace(",", ""))
                expected_total = qty * unit_price
                diff = abs(stated_total - expected_total)
                
                if diff > 0.05:
                    issues.append({
                        "category": "CALCULATION",
                        "severity": "HIGH",
                        "title": "Multiplication Calculation Error",
                        "location": f"Clause: '{match.group(0)}'",
                        "value": f"${stated_total:,.2f}",
                        "expected_value": f"${expected_total:,.2f}",
                        "evidence": f"Calculated: {qty} × ${unit_price:,.2f} = ${expected_total:,.2f}, but document states ${stated_total:,.2f}.",
                        "explanation": f"Discrepancy of ${diff:,.2f} detected in unit total product calculation.",
                        "impact": "Financial terms or billing will be inaccurate.",
                        "recommendation": f"Verify the line item and correct total to ${expected_total:,.2f}.",
                        "confidence": 0.99,
                        "suggested_correction": f"${expected_total:,.2f}"
                    })
            except Exception:
                pass

        # 2. Subtotal + Tax = Total pattern
        # e.g. "Subtotal: $10,000, Tax: $800, Total: $11,500"
        subtotal_match = re.search(r'Subtotal\s*[:=]\s*\$?([\d,]+(?:\.\d{2})?)', text, re.IGNORECASE)
        tax_match = re.search(r'Tax\s*[:=]\s*\$?([\d,]+(?:\.\d{2})?)', text, re.IGNORECASE)
        total_match = re.search(r'(?:Grand\s+Total|Total\s+Amount|Total\s+Due)\s*[:=]\s*\$?([\d,]+(?:\.\d{2})?)', text, re.IGNORECASE)
        
        if subtotal_match and tax_match and total_match:
            try:
                sub = float(subtotal_match.group(1).replace(",", ""))
                tax = float(tax_match.group(1).replace(",", ""))
                tot = float(total_match.group(1).replace(",", ""))
                expected = sub + tax
                diff = abs(tot - expected)
                if diff > 0.05:
                    issues.append({
                        "category": "CALCULATION",
                        "severity": "HIGH",
                        "title": "Subtotal and Tax Addition Mismatch",
                        "location": "Financial Summary Section",
                        "value": f"${tot:,.2f}",
                        "expected_value": f"${expected:,.2f}",
                        "evidence": f"Subtotal (${sub:,.2f}) + Tax (${tax:,.2f}) = ${expected:,.2f}, but Total is declared as ${tot:,.2f}.",
                        "explanation": f"Addition error: Total differs from subtotal + tax by ${diff:,.2f}.",
                        "impact": "Incorrect invoice or financial settlement amount.",
                        "recommendation": f"Recalculate invoice total to ${expected:,.2f}.",
                        "confidence": 0.99,
                        "suggested_correction": f"${expected:,.2f}"
                    })
            except Exception:
                pass

        # 3. Sum of Itemized Line Items vs Stated Total
        # Extract lists of currency values
        currency_matches = [float(x.replace(",", "")) for x in re.findall(r'\$([\d,]+(?:\.\d{2})?)', text)]
        if len(currency_matches) >= 4 and total_match:
            try:
                declared_total = float(total_match.group(1).replace(",", ""))
                line_items = [c for c in currency_matches if c != declared_total]
                sum_items = sum(line_items)
                if abs(sum_items - declared_total) > 1.0 and abs(sum_items - declared_total) < declared_total * 0.5:
                    issues.append({
                        "category": "CALCULATION",
                        "severity": "HIGH",
                        "title": "Line Items Sum Mismatch",
                        "location": "Itemized Summary",
                        "value": f"${declared_total:,.2f}",
                        "expected_value": f"${sum_items:,.2f}",
                        "evidence": f"Sum of {len(line_items)} line items equals ${sum_items:,.2f}, differing from declared total ${declared_total:,.2f}.",
                        "explanation": "The declared grand total does not match the sum of individual listed values.",
                        "impact": "Accounting reconciliation discrepancy.",
                        "recommendation": "Review individual item amounts and reconcile the total.",
                        "confidence": 0.94,
                        "suggested_correction": f"${sum_items:,.2f}"
                    })
            except Exception:
                pass

        return issues
