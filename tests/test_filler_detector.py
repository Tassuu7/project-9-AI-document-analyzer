"""Tests for Filler Word and Redundancy Detection."""
import unittest
from app.inspection.filler_detector import FillerDetector

class TestFillerDetector(unittest.TestCase):
    def test_detect_fillers(self):
        text = "In order to achieve the end result, it is absolutely essential that we collaborate together."
        findings = FillerDetector.detect_fillers(text)
        self.assertGreaterEqual(len(findings), 2)
        titles = [f["title"] for f in findings]
        self.assertTrue(any("In order to" in t or "end result" in t or "collaborate together" in t for t in titles))
