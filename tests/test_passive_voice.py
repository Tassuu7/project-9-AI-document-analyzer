"""Tests for Passive Voice Detection Engine."""
import unittest
from app.inspection.passive_voice_detector import PassiveVoiceDetector

class TestPassiveVoice(unittest.TestCase):
    def test_detect_passive_voice(self):
        text = "The report was conducted by the audit team. An investigation was initiated."
        findings = PassiveVoiceDetector.detect_passive_voice(text)
        self.assertGreaterEqual(len(findings), 1)
        cats = [f["category"] for f in findings]
        self.assertIn("PASSIVE_VOICE", cats)
