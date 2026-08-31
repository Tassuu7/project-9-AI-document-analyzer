"""Word Tokenizer."""
import re
from typing import List

class WordTokenizer:
    CONTRACTIONS = {
        "can't": "cannot", "won't": "will not", "n't": " not",
        "'re": " are", "'s": " is", "'d": " would",
        "'ll": " will", "'t": " not", "'ve": " have", "'m": " am"
    }

    @classmethod
    def expand_contractions(cls, text: str) -> str:
        expanded = text
        for k, v in cls.CONTRACTIONS.items():
            expanded = re.sub(k, v, expanded, flags=re.IGNORECASE)
        return expanded

    @classmethod
    def tokenize(cls, text: str, lower: bool = True, strip_punct: bool = True) -> List[str]:
        if not text: return []
        text = cls.expand_contractions(text)
        if lower: text = text.lower()
        if strip_punct:
            tokens = re.findall(r'[a-zA-Z0-9]+(?:[-_][a-zA-Z0-9]+)*', text)
        else:
            tokens = re.findall(r'\w+|[^\w\s]', text, re.UNICODE)
        return [t for t in tokens if t.strip()]
