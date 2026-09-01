"""Unit Tests for Cross-Section Consistency & Contradiction Checker."""
import unittest
from app.inspection.consistency_engine import ConsistencyEngine

class TestConsistencyEngine(unittest.TestCase):
    def test_duration_contradiction(self):
        text = "Section 1: The initial term shall be for 12 months.\n\nSection 8: Obligations shall survive for a period of 24 months."
        issues = ConsistencyEngine.check_consistency(text)
        self.assertTrue(any("Conflicting Duration Terms" in i["title"] for i in issues))

    def test_jurisdiction_contradiction(self):
        text = "Clause A: Governed by the laws of the State of Delaware.\n\nClause B: Any disputes subject to the jurisdiction of California."
        issues = ConsistencyEngine.check_consistency(text)
        self.assertTrue(any("Conflicting Governing Law" in i["title"] for i in issues))

if __name__ == "__main__":
    unittest.main()
