"""DOCX OpenXML Parser."""
import zipfile
import io
import xml.etree.ElementTree as ET
from typing import Dict, Any, List

class DOCXParser:
    @classmethod
    def parse_bytes(cls, data: bytes) -> Dict[str, Any]:
        text_lines: List[str] = []
        try:
            with zipfile.ZipFile(io.BytesIO(data)) as z:
                if "word/document.xml" in z.namelist():
                    xml_content = z.read("word/document.xml")
                    root = ET.fromstring(xml_content)
                    ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
                    for p in root.iter("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p"):
                        texts = [node.text for node in p.iter("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t") if node.text]
                        if texts:
                            text_lines.append("".join(texts))
        except Exception:
            pass

        full_text = "\n".join(text_lines).strip()
        return {
            "clean_text": full_text,
            "word_count": len(full_text.split()),
            "char_count": len(full_text)
        }
