"""Rule-Based Sentence Segmenter and Disambiguator."""
import re
from typing import List

class SentenceTokenizer:
    ABBREVIATIONS = {
        "mr.", "mrs.", "ms.", "dr.", "prof.", "sr.", "jr.", "inc.", "corp.", "ltd.", "llc.",
        "co.", "vs.", "v.", "etc.", "e.g.", "i.e.", "cf.", "al.", "jan.", "feb.", "mar.",
        "apr.", "jun.", "jul.", "aug.", "sep.", "sept.", "oct.", "nov.", "dec.", "u.s.",
        "u.k.", "e.u.", "no.", "art.", "sec.", "para.", "cl.", "vol.", "pp.", "dept."
    }

    @classmethod
    def tokenize(cls, text: str) -> List[str]:
        if not text or not text.strip():
            return []
        
        protected = text
        for abbr in cls.ABBREVIATIONS:
            def _repl(match):
                return match.group(0).replace(".", "@@DOT@@")
            pattern = re.compile(re.escape(abbr), re.IGNORECASE)
            protected = pattern.sub(_repl, protected)

        protected = re.sub(r'(\d+)\.(\d+)', r'\1@@DOT@@\2', protected)
        raw_sentences = re.split(r'([.!?]+(?:\s+|\n+|$))', protected)
        
        sentences: List[str] = []
        current = ""
        for part in raw_sentences:
            if not part:
                continue
            current += part
            if re.search(r'[.!?]+(?:\s+|\n+|$)', part):
                restored = current.replace("@@DOT@@", ".").strip()
                if restored:
                    sentences.append(restored)
                current = ""
                
        if current.strip():
            restored = current.replace("@@DOT@@", ".").strip()
            if restored:
                sentences.append(restored)

        return [s for s in sentences if len(s) > 1]
