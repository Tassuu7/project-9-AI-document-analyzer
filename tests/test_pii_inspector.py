"""Unit Tests for PII Inspector & Redaction."""
import unittest
from app.inspection.pii_inspector import PIIInspector

class TestPIIInspector(unittest.TestCase):
    def test_pii_detection_and_masking(self):
        text = "Customer John Doe with SSN 123-45-6789, email john.doe@example.com, and phone 555-123-4567."
        res = PIIInspector.inspect_pii(text)
        self.assertEqual(res["total_pii_count"], 3)
        self.assertIn("EMAIL", res["breakdown"])
        self.assertIn("SSN", res["breakdown"])
        self.assertIn("PHONE_NUMBER", res["breakdown"])
        self.assertNotIn("123-45-6789", res["redacted_text"])
        self.assertIn("***-**-6789", res["redacted_text"])

if __name__ == "__main__":
    unittest.main()
