"""Unit Tests for Text Error & Grammar Detector."""
import unittest
from app.inspection.text_error_detector import TextErrorDetector

class TestTextErrorDetector(unittest.TestCase):
    def test_detect_typos(self):
        text = "We have recieved the confidencial agrement untill tomorrow."
        issues = TextErrorDetector.detect_errors(text)
        typo_titles = [i["title"] for i in issues if i["category"] == "TEXT_ERROR"]
        self.assertIn("Spelling Error", typo_titles)

    def test_detect_subject_verb_agreement(self):
        text = "The company are responsible for all vendor liabilities."
        issues = TextErrorDetector.detect_errors(text)
        self.assertTrue(any("Subject-verb agreement" in i["explanation"] for i in issues))

    def test_detect_repeated_words(self):
        text = "This contract is for the the client benefit."
        issues = TextErrorDetector.detect_errors(text)
        self.assertTrue(any(i["title"] == "Repeated Word" for i in issues))

if __name__ == "__main__":
    unittest.main()
