"""PDF Stream Parser."""
import re
import zlib
from typing import Dict, Any, List

class PDFParser:
    @classmethod
    def parse_bytes(cls, data: bytes) -> Dict[str, Any]:
        text_chunks: List[str] = []
        bt_blocks = re.findall(rb"BT\s*(.*?)\s*ET", data, re.DOTALL)
        for block in bt_blocks:
            strings = re.findall(rb"\((.*?)\)\s*Tj", block)
            for s in strings:
                try: text_chunks.append(s.decode("latin1", errors="ignore"))
                except Exception: pass

        stream_matches = re.finditer(rb"stream[\r\n]+(.*?)[\r\n]+endstream", data, re.DOTALL)
        for sm in stream_matches:
            stream_data = sm.group(1)
            try:
                decompressed = zlib.decompress(stream_data)
                d_strings = re.findall(rb"\((.*?)\)\s*Tj", decompressed)
                for ds in d_strings:
                    text_chunks.append(ds.decode("latin1", errors="ignore"))
            except Exception:
                pass

        full_extracted = " ".join(text_chunks).strip()
        if not full_extracted:
            ascii_strings = re.findall(rb"[A-Za-z0-9 ,.!?:;\-'\"]{4,}", data)
            full_extracted = " ".join([s.decode('latin1', errors='ignore') for s in ascii_strings])

        words = full_extracted.split()
        return {
            "clean_text": full_extracted,
            "word_count": len(words),
            "char_count": len(full_extracted)
        }
