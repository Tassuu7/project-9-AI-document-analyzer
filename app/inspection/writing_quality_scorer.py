"""Comprehensive Writing Quality and Multi-Metric Readability Scorer."""
import re
import math
from typing import Dict, Any

class WritingQualityScorer:
    """Calculates comprehensive writing metrics, reading times, and multi-formula readability."""

    @classmethod
    def score_writing_quality(cls, text: str) -> Dict[str, Any]:
        words = re.findall(r'\b[a-zA-Z0-9_-]+\b', text)
        word_count = len(words)
        char_count = len(text)
        sentences = [s.strip() for s in re.split(r'(?<=[.?!])\s+', text) if s.strip()]
        sentence_count = max(1, len(sentences))
        paragraphs = [p.strip() for p in text.split("\n") if p.strip()]
        paragraph_count = max(1, len(paragraphs))
        headings = [h for h in paragraphs if h.startswith("#") or len(h.split()) < 8 and h.isupper()]
        heading_count = len(headings)

        if word_count == 0:
            return cls._empty_scorecard()

        # Syllables estimation
        syllable_count = sum(cls._count_syllables(w) for w in words)
        complex_word_count = sum(1 for w in words if cls._count_syllables(w) >= 3)

        # 1. Reading Time (Standard 200 words/min) & Speaking Time (130 words/min)
        reading_time_mins = round(word_count / 200.0, 1)
        speaking_time_mins = round(word_count / 130.0, 1)

        # 2. Readability Formulas
        # Flesch Reading Ease (0-100, higher = easier)
        asl = word_count / sentence_count
        asw = syllable_count / max(1, word_count)
        flesch_reading_ease = 206.835 - (1.015 * asl) - (84.6 * asw)
        flesch_reading_ease = max(0.0, min(100.0, round(flesch_reading_ease, 1)))

        # Flesch-Kincaid Grade Level
        fk_grade = (0.39 * asl) + (11.8 * asw) - 15.59
        fk_grade = max(1.0, round(fk_grade, 1))

        # Gunning Fog Index
        complex_pct = (complex_word_count / max(1, word_count)) * 100
        gunning_fog = 0.4 * (asl + complex_pct)
        gunning_fog = max(1.0, round(gunning_fog, 1))

        # Coleman-Liau Index
        letters = sum(len(w) for w in words)
        l_per_100 = (letters / max(1, word_count)) * 100
        s_per_100 = (sentence_count / max(1, word_count)) * 100
        coleman_liau = (0.0588 * l_per_100) - (0.296 * s_per_100) - 15.8
        coleman_liau = max(1.0, round(coleman_liau, 1))

        # SMOG Index
        smog = 1.0430 * math.sqrt(complex_word_count * (30.0 / max(1, sentence_count))) + 3.1291
        smog = max(1.0, round(smog, 1))

        # Vocabulary Richness (Type-Token Ratio)
        unique_words = len(set(w.lower() for w in words))
        ttr = round((unique_words / max(1, word_count)) * 100, 1)

        # Composite Writing Quality Score (0-100)
        # Combines Readability (30%), Sentence Balance (25%), Vocabulary Richness (25%), Paragraph Balance (20%)
        read_component = min(100, flesch_reading_ease)
        length_penalty = 0 if asl <= 20 else min(30, (asl - 20) * 2)
        vocab_component = min(100, ttr * 1.5)
        composite_score = round(0.35 * read_component + 0.35 * (100 - length_penalty) + 0.30 * vocab_component, 1)
        composite_score = max(35.0, min(99.0, composite_score))

        return {
            "word_count": word_count,
            "character_count": char_count,
            "sentence_count": sentence_count,
            "paragraph_count": paragraph_count,
            "heading_count": heading_count,
            "reading_time_minutes": reading_time_mins,
            "speaking_time_minutes": speaking_time_mins,
            "flesch_reading_ease": flesch_reading_ease,
            "flesch_kincaid_grade": fk_grade,
            "gunning_fog_index": gunning_fog,
            "coleman_liau_index": coleman_liau,
            "smog_index": smog,
            "vocabulary_richness_ttr": ttr,
            "average_sentence_length": round(asl, 1),
            "composite_writing_quality_score": composite_score,
            "readability_label": cls._get_readability_label(flesch_reading_ease)
        }

    @classmethod
    def _count_syllables(cls, word: str) -> int:
        w = word.lower()
        if len(w) <= 3:
            return 1
        w = re.sub(r'(?:[^laeiouy]|ed|es|e)$', '', w)
        w = re.sub(r'^y', '', w)
        syls = len(re.findall(r'[aeiouy]{1,2}', w))
        return max(1, syls)

    @classmethod
    def _get_readability_label(cls, score: float) -> str:
        if score >= 80:
            return "Easy to Read"
        elif score >= 60:
            return "Standard / Plain English"
        elif score >= 45:
            return "Fairly Difficult / Technical"
        else:
            return "Complex / Academic"

    @classmethod
    def _empty_scorecard(cls) -> Dict[str, Any]:
        return {
            "word_count": 0, "character_count": 0, "sentence_count": 0, "paragraph_count": 0,
            "heading_count": 0, "reading_time_minutes": 0.0, "speaking_time_minutes": 0.0,
            "flesch_reading_ease": 0.0, "flesch_kincaid_grade": 0.0, "gunning_fog_index": 0.0,
            "coleman_liau_index": 0.0, "smog_index": 0.0, "vocabulary_richness_ttr": 0.0,
            "average_sentence_length": 0.0, "composite_writing_quality_score": 0.0,
            "readability_label": "No Text"
        }
