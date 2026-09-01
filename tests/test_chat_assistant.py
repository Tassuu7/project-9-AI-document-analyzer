"""Unit Tests for Document AI Assistant."""
import unittest
from app.inspection.chat_engine import ChatEngine

class TestChatEngine(unittest.TestCase):
    def test_grounded_answers(self):
        text = "This contract is valid for 12 months. Payment terms require 50 units at $20.00 each = $1,200.00."
        analysis_data = {
            "issues": [
                {
                    "category": "CALCULATION",
                    "severity": "HIGH",
                    "title": "Multiplication Calculation Error",
                    "value": "$1,200.00",
                    "expected_value": "$1,000.00",
                    "explanation": "Calculated total is $1,000.00",
                    "location": "Payment terms"
                }
            ]
        }
        res = ChatEngine.answer_question("Show calculation and financial errors", text, analysis_data)
        self.assertIn("$1,200.00", res["answer"])
        self.assertTrue(len(res["citations"]) > 0)

    def test_hallucination_prevention(self):
        text = "Simple company memo."
        analysis_data = {"issues": []}
        res = ChatEngine.answer_question("Who won the 1994 world cup?", text, analysis_data)
        self.assertIn("couldn't find enough information", res["answer"])

if __name__ == "__main__":
    unittest.main()
