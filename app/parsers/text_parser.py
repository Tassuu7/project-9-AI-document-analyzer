"""Text & Markdown Document Parser."""
import re
from typing import Dict, Any, List

class TextParser:
    @classmethod
    def parse(cls, content: str) -> Dict[str, Any]:
        if not content:
            return {"clean_text": "", "paragraphs": [], "sections": [], "word_count": 0, "line_count": 0, "char_count": 0, "page_count": 1}
        
        lines = content.splitlines()
        clean_lines = [line.strip() for line in lines if line.strip()]
        paragraphs = [p.strip() for p in re.split(r'\n\s*\n+', content) if p.strip()]
        
        sections = []
        current_section = {"title": "Introduction", "content": []}
        for line in lines:
            if re.match(r'^(#{1,6}\s+|[0-9]+\.\s+|[A-Z\s]{4,}:)', line.strip()):
                if current_section["content"]:
                    sections.append({"title": current_section["title"], "content": "\n".join(current_section["content"])})
                current_section = {"title": line.strip(), "content": []}
            else:
                current_section["content"].append(line)
        if current_section["content"]:
            sections.append({"title": current_section["title"], "content": "\n".join(current_section["content"])})

        words = re.findall(r'[a-zA-Z0-9_-]+', content)
        pages = max(1, len(words) // 400 + (1 if len(words) % 400 > 0 else 0))

        return {
            "clean_text": content.strip(),
            "paragraphs": paragraphs,
            "paragraph_count": len(paragraphs),
            "sections": sections,
            "word_count": len(words),
            "line_count": len(lines),
            "char_count": len(content),
            "page_count": pages,
            "tables": []
        }
