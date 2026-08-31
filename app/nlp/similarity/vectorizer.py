"""TF-IDF Vectorizer."""
import math
from typing import List, Dict
from app.nlp.tokenizers.word_tokenizer import WordTokenizer
from app.nlp.lexicons.stopwords import get_all_stopwords

class TFIDFVectorizer:
    def __init__(self):
        self.stopwords = get_all_stopwords()

    def fit_transform(self, docs: List[str]) -> List[Dict[str, float]]:
        doc_tokens = []
        df = {}
        for d in docs:
            toks = [t for t in WordTokenizer.tokenize(d.lower()) if t not in self.stopwords and len(t) > 2]
            doc_tokens.append(toks)
            for t in set(toks): df[t] = df.get(t, 0) + 1

        n_docs = len(docs)
        idf = {t: math.log(1.0 + (n_docs / (1.0 + freq))) + 1.0 for t, freq in df.items()}
        vectors = []
        for toks in doc_tokens:
            tf = {}
            for t in toks: tf[t] = tf.get(t, 0) + 1
            vec = {}
            for t, c in tf.items():
                if t in idf: vec[t] = (c / len(toks)) * idf[t]
            norm = math.sqrt(sum(v**2 for v in vec.values()))
            if norm > 0: vec = {t: v / norm for t, v in vec.items()}
            vectors.append(vec)
        return vectors

    @classmethod
    def cosine_similarity(cls, a: Dict[str, float], b: Dict[str, float]) -> float:
        common = set(a.keys()) & set(b.keys())
        if not common: return 0.0
        return sum(a[t] * b[t] for t in common)
