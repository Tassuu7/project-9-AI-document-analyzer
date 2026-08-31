"""
Unit Tests for Risk and Liability Scoring
"""

import unittest
from app.nlp.risk.risk_scorer import RiskScorer

class TestRisk(unittest.TestCase):
    def test_high_risk_clause(self):
        text = "Vendor agrees to unlimited liability and shall indemnify customer with immediate termination without notice."
        res = RiskScorer.evaluate_risk(text)
        self.assertGreater(res["overall_risk_score"], 40.0)
        self.assertTrue(len(res["risk_factors"]) > 0)

if __name__ == "__main__":
    unittest.main()
