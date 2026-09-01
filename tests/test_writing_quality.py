"""Tests for Writing Quality and Readability Scoring."""
import unittest
from app.inspection.writing_quality_scorer import WritingQualityScorer

class TestWritingQuality(unittest.TestCase):
    def test_writing_metrics(self):
        text = "The platform delivers automated document quality inspection. Users upload files to detect risks and calculation discrepancies."
        res = WritingQualityScorer.score_writing_quality(text)
        self.assertGreater(res["word_count"], 10)
        self.assertGreater(res["character_count"], 50)
        self.assertGreater(res["flesch_reading_ease"], 0)
        self.assertGreater(res["composite_writing_quality_score"], 40)
        self.assertIn("readability_label", res)
