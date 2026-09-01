"""Academic Phrase Bank and Scholarly Discourse Patterns."""
from typing import Dict, List

ACADEMIC_TRANSITIONS: Dict[str, List[str]] = {
    "addition": ["Furthermore", "Moreover", "In addition", "Additionally", "Concurrently"],
    "contrast": ["Conversely", "In contrast", "On the other hand", "Notwithstanding", "Nevertheless"],
    "causation": ["Consequently", "Accordingly", "As a consequence", "Hence", "Thereby"],
    "evidence": ["As evidenced by", "Empirical observations indicate", "Substantiated by", "As illustrated in"],
    "conclusion": ["In summary", "Consequently, it can be inferred that", "Synthesizing the evidence", "Ultimately"]
}

ACADEMIC_REWRITES: Dict[str, str] = {
    "i think": "the evidence suggests",
    "in my opinion": "it can be argued that",
    "a lot of": "a substantial volume of",
    "good": "favorable",
    "bad": "suboptimal",
    "big": "extensive",
    "shows": "demonstrates",
    "proves": "substantiates",
    "find out": "ascertain",
    "look at": "examine",
    "talk about": "discuss",
    "make sure": "ensure",
    "get rid of": "eliminate",
    "put together": "synthesize"
}
