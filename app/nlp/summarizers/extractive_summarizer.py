"""Extractive Summarizer."""
from typing import Dict, Any, List
from app.nlp.tokenizers.sentence_tokenizer import SentenceTokenizer
from app.nlp.tokenizers.word_tokenizer import WordTokenizer
from app.nlp.lexicons.stopwords import get_all_stopwords

class ExtractiveSummarizer:
    @classmethod
    def summarize(cls, text: str, max_sentences: int = 5) -> Dict[str, Any]:
        sentences = SentenceTokenizer.tokenize(text)
        if len(sentences) <= max_sentences:
            return {"summary": " ".join(sentences), "sentence_count": len(sentences), "compression_ratio": 1.0}
        stopwords = get_all_stopwords()
        doc_tf = {}
        s_tokens = []
        for s in sentences:
            toks = [t for t in WordTokenizer.tokenize(s.lower()) if t not in stopwords and len(t) > 2]
            s_tokens.append(toks)
            for t in toks: doc_tf[t] = doc_tf.get(t, 0) + 1

        scores = []
        for idx, (s, toks) in enumerate(zip(sentences, s_tokens)):
            if not toks:
                scores.append(0.0)
                continue
            sc = sum(doc_tf.get(t, 1) for t in toks) / (len(toks) ** 0.5)
            if idx == 0 or idx == len(sentences) - 1: sc *= 1.3
            scores.append(sc)

        target = min(max_sentences, len(sentences))
        ranked_idx = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:target]
        selected = [sentences[i] for i in sorted(ranked_idx)]
        sum_text = " ".join(selected)
        return {
            "summary": sum_text,
            "sentence_count": len(selected),
            "compression_ratio": round(len(sum_text.split()) / max(1, len(text.split())), 3)
        }
