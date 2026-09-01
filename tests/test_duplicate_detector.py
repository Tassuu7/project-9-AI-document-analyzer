"""Tests for Duplicate Sentence Detection."""
import unittest
from app.inspection.duplicate_sentence_detector import DuplicateSentenceDetector

class TestDuplicateDetector(unittest.TestCase):
    def test_exact_duplicate(self):
        text = "The agreement shall continue for 12 months. The company shall protect data. The agreement shall continue for 12 months."
        findings = DuplicateSentenceDetector.detect_duplicate_sentences(text)
        self.assertGreaterEqual(len(findings), 1)
        self.assertEqual(findings[0]["category"], "DUPLICATE_TEXT")
