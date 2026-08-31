"""
Integration Tests for Services and End-to-End Analytics Pipeline
"""

import unittest
from app.services.auth_service import AuthService
from app.services.analyzer_service import AnalyzerService
from tests.test_fixtures import SAMPLE_NDA_TEXT

class TestServices(unittest.TestCase):
    def test_auth_service(self):
        try:
            reg = AuthService.register("test_service_user", "test_user@domain.com", "SecurePass123!", role="Analyst")
            self.assertTrue("token" in reg)
        except Exception:
            login = AuthService.login("test_service_user", "SecurePass123!")
            self.assertTrue("token" in login)

    def test_analyzer_service_pipeline(self):
        report = AnalyzerService.run_full_pipeline(SAMPLE_NDA_TEXT)
        self.assertTrue("classification" in report)
        self.assertTrue("summary" in report)
        self.assertTrue("entities" in report)
        self.assertTrue("sentiment" in report)
        self.assertTrue("compliance" in report)
        self.assertTrue("risk" in report)

if __name__ == "__main__":
    unittest.main()
