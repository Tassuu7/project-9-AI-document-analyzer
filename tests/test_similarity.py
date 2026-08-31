"""Unit Tests for Vectorizer and Document Comparator."""
import unittest
from app.nlp.similarity.vectorizer import TFIDFVectorizer
from app.nlp.similarity.comparator import DocumentComparator

class TestSimilarity(unittest.TestCase):
    def test_tfidf_cosine_similarity(self):
        doc1 = "The software platform provides document intelligence and compliance audits."
        doc2 = "This software system provides compliance audits and document intelligence."
        vectorizer = TFIDFVectorizer()
        vecs = vectorizer.fit_transform([doc1, doc2])
        sim = TFIDFVectorizer.cosine_similarity(vecs[0], vecs[1])
        self.assertGreater(sim, 0.7)

    def test_document_diff(self):
        text_a = "Line 1: Initial clause.\nLine 2: Confidentiality obligations."
        text_b = "Line 1: Initial clause.\nLine 2: Confidentiality obligations revised.\nLine 3: New clause."
        res = DocumentComparator.compare(text_a, text_b)
        self.assertGreaterEqual(res["lines_modified"] + res["lines_added"], 1)

if __name__ == "__main__":
    unittest.main()
