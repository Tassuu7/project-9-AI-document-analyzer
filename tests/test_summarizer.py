"""
Unit Tests for Extractive and Executive Summarizers
"""

import unittest
from app.nlp.summarizers.extractive_summarizer import ExtractiveSummarizer
from app.nlp.summarizers.executive_summarizer import ExecutiveSummarizer
from tests.test_fixtures import SAMPLE_NDA_TEXT

class TestSummarizer(unittest.TestCase):
    def test_extractive_summary(self):
        res = ExtractiveSummarizer.summarize(SAMPLE_NDA_TEXT, max_sentences=3)
        self.assertTrue(len(res["summary"]) > 0)
        self.assertLessEqual(res["sentence_count"], 3)

    def test_executive_brief(self):
        brief = ExecutiveSummarizer.generate_brief(SAMPLE_NDA_TEXT)
        self.assertTrue(len(brief["key_obligations"]) > 0)

if __name__ == "__main__":
    unittest.main()
