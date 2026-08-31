"""
Unit Tests for Named Entity Recognition and PII Masker
"""

import unittest
from app.nlp.ner.entity_extractor import EntityExtractor
from app.nlp.ner.pii_masker import PIIMasker
from tests.test_fixtures import SAMPLE_BREACH_COMPLIANCE_TEXT

class TestNER(unittest.TestCase):
    def test_entity_extraction(self):
        text = "Contact Alice at alice@cybercorp.com or call 555-123-4567 regarding the $50,000 fee on October 14, 2026."
        entities = EntityExtractor.extract_entities(text)
        types = [e["type"] for e in entities]
        self.assertIn("EMAIL", types)
        self.assertIn("PHONE_NUMBER", types)
        self.assertIn("MONETARY_VALUE", types)
        self.assertIn("DATE", types)

    def test_pii_masking(self):
        text = "Confidential: John Doe email john@domain.com SSN 123-45-6789."
        masked = PIIMasker.mask_document(text, mode="tag")
        self.assertIn("[EMAIL_1]", masked["masked_text"])
        self.assertNotIn("john@domain.com", masked["masked_text"])

    def test_breach_entities(self):
        entities = EntityExtractor.extract_entities(SAMPLE_BREACH_COMPLIANCE_TEXT)
        self.assertTrue(len(entities) > 3)

if __name__ == "__main__":
    unittest.main()
