"""
Unit Tests for Multi-Standard Regulatory Compliance Engine
"""

import unittest
from app.nlp.compliance.compliance_engine import ComplianceEngine
from tests.test_fixtures import SAMPLE_BREACH_COMPLIANCE_TEXT

class TestCompliance(unittest.TestCase):
    def test_breach_detection(self):
        audit = ComplianceEngine.audit_document(SAMPLE_BREACH_COMPLIANCE_TEXT)
        self.assertGreater(len(audit["violations_found"]), 0)
        self.assertTrue(audit["critical_violations"] > 0)
        standards = [v["standard"] for v in audit["violations_found"]]
        self.assertTrue("PCI-DSS" in standards or "GDPR" in standards)

if __name__ == "__main__":
    unittest.main()
