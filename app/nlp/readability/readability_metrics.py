"""Readability Metrics."""
import re
from typing import Dict, Any
from app.nlp.tokenizers.sentence_tokenizer import SentenceTokenizer
from app.nlp.tokenizers.word_tokenizer import WordTokenizer

class ReadabilityMetrics:
    @classmethod
    def count_syllables(cls, word: str) -> int:
        w = word.lower()
        if len(w) <= 3: return 1
        w = re.sub(r'(?:[^laeiouy]|ed|es|e)$', '', w)
        w = re.sub(r'^y', '', w)
        s = len(re.findall(r'[aeiouy]{1,2}', w))
        return max(1, s)

    @classmethod
    def analyze(cls, text: str) -> Dict[str, Any]:
        sentences = SentenceTokenizer.tokenize(text)
        words = WordTokenizer.tokenize(text)
        ns = max(1, len(sentences))
        nw = max(1, len(words))
        syllables = [cls.count_syllables(w) for w in words]
        total_syl = sum(syllables)
        asl = nw / ns
        asw = total_syl / nw
        fre = 206.835 - (1.015 * asl) - (84.6 * asw)
        fre = max(0.0, min(100.0, fre))
        fk = max(1.0, (0.39 * asl) + (11.8 * asw) - 15.59)
        level = "Easy" if fre >= 70 else "Standard Commercial" if fre >= 50 else "Complex Legal / Academic"
        return {
            "flesch_reading_ease": round(fre, 2),
            "flesch_kincaid_grade": round(fk, 1),
            "reading_level": level,
            "avg_sentence_length": round(asl, 1)
        }
