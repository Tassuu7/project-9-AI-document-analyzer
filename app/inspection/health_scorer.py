"""Document Health & Quality Composite Score Calculator."""
from typing import Dict, Any, List

class HealthScorer:
    @classmethod
    def calculate_health_score(
        cls,
        text_errors: List[Dict[str, Any]],
        data_quality_res: Dict[str, Any],
        consistency_errors: List[Dict[str, Any]],
        calc_errors: List[Dict[str, Any]],
        risk_res: Dict[str, Any],
        compliance_res: Dict[str, Any],
        word_count: int = 100
    ) -> Dict[str, Any]:
        # 1. Text Quality Score (Start 100, deduct per error)
        text_deductions = sum(8.0 if e.get("severity") == "HIGH" else 4.0 if e.get("severity") == "MEDIUM" else 2.0 for e in text_errors)
        text_score = max(20.0, 100.0 - text_deductions)

        # 2. Data Quality Score
        dq_score = data_quality_res.get("quality_score", 95.0)

        # 3. Consistency Score
        consistency_deductions = len(consistency_errors) * 15.0
        consistency_score = max(20.0, 100.0 - consistency_deductions)

        # 4. Calculation Score
        calc_deductions = len(calc_errors) * 20.0
        calc_score = max(10.0, 100.0 - calc_deductions)

        # 5. Risk Score (Inverted: high risk -> lower health)
        risk_score_val = risk_res.get("overall_risk_score", 20.0)
        risk_health = max(10.0, 100.0 - risk_score_val)

        # 6. Compliance Score
        violations = compliance_res.get("violations_found", [])
        comp_deductions = len(violations) * 18.0
        comp_score = max(15.0, 100.0 - comp_deductions)

        # Overall Weighted Composite
        overall_health = round(
            0.20 * text_score +
            0.15 * dq_score +
            0.15 * consistency_score +
            0.15 * calc_score +
            0.20 * risk_health +
            0.15 * comp_score,
            1
        )

        return {
            "overall_health_score": overall_health,
            "text_quality_score": round(text_score, 1),
            "data_quality_score": round(dq_score, 1),
            "consistency_score": round(consistency_score, 1),
            "calculation_score": round(calc_score, 1),
            "risk_health_score": round(risk_health, 1),
            "compliance_score": round(comp_score, 1),
            "health_level": "EXCELLENT" if overall_health >= 90 else "GOOD" if overall_health >= 75 else "FAIR" if overall_health >= 60 else "POOR"
        }
