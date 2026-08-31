"""NGram Tokenizer."""
from typing import List

class NGramTokenizer:
    @classmethod
    def generate_ngrams(cls, tokens: List[str], n: int = 2) -> List[str]:
        if len(tokens) < n: return []
        return [" ".join(tokens[i:i+n]) for i in range(len(tokens) - n + 1)]
