"""Unit Tests for Multi-Format Parsers."""
import unittest
from app.parsers.text_parser import TextParser
from app.parsers.csv_parser import CSVParser
from app.parsers.json_parser import JSONParser

class TestParsers(unittest.TestCase):
    def test_text_parser(self):
        raw = "First paragraph here with some text.\n\nSecond paragraph with more information."
        res = TextParser.parse(raw)
        self.assertEqual(res["paragraph_count"], 2)
        self.assertTrue(res["word_count"] > 5)

    def test_csv_parser(self):
        csv_text = "Name,Age,Salary\nAlice,30,80000\nBob,35,90000\nCharlie,null,75000"
        res = CSVParser.parse(csv_text)
        self.assertEqual(res["row_count"], 3)
        self.assertEqual(res["column_count"], 3)
        self.assertEqual(res["null_counts"]["Age"], 1)
        self.assertEqual(res["column_types"]["Salary"], "numeric")

    def test_json_parser(self):
        json_text = '{"company": "CyberCorp", "employees": [{"name": "John", "role": "Dev"}, {"name": "Jane", "role": "PM"}]}'
        res = JSONParser.parse(json_text)
        self.assertTrue(res["valid_json"])
        self.assertEqual(len(res["tables"]), 1)
        self.assertEqual(len(res["tables"][0]["rows"]), 2)

if __name__ == "__main__":
    unittest.main()
