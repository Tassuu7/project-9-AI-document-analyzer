"""Unit Tests for Multi-Format Exporter."""
import unittest
import json
from app.services.export_service import ExportService

class TestExportService(unittest.TestCase):
    def test_json_and_csv_exports(self):
        data = {
            "health": {"overall_health_score": 88.0, "health_level": "GOOD"},
            "issues": [
                {"category": "TEXT_ERROR", "severity": "LOW", "title": "Typo", "location": "p1", "value": "teh", "expected_value": "the", "explanation": "misspelled", "recommendation": "fix", "confidence": 0.95, "status": "OPEN"}
            ]
        }
        json_res = ExportService.generate_report(data, "json")
        self.assertEqual(json_res["mime_type"], "application/json")
        parsed = json.loads(json_res["content"])
        self.assertEqual(parsed["health"]["overall_health_score"], 88.0)

        csv_res = ExportService.generate_report(data, "csv")
        self.assertEqual(csv_res["mime_type"], "text/csv")
        self.assertIn("TEXT_ERROR", csv_res["content"])

if __name__ == "__main__":
    unittest.main()
