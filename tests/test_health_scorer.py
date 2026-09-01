"""Unit Tests for Composite Document Health Scorer."""
import unittest
from app.inspection.health_scorer import HealthScorer

class TestHealthScorer(unittest.TestCase):
    def test_health_calculation(self):
        text_errors = [{"severity": "LOW"}]
        dq_res = {"quality_score": 95.0}
        consistency_errors = []
        calc_errors = []
        risk_res = {"overall_risk_score": 10.0}
        compliance_res = {"violations_found": []}
        
        score_card = HealthScorer.calculate_health_score(
            text_errors, dq_res, consistency_errors, calc_errors, risk_res, compliance_res, 500
        )
        self.assertGreaterEqual(score_card["overall_health_score"], 85.0)
        self.assertIn(score_card["health_level"], ["EXCELLENT", "GOOD"])

if __name__ == "__main__":
    unittest.main()
