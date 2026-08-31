"""Executive Summarizer."""
from typing import Dict, Any, List
from app.nlp.tokenizers.sentence_tokenizer import SentenceTokenizer

class ExecutiveSummarizer:
    @classmethod
    def generate_brief(cls, text: str) -> Dict[str, Any]:
        sentences = SentenceTokenizer.tokenize(text)
        obligations: List[str] = []
        risks: List[str] = []
        for s in sentences:
            sl = s.lower()
            if any(k in sl for k in ["shall", "must", "agrees to", "covenants"]):
                if len(obligations) < 4: obligations.append(s.strip())
            if any(k in sl for k in ["breach", "terminate", "liability", "damages", "indemnif"]):
                if len(risks) < 4: risks.append(s.strip())
        return {"key_obligations": obligations, "critical_risks": risks}
