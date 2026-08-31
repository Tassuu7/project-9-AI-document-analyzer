"""Unit Tests for Text, CSV, JSON, and PDF Parsers."""
import unittest
from app.parsers.text_parser import TextParser
from app.parsers.csv_parser import CSVParser
from app.parsers.json_parser import JSONParser

class TestParsers(unittest.TestCase):
    def test_text_parser(self):
        raw = "Header Title\n\nParagraph one with **bold** text.\n\nParagraph two."
        res = TextParser.parse(raw)
        self.assertEqual(res["paragraph_count"], 3)
        self.assertIn("Header Title", res["clean_text"])

    def test_csv_parser(self):
        csv_data = "Name,Role,Department\nAlice,Lead,Security\nBob,Analyst,Compliance"
        res = CSVParser.parse(csv_data)
        self.assertEqual(res["row_count"], 2)
        self.assertEqual(res["column_count"], 3)

    def test_json_parser(self):
        json_data = '{"project": "DocAnalyzer", "version": "2.4.0", "active": true}'
        res = JSONParser.parse(json_data)
        self.assertTrue(res["valid_json"])
        self.assertIn("project: DocAnalyzer", res["clean_text"])

if __name__ == "__main__":
    unittest.main()
