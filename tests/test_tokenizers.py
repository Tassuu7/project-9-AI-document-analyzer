"""
Unit Tests for Sentence, Word, and NGram Tokenizers
"""

import unittest
from app.nlp.tokenizers.sentence_tokenizer import SentenceTokenizer
from app.nlp.tokenizers.word_tokenizer import WordTokenizer
from app.nlp.tokenizers.ngram_tokenizer import NGramTokenizer

class TestTokenizers(unittest.TestCase):
    def test_sentence_tokenizer_abbreviations(self):
        text = "Dr. Smith and Mr. Jones went to Inc. Corp. on Jan. 15. The meeting was productive!"
        sentences = SentenceTokenizer.tokenize(text)
        self.assertEqual(len(sentences), 2)
        self.assertIn("Dr. Smith and Mr. Jones", sentences[0])

    def test_word_tokenizer_contractions(self):
        text = "They can't accept the terms and won't agree."
        tokens = WordTokenizer.tokenize(text)
        self.assertIn("cannot", tokens)
        self.assertIn("will", tokens)
        self.assertIn("not", tokens)

    def test_ngram_tokenizer(self):
        tokens = ["artificial", "intelligence", "document", "analyzer"]
        bigrams = NGramTokenizer.generate_ngrams(tokens, 2)
        self.assertEqual(len(bigrams), 3)
        self.assertEqual(bigrams[0], "artificial intelligence")

if __name__ == "__main__":
    unittest.main()
