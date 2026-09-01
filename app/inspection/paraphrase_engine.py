"""Multi-Mode Local Rule-Based Paraphrasing Engine (100% Offline)."""
import re
from typing import Dict, Any, List
from app.nlp.lexicons.synonym_database import get_synonym, SYNONYM_MAP
from app.nlp.lexicons.filler_words_database import FILLER_PHRASES, REDUNDANT_PAIRS, SINGLE_FILLER_WORDS
from app.nlp.lexicons.academic_phrases_database import ACADEMIC_REWRITES

class ParaphraseEngine:
    """Provides Simple, Professional, Academic, Formal, and Concise text rewriting."""

    MODES = ["simple", "professional", "academic", "formal", "concise"]

    @classmethod
    def paraphrase_text(cls, text: str, mode: str = "professional") -> Dict[str, Any]:
        mode = mode.lower()
        if mode not in cls.MODES:
            mode = "professional"

        paragraphs = text.split("\n")
        rewritten_paras = []
        transformations = []

        for p in paragraphs:
            if not p.strip():
                rewritten_paras.append("")
                continue
            
            p_out, p_trans = cls._paraphrase_paragraph(p, mode)
            rewritten_paras.append(p_out)
            transformations.extend(p_trans)

        full_rewritten = "\n".join(rewritten_paras)

        return {
            "original_text": text,
            "paraphrased_text": full_rewritten,
            "mode": mode,
            "transformations_count": len(transformations),
            "transformations": transformations[:30]
        }

    @classmethod
    def _paraphrase_paragraph(cls, paragraph: str, mode: str) -> (str, List[Dict[str, str]]):
        sentences = re.split(r'(?<=[.?!])\s+', paragraph)
        out_sentences = []
        trans_list = []

        for s in sentences:
            s_out, s_trans = cls._paraphrase_sentence(s, mode)
            out_sentences.append(s_out)
            trans_list.extend(s_trans)

        return " ".join(out_sentences), trans_list

    @classmethod
    def _paraphrase_sentence(cls, sentence: str, mode: str) -> (str, List[Dict[str, str]]):
        res = sentence
        transformations = []

        # 1. Apply multi-word filler/redundancy replacement (especially in Concise & Professional mode)
        if mode in ["concise", "professional", "simple"]:
            for ph, rep in FILLER_PHRASES.items():
                pattern = re.compile(re.escape(ph), re.IGNORECASE)
                if pattern.search(res):
                    res = pattern.sub(rep, res)
                    transformations.append({"type": "phrase_simplification", "original": ph, "replacement": rep})

            for rp, rep in REDUNDANT_PAIRS.items():
                pattern = re.compile(re.escape(rp), re.IGNORECASE)
                if pattern.search(res):
                    res = pattern.sub(rep, res)
                    transformations.append({"type": "tautology_removal", "original": rp, "replacement": rep})

            if mode == "concise":
                for sfw in SINGLE_FILLER_WORDS:
                    pattern = re.compile(r'\b' + re.escape(sfw) + r'\s+', re.IGNORECASE)
                    if pattern.search(res):
                        res = pattern.sub("", res)
                        transformations.append({"type": "filler_word_drop", "original": sfw, "replacement": ""})

        # 2. Academic specific rewrites
        if mode == "academic":
            for phrase, rep in ACADEMIC_REWRITES.items():
                pattern = re.compile(r'\b' + re.escape(phrase) + r'\b', re.IGNORECASE)
                if pattern.search(res):
                    res = pattern.sub(rep, res)
                    transformations.append({"type": "academic_formulation", "original": phrase, "replacement": rep})

        # 3. Formal mode eliminates contractions
        if mode in ["formal", "academic"]:
            contractions = {
                "can't": "cannot", "won't": "will not", "n't": " not",
                "'re": " are", "'ve": " have", "'ll": " will", "'d": " would"
            }
            for c, exp in contractions.items():
                pattern = re.compile(re.escape(c), re.IGNORECASE)
                if pattern.search(res):
                    res = pattern.sub(exp, res)
                    transformations.append({"type": "expansion", "original": c, "replacement": exp})

        # 4. Token-level synonym mapping for target mode
        words = re.findall(r'\b[a-zA-Z]+\b|[^a-zA-Z]+', res)
        new_words = []
        for token in words:
            if re.match(r'^[a-zA-Z]+$', token):
                syn = get_synonym(token, mode)
                if syn and syn.lower() != token.lower():
                    new_words.append(syn)
                    transformations.append({"type": "synonym_substitution", "original": token, "replacement": syn})
                else:
                    new_words.append(token)
            else:
                new_words.append(token)

        res = "".join(new_words)
        # Clean extra spaces
        res = re.sub(r'\s{2,}', ' ', res).strip()
        return res, transformations
