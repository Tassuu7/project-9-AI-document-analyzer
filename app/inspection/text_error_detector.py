"""Text Error, Spelling, Grammar, and Formatting Quality Detector."""
import re
from typing import Dict, Any, List

class TextErrorDetector:
    COMMON_TYPOS = {
        "teh": "the", "recieved": "received", "seperate": "separate", "untill": "until",
        "occured": "occurred", "definately": "definitely", "accomodate": "accommodate",
        "goverment": "government", "priviledge": "privilege", "enviroment": "environment",
        "refering": "referring", "truely": "truly", "commited": "committed", "calender": "calendar",
        "maintainance": "maintenance", "possession": "possession", "liason": "liaison",
        "succesful": "successful", "neccessary": "necessary", "agrement": "agreement",
        "prodived": "provided", "responsbility": "responsibility", "confidencial": "confidential"
    }

    GRAMMAR_PATTERNS = [
        (r'\b(the company|the party|the client|the provider|each party|neither party)\s+(are|were|have)\b', 
         "Subject-verb agreement error: singular entity with plural verb.", 
         r'\1 is/was/has', "Grammar Error", "MEDIUM", 0.94),
        (r'\b(he|she|it)\s+(have|are|were)\b', 
         "Subject-verb agreement error.", 
         r'\1 has/is/was', "Grammar Error", "HIGH", 0.96),
        (r'\b(they|we|you)\s+(is|was|has)\b', 
         "Subject-verb agreement error: plural pronoun with singular verb.", 
         r'\1 are/were/have', "Grammar Error", "HIGH", 0.96),
        (r'\b(could|should|would|must)\s+of\b', 
         "Incorrect auxiliary verb usage: 'of' instead of 'have'.", 
         r'\1 have', "Grammar Error", "MEDIUM", 0.95),
        (r'\bbetween\s+you\s+and\s+I\b', 
         "Incorrect pronoun case in prepositional phrase: should be 'between you and me'.", 
         "between you and me", "Grammar Error", "LOW", 0.90)
    ]

    @classmethod
    def detect_errors(cls, text: str) -> List[Dict[str, Any]]:
        issues: List[Dict[str, Any]] = []
        if not text:
            return issues

        paragraphs = text.split("\n\n")
        sentences = re.split(r'(?<=[.!?])\s+', text)
        
        # 1. Spelling and Common Typos
        words = re.findall(r'\b[A-Za-z]+\b', text)
        for w in words:
            low_w = w.lower()
            if low_w in cls.COMMON_TYPOS:
                correction = cls.COMMON_TYPOS[low_w]
                if w[0].isupper():
                    correction = correction.capitalize()
                issues.append({
                    "category": "TEXT_ERROR",
                    "severity": "LOW",
                    "title": "Spelling Error",
                    "location": f"Word '{w}'",
                    "value": w,
                    "expected_value": correction,
                    "evidence": f"Found misspelled term '{w}' in document text.",
                    "explanation": f"The term '{w}' is misspelled.",
                    "impact": "Reduces document professionalism and readability.",
                    "recommendation": f"Replace '{w}' with '{correction}'.",
                    "confidence": 0.98,
                    "suggested_correction": correction
                })

        # 2. Grammar Rules
        for pattern, explanation, suggestion, title, severity, conf in cls.GRAMMAR_PATTERNS:
            for match in re.finditer(pattern, text, re.IGNORECASE):
                matched_text = match.group(0)
                issues.append({
                    "category": "TEXT_ERROR",
                    "severity": severity,
                    "title": title,
                    "location": f"Character position {match.start()}-{match.end()}",
                    "value": matched_text,
                    "expected_value": suggestion,
                    "evidence": f"'{matched_text}'",
                    "explanation": explanation,
                    "impact": "Grammatical inconsistency may introduce ambiguity in legal or commercial clauses.",
                    "recommendation": f"Change '{matched_text}' to follow grammatical agreement.",
                    "confidence": conf,
                    "suggested_correction": suggestion
                })

        # 3. Repeated Words (e.g. "the the", "in in")
        for match in re.finditer(r'\b([A-Za-z]+)\s+\1\b', text, re.IGNORECASE):
            word = match.group(1)
            if word.lower() not in ["that", "had"]:  # Allow valid repeated words
                issues.append({
                    "category": "TEXT_ERROR",
                    "severity": "LOW",
                    "title": "Repeated Word",
                    "location": f"Word sequence '{match.group(0)}'",
                    "value": match.group(0),
                    "expected_value": word,
                    "evidence": f"Found consecutive duplicate word: '{match.group(0)}'.",
                    "explanation": f"The word '{word}' is duplicated consecutively.",
                    "impact": "Formatting defect that harms clarity.",
                    "recommendation": f"Remove the redundant instance of '{word}'.",
                    "confidence": 0.99,
                    "suggested_correction": word
                })

        # 4. Duplicate Sentences
        seen_sentences = {}
        for s in sentences:
            clean_s = s.strip().lower()
            if len(clean_s) > 25:
                if clean_s in seen_sentences:
                    issues.append({
                        "category": "TEXT_ERROR",
                        "severity": "MEDIUM",
                        "title": "Duplicate Sentence",
                        "location": f"Sentence starting with '{s[:30]}...'",
                        "value": s[:60],
                        "expected_value": "Unique sentence",
                        "evidence": f"Sentence repeated: '{s[:80]}...'",
                        "explanation": "Identical sentence appears multiple times in the document.",
                        "impact": "Redundant text may indicate copy-paste errors or unintentional duplication.",
                        "recommendation": "Review and remove redundant sentence if unintentional.",
                        "confidence": 0.95,
                        "suggested_correction": ""
                    })
                else:
                    seen_sentences[clean_s] = s

        # 5. Punctuation & Formatting (e.g. Unmatched Quotes or Parentheses)
        double_quotes = text.count('"')
        if double_quotes % 2 != 0:
            issues.append({
                "category": "TEXT_ERROR",
                "severity": "LOW",
                "title": "Unmatched Quotation Marks",
                "location": "Global Document Text",
                "value": f"{double_quotes} quotation marks",
                "expected_value": "Even number of quotation marks",
                "evidence": f"Document contains an odd number ({double_quotes}) of double quotes.",
                "explanation": "A quotation was opened but not closed, or vice versa.",
                "impact": "May cause ambiguity regarding quoted clauses or definitions.",
                "recommendation": "Ensure all opened quotes are properly paired and closed.",
                "confidence": 0.92,
                "suggested_correction": ""
            })

        open_parens = text.count('(')
        close_parens = text.count(')')
        if open_parens != close_parens:
            issues.append({
                "category": "TEXT_ERROR",
                "severity": "LOW",
                "title": "Unmatched Parentheses",
                "location": "Global Document Text",
                "value": f"{open_parens} '(' vs {close_parens} ')'",
                "expected_value": "Equal number of opening and closing parentheses",
                "evidence": f"Found {open_parens} opening parentheses and {close_parens} closing parentheses.",
                "explanation": "Unbalanced parentheses detected in document structure.",
                "impact": "Formatting defect affecting visual clarity.",
                "recommendation": "Verify all parenthetical phrases are properly enclosed.",
                "confidence": 0.93,
                "suggested_correction": ""
            })

        # 6. Broken / Fragmented Lines & Double Spaces
        double_spaces = len(re.findall(r' {3,}', text))
        if double_spaces > 3:
            issues.append({
                "category": "TEXT_ERROR",
                "severity": "LOW",
                "title": "Irregular Whitespace & Spacing",
                "location": "Multiple positions",
                "value": f"{double_spaces} irregular whitespace blocks",
                "expected_value": "Single spacing between words",
                "evidence": f"Found {double_spaces} instances of consecutive multiple spaces.",
                "explanation": "Unusual whitespace sequences detected in text formatting.",
                "impact": "Inconsistent layout appearance.",
                "recommendation": "Normalize whitespace and spacing.",
                "confidence": 0.90,
                "suggested_correction": ""
            })

        return issues
