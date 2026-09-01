"""Unit Tests for Structured Data Quality & Anomaly Detection."""
import unittest
from app.inspection.data_quality_engine import DataQualityEngine

class TestDataQualityEngine(unittest.TestCase):
    def test_missing_and_outliers(self):
        headers = ["ID", "Age", "Salary"]
        rows = [
            ["101", "25", "50000"],
            ["102", "28", "52000"],
            ["103", "31", "54000"],
            ["104", "29", "51000"],
            ["105", "30", "53000"],
            ["106", "32", "55000"],
            ["107", "27", "51500"],
            ["108", "26", "50500"],
            ["109", "300", "53500"],  # Outlier and invalid age
            ["110", "null", "52500"]  # Missing
        ]
        res = DataQualityEngine.analyze_table_data(headers, rows)
        self.assertLess(res["quality_score"], 98.0)
        self.assertTrue(any("Invalid Age" in i["title"] or "Outlier" in i["title"] for i in res["issues"]))
        self.assertTrue(any("Missing Data" in i["title"] for i in res["issues"]))

    def test_duplicate_rows(self):
        headers = ["ID", "Name"]
        rows = [["1", "Alice"], ["2", "Bob"], ["1", "Alice"]]
        res = DataQualityEngine.analyze_table_data(headers, rows)
        self.assertTrue(any("Duplicate Records" in i["title"] for i in res["issues"]))

if __name__ == "__main__":
    unittest.main()
