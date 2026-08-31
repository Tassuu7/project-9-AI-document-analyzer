"""PCI-DSS v4.0 Requirements Catalog."""
from typing import Dict, Any

PCIDSS_RULES: Dict[str, Dict[str, Any]] = {
    "PCI_REQ_1_01": {
        "req_id": "1.1",
        "title": "PCI-DSS v4.0 Requirement 1.1",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_1_02": {
        "req_id": "1.2",
        "title": "PCI-DSS v4.0 Requirement 1.2",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_1_03": {
        "req_id": "1.3",
        "title": "PCI-DSS v4.0 Requirement 1.3",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_1_04": {
        "req_id": "1.4",
        "title": "PCI-DSS v4.0 Requirement 1.4",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_1_05": {
        "req_id": "1.5",
        "title": "PCI-DSS v4.0 Requirement 1.5",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_1_06": {
        "req_id": "1.6",
        "title": "PCI-DSS v4.0 Requirement 1.6",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_1_07": {
        "req_id": "1.7",
        "title": "PCI-DSS v4.0 Requirement 1.7",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_1_08": {
        "req_id": "1.8",
        "title": "PCI-DSS v4.0 Requirement 1.8",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_1_09": {
        "req_id": "1.9",
        "title": "PCI-DSS v4.0 Requirement 1.9",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_1_10": {
        "req_id": "1.10",
        "title": "PCI-DSS v4.0 Requirement 1.10",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_2_01": {
        "req_id": "2.1",
        "title": "PCI-DSS v4.0 Requirement 2.1",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_2_02": {
        "req_id": "2.2",
        "title": "PCI-DSS v4.0 Requirement 2.2",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_2_03": {
        "req_id": "2.3",
        "title": "PCI-DSS v4.0 Requirement 2.3",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_2_04": {
        "req_id": "2.4",
        "title": "PCI-DSS v4.0 Requirement 2.4",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_2_05": {
        "req_id": "2.5",
        "title": "PCI-DSS v4.0 Requirement 2.5",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_2_06": {
        "req_id": "2.6",
        "title": "PCI-DSS v4.0 Requirement 2.6",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_2_07": {
        "req_id": "2.7",
        "title": "PCI-DSS v4.0 Requirement 2.7",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_2_08": {
        "req_id": "2.8",
        "title": "PCI-DSS v4.0 Requirement 2.8",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_2_09": {
        "req_id": "2.9",
        "title": "PCI-DSS v4.0 Requirement 2.9",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_2_10": {
        "req_id": "2.10",
        "title": "PCI-DSS v4.0 Requirement 2.10",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_3_01": {
        "req_id": "3.1",
        "title": "PCI-DSS v4.0 Requirement 3.1",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_3_02": {
        "req_id": "3.2",
        "title": "PCI-DSS v4.0 Requirement 3.2",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_3_03": {
        "req_id": "3.3",
        "title": "PCI-DSS v4.0 Requirement 3.3",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_3_04": {
        "req_id": "3.4",
        "title": "PCI-DSS v4.0 Requirement 3.4",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_3_05": {
        "req_id": "3.5",
        "title": "PCI-DSS v4.0 Requirement 3.5",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_3_06": {
        "req_id": "3.6",
        "title": "PCI-DSS v4.0 Requirement 3.6",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_3_07": {
        "req_id": "3.7",
        "title": "PCI-DSS v4.0 Requirement 3.7",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_3_08": {
        "req_id": "3.8",
        "title": "PCI-DSS v4.0 Requirement 3.8",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_3_09": {
        "req_id": "3.9",
        "title": "PCI-DSS v4.0 Requirement 3.9",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_3_10": {
        "req_id": "3.10",
        "title": "PCI-DSS v4.0 Requirement 3.10",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_4_01": {
        "req_id": "4.1",
        "title": "PCI-DSS v4.0 Requirement 4.1",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_4_02": {
        "req_id": "4.2",
        "title": "PCI-DSS v4.0 Requirement 4.2",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_4_03": {
        "req_id": "4.3",
        "title": "PCI-DSS v4.0 Requirement 4.3",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_4_04": {
        "req_id": "4.4",
        "title": "PCI-DSS v4.0 Requirement 4.4",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_4_05": {
        "req_id": "4.5",
        "title": "PCI-DSS v4.0 Requirement 4.5",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_4_06": {
        "req_id": "4.6",
        "title": "PCI-DSS v4.0 Requirement 4.6",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_4_07": {
        "req_id": "4.7",
        "title": "PCI-DSS v4.0 Requirement 4.7",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_4_08": {
        "req_id": "4.8",
        "title": "PCI-DSS v4.0 Requirement 4.8",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_4_09": {
        "req_id": "4.9",
        "title": "PCI-DSS v4.0 Requirement 4.9",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_4_10": {
        "req_id": "4.10",
        "title": "PCI-DSS v4.0 Requirement 4.10",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_5_01": {
        "req_id": "5.1",
        "title": "PCI-DSS v4.0 Requirement 5.1",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_5_02": {
        "req_id": "5.2",
        "title": "PCI-DSS v4.0 Requirement 5.2",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_5_03": {
        "req_id": "5.3",
        "title": "PCI-DSS v4.0 Requirement 5.3",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_5_04": {
        "req_id": "5.4",
        "title": "PCI-DSS v4.0 Requirement 5.4",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_5_05": {
        "req_id": "5.5",
        "title": "PCI-DSS v4.0 Requirement 5.5",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_5_06": {
        "req_id": "5.6",
        "title": "PCI-DSS v4.0 Requirement 5.6",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_5_07": {
        "req_id": "5.7",
        "title": "PCI-DSS v4.0 Requirement 5.7",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_5_08": {
        "req_id": "5.8",
        "title": "PCI-DSS v4.0 Requirement 5.8",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_5_09": {
        "req_id": "5.9",
        "title": "PCI-DSS v4.0 Requirement 5.9",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_5_10": {
        "req_id": "5.10",
        "title": "PCI-DSS v4.0 Requirement 5.10",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_6_01": {
        "req_id": "6.1",
        "title": "PCI-DSS v4.0 Requirement 6.1",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_6_02": {
        "req_id": "6.2",
        "title": "PCI-DSS v4.0 Requirement 6.2",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_6_03": {
        "req_id": "6.3",
        "title": "PCI-DSS v4.0 Requirement 6.3",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_6_04": {
        "req_id": "6.4",
        "title": "PCI-DSS v4.0 Requirement 6.4",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_6_05": {
        "req_id": "6.5",
        "title": "PCI-DSS v4.0 Requirement 6.5",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_6_06": {
        "req_id": "6.6",
        "title": "PCI-DSS v4.0 Requirement 6.6",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_6_07": {
        "req_id": "6.7",
        "title": "PCI-DSS v4.0 Requirement 6.7",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_6_08": {
        "req_id": "6.8",
        "title": "PCI-DSS v4.0 Requirement 6.8",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_6_09": {
        "req_id": "6.9",
        "title": "PCI-DSS v4.0 Requirement 6.9",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_6_10": {
        "req_id": "6.10",
        "title": "PCI-DSS v4.0 Requirement 6.10",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_7_01": {
        "req_id": "7.1",
        "title": "PCI-DSS v4.0 Requirement 7.1",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_7_02": {
        "req_id": "7.2",
        "title": "PCI-DSS v4.0 Requirement 7.2",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_7_03": {
        "req_id": "7.3",
        "title": "PCI-DSS v4.0 Requirement 7.3",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_7_04": {
        "req_id": "7.4",
        "title": "PCI-DSS v4.0 Requirement 7.4",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_7_05": {
        "req_id": "7.5",
        "title": "PCI-DSS v4.0 Requirement 7.5",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_7_06": {
        "req_id": "7.6",
        "title": "PCI-DSS v4.0 Requirement 7.6",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_7_07": {
        "req_id": "7.7",
        "title": "PCI-DSS v4.0 Requirement 7.7",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_7_08": {
        "req_id": "7.8",
        "title": "PCI-DSS v4.0 Requirement 7.8",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_7_09": {
        "req_id": "7.9",
        "title": "PCI-DSS v4.0 Requirement 7.9",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_7_10": {
        "req_id": "7.10",
        "title": "PCI-DSS v4.0 Requirement 7.10",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_8_01": {
        "req_id": "8.1",
        "title": "PCI-DSS v4.0 Requirement 8.1",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_8_02": {
        "req_id": "8.2",
        "title": "PCI-DSS v4.0 Requirement 8.2",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_8_03": {
        "req_id": "8.3",
        "title": "PCI-DSS v4.0 Requirement 8.3",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_8_04": {
        "req_id": "8.4",
        "title": "PCI-DSS v4.0 Requirement 8.4",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_8_05": {
        "req_id": "8.5",
        "title": "PCI-DSS v4.0 Requirement 8.5",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_8_06": {
        "req_id": "8.6",
        "title": "PCI-DSS v4.0 Requirement 8.6",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_8_07": {
        "req_id": "8.7",
        "title": "PCI-DSS v4.0 Requirement 8.7",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_8_08": {
        "req_id": "8.8",
        "title": "PCI-DSS v4.0 Requirement 8.8",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_8_09": {
        "req_id": "8.9",
        "title": "PCI-DSS v4.0 Requirement 8.9",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_8_10": {
        "req_id": "8.10",
        "title": "PCI-DSS v4.0 Requirement 8.10",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_9_01": {
        "req_id": "9.1",
        "title": "PCI-DSS v4.0 Requirement 9.1",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_9_02": {
        "req_id": "9.2",
        "title": "PCI-DSS v4.0 Requirement 9.2",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_9_03": {
        "req_id": "9.3",
        "title": "PCI-DSS v4.0 Requirement 9.3",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_9_04": {
        "req_id": "9.4",
        "title": "PCI-DSS v4.0 Requirement 9.4",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_9_05": {
        "req_id": "9.5",
        "title": "PCI-DSS v4.0 Requirement 9.5",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_9_06": {
        "req_id": "9.6",
        "title": "PCI-DSS v4.0 Requirement 9.6",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_9_07": {
        "req_id": "9.7",
        "title": "PCI-DSS v4.0 Requirement 9.7",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_9_08": {
        "req_id": "9.8",
        "title": "PCI-DSS v4.0 Requirement 9.8",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_9_09": {
        "req_id": "9.9",
        "title": "PCI-DSS v4.0 Requirement 9.9",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_9_10": {
        "req_id": "9.10",
        "title": "PCI-DSS v4.0 Requirement 9.10",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_10_01": {
        "req_id": "10.1",
        "title": "PCI-DSS v4.0 Requirement 10.1",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_10_02": {
        "req_id": "10.2",
        "title": "PCI-DSS v4.0 Requirement 10.2",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_10_03": {
        "req_id": "10.3",
        "title": "PCI-DSS v4.0 Requirement 10.3",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_10_04": {
        "req_id": "10.4",
        "title": "PCI-DSS v4.0 Requirement 10.4",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_10_05": {
        "req_id": "10.5",
        "title": "PCI-DSS v4.0 Requirement 10.5",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_10_06": {
        "req_id": "10.6",
        "title": "PCI-DSS v4.0 Requirement 10.6",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_10_07": {
        "req_id": "10.7",
        "title": "PCI-DSS v4.0 Requirement 10.7",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_10_08": {
        "req_id": "10.8",
        "title": "PCI-DSS v4.0 Requirement 10.8",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_10_09": {
        "req_id": "10.9",
        "title": "PCI-DSS v4.0 Requirement 10.9",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_10_10": {
        "req_id": "10.10",
        "title": "PCI-DSS v4.0 Requirement 10.10",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_11_01": {
        "req_id": "11.1",
        "title": "PCI-DSS v4.0 Requirement 11.1",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_11_02": {
        "req_id": "11.2",
        "title": "PCI-DSS v4.0 Requirement 11.2",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_11_03": {
        "req_id": "11.3",
        "title": "PCI-DSS v4.0 Requirement 11.3",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_11_04": {
        "req_id": "11.4",
        "title": "PCI-DSS v4.0 Requirement 11.4",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_11_05": {
        "req_id": "11.5",
        "title": "PCI-DSS v4.0 Requirement 11.5",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_11_06": {
        "req_id": "11.6",
        "title": "PCI-DSS v4.0 Requirement 11.6",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_11_07": {
        "req_id": "11.7",
        "title": "PCI-DSS v4.0 Requirement 11.7",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_11_08": {
        "req_id": "11.8",
        "title": "PCI-DSS v4.0 Requirement 11.8",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_11_09": {
        "req_id": "11.9",
        "title": "PCI-DSS v4.0 Requirement 11.9",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_11_10": {
        "req_id": "11.10",
        "title": "PCI-DSS v4.0 Requirement 11.10",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_12_01": {
        "req_id": "12.1",
        "title": "PCI-DSS v4.0 Requirement 12.1",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_12_02": {
        "req_id": "12.2",
        "title": "PCI-DSS v4.0 Requirement 12.2",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_12_03": {
        "req_id": "12.3",
        "title": "PCI-DSS v4.0 Requirement 12.3",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_12_04": {
        "req_id": "12.4",
        "title": "PCI-DSS v4.0 Requirement 12.4",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_12_05": {
        "req_id": "12.5",
        "title": "PCI-DSS v4.0 Requirement 12.5",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_12_06": {
        "req_id": "12.6",
        "title": "PCI-DSS v4.0 Requirement 12.6",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_12_07": {
        "req_id": "12.7",
        "title": "PCI-DSS v4.0 Requirement 12.7",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_12_08": {
        "req_id": "12.8",
        "title": "PCI-DSS v4.0 Requirement 12.8",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_12_09": {
        "req_id": "12.9",
        "title": "PCI-DSS v4.0 Requirement 12.9",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
    "PCI_REQ_12_10": {
        "req_id": "12.10",
        "title": "PCI-DSS v4.0 Requirement 12.10",
        "description": "Protects Cardholder Data Environment (CDE) and Primary Account Numbers (PAN).",
        "inspection_steps": [
            "Verify firewall and router configurations restrict unauthorized traffic to CDE.",
            "Ensure vendor-supplied defaults for passwords and security parameters are changed.",
            "Confirm primary account numbers are truncated or masked when displayed or stored.",
            "Verify sensitive authentication data (CVV, CVC, PIN block) is never stored post-authorization.",
            "Ensure strong cryptography and security protocols are used for card data in transit."
        ],
        "severity": "CRITICAL" if major in [3, 4, 7, 8] else "HIGH",
        "penalty": 35.0 if major in [3, 4, 7, 8] else 18.0,
        "remediation_guideline": "Immediately purge prohibited CVV/PIN data and implement tokenization for payment processing."
    },
}
