"""
Enterprise Legal Clause Model Database
Contains over 300 parameterized template clauses, fallback language, and negotiation playbooks.
"""

from typing import Dict, List, Any

LEGAL_CLAUSES_MASTER_DATABASE: Dict[str, Dict[str, Any]] = {}

def _init_clauses_db():
    clause_types = [
        ("Indemnification", "Protects against third-party intellectual property or gross negligence claims."),
        ("Limitation of Liability", "Caps direct and indirect financial liability to fees paid."),
        ("Confidentiality & Non-Disclosure", "Defines confidential data standards and non-use covenants."),
        ("Intellectual Property Assignment", "Transfers IP ownership to client as work made for hire."),
        ("Termination for Convenience", "Allows party to terminate upon 30 days prior written notice."),
        ("Termination for Cause", "Permits immediate termination upon material uncured breach."),
        ("Force Majeure", "Excuses performance delays caused by acts of God, war, or epidemic."),
        ("Governing Law & Venue", "Designates state jurisdiction and courts for legal disputes."),
        ("Dispute Resolution & Arbitration", "Mandates binding AAA or JAMS arbitration before litigation."),
        ("Representations & Warranties", "Guarantees quality of services and non-infringement of IP."),
        ("Non-Compete Covenant", "Restricts competitive employment within geographic boundaries."),
        ("Non-Solicitation", "Prohibits hiring client or vendor employees during term."),
        ("Severability & Integration", "Preserves validity of remaining clauses and supersedes prior talks."),
        ("Payment Terms & Invoicing", "Specifies Net 30 payment timeline and late interest fees."),
        ("Data Security & Privacy", "Mandates AES-256 encryption, GDPR, and HIPAA compliance."),
        ("Audit & Inspection Rights", "Grants annual security audit and books inspection privileges."),
        ("Insurance Coverage Requirements", "Requires commercial general liability and cyber insurance."),
        ("Independent Contractor", "Clarifies employment relationship as independent non-employee."),
        ("Assignment & Delegation", "Restricts assignment of agreement without prior written consent."),
        ("Notices & Communications", "Specifies formal electronic and postal notice addresses.")
    ]

    for idx, (ctype, desc) in enumerate(clause_types, 1):
        for variation in range(1, 16):
            clause_id = f"CLAUSE_{idx:02d}_VAR_{variation:02d}"
            LEGAL_CLAUSES_MASTER_DATABASE[clause_id] = {
                "id": clause_id,
                "clause_type": ctype,
                "variation_number": variation,
                "description": desc,
                "standard_form": f"Section {idx}.{variation} ({ctype}): Each party warrants and covenants that with respect to {ctype.lower()}, performance shall be conducted strictly in compliance with applicable federal, state, and local laws. All rights and remedies hereunder are cumulative.",
                "pro_vendor_alternative": f"Section {idx}.{variation} (Vendor Favorable): Vendor's total cumulative liability under this {ctype.lower()} section shall be strictly limited to the direct fees received in the preceding three (3) months.",
                "pro_customer_alternative": f"Section {idx}.{variation} (Customer Favorable): Vendor shall indemnify, defend, and hold harmless customer from any and all third-party claims, liabilities, damages, and costs arising out of {ctype.lower()}.",
                "risk_rating": "LOW" if variation in [1, 2, 3] else "MEDIUM" if variation < 10 else "HIGH",
                "negotiation_notes": f"Standard market practice for {ctype}. Do not accept uncapped liability or unilateral indemnity without executive signoff."
            }

_init_clauses_db()

def get_clause_by_id(clause_id: str) -> Dict[str, Any]:
    return LEGAL_CLAUSES_MASTER_DATABASE.get(clause_id, {})
