"""
Unit Tests for Readability Formulas
"""

import unittest
from app.nlp.readability.readability_metrics import ReadabilityMetrics

class TestReadability(unittest.TestCase):
    def test_readability_metrics(self):
        text = "The cat sat on the mat. It was a sunny and pleasant day in the park."
        res = ReadabilityMetrics.analyze(text)
        self.assertGreater(res["flesch_reading_ease"], 60.0)
        self.assertTrue("reading_level" in res)
        self.assertTrue("flesch_kincaid_grade" in res)

if __name__ == "__main__":
    unittest.main()
