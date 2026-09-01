"""End-to-End System Inspection Pipeline Tests."""
import unittest
from app.services.document_service import DocumentService
from app.services.analyzer_service import AnalyzerService
from app.services.issue_service import IssueService

class TestEndToEnd(unittest.TestCase):
    def test_full_pipeline(self):
        sample = b"CONFIDENTIAL AGREEMENT\n1. Term: 12 months.\n2. Standard: The company are responsible.\n3. Cost: 50 units at $20.00 each = $1,200.00 total.\n4. Auto-renew annually."
        doc_info = DocumentService.save_and_process_upload("test_contract.txt", sample, "user_default")
        self.assertIsNotNone(doc_info["id"])

        report = AnalyzerService.inspect_document_by_id(doc_info["id"], "user_default")
        self.assertIn("health", report)
        self.assertIn("issues", report)
        self.assertTrue(len(report["issues"]) >= 3)

        issues = IssueService.list_issues(document_id=doc_info["id"])
        self.assertTrue(len(issues) >= 3)

        # Resolve first issue
        first_iss = issues[0]
        ok = IssueService.update_issue_status(first_iss["id"], "RESOLVED", "Audited and verified.")
        self.assertTrue(ok)

if __name__ == "__main__":
    unittest.main()
