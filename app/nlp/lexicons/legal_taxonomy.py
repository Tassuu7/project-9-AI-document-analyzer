"""Legal Taxonomy."""
from typing import Dict, List

LEGAL_CLAUSE_CATEGORIES: Dict[str, List[str]] = {
    "Indemnification": ["indemnify", "indemnification", "hold harmless", "defend and hold harmless"],
    "Limitation of Liability": ["limitation of liability", "consequential damages", "cap on liability"],
    "Confidentiality & Non-Disclosure": ["confidential information", "non-disclosure", "trade secrets"],
    "Intellectual Property & Assignment": ["intellectual property", "work made for hire", "assignment of inventions"],
    "Termination & Suspension": ["term and termination", "termination for cause", "termination for convenience"],
    "Force Majeure": ["force majeure", "acts of god", "natural disaster", "war or civil unrest"],
    "Governing Law & Jurisdiction": ["governing law", "jurisdiction", "exclusive jurisdiction", "laws of the state"],
    "Dispute Resolution & Arbitration": ["arbitration", "binding arbitration", "mediation", "waiver of jury trial"]
}
