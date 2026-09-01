"""DOCX Document Parser using pure Python OpenXML XML parsing."""
import zipfile
import io
import xml.etree.ElementTree as ET
from typing import Dict, Any, List

class DOCXParser:
    @classmethod
    def parse_bytes(cls, file_bytes: bytes) -> Dict[str, Any]:
        try:
            with zipfile.ZipFile(io.BytesIO(file_bytes)) as zf:
                xml_content = zf.read("word/document.xml")
                tree = ET.fromstring(xml_content)
                
                paragraphs = []
                tables = []
                
                # Extract Paragraphs
                for p in tree.iter("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p"):
                    texts = [t.text for t in p.iter("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t") if t.text]
                    if texts:
                        paragraphs.append("".join(texts).strip())

                # Extract Tables
                for tbl in tree.iter("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}tbl"):
                    tbl_rows = []
                    for tr in tbl.iter("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}tr"):
                        row = []
                        for tc in tr.iter("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}tc"):
                            cell_text = "".join([t.text for t in tc.iter("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t") if t.text])
                            row.append(cell_text.strip())
                        if row:
                            tbl_rows.append(row)
                    if tbl_rows:
                        headers = tbl_rows[0]
                        data_rows = tbl_rows[1:] if len(tbl_rows) > 1 else []
                        tables.append({"name": f"Table {len(tables)+1}", "headers": headers, "rows": data_rows})

                clean_text = "\n\n".join(paragraphs)
                words = clean_text.split()
                
                return {
                    "clean_text": clean_text,
                    "paragraphs": paragraphs,
                    "paragraph_count": len(paragraphs),
                    "word_count": len(words),
                    "char_count": len(clean_text),
                    "page_count": max(1, len(words) // 350),
                    "tables": tables
                }
        except Exception as e:
            return {"clean_text": f"DOCX Parse Error: {str(e)}", "paragraphs": [], "paragraph_count": 0, "word_count": 0, "page_count": 1, "error": str(e), "tables": []}
