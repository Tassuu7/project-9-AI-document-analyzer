"""Plain Text & Markdown Parser."""
import re
from typing import Dict, Any

class TextParser:
    @classmethod
    def parse(cls, content: str) -> Dict[str, Any]:
        normalized = content.replace("\r\n", "\n").replace("\r", "\n")
        clean_text = re.sub(r"^#+\s+", "", normalized, flags=re.MULTILINE)
        clean_text = re.sub(r"[*_]{1,3}(.*?)[*_]{1,3}", r"\1", clean_text)
        clean_text = re.sub(r"\[(.*?)\]\(.*?\)", r"\1", clean_text)
        paragraphs = [p.strip() for p in clean_text.split("\n\n") if p.strip()]
        lines = [line.strip() for line in clean_text.split("\n") if line.strip()]
        words = clean_text.split()
        return {
            "clean_text": clean_text,
            "paragraphs": paragraphs,
            "lines": lines,
            "word_count": len(words),
            "char_count": len(clean_text),
            "line_count": len(lines),
            "paragraph_count": len(paragraphs)
        }
