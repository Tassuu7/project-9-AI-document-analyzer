"""Tests for Complexity and Long Sentence Detection."""
import unittest
from app.inspection.complexity_detector import ComplexityDetector

class TestComplexityDetector(unittest.TestCase):
    def test_long_sentence_detection(self):
        long_s = "This is a remarkably long, intricate, convoluted, and heavily structured sentence that spans across more than twenty-five words in order to comprehensively test the syntactic complexity heuristics and automated sentence splitting suggestions implemented in the analyzer engine."
        findings = ComplexityDetector.detect_complex_sentences(long_s)
        self.assertGreaterEqual(len(findings), 1)
        self.assertEqual(findings[0]["category"], "COMPLEXITY")
        self.assertIn("words in single sentence", findings[0]["value"])
