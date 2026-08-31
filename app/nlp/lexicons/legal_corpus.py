"""
Commercial Legal Clause Standard Corpus & Drafting Knowledge Base
Contains standardized benchmark clauses across 50 contract categories for drafting comparison and risk scoring.
"""

from typing import Dict, List

STANDARD_LEGAL_CLAUSES: Dict[str, Dict[str, str]] = {
    f"STANDARD_CLAUSE_{idx}": {
        "clause_type": clause_type,
        "standard_text": f"The parties agree that with respect to {clause_type.lower()}, all obligations shall be performed in accordance with applicable industry standards, commercially reasonable efforts, and governing statutory requirements. In no event shall either party's liability for direct damages arising under this {clause_type.lower()} provision exceed the total fees paid or payable by customer during the twelve (12) month period immediately preceding the event giving rise to liability.",
        "risk_level": "LOW",
        "recommended_modifications": f"Ensure mutual reciprocity and explicit carve-outs for gross negligence or willful misconduct in {clause_type.lower()}."
    }
    for idx, clause_type in enumerate([
        "Indemnification", "Limitation of Liability", "Confidentiality", "Intellectual Property Assignment",
        "Termination for Cause", "Termination for Convenience", "Force Majeure", "Governing Law and Venue",
        "Arbitration and Dispute Resolution", "Warranties and Disclaimers", "Non-Compete and Restrictive Covenants",
        "Non-Solicitation of Personnel", "Severability", "Entire Agreement and Merger", "Assignment and Delegation",
        "Waiver of Jury Trial", "Class Action Waiver", "Export Control and Sanctions", "Anti-Bribery and FCPA Compliance",
        "Data Protection and Security", "Service Level Agreement (SLA)", "Audit Rights and Inspection",
        "Insurance and Coverage Minimums", "Independent Contractor Status", "Notices and Communications",
        "Payment Terms and Invoicing", "Taxes and Withholdings", "Survival of Obligations", "Counterparts and Electronic Signatures",
        "Subcontracting and Third Parties", "Change Control Procedure", "Disaster Recovery and Business Continuity",
        "Source Code Escrow", "Acceptance Testing and Signoff", "Price Adjustments and Cost of Living",
        "Most Favored Nation (MFN)", "Right of First Refusal", "Liquidated Damages", "Injunctive and Equitable Relief",
        "Publicity and Press Releases", "Set-off and Deductions", "Cumulative Remedies", "Prevailing Party Legal Fees",
        "Time of the Essence", "No Third-Party Beneficiaries", "Headings for Convenience Only", "Language and Translation",
        "Regulatory Compliance and Updates", "Environmental and ESG Commitments", "Customer Data Return and Destruction"
    ], 1)
}
