"""Tests for Multi-Mode Local Paraphrasing Engine."""
import unittest
from app.inspection.paraphrase_engine import ParaphraseEngine

class TestParaphraser(unittest.TestCase):
    def test_simple_mode(self):
        text = "In order to facilitate the project commencement, we utilize advanced methodologies."
        res = ParaphraseEngine.paraphrase_text(text, mode="simple")
        self.assertEqual(res["mode"], "simple")
        self.assertIn("to", res["paraphrased_text"])
        self.assertNotIn("In order to", res["paraphrased_text"])

    def test_professional_mode(self):
        text = "We want to do this work and get good results."
        res = ParaphraseEngine.paraphrase_text(text, mode="professional")
        self.assertEqual(res["mode"], "professional")
        self.assertIsInstance(res["paraphrased_text"], str)

    def test_concise_mode(self):
        text = "At the present time, it is basically true that each and every user is satisfied."
        res = ParaphraseEngine.paraphrase_text(text, mode="concise")
        self.assertEqual(res["mode"], "concise")
        # Should eliminate 'basically' and simplify 'each and every'
        self.assertNotIn("basically", res["paraphrased_text"].lower())

    def test_academic_mode(self):
        text = "I think a lot of people agree that this is good."
        res = ParaphraseEngine.paraphrase_text(text, mode="academic")
        self.assertEqual(res["mode"], "academic")
        self.assertIn("evidence suggests", res["paraphrased_text"].lower())
