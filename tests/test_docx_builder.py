"""Tests for Native Pure-Python OpenXML DOCX Document Builder."""
import unittest
import io
import zipfile
from app.builders.docx_builder import DocxBuilder

class TestDocxBuilder(unittest.TestCase):
    def test_text_to_docx_bytes(self):
        text = "# Sample Heading 1\n## Subheading 2\nThis is a regular paragraph with some analysis text.\n- Bullet item one\n- Bullet item two"
        docx_bytes = DocxBuilder.text_to_docx_bytes(text, title="Test Report")
        self.assertIsInstance(docx_bytes, bytes)
        self.assertGreater(len(docx_bytes), 500)

        # Verify it is a valid zip archive with standard Word XML files
        with zipfile.ZipFile(io.BytesIO(docx_bytes), "r") as z:
            names = z.namelist()
            self.assertIn("[Content_Types].xml", names)
            self.assertIn("_rels/.rels", names)
            self.assertIn("word/document.xml", names)
            self.assertIn("word/styles.xml", names)
            
            doc_xml = z.read("word/document.xml").decode("utf-8")
            self.assertIn("Test Report", doc_xml)
            self.assertIn("Sample Heading 1", doc_xml)
            self.assertIn("Bullet item one", doc_xml)

    def test_create_document_with_table(self):
        paragraphs = [
            {"type": "heading_1", "text": "Financial Summary"},
            {"type": "paragraph", "text": "Below is the itemized table:"},
            {"type": "table", "rows": [["Item", "Quantity", "Rate"], ["Widget A", "10", "$50.00"]]}
        ]
        b = DocxBuilder.create_document_bytes("Table Document", paragraphs)
        with zipfile.ZipFile(io.BytesIO(b), "r") as z:
            doc_xml = z.read("word/document.xml").decode("utf-8")
            self.assertIn("Widget A", doc_xml)
            self.assertIn("<w:tbl>", doc_xml)
