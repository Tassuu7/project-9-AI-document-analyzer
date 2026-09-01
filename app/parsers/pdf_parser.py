"""PDF Document Parser (Pure Python Structural Page & Stream Extractor)."""
import re
from typing import Dict, Any, List

class PDFParser:
    @classmethod
    def parse_bytes(cls, file_bytes: bytes) -> Dict[str, Any]:
        try:
            content = file_bytes.decode("latin-1", errors="ignore")
            
            # Extract plain text streams
            text_chunks = []
            stream_matches = re.findall(r'stream\r?\n(.*?)\r?\nendstream', content, re.DOTALL)
            for sm in stream_matches:
                # Extract text within parentheses
                strings = re.findall(r'\((.*?)\)\s*Tj', sm)
                if strings:
                    text_chunks.append(" ".join(strings))
                else:
                    strings_alt = re.findall(r'\((.*?)\)', sm)
                    clean_s = [s for s in strings_alt if len(s) > 2 and any(c.isalnum() for c in s)]
                    if clean_s:
                        text_chunks.append(" ".join(clean_s))

            if text_chunks:
                clean_text = "\n\n".join(text_chunks)
            else:
                # Fallback readable ASCII scanner
                readable = re.findall(r'[A-Za-z0-9\s.,!?:;\-/$#%@]{4,}', content)
                clean_text = " ".join([r.strip() for r in readable if len(r.strip()) > 3])

            paragraphs = [p.strip() for p in clean_text.split("\n\n") if len(p.strip()) > 5]
            words = clean_text.split()
            pages = max(1, len(re.findall(r'/Type\s*/Page\b', content))) or max(1, len(words) // 350)
            
            return {
                "clean_text": clean_text.strip(),
                "paragraphs": paragraphs,
                "paragraph_count": len(paragraphs),
                "word_count": len(words),
                "char_count": len(clean_text),
                "page_count": pages,
                "tables": []
            }
        except Exception as e:
            return {"clean_text": f"PDF Extraction Error: {str(e)}", "paragraphs": [], "paragraph_count": 0, "word_count": 0, "page_count": 1, "error": str(e), "tables": []}
