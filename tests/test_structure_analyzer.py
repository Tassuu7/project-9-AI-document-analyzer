"""Tests for Document Structure Analyzer."""
import unittest
from app.inspection.structure_analyzer import StructureAnalyzer

class TestStructureAnalyzer(unittest.TestCase):
    def test_structure_analysis(self):
        text = "# Title 1\nParagraph one of content.\n### Skipped Level Subheading\nParagraph two of content."
        res = StructureAnalyzer.analyze_structure(text)
        self.assertEqual(res["total_headings"], 2)
        self.assertGreaterEqual(len(res["heading_hierarchy_issues"]), 1)
        self.assertIn("Skipped heading level", res["heading_hierarchy_issues"][0]["issue"])
