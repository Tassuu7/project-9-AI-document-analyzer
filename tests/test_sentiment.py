"""
Unit Tests for Sentiment, Tone, and Assertiveness
"""

import unittest
from app.nlp.sentiment.sentiment_analyzer import SentimentAnalyzer

class TestSentiment(unittest.TestCase):
    def test_positive_text(self):
        text = "The vendor delivered outstanding performance with exceptional efficiency and profitable results."
        res = SentimentAnalyzer.analyze(text)
        self.assertGreater(res["polarity"], 0.2)

    def test_negative_risk_text(self):
        text = "Severe breach of agreement with fraudulent damages and default on debt liabilities."
        res = SentimentAnalyzer.analyze(text)
        self.assertLess(res["polarity"], -0.2)

    def test_assertive_legal_tone(self):
        text = "Receiving party shall strictly indemnify and hold harmless the disclosing party unconditionally."
        res = SentimentAnalyzer.analyze(text)
        self.assertIn("Assertive", res["tone"])

if __name__ == "__main__":
    unittest.main()
