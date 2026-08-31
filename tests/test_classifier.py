"""
Unit Tests for Document Type Classifier
"""

import unittest
from app.nlp.classification.doc_classifier import DocumentClassifier
from tests.test_fixtures import SAMPLE_NDA_TEXT, SAMPLE_FINANCIAL_TEXT, SAMPLE_MEDICAL_TEXT

class TestClassifier(unittest.TestCase):
    def test_classify_nda(self):
        res = DocumentClassifier.classify(SAMPLE_NDA_TEXT)
        self.assertIn("NDA", res["category"])
        self.assertGreater(res["confidence"], 0.5)

    def test_classify_financial(self):
        res = DocumentClassifier.classify(SAMPLE_FINANCIAL_TEXT)
        self.assertIn("Financial", res["category"])

    def test_classify_medical(self):
        res = DocumentClassifier.classify(SAMPLE_MEDICAL_TEXT)
        self.assertIn("Medical", res["category"])

if __name__ == "__main__":
    unittest.main()
