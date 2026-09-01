"""Unit Tests for Contract & Security Risk Analyzer."""
import unittest
from app.inspection.risk_analyzer import RiskAnalyzer

class TestRiskAnalyzer(unittest.TestCase):
    def test_auto_renewal_and_unilateral_termination(self):
        text = "This contract will automatically renew annually. Either party may terminate at any time without notice."
        res = RiskAnalyzer.evaluate_risks(text)
        self.assertGreater(res["overall_risk_score"], 30.0)
        titles = [f["title"] for f in res["findings"]]
        self.assertIn("Automatic Renewal Trap", titles)
        self.assertIn("Unilateral Termination Rights", titles)

    def test_credential_leak(self):
        text = "Server connection config: password = 'SuperSecretPassword123' on db01."
        res = RiskAnalyzer.evaluate_risks(text)
        self.assertEqual(res["risk_level"], "CRITICAL")
        self.assertTrue(any("Plain Text Credentials" in f["title"] for f in res["findings"]))

if __name__ == "__main__":
    unittest.main()
