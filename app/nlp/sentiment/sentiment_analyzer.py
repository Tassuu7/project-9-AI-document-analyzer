"""Sentiment Analyzer."""
from typing import Dict, Any
from app.nlp.tokenizers.word_tokenizer import WordTokenizer
from app.nlp.lexicons.sentiment_lexicon import (
    POSITIVE_POLARITY_LEXICON, NEGATIVE_POLARITY_LEXICON,
    URGENCY_LEXICON, HEDGING_LEXICON, LEGAL_ASSERTIVENESS_LEXICON
)

class SentimentAnalyzer:
    @classmethod
    def analyze(cls, text: str) -> Dict[str, Any]:
        tokens = WordTokenizer.tokenize(text.lower())
        pos, neg, urgency, hedging, assertive = 0.0, 0.0, 0.0, 0.0, 0.0
        for t in tokens:
            if t in POSITIVE_POLARITY_LEXICON: pos += POSITIVE_POLARITY_LEXICON[t]
            if t in NEGATIVE_POLARITY_LEXICON: neg += abs(NEGATIVE_POLARITY_LEXICON[t])
            if t in URGENCY_LEXICON: urgency += URGENCY_LEXICON[t]
            if t in HEDGING_LEXICON: hedging += HEDGING_LEXICON[t]
            if t in LEGAL_ASSERTIVENESS_LEXICON: assertive += LEGAL_ASSERTIVENESS_LEXICON[t]

        polarity = (pos - neg) / max(1.0, (pos + neg + 1.0))
        polarity = max(-1.0, min(1.0, polarity))

        if assertive >= 1.5 and assertive > (pos + neg) * 0.5:
            tone = "Strict / Highly Assertive"
        elif neg > pos * 1.5:
            tone = "Cautious / Defensive / Risk-Bearing"
        elif pos > neg * 1.5:
            tone = "Collaborative / Positive"
        elif hedging > 3.0:
            tone = "Tentative / Ambiguous"
        else:
            tone = "Formal / Neutral Commercial"

        return {
            "polarity": round(polarity, 4),
            "tone": tone,
            "assertiveness_score": round(assertive, 2),
            "urgency_score": round(urgency, 2)
        }
