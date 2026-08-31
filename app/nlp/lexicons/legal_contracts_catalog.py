"""Commercial Legal Contract Clauses Master Database."""
from typing import Dict, Any

LEGAL_CLAUSES_BANK: Dict[str, Dict[str, Any]] = {
    "LEGAL_CLAUSE_01_V1": {
        "clause_type": "Indemnification",
        "variant": 1,
        "standard_clause_text": "Section 1.1 (Indemnification): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 1.1 (Vendor Version): Vendor liability with respect to indemnification shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 1.1 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of indemnification.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Indemnification. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_01_V2": {
        "clause_type": "Indemnification",
        "variant": 2,
        "standard_clause_text": "Section 1.2 (Indemnification): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 1.2 (Vendor Version): Vendor liability with respect to indemnification shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 1.2 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of indemnification.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Indemnification. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_01_V3": {
        "clause_type": "Indemnification",
        "variant": 3,
        "standard_clause_text": "Section 1.3 (Indemnification): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 1.3 (Vendor Version): Vendor liability with respect to indemnification shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 1.3 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of indemnification.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Indemnification. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_01_V4": {
        "clause_type": "Indemnification",
        "variant": 4,
        "standard_clause_text": "Section 1.4 (Indemnification): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 1.4 (Vendor Version): Vendor liability with respect to indemnification shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 1.4 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of indemnification.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Indemnification. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_01_V5": {
        "clause_type": "Indemnification",
        "variant": 5,
        "standard_clause_text": "Section 1.5 (Indemnification): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 1.5 (Vendor Version): Vendor liability with respect to indemnification shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 1.5 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of indemnification.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Indemnification. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_01_V6": {
        "clause_type": "Indemnification",
        "variant": 6,
        "standard_clause_text": "Section 1.6 (Indemnification): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 1.6 (Vendor Version): Vendor liability with respect to indemnification shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 1.6 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of indemnification.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Indemnification. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_01_V7": {
        "clause_type": "Indemnification",
        "variant": 7,
        "standard_clause_text": "Section 1.7 (Indemnification): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 1.7 (Vendor Version): Vendor liability with respect to indemnification shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 1.7 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of indemnification.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Indemnification. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_02_V1": {
        "clause_type": "Limitation of Liability",
        "variant": 1,
        "standard_clause_text": "Section 2.1 (Limitation of Liability): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 2.1 (Vendor Version): Vendor liability with respect to limitation of liability shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 2.1 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of limitation of liability.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Limitation of Liability. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_02_V2": {
        "clause_type": "Limitation of Liability",
        "variant": 2,
        "standard_clause_text": "Section 2.2 (Limitation of Liability): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 2.2 (Vendor Version): Vendor liability with respect to limitation of liability shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 2.2 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of limitation of liability.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Limitation of Liability. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_02_V3": {
        "clause_type": "Limitation of Liability",
        "variant": 3,
        "standard_clause_text": "Section 2.3 (Limitation of Liability): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 2.3 (Vendor Version): Vendor liability with respect to limitation of liability shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 2.3 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of limitation of liability.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Limitation of Liability. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_02_V4": {
        "clause_type": "Limitation of Liability",
        "variant": 4,
        "standard_clause_text": "Section 2.4 (Limitation of Liability): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 2.4 (Vendor Version): Vendor liability with respect to limitation of liability shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 2.4 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of limitation of liability.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Limitation of Liability. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_02_V5": {
        "clause_type": "Limitation of Liability",
        "variant": 5,
        "standard_clause_text": "Section 2.5 (Limitation of Liability): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 2.5 (Vendor Version): Vendor liability with respect to limitation of liability shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 2.5 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of limitation of liability.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Limitation of Liability. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_02_V6": {
        "clause_type": "Limitation of Liability",
        "variant": 6,
        "standard_clause_text": "Section 2.6 (Limitation of Liability): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 2.6 (Vendor Version): Vendor liability with respect to limitation of liability shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 2.6 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of limitation of liability.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Limitation of Liability. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_02_V7": {
        "clause_type": "Limitation of Liability",
        "variant": 7,
        "standard_clause_text": "Section 2.7 (Limitation of Liability): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 2.7 (Vendor Version): Vendor liability with respect to limitation of liability shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 2.7 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of limitation of liability.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Limitation of Liability. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_03_V1": {
        "clause_type": "Confidentiality",
        "variant": 1,
        "standard_clause_text": "Section 3.1 (Confidentiality): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 3.1 (Vendor Version): Vendor liability with respect to confidentiality shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 3.1 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of confidentiality.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Confidentiality. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_03_V2": {
        "clause_type": "Confidentiality",
        "variant": 2,
        "standard_clause_text": "Section 3.2 (Confidentiality): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 3.2 (Vendor Version): Vendor liability with respect to confidentiality shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 3.2 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of confidentiality.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Confidentiality. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_03_V3": {
        "clause_type": "Confidentiality",
        "variant": 3,
        "standard_clause_text": "Section 3.3 (Confidentiality): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 3.3 (Vendor Version): Vendor liability with respect to confidentiality shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 3.3 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of confidentiality.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Confidentiality. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_03_V4": {
        "clause_type": "Confidentiality",
        "variant": 4,
        "standard_clause_text": "Section 3.4 (Confidentiality): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 3.4 (Vendor Version): Vendor liability with respect to confidentiality shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 3.4 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of confidentiality.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Confidentiality. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_03_V5": {
        "clause_type": "Confidentiality",
        "variant": 5,
        "standard_clause_text": "Section 3.5 (Confidentiality): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 3.5 (Vendor Version): Vendor liability with respect to confidentiality shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 3.5 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of confidentiality.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Confidentiality. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_03_V6": {
        "clause_type": "Confidentiality",
        "variant": 6,
        "standard_clause_text": "Section 3.6 (Confidentiality): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 3.6 (Vendor Version): Vendor liability with respect to confidentiality shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 3.6 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of confidentiality.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Confidentiality. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_03_V7": {
        "clause_type": "Confidentiality",
        "variant": 7,
        "standard_clause_text": "Section 3.7 (Confidentiality): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 3.7 (Vendor Version): Vendor liability with respect to confidentiality shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 3.7 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of confidentiality.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Confidentiality. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_04_V1": {
        "clause_type": "Intellectual Property Assignment",
        "variant": 1,
        "standard_clause_text": "Section 4.1 (Intellectual Property Assignment): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 4.1 (Vendor Version): Vendor liability with respect to intellectual property assignment shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 4.1 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of intellectual property assignment.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Intellectual Property Assignment. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_04_V2": {
        "clause_type": "Intellectual Property Assignment",
        "variant": 2,
        "standard_clause_text": "Section 4.2 (Intellectual Property Assignment): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 4.2 (Vendor Version): Vendor liability with respect to intellectual property assignment shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 4.2 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of intellectual property assignment.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Intellectual Property Assignment. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_04_V3": {
        "clause_type": "Intellectual Property Assignment",
        "variant": 3,
        "standard_clause_text": "Section 4.3 (Intellectual Property Assignment): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 4.3 (Vendor Version): Vendor liability with respect to intellectual property assignment shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 4.3 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of intellectual property assignment.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Intellectual Property Assignment. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_04_V4": {
        "clause_type": "Intellectual Property Assignment",
        "variant": 4,
        "standard_clause_text": "Section 4.4 (Intellectual Property Assignment): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 4.4 (Vendor Version): Vendor liability with respect to intellectual property assignment shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 4.4 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of intellectual property assignment.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Intellectual Property Assignment. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_04_V5": {
        "clause_type": "Intellectual Property Assignment",
        "variant": 5,
        "standard_clause_text": "Section 4.5 (Intellectual Property Assignment): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 4.5 (Vendor Version): Vendor liability with respect to intellectual property assignment shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 4.5 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of intellectual property assignment.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Intellectual Property Assignment. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_04_V6": {
        "clause_type": "Intellectual Property Assignment",
        "variant": 6,
        "standard_clause_text": "Section 4.6 (Intellectual Property Assignment): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 4.6 (Vendor Version): Vendor liability with respect to intellectual property assignment shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 4.6 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of intellectual property assignment.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Intellectual Property Assignment. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_04_V7": {
        "clause_type": "Intellectual Property Assignment",
        "variant": 7,
        "standard_clause_text": "Section 4.7 (Intellectual Property Assignment): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 4.7 (Vendor Version): Vendor liability with respect to intellectual property assignment shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 4.7 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of intellectual property assignment.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Intellectual Property Assignment. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_05_V1": {
        "clause_type": "Termination for Cause",
        "variant": 1,
        "standard_clause_text": "Section 5.1 (Termination for Cause): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 5.1 (Vendor Version): Vendor liability with respect to termination for cause shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 5.1 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of termination for cause.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Termination for Cause. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_05_V2": {
        "clause_type": "Termination for Cause",
        "variant": 2,
        "standard_clause_text": "Section 5.2 (Termination for Cause): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 5.2 (Vendor Version): Vendor liability with respect to termination for cause shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 5.2 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of termination for cause.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Termination for Cause. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_05_V3": {
        "clause_type": "Termination for Cause",
        "variant": 3,
        "standard_clause_text": "Section 5.3 (Termination for Cause): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 5.3 (Vendor Version): Vendor liability with respect to termination for cause shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 5.3 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of termination for cause.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Termination for Cause. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_05_V4": {
        "clause_type": "Termination for Cause",
        "variant": 4,
        "standard_clause_text": "Section 5.4 (Termination for Cause): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 5.4 (Vendor Version): Vendor liability with respect to termination for cause shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 5.4 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of termination for cause.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Termination for Cause. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_05_V5": {
        "clause_type": "Termination for Cause",
        "variant": 5,
        "standard_clause_text": "Section 5.5 (Termination for Cause): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 5.5 (Vendor Version): Vendor liability with respect to termination for cause shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 5.5 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of termination for cause.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Termination for Cause. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_05_V6": {
        "clause_type": "Termination for Cause",
        "variant": 6,
        "standard_clause_text": "Section 5.6 (Termination for Cause): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 5.6 (Vendor Version): Vendor liability with respect to termination for cause shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 5.6 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of termination for cause.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Termination for Cause. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_05_V7": {
        "clause_type": "Termination for Cause",
        "variant": 7,
        "standard_clause_text": "Section 5.7 (Termination for Cause): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 5.7 (Vendor Version): Vendor liability with respect to termination for cause shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 5.7 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of termination for cause.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Termination for Cause. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_06_V1": {
        "clause_type": "Termination for Convenience",
        "variant": 1,
        "standard_clause_text": "Section 6.1 (Termination for Convenience): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 6.1 (Vendor Version): Vendor liability with respect to termination for convenience shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 6.1 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of termination for convenience.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Termination for Convenience. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_06_V2": {
        "clause_type": "Termination for Convenience",
        "variant": 2,
        "standard_clause_text": "Section 6.2 (Termination for Convenience): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 6.2 (Vendor Version): Vendor liability with respect to termination for convenience shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 6.2 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of termination for convenience.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Termination for Convenience. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_06_V3": {
        "clause_type": "Termination for Convenience",
        "variant": 3,
        "standard_clause_text": "Section 6.3 (Termination for Convenience): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 6.3 (Vendor Version): Vendor liability with respect to termination for convenience shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 6.3 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of termination for convenience.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Termination for Convenience. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_06_V4": {
        "clause_type": "Termination for Convenience",
        "variant": 4,
        "standard_clause_text": "Section 6.4 (Termination for Convenience): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 6.4 (Vendor Version): Vendor liability with respect to termination for convenience shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 6.4 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of termination for convenience.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Termination for Convenience. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_06_V5": {
        "clause_type": "Termination for Convenience",
        "variant": 5,
        "standard_clause_text": "Section 6.5 (Termination for Convenience): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 6.5 (Vendor Version): Vendor liability with respect to termination for convenience shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 6.5 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of termination for convenience.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Termination for Convenience. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_06_V6": {
        "clause_type": "Termination for Convenience",
        "variant": 6,
        "standard_clause_text": "Section 6.6 (Termination for Convenience): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 6.6 (Vendor Version): Vendor liability with respect to termination for convenience shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 6.6 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of termination for convenience.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Termination for Convenience. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_06_V7": {
        "clause_type": "Termination for Convenience",
        "variant": 7,
        "standard_clause_text": "Section 6.7 (Termination for Convenience): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 6.7 (Vendor Version): Vendor liability with respect to termination for convenience shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 6.7 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of termination for convenience.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Termination for Convenience. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_07_V1": {
        "clause_type": "Force Majeure",
        "variant": 1,
        "standard_clause_text": "Section 7.1 (Force Majeure): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 7.1 (Vendor Version): Vendor liability with respect to force majeure shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 7.1 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of force majeure.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Force Majeure. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_07_V2": {
        "clause_type": "Force Majeure",
        "variant": 2,
        "standard_clause_text": "Section 7.2 (Force Majeure): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 7.2 (Vendor Version): Vendor liability with respect to force majeure shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 7.2 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of force majeure.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Force Majeure. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_07_V3": {
        "clause_type": "Force Majeure",
        "variant": 3,
        "standard_clause_text": "Section 7.3 (Force Majeure): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 7.3 (Vendor Version): Vendor liability with respect to force majeure shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 7.3 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of force majeure.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Force Majeure. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_07_V4": {
        "clause_type": "Force Majeure",
        "variant": 4,
        "standard_clause_text": "Section 7.4 (Force Majeure): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 7.4 (Vendor Version): Vendor liability with respect to force majeure shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 7.4 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of force majeure.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Force Majeure. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_07_V5": {
        "clause_type": "Force Majeure",
        "variant": 5,
        "standard_clause_text": "Section 7.5 (Force Majeure): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 7.5 (Vendor Version): Vendor liability with respect to force majeure shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 7.5 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of force majeure.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Force Majeure. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_07_V6": {
        "clause_type": "Force Majeure",
        "variant": 6,
        "standard_clause_text": "Section 7.6 (Force Majeure): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 7.6 (Vendor Version): Vendor liability with respect to force majeure shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 7.6 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of force majeure.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Force Majeure. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_07_V7": {
        "clause_type": "Force Majeure",
        "variant": 7,
        "standard_clause_text": "Section 7.7 (Force Majeure): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 7.7 (Vendor Version): Vendor liability with respect to force majeure shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 7.7 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of force majeure.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Force Majeure. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_08_V1": {
        "clause_type": "Governing Law and Venue",
        "variant": 1,
        "standard_clause_text": "Section 8.1 (Governing Law and Venue): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 8.1 (Vendor Version): Vendor liability with respect to governing law and venue shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 8.1 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of governing law and venue.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Governing Law and Venue. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_08_V2": {
        "clause_type": "Governing Law and Venue",
        "variant": 2,
        "standard_clause_text": "Section 8.2 (Governing Law and Venue): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 8.2 (Vendor Version): Vendor liability with respect to governing law and venue shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 8.2 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of governing law and venue.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Governing Law and Venue. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_08_V3": {
        "clause_type": "Governing Law and Venue",
        "variant": 3,
        "standard_clause_text": "Section 8.3 (Governing Law and Venue): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 8.3 (Vendor Version): Vendor liability with respect to governing law and venue shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 8.3 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of governing law and venue.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Governing Law and Venue. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_08_V4": {
        "clause_type": "Governing Law and Venue",
        "variant": 4,
        "standard_clause_text": "Section 8.4 (Governing Law and Venue): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 8.4 (Vendor Version): Vendor liability with respect to governing law and venue shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 8.4 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of governing law and venue.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Governing Law and Venue. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_08_V5": {
        "clause_type": "Governing Law and Venue",
        "variant": 5,
        "standard_clause_text": "Section 8.5 (Governing Law and Venue): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 8.5 (Vendor Version): Vendor liability with respect to governing law and venue shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 8.5 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of governing law and venue.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Governing Law and Venue. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_08_V6": {
        "clause_type": "Governing Law and Venue",
        "variant": 6,
        "standard_clause_text": "Section 8.6 (Governing Law and Venue): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 8.6 (Vendor Version): Vendor liability with respect to governing law and venue shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 8.6 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of governing law and venue.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Governing Law and Venue. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_08_V7": {
        "clause_type": "Governing Law and Venue",
        "variant": 7,
        "standard_clause_text": "Section 8.7 (Governing Law and Venue): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 8.7 (Vendor Version): Vendor liability with respect to governing law and venue shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 8.7 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of governing law and venue.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Governing Law and Venue. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_09_V1": {
        "clause_type": "Arbitration and Dispute Resolution",
        "variant": 1,
        "standard_clause_text": "Section 9.1 (Arbitration and Dispute Resolution): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 9.1 (Vendor Version): Vendor liability with respect to arbitration and dispute resolution shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 9.1 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of arbitration and dispute resolution.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Arbitration and Dispute Resolution. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_09_V2": {
        "clause_type": "Arbitration and Dispute Resolution",
        "variant": 2,
        "standard_clause_text": "Section 9.2 (Arbitration and Dispute Resolution): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 9.2 (Vendor Version): Vendor liability with respect to arbitration and dispute resolution shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 9.2 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of arbitration and dispute resolution.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Arbitration and Dispute Resolution. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_09_V3": {
        "clause_type": "Arbitration and Dispute Resolution",
        "variant": 3,
        "standard_clause_text": "Section 9.3 (Arbitration and Dispute Resolution): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 9.3 (Vendor Version): Vendor liability with respect to arbitration and dispute resolution shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 9.3 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of arbitration and dispute resolution.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Arbitration and Dispute Resolution. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_09_V4": {
        "clause_type": "Arbitration and Dispute Resolution",
        "variant": 4,
        "standard_clause_text": "Section 9.4 (Arbitration and Dispute Resolution): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 9.4 (Vendor Version): Vendor liability with respect to arbitration and dispute resolution shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 9.4 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of arbitration and dispute resolution.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Arbitration and Dispute Resolution. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_09_V5": {
        "clause_type": "Arbitration and Dispute Resolution",
        "variant": 5,
        "standard_clause_text": "Section 9.5 (Arbitration and Dispute Resolution): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 9.5 (Vendor Version): Vendor liability with respect to arbitration and dispute resolution shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 9.5 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of arbitration and dispute resolution.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Arbitration and Dispute Resolution. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_09_V6": {
        "clause_type": "Arbitration and Dispute Resolution",
        "variant": 6,
        "standard_clause_text": "Section 9.6 (Arbitration and Dispute Resolution): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 9.6 (Vendor Version): Vendor liability with respect to arbitration and dispute resolution shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 9.6 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of arbitration and dispute resolution.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Arbitration and Dispute Resolution. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_09_V7": {
        "clause_type": "Arbitration and Dispute Resolution",
        "variant": 7,
        "standard_clause_text": "Section 9.7 (Arbitration and Dispute Resolution): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 9.7 (Vendor Version): Vendor liability with respect to arbitration and dispute resolution shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 9.7 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of arbitration and dispute resolution.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Arbitration and Dispute Resolution. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_10_V1": {
        "clause_type": "Warranties and Disclaimers",
        "variant": 1,
        "standard_clause_text": "Section 10.1 (Warranties and Disclaimers): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 10.1 (Vendor Version): Vendor liability with respect to warranties and disclaimers shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 10.1 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of warranties and disclaimers.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Warranties and Disclaimers. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_10_V2": {
        "clause_type": "Warranties and Disclaimers",
        "variant": 2,
        "standard_clause_text": "Section 10.2 (Warranties and Disclaimers): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 10.2 (Vendor Version): Vendor liability with respect to warranties and disclaimers shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 10.2 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of warranties and disclaimers.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Warranties and Disclaimers. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_10_V3": {
        "clause_type": "Warranties and Disclaimers",
        "variant": 3,
        "standard_clause_text": "Section 10.3 (Warranties and Disclaimers): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 10.3 (Vendor Version): Vendor liability with respect to warranties and disclaimers shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 10.3 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of warranties and disclaimers.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Warranties and Disclaimers. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_10_V4": {
        "clause_type": "Warranties and Disclaimers",
        "variant": 4,
        "standard_clause_text": "Section 10.4 (Warranties and Disclaimers): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 10.4 (Vendor Version): Vendor liability with respect to warranties and disclaimers shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 10.4 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of warranties and disclaimers.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Warranties and Disclaimers. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_10_V5": {
        "clause_type": "Warranties and Disclaimers",
        "variant": 5,
        "standard_clause_text": "Section 10.5 (Warranties and Disclaimers): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 10.5 (Vendor Version): Vendor liability with respect to warranties and disclaimers shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 10.5 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of warranties and disclaimers.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Warranties and Disclaimers. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_10_V6": {
        "clause_type": "Warranties and Disclaimers",
        "variant": 6,
        "standard_clause_text": "Section 10.6 (Warranties and Disclaimers): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 10.6 (Vendor Version): Vendor liability with respect to warranties and disclaimers shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 10.6 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of warranties and disclaimers.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Warranties and Disclaimers. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_10_V7": {
        "clause_type": "Warranties and Disclaimers",
        "variant": 7,
        "standard_clause_text": "Section 10.7 (Warranties and Disclaimers): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 10.7 (Vendor Version): Vendor liability with respect to warranties and disclaimers shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 10.7 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of warranties and disclaimers.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Warranties and Disclaimers. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_11_V1": {
        "clause_type": "Non-Compete and Restrictive Covenants",
        "variant": 1,
        "standard_clause_text": "Section 11.1 (Non-Compete and Restrictive Covenants): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 11.1 (Vendor Version): Vendor liability with respect to non-compete and restrictive covenants shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 11.1 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of non-compete and restrictive covenants.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Non-Compete and Restrictive Covenants. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_11_V2": {
        "clause_type": "Non-Compete and Restrictive Covenants",
        "variant": 2,
        "standard_clause_text": "Section 11.2 (Non-Compete and Restrictive Covenants): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 11.2 (Vendor Version): Vendor liability with respect to non-compete and restrictive covenants shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 11.2 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of non-compete and restrictive covenants.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Non-Compete and Restrictive Covenants. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_11_V3": {
        "clause_type": "Non-Compete and Restrictive Covenants",
        "variant": 3,
        "standard_clause_text": "Section 11.3 (Non-Compete and Restrictive Covenants): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 11.3 (Vendor Version): Vendor liability with respect to non-compete and restrictive covenants shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 11.3 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of non-compete and restrictive covenants.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Non-Compete and Restrictive Covenants. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_11_V4": {
        "clause_type": "Non-Compete and Restrictive Covenants",
        "variant": 4,
        "standard_clause_text": "Section 11.4 (Non-Compete and Restrictive Covenants): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 11.4 (Vendor Version): Vendor liability with respect to non-compete and restrictive covenants shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 11.4 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of non-compete and restrictive covenants.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Non-Compete and Restrictive Covenants. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_11_V5": {
        "clause_type": "Non-Compete and Restrictive Covenants",
        "variant": 5,
        "standard_clause_text": "Section 11.5 (Non-Compete and Restrictive Covenants): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 11.5 (Vendor Version): Vendor liability with respect to non-compete and restrictive covenants shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 11.5 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of non-compete and restrictive covenants.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Non-Compete and Restrictive Covenants. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_11_V6": {
        "clause_type": "Non-Compete and Restrictive Covenants",
        "variant": 6,
        "standard_clause_text": "Section 11.6 (Non-Compete and Restrictive Covenants): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 11.6 (Vendor Version): Vendor liability with respect to non-compete and restrictive covenants shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 11.6 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of non-compete and restrictive covenants.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Non-Compete and Restrictive Covenants. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_11_V7": {
        "clause_type": "Non-Compete and Restrictive Covenants",
        "variant": 7,
        "standard_clause_text": "Section 11.7 (Non-Compete and Restrictive Covenants): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 11.7 (Vendor Version): Vendor liability with respect to non-compete and restrictive covenants shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 11.7 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of non-compete and restrictive covenants.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Non-Compete and Restrictive Covenants. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_12_V1": {
        "clause_type": "Non-Solicitation of Personnel",
        "variant": 1,
        "standard_clause_text": "Section 12.1 (Non-Solicitation of Personnel): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 12.1 (Vendor Version): Vendor liability with respect to non-solicitation of personnel shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 12.1 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of non-solicitation of personnel.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Non-Solicitation of Personnel. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_12_V2": {
        "clause_type": "Non-Solicitation of Personnel",
        "variant": 2,
        "standard_clause_text": "Section 12.2 (Non-Solicitation of Personnel): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 12.2 (Vendor Version): Vendor liability with respect to non-solicitation of personnel shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 12.2 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of non-solicitation of personnel.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Non-Solicitation of Personnel. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_12_V3": {
        "clause_type": "Non-Solicitation of Personnel",
        "variant": 3,
        "standard_clause_text": "Section 12.3 (Non-Solicitation of Personnel): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 12.3 (Vendor Version): Vendor liability with respect to non-solicitation of personnel shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 12.3 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of non-solicitation of personnel.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Non-Solicitation of Personnel. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_12_V4": {
        "clause_type": "Non-Solicitation of Personnel",
        "variant": 4,
        "standard_clause_text": "Section 12.4 (Non-Solicitation of Personnel): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 12.4 (Vendor Version): Vendor liability with respect to non-solicitation of personnel shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 12.4 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of non-solicitation of personnel.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Non-Solicitation of Personnel. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_12_V5": {
        "clause_type": "Non-Solicitation of Personnel",
        "variant": 5,
        "standard_clause_text": "Section 12.5 (Non-Solicitation of Personnel): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 12.5 (Vendor Version): Vendor liability with respect to non-solicitation of personnel shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 12.5 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of non-solicitation of personnel.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Non-Solicitation of Personnel. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_12_V6": {
        "clause_type": "Non-Solicitation of Personnel",
        "variant": 6,
        "standard_clause_text": "Section 12.6 (Non-Solicitation of Personnel): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 12.6 (Vendor Version): Vendor liability with respect to non-solicitation of personnel shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 12.6 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of non-solicitation of personnel.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Non-Solicitation of Personnel. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_12_V7": {
        "clause_type": "Non-Solicitation of Personnel",
        "variant": 7,
        "standard_clause_text": "Section 12.7 (Non-Solicitation of Personnel): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 12.7 (Vendor Version): Vendor liability with respect to non-solicitation of personnel shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 12.7 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of non-solicitation of personnel.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Non-Solicitation of Personnel. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_13_V1": {
        "clause_type": "Severability",
        "variant": 1,
        "standard_clause_text": "Section 13.1 (Severability): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 13.1 (Vendor Version): Vendor liability with respect to severability shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 13.1 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of severability.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Severability. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_13_V2": {
        "clause_type": "Severability",
        "variant": 2,
        "standard_clause_text": "Section 13.2 (Severability): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 13.2 (Vendor Version): Vendor liability with respect to severability shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 13.2 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of severability.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Severability. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_13_V3": {
        "clause_type": "Severability",
        "variant": 3,
        "standard_clause_text": "Section 13.3 (Severability): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 13.3 (Vendor Version): Vendor liability with respect to severability shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 13.3 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of severability.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Severability. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_13_V4": {
        "clause_type": "Severability",
        "variant": 4,
        "standard_clause_text": "Section 13.4 (Severability): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 13.4 (Vendor Version): Vendor liability with respect to severability shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 13.4 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of severability.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Severability. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_13_V5": {
        "clause_type": "Severability",
        "variant": 5,
        "standard_clause_text": "Section 13.5 (Severability): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 13.5 (Vendor Version): Vendor liability with respect to severability shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 13.5 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of severability.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Severability. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_13_V6": {
        "clause_type": "Severability",
        "variant": 6,
        "standard_clause_text": "Section 13.6 (Severability): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 13.6 (Vendor Version): Vendor liability with respect to severability shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 13.6 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of severability.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Severability. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_13_V7": {
        "clause_type": "Severability",
        "variant": 7,
        "standard_clause_text": "Section 13.7 (Severability): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 13.7 (Vendor Version): Vendor liability with respect to severability shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 13.7 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of severability.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Severability. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_14_V1": {
        "clause_type": "Entire Agreement and Merger",
        "variant": 1,
        "standard_clause_text": "Section 14.1 (Entire Agreement and Merger): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 14.1 (Vendor Version): Vendor liability with respect to entire agreement and merger shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 14.1 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of entire agreement and merger.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Entire Agreement and Merger. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_14_V2": {
        "clause_type": "Entire Agreement and Merger",
        "variant": 2,
        "standard_clause_text": "Section 14.2 (Entire Agreement and Merger): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 14.2 (Vendor Version): Vendor liability with respect to entire agreement and merger shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 14.2 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of entire agreement and merger.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Entire Agreement and Merger. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_14_V3": {
        "clause_type": "Entire Agreement and Merger",
        "variant": 3,
        "standard_clause_text": "Section 14.3 (Entire Agreement and Merger): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 14.3 (Vendor Version): Vendor liability with respect to entire agreement and merger shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 14.3 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of entire agreement and merger.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Entire Agreement and Merger. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_14_V4": {
        "clause_type": "Entire Agreement and Merger",
        "variant": 4,
        "standard_clause_text": "Section 14.4 (Entire Agreement and Merger): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 14.4 (Vendor Version): Vendor liability with respect to entire agreement and merger shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 14.4 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of entire agreement and merger.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Entire Agreement and Merger. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_14_V5": {
        "clause_type": "Entire Agreement and Merger",
        "variant": 5,
        "standard_clause_text": "Section 14.5 (Entire Agreement and Merger): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 14.5 (Vendor Version): Vendor liability with respect to entire agreement and merger shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 14.5 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of entire agreement and merger.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Entire Agreement and Merger. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_14_V6": {
        "clause_type": "Entire Agreement and Merger",
        "variant": 6,
        "standard_clause_text": "Section 14.6 (Entire Agreement and Merger): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 14.6 (Vendor Version): Vendor liability with respect to entire agreement and merger shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 14.6 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of entire agreement and merger.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Entire Agreement and Merger. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_14_V7": {
        "clause_type": "Entire Agreement and Merger",
        "variant": 7,
        "standard_clause_text": "Section 14.7 (Entire Agreement and Merger): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 14.7 (Vendor Version): Vendor liability with respect to entire agreement and merger shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 14.7 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of entire agreement and merger.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Entire Agreement and Merger. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_15_V1": {
        "clause_type": "Assignment and Delegation",
        "variant": 1,
        "standard_clause_text": "Section 15.1 (Assignment and Delegation): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 15.1 (Vendor Version): Vendor liability with respect to assignment and delegation shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 15.1 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of assignment and delegation.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Assignment and Delegation. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_15_V2": {
        "clause_type": "Assignment and Delegation",
        "variant": 2,
        "standard_clause_text": "Section 15.2 (Assignment and Delegation): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 15.2 (Vendor Version): Vendor liability with respect to assignment and delegation shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 15.2 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of assignment and delegation.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Assignment and Delegation. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_15_V3": {
        "clause_type": "Assignment and Delegation",
        "variant": 3,
        "standard_clause_text": "Section 15.3 (Assignment and Delegation): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 15.3 (Vendor Version): Vendor liability with respect to assignment and delegation shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 15.3 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of assignment and delegation.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Assignment and Delegation. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_15_V4": {
        "clause_type": "Assignment and Delegation",
        "variant": 4,
        "standard_clause_text": "Section 15.4 (Assignment and Delegation): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 15.4 (Vendor Version): Vendor liability with respect to assignment and delegation shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 15.4 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of assignment and delegation.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Assignment and Delegation. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_15_V5": {
        "clause_type": "Assignment and Delegation",
        "variant": 5,
        "standard_clause_text": "Section 15.5 (Assignment and Delegation): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 15.5 (Vendor Version): Vendor liability with respect to assignment and delegation shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 15.5 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of assignment and delegation.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Assignment and Delegation. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_15_V6": {
        "clause_type": "Assignment and Delegation",
        "variant": 6,
        "standard_clause_text": "Section 15.6 (Assignment and Delegation): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 15.6 (Vendor Version): Vendor liability with respect to assignment and delegation shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 15.6 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of assignment and delegation.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Assignment and Delegation. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_15_V7": {
        "clause_type": "Assignment and Delegation",
        "variant": 7,
        "standard_clause_text": "Section 15.7 (Assignment and Delegation): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 15.7 (Vendor Version): Vendor liability with respect to assignment and delegation shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 15.7 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of assignment and delegation.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Assignment and Delegation. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_16_V1": {
        "clause_type": "Waiver of Jury Trial",
        "variant": 1,
        "standard_clause_text": "Section 16.1 (Waiver of Jury Trial): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 16.1 (Vendor Version): Vendor liability with respect to waiver of jury trial shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 16.1 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of waiver of jury trial.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Waiver of Jury Trial. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_16_V2": {
        "clause_type": "Waiver of Jury Trial",
        "variant": 2,
        "standard_clause_text": "Section 16.2 (Waiver of Jury Trial): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 16.2 (Vendor Version): Vendor liability with respect to waiver of jury trial shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 16.2 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of waiver of jury trial.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Waiver of Jury Trial. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_16_V3": {
        "clause_type": "Waiver of Jury Trial",
        "variant": 3,
        "standard_clause_text": "Section 16.3 (Waiver of Jury Trial): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 16.3 (Vendor Version): Vendor liability with respect to waiver of jury trial shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 16.3 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of waiver of jury trial.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Waiver of Jury Trial. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_16_V4": {
        "clause_type": "Waiver of Jury Trial",
        "variant": 4,
        "standard_clause_text": "Section 16.4 (Waiver of Jury Trial): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 16.4 (Vendor Version): Vendor liability with respect to waiver of jury trial shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 16.4 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of waiver of jury trial.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Waiver of Jury Trial. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_16_V5": {
        "clause_type": "Waiver of Jury Trial",
        "variant": 5,
        "standard_clause_text": "Section 16.5 (Waiver of Jury Trial): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 16.5 (Vendor Version): Vendor liability with respect to waiver of jury trial shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 16.5 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of waiver of jury trial.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Waiver of Jury Trial. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_16_V6": {
        "clause_type": "Waiver of Jury Trial",
        "variant": 6,
        "standard_clause_text": "Section 16.6 (Waiver of Jury Trial): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 16.6 (Vendor Version): Vendor liability with respect to waiver of jury trial shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 16.6 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of waiver of jury trial.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Waiver of Jury Trial. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_16_V7": {
        "clause_type": "Waiver of Jury Trial",
        "variant": 7,
        "standard_clause_text": "Section 16.7 (Waiver of Jury Trial): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 16.7 (Vendor Version): Vendor liability with respect to waiver of jury trial shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 16.7 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of waiver of jury trial.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Waiver of Jury Trial. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_17_V1": {
        "clause_type": "Class Action Waiver",
        "variant": 1,
        "standard_clause_text": "Section 17.1 (Class Action Waiver): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 17.1 (Vendor Version): Vendor liability with respect to class action waiver shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 17.1 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of class action waiver.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Class Action Waiver. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_17_V2": {
        "clause_type": "Class Action Waiver",
        "variant": 2,
        "standard_clause_text": "Section 17.2 (Class Action Waiver): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 17.2 (Vendor Version): Vendor liability with respect to class action waiver shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 17.2 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of class action waiver.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Class Action Waiver. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_17_V3": {
        "clause_type": "Class Action Waiver",
        "variant": 3,
        "standard_clause_text": "Section 17.3 (Class Action Waiver): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 17.3 (Vendor Version): Vendor liability with respect to class action waiver shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 17.3 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of class action waiver.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Class Action Waiver. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_17_V4": {
        "clause_type": "Class Action Waiver",
        "variant": 4,
        "standard_clause_text": "Section 17.4 (Class Action Waiver): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 17.4 (Vendor Version): Vendor liability with respect to class action waiver shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 17.4 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of class action waiver.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Class Action Waiver. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_17_V5": {
        "clause_type": "Class Action Waiver",
        "variant": 5,
        "standard_clause_text": "Section 17.5 (Class Action Waiver): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 17.5 (Vendor Version): Vendor liability with respect to class action waiver shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 17.5 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of class action waiver.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Class Action Waiver. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_17_V6": {
        "clause_type": "Class Action Waiver",
        "variant": 6,
        "standard_clause_text": "Section 17.6 (Class Action Waiver): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 17.6 (Vendor Version): Vendor liability with respect to class action waiver shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 17.6 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of class action waiver.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Class Action Waiver. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_17_V7": {
        "clause_type": "Class Action Waiver",
        "variant": 7,
        "standard_clause_text": "Section 17.7 (Class Action Waiver): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 17.7 (Vendor Version): Vendor liability with respect to class action waiver shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 17.7 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of class action waiver.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Class Action Waiver. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_18_V1": {
        "clause_type": "Export Control and Sanctions",
        "variant": 1,
        "standard_clause_text": "Section 18.1 (Export Control and Sanctions): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 18.1 (Vendor Version): Vendor liability with respect to export control and sanctions shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 18.1 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of export control and sanctions.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Export Control and Sanctions. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_18_V2": {
        "clause_type": "Export Control and Sanctions",
        "variant": 2,
        "standard_clause_text": "Section 18.2 (Export Control and Sanctions): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 18.2 (Vendor Version): Vendor liability with respect to export control and sanctions shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 18.2 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of export control and sanctions.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Export Control and Sanctions. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_18_V3": {
        "clause_type": "Export Control and Sanctions",
        "variant": 3,
        "standard_clause_text": "Section 18.3 (Export Control and Sanctions): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 18.3 (Vendor Version): Vendor liability with respect to export control and sanctions shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 18.3 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of export control and sanctions.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Export Control and Sanctions. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_18_V4": {
        "clause_type": "Export Control and Sanctions",
        "variant": 4,
        "standard_clause_text": "Section 18.4 (Export Control and Sanctions): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 18.4 (Vendor Version): Vendor liability with respect to export control and sanctions shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 18.4 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of export control and sanctions.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Export Control and Sanctions. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_18_V5": {
        "clause_type": "Export Control and Sanctions",
        "variant": 5,
        "standard_clause_text": "Section 18.5 (Export Control and Sanctions): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 18.5 (Vendor Version): Vendor liability with respect to export control and sanctions shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 18.5 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of export control and sanctions.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Export Control and Sanctions. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_18_V6": {
        "clause_type": "Export Control and Sanctions",
        "variant": 6,
        "standard_clause_text": "Section 18.6 (Export Control and Sanctions): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 18.6 (Vendor Version): Vendor liability with respect to export control and sanctions shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 18.6 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of export control and sanctions.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Export Control and Sanctions. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_18_V7": {
        "clause_type": "Export Control and Sanctions",
        "variant": 7,
        "standard_clause_text": "Section 18.7 (Export Control and Sanctions): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 18.7 (Vendor Version): Vendor liability with respect to export control and sanctions shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 18.7 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of export control and sanctions.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Export Control and Sanctions. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_19_V1": {
        "clause_type": "Anti-Bribery and FCPA Compliance",
        "variant": 1,
        "standard_clause_text": "Section 19.1 (Anti-Bribery and FCPA Compliance): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 19.1 (Vendor Version): Vendor liability with respect to anti-bribery and fcpa compliance shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 19.1 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of anti-bribery and fcpa compliance.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Anti-Bribery and FCPA Compliance. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_19_V2": {
        "clause_type": "Anti-Bribery and FCPA Compliance",
        "variant": 2,
        "standard_clause_text": "Section 19.2 (Anti-Bribery and FCPA Compliance): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 19.2 (Vendor Version): Vendor liability with respect to anti-bribery and fcpa compliance shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 19.2 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of anti-bribery and fcpa compliance.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Anti-Bribery and FCPA Compliance. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_19_V3": {
        "clause_type": "Anti-Bribery and FCPA Compliance",
        "variant": 3,
        "standard_clause_text": "Section 19.3 (Anti-Bribery and FCPA Compliance): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 19.3 (Vendor Version): Vendor liability with respect to anti-bribery and fcpa compliance shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 19.3 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of anti-bribery and fcpa compliance.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Anti-Bribery and FCPA Compliance. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_19_V4": {
        "clause_type": "Anti-Bribery and FCPA Compliance",
        "variant": 4,
        "standard_clause_text": "Section 19.4 (Anti-Bribery and FCPA Compliance): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 19.4 (Vendor Version): Vendor liability with respect to anti-bribery and fcpa compliance shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 19.4 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of anti-bribery and fcpa compliance.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Anti-Bribery and FCPA Compliance. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_19_V5": {
        "clause_type": "Anti-Bribery and FCPA Compliance",
        "variant": 5,
        "standard_clause_text": "Section 19.5 (Anti-Bribery and FCPA Compliance): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 19.5 (Vendor Version): Vendor liability with respect to anti-bribery and fcpa compliance shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 19.5 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of anti-bribery and fcpa compliance.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Anti-Bribery and FCPA Compliance. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_19_V6": {
        "clause_type": "Anti-Bribery and FCPA Compliance",
        "variant": 6,
        "standard_clause_text": "Section 19.6 (Anti-Bribery and FCPA Compliance): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 19.6 (Vendor Version): Vendor liability with respect to anti-bribery and fcpa compliance shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 19.6 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of anti-bribery and fcpa compliance.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Anti-Bribery and FCPA Compliance. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_19_V7": {
        "clause_type": "Anti-Bribery and FCPA Compliance",
        "variant": 7,
        "standard_clause_text": "Section 19.7 (Anti-Bribery and FCPA Compliance): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 19.7 (Vendor Version): Vendor liability with respect to anti-bribery and fcpa compliance shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 19.7 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of anti-bribery and fcpa compliance.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Anti-Bribery and FCPA Compliance. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_20_V1": {
        "clause_type": "Data Protection and Security",
        "variant": 1,
        "standard_clause_text": "Section 20.1 (Data Protection and Security): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 20.1 (Vendor Version): Vendor liability with respect to data protection and security shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 20.1 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of data protection and security.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Data Protection and Security. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_20_V2": {
        "clause_type": "Data Protection and Security",
        "variant": 2,
        "standard_clause_text": "Section 20.2 (Data Protection and Security): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 20.2 (Vendor Version): Vendor liability with respect to data protection and security shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 20.2 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of data protection and security.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Data Protection and Security. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_20_V3": {
        "clause_type": "Data Protection and Security",
        "variant": 3,
        "standard_clause_text": "Section 20.3 (Data Protection and Security): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 20.3 (Vendor Version): Vendor liability with respect to data protection and security shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 20.3 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of data protection and security.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Data Protection and Security. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_20_V4": {
        "clause_type": "Data Protection and Security",
        "variant": 4,
        "standard_clause_text": "Section 20.4 (Data Protection and Security): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 20.4 (Vendor Version): Vendor liability with respect to data protection and security shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 20.4 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of data protection and security.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Data Protection and Security. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_20_V5": {
        "clause_type": "Data Protection and Security",
        "variant": 5,
        "standard_clause_text": "Section 20.5 (Data Protection and Security): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 20.5 (Vendor Version): Vendor liability with respect to data protection and security shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 20.5 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of data protection and security.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Data Protection and Security. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_20_V6": {
        "clause_type": "Data Protection and Security",
        "variant": 6,
        "standard_clause_text": "Section 20.6 (Data Protection and Security): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 20.6 (Vendor Version): Vendor liability with respect to data protection and security shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 20.6 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of data protection and security.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Data Protection and Security. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_20_V7": {
        "clause_type": "Data Protection and Security",
        "variant": 7,
        "standard_clause_text": "Section 20.7 (Data Protection and Security): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 20.7 (Vendor Version): Vendor liability with respect to data protection and security shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 20.7 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of data protection and security.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Data Protection and Security. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_21_V1": {
        "clause_type": "Service Level Agreement (SLA)",
        "variant": 1,
        "standard_clause_text": "Section 21.1 (Service Level Agreement (SLA)): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 21.1 (Vendor Version): Vendor liability with respect to service level agreement (sla) shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 21.1 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of service level agreement (sla).",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Service Level Agreement (SLA). Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_21_V2": {
        "clause_type": "Service Level Agreement (SLA)",
        "variant": 2,
        "standard_clause_text": "Section 21.2 (Service Level Agreement (SLA)): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 21.2 (Vendor Version): Vendor liability with respect to service level agreement (sla) shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 21.2 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of service level agreement (sla).",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Service Level Agreement (SLA). Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_21_V3": {
        "clause_type": "Service Level Agreement (SLA)",
        "variant": 3,
        "standard_clause_text": "Section 21.3 (Service Level Agreement (SLA)): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 21.3 (Vendor Version): Vendor liability with respect to service level agreement (sla) shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 21.3 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of service level agreement (sla).",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Service Level Agreement (SLA). Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_21_V4": {
        "clause_type": "Service Level Agreement (SLA)",
        "variant": 4,
        "standard_clause_text": "Section 21.4 (Service Level Agreement (SLA)): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 21.4 (Vendor Version): Vendor liability with respect to service level agreement (sla) shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 21.4 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of service level agreement (sla).",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Service Level Agreement (SLA). Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_21_V5": {
        "clause_type": "Service Level Agreement (SLA)",
        "variant": 5,
        "standard_clause_text": "Section 21.5 (Service Level Agreement (SLA)): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 21.5 (Vendor Version): Vendor liability with respect to service level agreement (sla) shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 21.5 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of service level agreement (sla).",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Service Level Agreement (SLA). Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_21_V6": {
        "clause_type": "Service Level Agreement (SLA)",
        "variant": 6,
        "standard_clause_text": "Section 21.6 (Service Level Agreement (SLA)): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 21.6 (Vendor Version): Vendor liability with respect to service level agreement (sla) shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 21.6 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of service level agreement (sla).",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Service Level Agreement (SLA). Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_21_V7": {
        "clause_type": "Service Level Agreement (SLA)",
        "variant": 7,
        "standard_clause_text": "Section 21.7 (Service Level Agreement (SLA)): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 21.7 (Vendor Version): Vendor liability with respect to service level agreement (sla) shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 21.7 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of service level agreement (sla).",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Service Level Agreement (SLA). Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_22_V1": {
        "clause_type": "Audit Rights and Inspection",
        "variant": 1,
        "standard_clause_text": "Section 22.1 (Audit Rights and Inspection): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 22.1 (Vendor Version): Vendor liability with respect to audit rights and inspection shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 22.1 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of audit rights and inspection.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Audit Rights and Inspection. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_22_V2": {
        "clause_type": "Audit Rights and Inspection",
        "variant": 2,
        "standard_clause_text": "Section 22.2 (Audit Rights and Inspection): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 22.2 (Vendor Version): Vendor liability with respect to audit rights and inspection shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 22.2 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of audit rights and inspection.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Audit Rights and Inspection. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_22_V3": {
        "clause_type": "Audit Rights and Inspection",
        "variant": 3,
        "standard_clause_text": "Section 22.3 (Audit Rights and Inspection): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 22.3 (Vendor Version): Vendor liability with respect to audit rights and inspection shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 22.3 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of audit rights and inspection.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Audit Rights and Inspection. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_22_V4": {
        "clause_type": "Audit Rights and Inspection",
        "variant": 4,
        "standard_clause_text": "Section 22.4 (Audit Rights and Inspection): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 22.4 (Vendor Version): Vendor liability with respect to audit rights and inspection shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 22.4 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of audit rights and inspection.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Audit Rights and Inspection. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_22_V5": {
        "clause_type": "Audit Rights and Inspection",
        "variant": 5,
        "standard_clause_text": "Section 22.5 (Audit Rights and Inspection): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 22.5 (Vendor Version): Vendor liability with respect to audit rights and inspection shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 22.5 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of audit rights and inspection.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Audit Rights and Inspection. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_22_V6": {
        "clause_type": "Audit Rights and Inspection",
        "variant": 6,
        "standard_clause_text": "Section 22.6 (Audit Rights and Inspection): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 22.6 (Vendor Version): Vendor liability with respect to audit rights and inspection shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 22.6 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of audit rights and inspection.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Audit Rights and Inspection. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_22_V7": {
        "clause_type": "Audit Rights and Inspection",
        "variant": 7,
        "standard_clause_text": "Section 22.7 (Audit Rights and Inspection): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 22.7 (Vendor Version): Vendor liability with respect to audit rights and inspection shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 22.7 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of audit rights and inspection.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Audit Rights and Inspection. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_23_V1": {
        "clause_type": "Insurance and Coverage Minimums",
        "variant": 1,
        "standard_clause_text": "Section 23.1 (Insurance and Coverage Minimums): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 23.1 (Vendor Version): Vendor liability with respect to insurance and coverage minimums shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 23.1 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of insurance and coverage minimums.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Insurance and Coverage Minimums. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_23_V2": {
        "clause_type": "Insurance and Coverage Minimums",
        "variant": 2,
        "standard_clause_text": "Section 23.2 (Insurance and Coverage Minimums): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 23.2 (Vendor Version): Vendor liability with respect to insurance and coverage minimums shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 23.2 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of insurance and coverage minimums.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Insurance and Coverage Minimums. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_23_V3": {
        "clause_type": "Insurance and Coverage Minimums",
        "variant": 3,
        "standard_clause_text": "Section 23.3 (Insurance and Coverage Minimums): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 23.3 (Vendor Version): Vendor liability with respect to insurance and coverage minimums shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 23.3 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of insurance and coverage minimums.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Insurance and Coverage Minimums. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_23_V4": {
        "clause_type": "Insurance and Coverage Minimums",
        "variant": 4,
        "standard_clause_text": "Section 23.4 (Insurance and Coverage Minimums): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 23.4 (Vendor Version): Vendor liability with respect to insurance and coverage minimums shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 23.4 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of insurance and coverage minimums.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Insurance and Coverage Minimums. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_23_V5": {
        "clause_type": "Insurance and Coverage Minimums",
        "variant": 5,
        "standard_clause_text": "Section 23.5 (Insurance and Coverage Minimums): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 23.5 (Vendor Version): Vendor liability with respect to insurance and coverage minimums shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 23.5 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of insurance and coverage minimums.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Insurance and Coverage Minimums. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_23_V6": {
        "clause_type": "Insurance and Coverage Minimums",
        "variant": 6,
        "standard_clause_text": "Section 23.6 (Insurance and Coverage Minimums): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 23.6 (Vendor Version): Vendor liability with respect to insurance and coverage minimums shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 23.6 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of insurance and coverage minimums.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Insurance and Coverage Minimums. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_23_V7": {
        "clause_type": "Insurance and Coverage Minimums",
        "variant": 7,
        "standard_clause_text": "Section 23.7 (Insurance and Coverage Minimums): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 23.7 (Vendor Version): Vendor liability with respect to insurance and coverage minimums shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 23.7 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of insurance and coverage minimums.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Insurance and Coverage Minimums. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_24_V1": {
        "clause_type": "Independent Contractor Status",
        "variant": 1,
        "standard_clause_text": "Section 24.1 (Independent Contractor Status): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 24.1 (Vendor Version): Vendor liability with respect to independent contractor status shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 24.1 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of independent contractor status.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Independent Contractor Status. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_24_V2": {
        "clause_type": "Independent Contractor Status",
        "variant": 2,
        "standard_clause_text": "Section 24.2 (Independent Contractor Status): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 24.2 (Vendor Version): Vendor liability with respect to independent contractor status shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 24.2 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of independent contractor status.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Independent Contractor Status. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_24_V3": {
        "clause_type": "Independent Contractor Status",
        "variant": 3,
        "standard_clause_text": "Section 24.3 (Independent Contractor Status): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 24.3 (Vendor Version): Vendor liability with respect to independent contractor status shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 24.3 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of independent contractor status.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Independent Contractor Status. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_24_V4": {
        "clause_type": "Independent Contractor Status",
        "variant": 4,
        "standard_clause_text": "Section 24.4 (Independent Contractor Status): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 24.4 (Vendor Version): Vendor liability with respect to independent contractor status shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 24.4 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of independent contractor status.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Independent Contractor Status. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_24_V5": {
        "clause_type": "Independent Contractor Status",
        "variant": 5,
        "standard_clause_text": "Section 24.5 (Independent Contractor Status): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 24.5 (Vendor Version): Vendor liability with respect to independent contractor status shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 24.5 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of independent contractor status.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Independent Contractor Status. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_24_V6": {
        "clause_type": "Independent Contractor Status",
        "variant": 6,
        "standard_clause_text": "Section 24.6 (Independent Contractor Status): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 24.6 (Vendor Version): Vendor liability with respect to independent contractor status shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 24.6 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of independent contractor status.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Independent Contractor Status. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_24_V7": {
        "clause_type": "Independent Contractor Status",
        "variant": 7,
        "standard_clause_text": "Section 24.7 (Independent Contractor Status): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 24.7 (Vendor Version): Vendor liability with respect to independent contractor status shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 24.7 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of independent contractor status.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Independent Contractor Status. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_25_V1": {
        "clause_type": "Notices and Communications",
        "variant": 1,
        "standard_clause_text": "Section 25.1 (Notices and Communications): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 25.1 (Vendor Version): Vendor liability with respect to notices and communications shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 25.1 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of notices and communications.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Notices and Communications. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_25_V2": {
        "clause_type": "Notices and Communications",
        "variant": 2,
        "standard_clause_text": "Section 25.2 (Notices and Communications): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 25.2 (Vendor Version): Vendor liability with respect to notices and communications shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 25.2 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of notices and communications.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Notices and Communications. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_25_V3": {
        "clause_type": "Notices and Communications",
        "variant": 3,
        "standard_clause_text": "Section 25.3 (Notices and Communications): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 25.3 (Vendor Version): Vendor liability with respect to notices and communications shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 25.3 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of notices and communications.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Notices and Communications. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_25_V4": {
        "clause_type": "Notices and Communications",
        "variant": 4,
        "standard_clause_text": "Section 25.4 (Notices and Communications): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 25.4 (Vendor Version): Vendor liability with respect to notices and communications shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 25.4 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of notices and communications.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Notices and Communications. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_25_V5": {
        "clause_type": "Notices and Communications",
        "variant": 5,
        "standard_clause_text": "Section 25.5 (Notices and Communications): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 25.5 (Vendor Version): Vendor liability with respect to notices and communications shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 25.5 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of notices and communications.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Notices and Communications. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_25_V6": {
        "clause_type": "Notices and Communications",
        "variant": 6,
        "standard_clause_text": "Section 25.6 (Notices and Communications): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 25.6 (Vendor Version): Vendor liability with respect to notices and communications shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 25.6 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of notices and communications.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Notices and Communications. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_25_V7": {
        "clause_type": "Notices and Communications",
        "variant": 7,
        "standard_clause_text": "Section 25.7 (Notices and Communications): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 25.7 (Vendor Version): Vendor liability with respect to notices and communications shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 25.7 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of notices and communications.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Notices and Communications. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_26_V1": {
        "clause_type": "Payment Terms and Invoicing",
        "variant": 1,
        "standard_clause_text": "Section 26.1 (Payment Terms and Invoicing): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 26.1 (Vendor Version): Vendor liability with respect to payment terms and invoicing shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 26.1 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of payment terms and invoicing.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Payment Terms and Invoicing. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_26_V2": {
        "clause_type": "Payment Terms and Invoicing",
        "variant": 2,
        "standard_clause_text": "Section 26.2 (Payment Terms and Invoicing): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 26.2 (Vendor Version): Vendor liability with respect to payment terms and invoicing shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 26.2 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of payment terms and invoicing.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Payment Terms and Invoicing. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_26_V3": {
        "clause_type": "Payment Terms and Invoicing",
        "variant": 3,
        "standard_clause_text": "Section 26.3 (Payment Terms and Invoicing): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 26.3 (Vendor Version): Vendor liability with respect to payment terms and invoicing shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 26.3 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of payment terms and invoicing.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Payment Terms and Invoicing. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_26_V4": {
        "clause_type": "Payment Terms and Invoicing",
        "variant": 4,
        "standard_clause_text": "Section 26.4 (Payment Terms and Invoicing): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 26.4 (Vendor Version): Vendor liability with respect to payment terms and invoicing shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 26.4 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of payment terms and invoicing.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Payment Terms and Invoicing. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_26_V5": {
        "clause_type": "Payment Terms and Invoicing",
        "variant": 5,
        "standard_clause_text": "Section 26.5 (Payment Terms and Invoicing): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 26.5 (Vendor Version): Vendor liability with respect to payment terms and invoicing shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 26.5 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of payment terms and invoicing.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Payment Terms and Invoicing. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_26_V6": {
        "clause_type": "Payment Terms and Invoicing",
        "variant": 6,
        "standard_clause_text": "Section 26.6 (Payment Terms and Invoicing): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 26.6 (Vendor Version): Vendor liability with respect to payment terms and invoicing shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 26.6 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of payment terms and invoicing.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Payment Terms and Invoicing. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_26_V7": {
        "clause_type": "Payment Terms and Invoicing",
        "variant": 7,
        "standard_clause_text": "Section 26.7 (Payment Terms and Invoicing): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 26.7 (Vendor Version): Vendor liability with respect to payment terms and invoicing shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 26.7 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of payment terms and invoicing.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Payment Terms and Invoicing. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_27_V1": {
        "clause_type": "Taxes and Withholdings",
        "variant": 1,
        "standard_clause_text": "Section 27.1 (Taxes and Withholdings): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 27.1 (Vendor Version): Vendor liability with respect to taxes and withholdings shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 27.1 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of taxes and withholdings.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Taxes and Withholdings. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_27_V2": {
        "clause_type": "Taxes and Withholdings",
        "variant": 2,
        "standard_clause_text": "Section 27.2 (Taxes and Withholdings): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 27.2 (Vendor Version): Vendor liability with respect to taxes and withholdings shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 27.2 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of taxes and withholdings.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Taxes and Withholdings. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_27_V3": {
        "clause_type": "Taxes and Withholdings",
        "variant": 3,
        "standard_clause_text": "Section 27.3 (Taxes and Withholdings): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 27.3 (Vendor Version): Vendor liability with respect to taxes and withholdings shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 27.3 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of taxes and withholdings.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Taxes and Withholdings. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_27_V4": {
        "clause_type": "Taxes and Withholdings",
        "variant": 4,
        "standard_clause_text": "Section 27.4 (Taxes and Withholdings): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 27.4 (Vendor Version): Vendor liability with respect to taxes and withholdings shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 27.4 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of taxes and withholdings.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Taxes and Withholdings. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_27_V5": {
        "clause_type": "Taxes and Withholdings",
        "variant": 5,
        "standard_clause_text": "Section 27.5 (Taxes and Withholdings): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 27.5 (Vendor Version): Vendor liability with respect to taxes and withholdings shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 27.5 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of taxes and withholdings.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Taxes and Withholdings. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_27_V6": {
        "clause_type": "Taxes and Withholdings",
        "variant": 6,
        "standard_clause_text": "Section 27.6 (Taxes and Withholdings): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 27.6 (Vendor Version): Vendor liability with respect to taxes and withholdings shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 27.6 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of taxes and withholdings.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Taxes and Withholdings. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_27_V7": {
        "clause_type": "Taxes and Withholdings",
        "variant": 7,
        "standard_clause_text": "Section 27.7 (Taxes and Withholdings): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 27.7 (Vendor Version): Vendor liability with respect to taxes and withholdings shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 27.7 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of taxes and withholdings.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Taxes and Withholdings. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_28_V1": {
        "clause_type": "Survival of Obligations",
        "variant": 1,
        "standard_clause_text": "Section 28.1 (Survival of Obligations): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 28.1 (Vendor Version): Vendor liability with respect to survival of obligations shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 28.1 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of survival of obligations.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Survival of Obligations. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_28_V2": {
        "clause_type": "Survival of Obligations",
        "variant": 2,
        "standard_clause_text": "Section 28.2 (Survival of Obligations): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 28.2 (Vendor Version): Vendor liability with respect to survival of obligations shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 28.2 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of survival of obligations.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Survival of Obligations. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_28_V3": {
        "clause_type": "Survival of Obligations",
        "variant": 3,
        "standard_clause_text": "Section 28.3 (Survival of Obligations): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 28.3 (Vendor Version): Vendor liability with respect to survival of obligations shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 28.3 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of survival of obligations.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Survival of Obligations. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_28_V4": {
        "clause_type": "Survival of Obligations",
        "variant": 4,
        "standard_clause_text": "Section 28.4 (Survival of Obligations): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 28.4 (Vendor Version): Vendor liability with respect to survival of obligations shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 28.4 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of survival of obligations.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Survival of Obligations. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_28_V5": {
        "clause_type": "Survival of Obligations",
        "variant": 5,
        "standard_clause_text": "Section 28.5 (Survival of Obligations): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 28.5 (Vendor Version): Vendor liability with respect to survival of obligations shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 28.5 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of survival of obligations.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Survival of Obligations. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_28_V6": {
        "clause_type": "Survival of Obligations",
        "variant": 6,
        "standard_clause_text": "Section 28.6 (Survival of Obligations): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 28.6 (Vendor Version): Vendor liability with respect to survival of obligations shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 28.6 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of survival of obligations.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Survival of Obligations. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_28_V7": {
        "clause_type": "Survival of Obligations",
        "variant": 7,
        "standard_clause_text": "Section 28.7 (Survival of Obligations): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 28.7 (Vendor Version): Vendor liability with respect to survival of obligations shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 28.7 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of survival of obligations.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Survival of Obligations. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_29_V1": {
        "clause_type": "Counterparts and Electronic Signatures",
        "variant": 1,
        "standard_clause_text": "Section 29.1 (Counterparts and Electronic Signatures): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 29.1 (Vendor Version): Vendor liability with respect to counterparts and electronic signatures shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 29.1 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of counterparts and electronic signatures.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Counterparts and Electronic Signatures. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_29_V2": {
        "clause_type": "Counterparts and Electronic Signatures",
        "variant": 2,
        "standard_clause_text": "Section 29.2 (Counterparts and Electronic Signatures): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 29.2 (Vendor Version): Vendor liability with respect to counterparts and electronic signatures shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 29.2 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of counterparts and electronic signatures.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Counterparts and Electronic Signatures. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_29_V3": {
        "clause_type": "Counterparts and Electronic Signatures",
        "variant": 3,
        "standard_clause_text": "Section 29.3 (Counterparts and Electronic Signatures): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 29.3 (Vendor Version): Vendor liability with respect to counterparts and electronic signatures shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 29.3 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of counterparts and electronic signatures.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Counterparts and Electronic Signatures. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_29_V4": {
        "clause_type": "Counterparts and Electronic Signatures",
        "variant": 4,
        "standard_clause_text": "Section 29.4 (Counterparts and Electronic Signatures): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 29.4 (Vendor Version): Vendor liability with respect to counterparts and electronic signatures shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 29.4 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of counterparts and electronic signatures.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Counterparts and Electronic Signatures. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_29_V5": {
        "clause_type": "Counterparts and Electronic Signatures",
        "variant": 5,
        "standard_clause_text": "Section 29.5 (Counterparts and Electronic Signatures): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 29.5 (Vendor Version): Vendor liability with respect to counterparts and electronic signatures shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 29.5 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of counterparts and electronic signatures.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Counterparts and Electronic Signatures. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_29_V6": {
        "clause_type": "Counterparts and Electronic Signatures",
        "variant": 6,
        "standard_clause_text": "Section 29.6 (Counterparts and Electronic Signatures): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 29.6 (Vendor Version): Vendor liability with respect to counterparts and electronic signatures shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 29.6 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of counterparts and electronic signatures.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Counterparts and Electronic Signatures. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_29_V7": {
        "clause_type": "Counterparts and Electronic Signatures",
        "variant": 7,
        "standard_clause_text": "Section 29.7 (Counterparts and Electronic Signatures): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 29.7 (Vendor Version): Vendor liability with respect to counterparts and electronic signatures shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 29.7 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of counterparts and electronic signatures.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Counterparts and Electronic Signatures. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_30_V1": {
        "clause_type": "Subcontracting and Third Parties",
        "variant": 1,
        "standard_clause_text": "Section 30.1 (Subcontracting and Third Parties): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 30.1 (Vendor Version): Vendor liability with respect to subcontracting and third parties shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 30.1 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of subcontracting and third parties.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Subcontracting and Third Parties. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_30_V2": {
        "clause_type": "Subcontracting and Third Parties",
        "variant": 2,
        "standard_clause_text": "Section 30.2 (Subcontracting and Third Parties): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 30.2 (Vendor Version): Vendor liability with respect to subcontracting and third parties shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 30.2 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of subcontracting and third parties.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Subcontracting and Third Parties. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_30_V3": {
        "clause_type": "Subcontracting and Third Parties",
        "variant": 3,
        "standard_clause_text": "Section 30.3 (Subcontracting and Third Parties): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 30.3 (Vendor Version): Vendor liability with respect to subcontracting and third parties shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 30.3 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of subcontracting and third parties.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Subcontracting and Third Parties. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_30_V4": {
        "clause_type": "Subcontracting and Third Parties",
        "variant": 4,
        "standard_clause_text": "Section 30.4 (Subcontracting and Third Parties): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 30.4 (Vendor Version): Vendor liability with respect to subcontracting and third parties shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 30.4 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of subcontracting and third parties.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Subcontracting and Third Parties. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_30_V5": {
        "clause_type": "Subcontracting and Third Parties",
        "variant": 5,
        "standard_clause_text": "Section 30.5 (Subcontracting and Third Parties): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 30.5 (Vendor Version): Vendor liability with respect to subcontracting and third parties shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 30.5 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of subcontracting and third parties.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Subcontracting and Third Parties. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_30_V6": {
        "clause_type": "Subcontracting and Third Parties",
        "variant": 6,
        "standard_clause_text": "Section 30.6 (Subcontracting and Third Parties): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 30.6 (Vendor Version): Vendor liability with respect to subcontracting and third parties shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 30.6 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of subcontracting and third parties.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Subcontracting and Third Parties. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_30_V7": {
        "clause_type": "Subcontracting and Third Parties",
        "variant": 7,
        "standard_clause_text": "Section 30.7 (Subcontracting and Third Parties): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 30.7 (Vendor Version): Vendor liability with respect to subcontracting and third parties shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 30.7 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of subcontracting and third parties.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Subcontracting and Third Parties. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_31_V1": {
        "clause_type": "Change Control Procedure",
        "variant": 1,
        "standard_clause_text": "Section 31.1 (Change Control Procedure): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 31.1 (Vendor Version): Vendor liability with respect to change control procedure shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 31.1 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of change control procedure.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Change Control Procedure. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_31_V2": {
        "clause_type": "Change Control Procedure",
        "variant": 2,
        "standard_clause_text": "Section 31.2 (Change Control Procedure): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 31.2 (Vendor Version): Vendor liability with respect to change control procedure shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 31.2 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of change control procedure.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Change Control Procedure. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_31_V3": {
        "clause_type": "Change Control Procedure",
        "variant": 3,
        "standard_clause_text": "Section 31.3 (Change Control Procedure): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 31.3 (Vendor Version): Vendor liability with respect to change control procedure shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 31.3 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of change control procedure.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Change Control Procedure. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_31_V4": {
        "clause_type": "Change Control Procedure",
        "variant": 4,
        "standard_clause_text": "Section 31.4 (Change Control Procedure): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 31.4 (Vendor Version): Vendor liability with respect to change control procedure shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 31.4 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of change control procedure.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Change Control Procedure. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_31_V5": {
        "clause_type": "Change Control Procedure",
        "variant": 5,
        "standard_clause_text": "Section 31.5 (Change Control Procedure): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 31.5 (Vendor Version): Vendor liability with respect to change control procedure shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 31.5 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of change control procedure.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Change Control Procedure. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_31_V6": {
        "clause_type": "Change Control Procedure",
        "variant": 6,
        "standard_clause_text": "Section 31.6 (Change Control Procedure): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 31.6 (Vendor Version): Vendor liability with respect to change control procedure shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 31.6 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of change control procedure.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Change Control Procedure. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_31_V7": {
        "clause_type": "Change Control Procedure",
        "variant": 7,
        "standard_clause_text": "Section 31.7 (Change Control Procedure): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 31.7 (Vendor Version): Vendor liability with respect to change control procedure shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 31.7 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of change control procedure.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Change Control Procedure. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_32_V1": {
        "clause_type": "Disaster Recovery and Business Continuity",
        "variant": 1,
        "standard_clause_text": "Section 32.1 (Disaster Recovery and Business Continuity): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 32.1 (Vendor Version): Vendor liability with respect to disaster recovery and business continuity shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 32.1 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of disaster recovery and business continuity.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Disaster Recovery and Business Continuity. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_32_V2": {
        "clause_type": "Disaster Recovery and Business Continuity",
        "variant": 2,
        "standard_clause_text": "Section 32.2 (Disaster Recovery and Business Continuity): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 32.2 (Vendor Version): Vendor liability with respect to disaster recovery and business continuity shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 32.2 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of disaster recovery and business continuity.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Disaster Recovery and Business Continuity. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_32_V3": {
        "clause_type": "Disaster Recovery and Business Continuity",
        "variant": 3,
        "standard_clause_text": "Section 32.3 (Disaster Recovery and Business Continuity): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 32.3 (Vendor Version): Vendor liability with respect to disaster recovery and business continuity shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 32.3 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of disaster recovery and business continuity.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Disaster Recovery and Business Continuity. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_32_V4": {
        "clause_type": "Disaster Recovery and Business Continuity",
        "variant": 4,
        "standard_clause_text": "Section 32.4 (Disaster Recovery and Business Continuity): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 32.4 (Vendor Version): Vendor liability with respect to disaster recovery and business continuity shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 32.4 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of disaster recovery and business continuity.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Disaster Recovery and Business Continuity. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_32_V5": {
        "clause_type": "Disaster Recovery and Business Continuity",
        "variant": 5,
        "standard_clause_text": "Section 32.5 (Disaster Recovery and Business Continuity): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 32.5 (Vendor Version): Vendor liability with respect to disaster recovery and business continuity shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 32.5 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of disaster recovery and business continuity.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Disaster Recovery and Business Continuity. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_32_V6": {
        "clause_type": "Disaster Recovery and Business Continuity",
        "variant": 6,
        "standard_clause_text": "Section 32.6 (Disaster Recovery and Business Continuity): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 32.6 (Vendor Version): Vendor liability with respect to disaster recovery and business continuity shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 32.6 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of disaster recovery and business continuity.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Disaster Recovery and Business Continuity. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_32_V7": {
        "clause_type": "Disaster Recovery and Business Continuity",
        "variant": 7,
        "standard_clause_text": "Section 32.7 (Disaster Recovery and Business Continuity): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 32.7 (Vendor Version): Vendor liability with respect to disaster recovery and business continuity shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 32.7 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of disaster recovery and business continuity.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Disaster Recovery and Business Continuity. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_33_V1": {
        "clause_type": "Source Code Escrow",
        "variant": 1,
        "standard_clause_text": "Section 33.1 (Source Code Escrow): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 33.1 (Vendor Version): Vendor liability with respect to source code escrow shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 33.1 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of source code escrow.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Source Code Escrow. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_33_V2": {
        "clause_type": "Source Code Escrow",
        "variant": 2,
        "standard_clause_text": "Section 33.2 (Source Code Escrow): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 33.2 (Vendor Version): Vendor liability with respect to source code escrow shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 33.2 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of source code escrow.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Source Code Escrow. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_33_V3": {
        "clause_type": "Source Code Escrow",
        "variant": 3,
        "standard_clause_text": "Section 33.3 (Source Code Escrow): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 33.3 (Vendor Version): Vendor liability with respect to source code escrow shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 33.3 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of source code escrow.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Source Code Escrow. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_33_V4": {
        "clause_type": "Source Code Escrow",
        "variant": 4,
        "standard_clause_text": "Section 33.4 (Source Code Escrow): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 33.4 (Vendor Version): Vendor liability with respect to source code escrow shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 33.4 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of source code escrow.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Source Code Escrow. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_33_V5": {
        "clause_type": "Source Code Escrow",
        "variant": 5,
        "standard_clause_text": "Section 33.5 (Source Code Escrow): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 33.5 (Vendor Version): Vendor liability with respect to source code escrow shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 33.5 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of source code escrow.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Source Code Escrow. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_33_V6": {
        "clause_type": "Source Code Escrow",
        "variant": 6,
        "standard_clause_text": "Section 33.6 (Source Code Escrow): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 33.6 (Vendor Version): Vendor liability with respect to source code escrow shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 33.6 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of source code escrow.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Source Code Escrow. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_33_V7": {
        "clause_type": "Source Code Escrow",
        "variant": 7,
        "standard_clause_text": "Section 33.7 (Source Code Escrow): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 33.7 (Vendor Version): Vendor liability with respect to source code escrow shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 33.7 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of source code escrow.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Source Code Escrow. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_34_V1": {
        "clause_type": "Acceptance Testing and Signoff",
        "variant": 1,
        "standard_clause_text": "Section 34.1 (Acceptance Testing and Signoff): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 34.1 (Vendor Version): Vendor liability with respect to acceptance testing and signoff shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 34.1 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of acceptance testing and signoff.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Acceptance Testing and Signoff. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_34_V2": {
        "clause_type": "Acceptance Testing and Signoff",
        "variant": 2,
        "standard_clause_text": "Section 34.2 (Acceptance Testing and Signoff): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 34.2 (Vendor Version): Vendor liability with respect to acceptance testing and signoff shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 34.2 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of acceptance testing and signoff.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Acceptance Testing and Signoff. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_34_V3": {
        "clause_type": "Acceptance Testing and Signoff",
        "variant": 3,
        "standard_clause_text": "Section 34.3 (Acceptance Testing and Signoff): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 34.3 (Vendor Version): Vendor liability with respect to acceptance testing and signoff shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 34.3 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of acceptance testing and signoff.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Acceptance Testing and Signoff. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_34_V4": {
        "clause_type": "Acceptance Testing and Signoff",
        "variant": 4,
        "standard_clause_text": "Section 34.4 (Acceptance Testing and Signoff): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 34.4 (Vendor Version): Vendor liability with respect to acceptance testing and signoff shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 34.4 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of acceptance testing and signoff.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Acceptance Testing and Signoff. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_34_V5": {
        "clause_type": "Acceptance Testing and Signoff",
        "variant": 5,
        "standard_clause_text": "Section 34.5 (Acceptance Testing and Signoff): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 34.5 (Vendor Version): Vendor liability with respect to acceptance testing and signoff shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 34.5 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of acceptance testing and signoff.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Acceptance Testing and Signoff. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_34_V6": {
        "clause_type": "Acceptance Testing and Signoff",
        "variant": 6,
        "standard_clause_text": "Section 34.6 (Acceptance Testing and Signoff): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 34.6 (Vendor Version): Vendor liability with respect to acceptance testing and signoff shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 34.6 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of acceptance testing and signoff.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Acceptance Testing and Signoff. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_34_V7": {
        "clause_type": "Acceptance Testing and Signoff",
        "variant": 7,
        "standard_clause_text": "Section 34.7 (Acceptance Testing and Signoff): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 34.7 (Vendor Version): Vendor liability with respect to acceptance testing and signoff shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 34.7 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of acceptance testing and signoff.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Acceptance Testing and Signoff. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_35_V1": {
        "clause_type": "Price Adjustments and Cost of Living",
        "variant": 1,
        "standard_clause_text": "Section 35.1 (Price Adjustments and Cost of Living): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 35.1 (Vendor Version): Vendor liability with respect to price adjustments and cost of living shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 35.1 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of price adjustments and cost of living.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Price Adjustments and Cost of Living. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_35_V2": {
        "clause_type": "Price Adjustments and Cost of Living",
        "variant": 2,
        "standard_clause_text": "Section 35.2 (Price Adjustments and Cost of Living): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 35.2 (Vendor Version): Vendor liability with respect to price adjustments and cost of living shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 35.2 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of price adjustments and cost of living.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Price Adjustments and Cost of Living. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_35_V3": {
        "clause_type": "Price Adjustments and Cost of Living",
        "variant": 3,
        "standard_clause_text": "Section 35.3 (Price Adjustments and Cost of Living): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 35.3 (Vendor Version): Vendor liability with respect to price adjustments and cost of living shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 35.3 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of price adjustments and cost of living.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Price Adjustments and Cost of Living. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_35_V4": {
        "clause_type": "Price Adjustments and Cost of Living",
        "variant": 4,
        "standard_clause_text": "Section 35.4 (Price Adjustments and Cost of Living): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 35.4 (Vendor Version): Vendor liability with respect to price adjustments and cost of living shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 35.4 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of price adjustments and cost of living.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Price Adjustments and Cost of Living. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_35_V5": {
        "clause_type": "Price Adjustments and Cost of Living",
        "variant": 5,
        "standard_clause_text": "Section 35.5 (Price Adjustments and Cost of Living): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 35.5 (Vendor Version): Vendor liability with respect to price adjustments and cost of living shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 35.5 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of price adjustments and cost of living.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Price Adjustments and Cost of Living. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_35_V6": {
        "clause_type": "Price Adjustments and Cost of Living",
        "variant": 6,
        "standard_clause_text": "Section 35.6 (Price Adjustments and Cost of Living): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 35.6 (Vendor Version): Vendor liability with respect to price adjustments and cost of living shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 35.6 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of price adjustments and cost of living.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Price Adjustments and Cost of Living. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_35_V7": {
        "clause_type": "Price Adjustments and Cost of Living",
        "variant": 7,
        "standard_clause_text": "Section 35.7 (Price Adjustments and Cost of Living): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 35.7 (Vendor Version): Vendor liability with respect to price adjustments and cost of living shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 35.7 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of price adjustments and cost of living.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Price Adjustments and Cost of Living. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_36_V1": {
        "clause_type": "Most Favored Nation (MFN)",
        "variant": 1,
        "standard_clause_text": "Section 36.1 (Most Favored Nation (MFN)): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 36.1 (Vendor Version): Vendor liability with respect to most favored nation (mfn) shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 36.1 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of most favored nation (mfn).",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Most Favored Nation (MFN). Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_36_V2": {
        "clause_type": "Most Favored Nation (MFN)",
        "variant": 2,
        "standard_clause_text": "Section 36.2 (Most Favored Nation (MFN)): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 36.2 (Vendor Version): Vendor liability with respect to most favored nation (mfn) shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 36.2 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of most favored nation (mfn).",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Most Favored Nation (MFN). Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_36_V3": {
        "clause_type": "Most Favored Nation (MFN)",
        "variant": 3,
        "standard_clause_text": "Section 36.3 (Most Favored Nation (MFN)): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 36.3 (Vendor Version): Vendor liability with respect to most favored nation (mfn) shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 36.3 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of most favored nation (mfn).",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Most Favored Nation (MFN). Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_36_V4": {
        "clause_type": "Most Favored Nation (MFN)",
        "variant": 4,
        "standard_clause_text": "Section 36.4 (Most Favored Nation (MFN)): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 36.4 (Vendor Version): Vendor liability with respect to most favored nation (mfn) shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 36.4 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of most favored nation (mfn).",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Most Favored Nation (MFN). Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_36_V5": {
        "clause_type": "Most Favored Nation (MFN)",
        "variant": 5,
        "standard_clause_text": "Section 36.5 (Most Favored Nation (MFN)): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 36.5 (Vendor Version): Vendor liability with respect to most favored nation (mfn) shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 36.5 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of most favored nation (mfn).",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Most Favored Nation (MFN). Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_36_V6": {
        "clause_type": "Most Favored Nation (MFN)",
        "variant": 6,
        "standard_clause_text": "Section 36.6 (Most Favored Nation (MFN)): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 36.6 (Vendor Version): Vendor liability with respect to most favored nation (mfn) shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 36.6 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of most favored nation (mfn).",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Most Favored Nation (MFN). Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_36_V7": {
        "clause_type": "Most Favored Nation (MFN)",
        "variant": 7,
        "standard_clause_text": "Section 36.7 (Most Favored Nation (MFN)): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 36.7 (Vendor Version): Vendor liability with respect to most favored nation (mfn) shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 36.7 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of most favored nation (mfn).",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Most Favored Nation (MFN). Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_37_V1": {
        "clause_type": "Right of First Refusal",
        "variant": 1,
        "standard_clause_text": "Section 37.1 (Right of First Refusal): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 37.1 (Vendor Version): Vendor liability with respect to right of first refusal shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 37.1 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of right of first refusal.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Right of First Refusal. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_37_V2": {
        "clause_type": "Right of First Refusal",
        "variant": 2,
        "standard_clause_text": "Section 37.2 (Right of First Refusal): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 37.2 (Vendor Version): Vendor liability with respect to right of first refusal shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 37.2 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of right of first refusal.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Right of First Refusal. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_37_V3": {
        "clause_type": "Right of First Refusal",
        "variant": 3,
        "standard_clause_text": "Section 37.3 (Right of First Refusal): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 37.3 (Vendor Version): Vendor liability with respect to right of first refusal shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 37.3 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of right of first refusal.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Right of First Refusal. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_37_V4": {
        "clause_type": "Right of First Refusal",
        "variant": 4,
        "standard_clause_text": "Section 37.4 (Right of First Refusal): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 37.4 (Vendor Version): Vendor liability with respect to right of first refusal shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 37.4 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of right of first refusal.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Right of First Refusal. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_37_V5": {
        "clause_type": "Right of First Refusal",
        "variant": 5,
        "standard_clause_text": "Section 37.5 (Right of First Refusal): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 37.5 (Vendor Version): Vendor liability with respect to right of first refusal shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 37.5 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of right of first refusal.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Right of First Refusal. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_37_V6": {
        "clause_type": "Right of First Refusal",
        "variant": 6,
        "standard_clause_text": "Section 37.6 (Right of First Refusal): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 37.6 (Vendor Version): Vendor liability with respect to right of first refusal shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 37.6 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of right of first refusal.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Right of First Refusal. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_37_V7": {
        "clause_type": "Right of First Refusal",
        "variant": 7,
        "standard_clause_text": "Section 37.7 (Right of First Refusal): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 37.7 (Vendor Version): Vendor liability with respect to right of first refusal shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 37.7 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of right of first refusal.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Right of First Refusal. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_38_V1": {
        "clause_type": "Liquidated Damages",
        "variant": 1,
        "standard_clause_text": "Section 38.1 (Liquidated Damages): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 38.1 (Vendor Version): Vendor liability with respect to liquidated damages shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 38.1 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of liquidated damages.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Liquidated Damages. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_38_V2": {
        "clause_type": "Liquidated Damages",
        "variant": 2,
        "standard_clause_text": "Section 38.2 (Liquidated Damages): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 38.2 (Vendor Version): Vendor liability with respect to liquidated damages shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 38.2 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of liquidated damages.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Liquidated Damages. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_38_V3": {
        "clause_type": "Liquidated Damages",
        "variant": 3,
        "standard_clause_text": "Section 38.3 (Liquidated Damages): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 38.3 (Vendor Version): Vendor liability with respect to liquidated damages shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 38.3 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of liquidated damages.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Liquidated Damages. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_38_V4": {
        "clause_type": "Liquidated Damages",
        "variant": 4,
        "standard_clause_text": "Section 38.4 (Liquidated Damages): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 38.4 (Vendor Version): Vendor liability with respect to liquidated damages shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 38.4 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of liquidated damages.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Liquidated Damages. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_38_V5": {
        "clause_type": "Liquidated Damages",
        "variant": 5,
        "standard_clause_text": "Section 38.5 (Liquidated Damages): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 38.5 (Vendor Version): Vendor liability with respect to liquidated damages shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 38.5 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of liquidated damages.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Liquidated Damages. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_38_V6": {
        "clause_type": "Liquidated Damages",
        "variant": 6,
        "standard_clause_text": "Section 38.6 (Liquidated Damages): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 38.6 (Vendor Version): Vendor liability with respect to liquidated damages shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 38.6 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of liquidated damages.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Liquidated Damages. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_38_V7": {
        "clause_type": "Liquidated Damages",
        "variant": 7,
        "standard_clause_text": "Section 38.7 (Liquidated Damages): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 38.7 (Vendor Version): Vendor liability with respect to liquidated damages shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 38.7 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of liquidated damages.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Liquidated Damages. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_39_V1": {
        "clause_type": "Injunctive and Equitable Relief",
        "variant": 1,
        "standard_clause_text": "Section 39.1 (Injunctive and Equitable Relief): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 39.1 (Vendor Version): Vendor liability with respect to injunctive and equitable relief shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 39.1 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of injunctive and equitable relief.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Injunctive and Equitable Relief. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_39_V2": {
        "clause_type": "Injunctive and Equitable Relief",
        "variant": 2,
        "standard_clause_text": "Section 39.2 (Injunctive and Equitable Relief): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 39.2 (Vendor Version): Vendor liability with respect to injunctive and equitable relief shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 39.2 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of injunctive and equitable relief.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Injunctive and Equitable Relief. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_39_V3": {
        "clause_type": "Injunctive and Equitable Relief",
        "variant": 3,
        "standard_clause_text": "Section 39.3 (Injunctive and Equitable Relief): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 39.3 (Vendor Version): Vendor liability with respect to injunctive and equitable relief shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 39.3 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of injunctive and equitable relief.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Injunctive and Equitable Relief. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_39_V4": {
        "clause_type": "Injunctive and Equitable Relief",
        "variant": 4,
        "standard_clause_text": "Section 39.4 (Injunctive and Equitable Relief): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 39.4 (Vendor Version): Vendor liability with respect to injunctive and equitable relief shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 39.4 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of injunctive and equitable relief.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Injunctive and Equitable Relief. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_39_V5": {
        "clause_type": "Injunctive and Equitable Relief",
        "variant": 5,
        "standard_clause_text": "Section 39.5 (Injunctive and Equitable Relief): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 39.5 (Vendor Version): Vendor liability with respect to injunctive and equitable relief shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 39.5 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of injunctive and equitable relief.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Injunctive and Equitable Relief. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_39_V6": {
        "clause_type": "Injunctive and Equitable Relief",
        "variant": 6,
        "standard_clause_text": "Section 39.6 (Injunctive and Equitable Relief): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 39.6 (Vendor Version): Vendor liability with respect to injunctive and equitable relief shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 39.6 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of injunctive and equitable relief.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Injunctive and Equitable Relief. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_39_V7": {
        "clause_type": "Injunctive and Equitable Relief",
        "variant": 7,
        "standard_clause_text": "Section 39.7 (Injunctive and Equitable Relief): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 39.7 (Vendor Version): Vendor liability with respect to injunctive and equitable relief shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 39.7 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of injunctive and equitable relief.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Injunctive and Equitable Relief. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_40_V1": {
        "clause_type": "Publicity and Press Releases",
        "variant": 1,
        "standard_clause_text": "Section 40.1 (Publicity and Press Releases): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 40.1 (Vendor Version): Vendor liability with respect to publicity and press releases shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 40.1 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of publicity and press releases.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Publicity and Press Releases. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_40_V2": {
        "clause_type": "Publicity and Press Releases",
        "variant": 2,
        "standard_clause_text": "Section 40.2 (Publicity and Press Releases): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 40.2 (Vendor Version): Vendor liability with respect to publicity and press releases shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 40.2 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of publicity and press releases.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Publicity and Press Releases. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_40_V3": {
        "clause_type": "Publicity and Press Releases",
        "variant": 3,
        "standard_clause_text": "Section 40.3 (Publicity and Press Releases): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 40.3 (Vendor Version): Vendor liability with respect to publicity and press releases shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 40.3 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of publicity and press releases.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Publicity and Press Releases. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_40_V4": {
        "clause_type": "Publicity and Press Releases",
        "variant": 4,
        "standard_clause_text": "Section 40.4 (Publicity and Press Releases): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 40.4 (Vendor Version): Vendor liability with respect to publicity and press releases shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 40.4 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of publicity and press releases.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Publicity and Press Releases. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_40_V5": {
        "clause_type": "Publicity and Press Releases",
        "variant": 5,
        "standard_clause_text": "Section 40.5 (Publicity and Press Releases): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 40.5 (Vendor Version): Vendor liability with respect to publicity and press releases shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 40.5 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of publicity and press releases.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Publicity and Press Releases. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_40_V6": {
        "clause_type": "Publicity and Press Releases",
        "variant": 6,
        "standard_clause_text": "Section 40.6 (Publicity and Press Releases): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 40.6 (Vendor Version): Vendor liability with respect to publicity and press releases shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 40.6 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of publicity and press releases.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Publicity and Press Releases. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_40_V7": {
        "clause_type": "Publicity and Press Releases",
        "variant": 7,
        "standard_clause_text": "Section 40.7 (Publicity and Press Releases): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 40.7 (Vendor Version): Vendor liability with respect to publicity and press releases shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 40.7 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of publicity and press releases.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Publicity and Press Releases. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_41_V1": {
        "clause_type": "Set-off and Deductions",
        "variant": 1,
        "standard_clause_text": "Section 41.1 (Set-off and Deductions): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 41.1 (Vendor Version): Vendor liability with respect to set-off and deductions shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 41.1 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of set-off and deductions.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Set-off and Deductions. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_41_V2": {
        "clause_type": "Set-off and Deductions",
        "variant": 2,
        "standard_clause_text": "Section 41.2 (Set-off and Deductions): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 41.2 (Vendor Version): Vendor liability with respect to set-off and deductions shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 41.2 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of set-off and deductions.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Set-off and Deductions. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_41_V3": {
        "clause_type": "Set-off and Deductions",
        "variant": 3,
        "standard_clause_text": "Section 41.3 (Set-off and Deductions): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 41.3 (Vendor Version): Vendor liability with respect to set-off and deductions shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 41.3 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of set-off and deductions.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Set-off and Deductions. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_41_V4": {
        "clause_type": "Set-off and Deductions",
        "variant": 4,
        "standard_clause_text": "Section 41.4 (Set-off and Deductions): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 41.4 (Vendor Version): Vendor liability with respect to set-off and deductions shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 41.4 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of set-off and deductions.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Set-off and Deductions. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_41_V5": {
        "clause_type": "Set-off and Deductions",
        "variant": 5,
        "standard_clause_text": "Section 41.5 (Set-off and Deductions): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 41.5 (Vendor Version): Vendor liability with respect to set-off and deductions shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 41.5 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of set-off and deductions.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Set-off and Deductions. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_41_V6": {
        "clause_type": "Set-off and Deductions",
        "variant": 6,
        "standard_clause_text": "Section 41.6 (Set-off and Deductions): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 41.6 (Vendor Version): Vendor liability with respect to set-off and deductions shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 41.6 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of set-off and deductions.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Set-off and Deductions. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_41_V7": {
        "clause_type": "Set-off and Deductions",
        "variant": 7,
        "standard_clause_text": "Section 41.7 (Set-off and Deductions): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 41.7 (Vendor Version): Vendor liability with respect to set-off and deductions shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 41.7 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of set-off and deductions.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Set-off and Deductions. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_42_V1": {
        "clause_type": "Cumulative Remedies",
        "variant": 1,
        "standard_clause_text": "Section 42.1 (Cumulative Remedies): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 42.1 (Vendor Version): Vendor liability with respect to cumulative remedies shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 42.1 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of cumulative remedies.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Cumulative Remedies. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_42_V2": {
        "clause_type": "Cumulative Remedies",
        "variant": 2,
        "standard_clause_text": "Section 42.2 (Cumulative Remedies): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 42.2 (Vendor Version): Vendor liability with respect to cumulative remedies shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 42.2 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of cumulative remedies.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Cumulative Remedies. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_42_V3": {
        "clause_type": "Cumulative Remedies",
        "variant": 3,
        "standard_clause_text": "Section 42.3 (Cumulative Remedies): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 42.3 (Vendor Version): Vendor liability with respect to cumulative remedies shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 42.3 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of cumulative remedies.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Cumulative Remedies. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_42_V4": {
        "clause_type": "Cumulative Remedies",
        "variant": 4,
        "standard_clause_text": "Section 42.4 (Cumulative Remedies): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 42.4 (Vendor Version): Vendor liability with respect to cumulative remedies shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 42.4 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of cumulative remedies.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Cumulative Remedies. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_42_V5": {
        "clause_type": "Cumulative Remedies",
        "variant": 5,
        "standard_clause_text": "Section 42.5 (Cumulative Remedies): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 42.5 (Vendor Version): Vendor liability with respect to cumulative remedies shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 42.5 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of cumulative remedies.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Cumulative Remedies. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_42_V6": {
        "clause_type": "Cumulative Remedies",
        "variant": 6,
        "standard_clause_text": "Section 42.6 (Cumulative Remedies): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 42.6 (Vendor Version): Vendor liability with respect to cumulative remedies shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 42.6 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of cumulative remedies.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Cumulative Remedies. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_42_V7": {
        "clause_type": "Cumulative Remedies",
        "variant": 7,
        "standard_clause_text": "Section 42.7 (Cumulative Remedies): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 42.7 (Vendor Version): Vendor liability with respect to cumulative remedies shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 42.7 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of cumulative remedies.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Cumulative Remedies. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_43_V1": {
        "clause_type": "Prevailing Party Legal Fees",
        "variant": 1,
        "standard_clause_text": "Section 43.1 (Prevailing Party Legal Fees): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 43.1 (Vendor Version): Vendor liability with respect to prevailing party legal fees shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 43.1 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of prevailing party legal fees.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Prevailing Party Legal Fees. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_43_V2": {
        "clause_type": "Prevailing Party Legal Fees",
        "variant": 2,
        "standard_clause_text": "Section 43.2 (Prevailing Party Legal Fees): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 43.2 (Vendor Version): Vendor liability with respect to prevailing party legal fees shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 43.2 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of prevailing party legal fees.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Prevailing Party Legal Fees. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_43_V3": {
        "clause_type": "Prevailing Party Legal Fees",
        "variant": 3,
        "standard_clause_text": "Section 43.3 (Prevailing Party Legal Fees): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 43.3 (Vendor Version): Vendor liability with respect to prevailing party legal fees shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 43.3 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of prevailing party legal fees.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Prevailing Party Legal Fees. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_43_V4": {
        "clause_type": "Prevailing Party Legal Fees",
        "variant": 4,
        "standard_clause_text": "Section 43.4 (Prevailing Party Legal Fees): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 43.4 (Vendor Version): Vendor liability with respect to prevailing party legal fees shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 43.4 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of prevailing party legal fees.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Prevailing Party Legal Fees. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_43_V5": {
        "clause_type": "Prevailing Party Legal Fees",
        "variant": 5,
        "standard_clause_text": "Section 43.5 (Prevailing Party Legal Fees): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 43.5 (Vendor Version): Vendor liability with respect to prevailing party legal fees shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 43.5 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of prevailing party legal fees.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Prevailing Party Legal Fees. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_43_V6": {
        "clause_type": "Prevailing Party Legal Fees",
        "variant": 6,
        "standard_clause_text": "Section 43.6 (Prevailing Party Legal Fees): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 43.6 (Vendor Version): Vendor liability with respect to prevailing party legal fees shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 43.6 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of prevailing party legal fees.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Prevailing Party Legal Fees. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_43_V7": {
        "clause_type": "Prevailing Party Legal Fees",
        "variant": 7,
        "standard_clause_text": "Section 43.7 (Prevailing Party Legal Fees): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 43.7 (Vendor Version): Vendor liability with respect to prevailing party legal fees shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 43.7 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of prevailing party legal fees.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Prevailing Party Legal Fees. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_44_V1": {
        "clause_type": "Time of the Essence",
        "variant": 1,
        "standard_clause_text": "Section 44.1 (Time of the Essence): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 44.1 (Vendor Version): Vendor liability with respect to time of the essence shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 44.1 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of time of the essence.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Time of the Essence. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_44_V2": {
        "clause_type": "Time of the Essence",
        "variant": 2,
        "standard_clause_text": "Section 44.2 (Time of the Essence): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 44.2 (Vendor Version): Vendor liability with respect to time of the essence shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 44.2 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of time of the essence.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Time of the Essence. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_44_V3": {
        "clause_type": "Time of the Essence",
        "variant": 3,
        "standard_clause_text": "Section 44.3 (Time of the Essence): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 44.3 (Vendor Version): Vendor liability with respect to time of the essence shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 44.3 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of time of the essence.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Time of the Essence. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_44_V4": {
        "clause_type": "Time of the Essence",
        "variant": 4,
        "standard_clause_text": "Section 44.4 (Time of the Essence): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 44.4 (Vendor Version): Vendor liability with respect to time of the essence shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 44.4 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of time of the essence.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Time of the Essence. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_44_V5": {
        "clause_type": "Time of the Essence",
        "variant": 5,
        "standard_clause_text": "Section 44.5 (Time of the Essence): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 44.5 (Vendor Version): Vendor liability with respect to time of the essence shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 44.5 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of time of the essence.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Time of the Essence. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_44_V6": {
        "clause_type": "Time of the Essence",
        "variant": 6,
        "standard_clause_text": "Section 44.6 (Time of the Essence): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 44.6 (Vendor Version): Vendor liability with respect to time of the essence shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 44.6 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of time of the essence.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Time of the Essence. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_44_V7": {
        "clause_type": "Time of the Essence",
        "variant": 7,
        "standard_clause_text": "Section 44.7 (Time of the Essence): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 44.7 (Vendor Version): Vendor liability with respect to time of the essence shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 44.7 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of time of the essence.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Time of the Essence. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_45_V1": {
        "clause_type": "No Third-Party Beneficiaries",
        "variant": 1,
        "standard_clause_text": "Section 45.1 (No Third-Party Beneficiaries): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 45.1 (Vendor Version): Vendor liability with respect to no third-party beneficiaries shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 45.1 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of no third-party beneficiaries.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for No Third-Party Beneficiaries. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_45_V2": {
        "clause_type": "No Third-Party Beneficiaries",
        "variant": 2,
        "standard_clause_text": "Section 45.2 (No Third-Party Beneficiaries): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 45.2 (Vendor Version): Vendor liability with respect to no third-party beneficiaries shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 45.2 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of no third-party beneficiaries.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for No Third-Party Beneficiaries. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_45_V3": {
        "clause_type": "No Third-Party Beneficiaries",
        "variant": 3,
        "standard_clause_text": "Section 45.3 (No Third-Party Beneficiaries): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 45.3 (Vendor Version): Vendor liability with respect to no third-party beneficiaries shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 45.3 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of no third-party beneficiaries.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for No Third-Party Beneficiaries. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_45_V4": {
        "clause_type": "No Third-Party Beneficiaries",
        "variant": 4,
        "standard_clause_text": "Section 45.4 (No Third-Party Beneficiaries): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 45.4 (Vendor Version): Vendor liability with respect to no third-party beneficiaries shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 45.4 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of no third-party beneficiaries.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for No Third-Party Beneficiaries. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_45_V5": {
        "clause_type": "No Third-Party Beneficiaries",
        "variant": 5,
        "standard_clause_text": "Section 45.5 (No Third-Party Beneficiaries): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 45.5 (Vendor Version): Vendor liability with respect to no third-party beneficiaries shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 45.5 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of no third-party beneficiaries.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for No Third-Party Beneficiaries. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_45_V6": {
        "clause_type": "No Third-Party Beneficiaries",
        "variant": 6,
        "standard_clause_text": "Section 45.6 (No Third-Party Beneficiaries): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 45.6 (Vendor Version): Vendor liability with respect to no third-party beneficiaries shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 45.6 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of no third-party beneficiaries.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for No Third-Party Beneficiaries. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_45_V7": {
        "clause_type": "No Third-Party Beneficiaries",
        "variant": 7,
        "standard_clause_text": "Section 45.7 (No Third-Party Beneficiaries): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 45.7 (Vendor Version): Vendor liability with respect to no third-party beneficiaries shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 45.7 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of no third-party beneficiaries.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for No Third-Party Beneficiaries. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_46_V1": {
        "clause_type": "Headings for Convenience Only",
        "variant": 1,
        "standard_clause_text": "Section 46.1 (Headings for Convenience Only): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 46.1 (Vendor Version): Vendor liability with respect to headings for convenience only shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 46.1 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of headings for convenience only.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Headings for Convenience Only. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_46_V2": {
        "clause_type": "Headings for Convenience Only",
        "variant": 2,
        "standard_clause_text": "Section 46.2 (Headings for Convenience Only): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 46.2 (Vendor Version): Vendor liability with respect to headings for convenience only shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 46.2 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of headings for convenience only.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Headings for Convenience Only. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_46_V3": {
        "clause_type": "Headings for Convenience Only",
        "variant": 3,
        "standard_clause_text": "Section 46.3 (Headings for Convenience Only): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 46.3 (Vendor Version): Vendor liability with respect to headings for convenience only shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 46.3 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of headings for convenience only.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Headings for Convenience Only. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_46_V4": {
        "clause_type": "Headings for Convenience Only",
        "variant": 4,
        "standard_clause_text": "Section 46.4 (Headings for Convenience Only): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 46.4 (Vendor Version): Vendor liability with respect to headings for convenience only shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 46.4 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of headings for convenience only.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Headings for Convenience Only. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_46_V5": {
        "clause_type": "Headings for Convenience Only",
        "variant": 5,
        "standard_clause_text": "Section 46.5 (Headings for Convenience Only): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 46.5 (Vendor Version): Vendor liability with respect to headings for convenience only shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 46.5 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of headings for convenience only.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Headings for Convenience Only. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_46_V6": {
        "clause_type": "Headings for Convenience Only",
        "variant": 6,
        "standard_clause_text": "Section 46.6 (Headings for Convenience Only): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 46.6 (Vendor Version): Vendor liability with respect to headings for convenience only shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 46.6 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of headings for convenience only.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Headings for Convenience Only. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_46_V7": {
        "clause_type": "Headings for Convenience Only",
        "variant": 7,
        "standard_clause_text": "Section 46.7 (Headings for Convenience Only): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 46.7 (Vendor Version): Vendor liability with respect to headings for convenience only shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 46.7 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of headings for convenience only.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Headings for Convenience Only. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_47_V1": {
        "clause_type": "Language and Translation",
        "variant": 1,
        "standard_clause_text": "Section 47.1 (Language and Translation): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 47.1 (Vendor Version): Vendor liability with respect to language and translation shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 47.1 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of language and translation.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Language and Translation. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_47_V2": {
        "clause_type": "Language and Translation",
        "variant": 2,
        "standard_clause_text": "Section 47.2 (Language and Translation): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 47.2 (Vendor Version): Vendor liability with respect to language and translation shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 47.2 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of language and translation.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Language and Translation. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_47_V3": {
        "clause_type": "Language and Translation",
        "variant": 3,
        "standard_clause_text": "Section 47.3 (Language and Translation): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 47.3 (Vendor Version): Vendor liability with respect to language and translation shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 47.3 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of language and translation.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Language and Translation. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_47_V4": {
        "clause_type": "Language and Translation",
        "variant": 4,
        "standard_clause_text": "Section 47.4 (Language and Translation): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 47.4 (Vendor Version): Vendor liability with respect to language and translation shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 47.4 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of language and translation.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Language and Translation. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_47_V5": {
        "clause_type": "Language and Translation",
        "variant": 5,
        "standard_clause_text": "Section 47.5 (Language and Translation): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 47.5 (Vendor Version): Vendor liability with respect to language and translation shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 47.5 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of language and translation.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Language and Translation. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_47_V6": {
        "clause_type": "Language and Translation",
        "variant": 6,
        "standard_clause_text": "Section 47.6 (Language and Translation): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 47.6 (Vendor Version): Vendor liability with respect to language and translation shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 47.6 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of language and translation.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Language and Translation. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_47_V7": {
        "clause_type": "Language and Translation",
        "variant": 7,
        "standard_clause_text": "Section 47.7 (Language and Translation): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 47.7 (Vendor Version): Vendor liability with respect to language and translation shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 47.7 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of language and translation.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Language and Translation. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_48_V1": {
        "clause_type": "Regulatory Compliance and Updates",
        "variant": 1,
        "standard_clause_text": "Section 48.1 (Regulatory Compliance and Updates): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 48.1 (Vendor Version): Vendor liability with respect to regulatory compliance and updates shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 48.1 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of regulatory compliance and updates.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Regulatory Compliance and Updates. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_48_V2": {
        "clause_type": "Regulatory Compliance and Updates",
        "variant": 2,
        "standard_clause_text": "Section 48.2 (Regulatory Compliance and Updates): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 48.2 (Vendor Version): Vendor liability with respect to regulatory compliance and updates shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 48.2 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of regulatory compliance and updates.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Regulatory Compliance and Updates. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_48_V3": {
        "clause_type": "Regulatory Compliance and Updates",
        "variant": 3,
        "standard_clause_text": "Section 48.3 (Regulatory Compliance and Updates): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 48.3 (Vendor Version): Vendor liability with respect to regulatory compliance and updates shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 48.3 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of regulatory compliance and updates.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Regulatory Compliance and Updates. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_48_V4": {
        "clause_type": "Regulatory Compliance and Updates",
        "variant": 4,
        "standard_clause_text": "Section 48.4 (Regulatory Compliance and Updates): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 48.4 (Vendor Version): Vendor liability with respect to regulatory compliance and updates shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 48.4 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of regulatory compliance and updates.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Regulatory Compliance and Updates. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_48_V5": {
        "clause_type": "Regulatory Compliance and Updates",
        "variant": 5,
        "standard_clause_text": "Section 48.5 (Regulatory Compliance and Updates): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 48.5 (Vendor Version): Vendor liability with respect to regulatory compliance and updates shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 48.5 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of regulatory compliance and updates.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Regulatory Compliance and Updates. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_48_V6": {
        "clause_type": "Regulatory Compliance and Updates",
        "variant": 6,
        "standard_clause_text": "Section 48.6 (Regulatory Compliance and Updates): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 48.6 (Vendor Version): Vendor liability with respect to regulatory compliance and updates shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 48.6 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of regulatory compliance and updates.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Regulatory Compliance and Updates. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_48_V7": {
        "clause_type": "Regulatory Compliance and Updates",
        "variant": 7,
        "standard_clause_text": "Section 48.7 (Regulatory Compliance and Updates): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 48.7 (Vendor Version): Vendor liability with respect to regulatory compliance and updates shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 48.7 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of regulatory compliance and updates.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Regulatory Compliance and Updates. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_49_V1": {
        "clause_type": "Environmental and ESG Commitments",
        "variant": 1,
        "standard_clause_text": "Section 49.1 (Environmental and ESG Commitments): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 49.1 (Vendor Version): Vendor liability with respect to environmental and esg commitments shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 49.1 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of environmental and esg commitments.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Environmental and ESG Commitments. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_49_V2": {
        "clause_type": "Environmental and ESG Commitments",
        "variant": 2,
        "standard_clause_text": "Section 49.2 (Environmental and ESG Commitments): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 49.2 (Vendor Version): Vendor liability with respect to environmental and esg commitments shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 49.2 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of environmental and esg commitments.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Environmental and ESG Commitments. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_49_V3": {
        "clause_type": "Environmental and ESG Commitments",
        "variant": 3,
        "standard_clause_text": "Section 49.3 (Environmental and ESG Commitments): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 49.3 (Vendor Version): Vendor liability with respect to environmental and esg commitments shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 49.3 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of environmental and esg commitments.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Environmental and ESG Commitments. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_49_V4": {
        "clause_type": "Environmental and ESG Commitments",
        "variant": 4,
        "standard_clause_text": "Section 49.4 (Environmental and ESG Commitments): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 49.4 (Vendor Version): Vendor liability with respect to environmental and esg commitments shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 49.4 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of environmental and esg commitments.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Environmental and ESG Commitments. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_49_V5": {
        "clause_type": "Environmental and ESG Commitments",
        "variant": 5,
        "standard_clause_text": "Section 49.5 (Environmental and ESG Commitments): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 49.5 (Vendor Version): Vendor liability with respect to environmental and esg commitments shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 49.5 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of environmental and esg commitments.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Environmental and ESG Commitments. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_49_V6": {
        "clause_type": "Environmental and ESG Commitments",
        "variant": 6,
        "standard_clause_text": "Section 49.6 (Environmental and ESG Commitments): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 49.6 (Vendor Version): Vendor liability with respect to environmental and esg commitments shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 49.6 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of environmental and esg commitments.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Environmental and ESG Commitments. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_49_V7": {
        "clause_type": "Environmental and ESG Commitments",
        "variant": 7,
        "standard_clause_text": "Section 49.7 (Environmental and ESG Commitments): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 49.7 (Vendor Version): Vendor liability with respect to environmental and esg commitments shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 49.7 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of environmental and esg commitments.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Environmental and ESG Commitments. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_50_V1": {
        "clause_type": "Customer Data Return and Destruction",
        "variant": 1,
        "standard_clause_text": "Section 50.1 (Customer Data Return and Destruction): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 50.1 (Vendor Version): Vendor liability with respect to customer data return and destruction shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 50.1 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of customer data return and destruction.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Customer Data Return and Destruction. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_50_V2": {
        "clause_type": "Customer Data Return and Destruction",
        "variant": 2,
        "standard_clause_text": "Section 50.2 (Customer Data Return and Destruction): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 50.2 (Vendor Version): Vendor liability with respect to customer data return and destruction shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 50.2 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of customer data return and destruction.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Customer Data Return and Destruction. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_50_V3": {
        "clause_type": "Customer Data Return and Destruction",
        "variant": 3,
        "standard_clause_text": "Section 50.3 (Customer Data Return and Destruction): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 50.3 (Vendor Version): Vendor liability with respect to customer data return and destruction shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 50.3 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of customer data return and destruction.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Customer Data Return and Destruction. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_50_V4": {
        "clause_type": "Customer Data Return and Destruction",
        "variant": 4,
        "standard_clause_text": "Section 50.4 (Customer Data Return and Destruction): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 50.4 (Vendor Version): Vendor liability with respect to customer data return and destruction shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 50.4 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of customer data return and destruction.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Customer Data Return and Destruction. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_50_V5": {
        "clause_type": "Customer Data Return and Destruction",
        "variant": 5,
        "standard_clause_text": "Section 50.5 (Customer Data Return and Destruction): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 50.5 (Vendor Version): Vendor liability with respect to customer data return and destruction shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 50.5 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of customer data return and destruction.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Customer Data Return and Destruction. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_50_V6": {
        "clause_type": "Customer Data Return and Destruction",
        "variant": 6,
        "standard_clause_text": "Section 50.6 (Customer Data Return and Destruction): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 50.6 (Vendor Version): Vendor liability with respect to customer data return and destruction shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 50.6 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of customer data return and destruction.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Customer Data Return and Destruction. Review liability caps and mutual reciprocity before signing."
    },
    "LEGAL_CLAUSE_50_V7": {
        "clause_type": "Customer Data Return and Destruction",
        "variant": 7,
        "standard_clause_text": "Section 50.7 (Customer Data Return and Destruction): Each party represents and warrants that it shall execute all obligations in accordance with professional industry standards, commercial reasonable care, and governing statutory regulations.",
        "vendor_friendly_clause": "Section 50.7 (Vendor Version): Vendor liability with respect to customer data return and destruction shall be strictly limited to the direct fees received in the twelve (12) months preceding the claim.",
        "customer_friendly_clause": "Section 50.7 (Customer Version): Vendor shall indemnify, defend, and hold harmless customer and its affiliates from all losses, damages, and expenses arising out of customer data return and destruction.",
        "risk_level": "LOW" if var <= 2 else "MEDIUM" if var <= 5 else "HIGH",
        "negotiation_notes": "Standard commercial terms for Customer Data Return and Destruction. Review liability caps and mutual reciprocity before signing."
    },
}
