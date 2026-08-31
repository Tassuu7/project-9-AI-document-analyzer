"""Financial GAAP and IFRS Terms Master Catalog."""
from typing import Dict, Any

FINANCIAL_TERMS_BANK: Dict[str, Dict[str, Any]] = {
    "FIN_METRIC_001": {
        "id": 1,
        "term_name": "Financial Reporting Metric #1",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_002": {
        "id": 2,
        "term_name": "Financial Reporting Metric #2",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_003": {
        "id": 3,
        "term_name": "Financial Reporting Metric #3",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_004": {
        "id": 4,
        "term_name": "Financial Reporting Metric #4",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_005": {
        "id": 5,
        "term_name": "Financial Reporting Metric #5",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_006": {
        "id": 6,
        "term_name": "Financial Reporting Metric #6",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_007": {
        "id": 7,
        "term_name": "Financial Reporting Metric #7",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_008": {
        "id": 8,
        "term_name": "Financial Reporting Metric #8",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_009": {
        "id": 9,
        "term_name": "Financial Reporting Metric #9",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_010": {
        "id": 10,
        "term_name": "Financial Reporting Metric #10",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_011": {
        "id": 11,
        "term_name": "Financial Reporting Metric #11",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_012": {
        "id": 12,
        "term_name": "Financial Reporting Metric #12",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_013": {
        "id": 13,
        "term_name": "Financial Reporting Metric #13",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_014": {
        "id": 14,
        "term_name": "Financial Reporting Metric #14",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_015": {
        "id": 15,
        "term_name": "Financial Reporting Metric #15",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_016": {
        "id": 16,
        "term_name": "Financial Reporting Metric #16",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_017": {
        "id": 17,
        "term_name": "Financial Reporting Metric #17",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_018": {
        "id": 18,
        "term_name": "Financial Reporting Metric #18",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_019": {
        "id": 19,
        "term_name": "Financial Reporting Metric #19",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_020": {
        "id": 20,
        "term_name": "Financial Reporting Metric #20",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_021": {
        "id": 21,
        "term_name": "Financial Reporting Metric #21",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_022": {
        "id": 22,
        "term_name": "Financial Reporting Metric #22",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_023": {
        "id": 23,
        "term_name": "Financial Reporting Metric #23",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_024": {
        "id": 24,
        "term_name": "Financial Reporting Metric #24",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_025": {
        "id": 25,
        "term_name": "Financial Reporting Metric #25",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_026": {
        "id": 26,
        "term_name": "Financial Reporting Metric #26",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_027": {
        "id": 27,
        "term_name": "Financial Reporting Metric #27",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_028": {
        "id": 28,
        "term_name": "Financial Reporting Metric #28",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_029": {
        "id": 29,
        "term_name": "Financial Reporting Metric #29",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_030": {
        "id": 30,
        "term_name": "Financial Reporting Metric #30",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_031": {
        "id": 31,
        "term_name": "Financial Reporting Metric #31",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_032": {
        "id": 32,
        "term_name": "Financial Reporting Metric #32",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_033": {
        "id": 33,
        "term_name": "Financial Reporting Metric #33",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_034": {
        "id": 34,
        "term_name": "Financial Reporting Metric #34",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_035": {
        "id": 35,
        "term_name": "Financial Reporting Metric #35",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_036": {
        "id": 36,
        "term_name": "Financial Reporting Metric #36",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_037": {
        "id": 37,
        "term_name": "Financial Reporting Metric #37",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_038": {
        "id": 38,
        "term_name": "Financial Reporting Metric #38",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_039": {
        "id": 39,
        "term_name": "Financial Reporting Metric #39",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_040": {
        "id": 40,
        "term_name": "Financial Reporting Metric #40",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_041": {
        "id": 41,
        "term_name": "Financial Reporting Metric #41",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_042": {
        "id": 42,
        "term_name": "Financial Reporting Metric #42",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_043": {
        "id": 43,
        "term_name": "Financial Reporting Metric #43",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_044": {
        "id": 44,
        "term_name": "Financial Reporting Metric #44",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_045": {
        "id": 45,
        "term_name": "Financial Reporting Metric #45",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_046": {
        "id": 46,
        "term_name": "Financial Reporting Metric #46",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_047": {
        "id": 47,
        "term_name": "Financial Reporting Metric #47",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_048": {
        "id": 48,
        "term_name": "Financial Reporting Metric #48",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_049": {
        "id": 49,
        "term_name": "Financial Reporting Metric #49",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_050": {
        "id": 50,
        "term_name": "Financial Reporting Metric #50",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_051": {
        "id": 51,
        "term_name": "Financial Reporting Metric #51",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_052": {
        "id": 52,
        "term_name": "Financial Reporting Metric #52",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_053": {
        "id": 53,
        "term_name": "Financial Reporting Metric #53",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_054": {
        "id": 54,
        "term_name": "Financial Reporting Metric #54",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_055": {
        "id": 55,
        "term_name": "Financial Reporting Metric #55",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_056": {
        "id": 56,
        "term_name": "Financial Reporting Metric #56",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_057": {
        "id": 57,
        "term_name": "Financial Reporting Metric #57",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_058": {
        "id": 58,
        "term_name": "Financial Reporting Metric #58",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_059": {
        "id": 59,
        "term_name": "Financial Reporting Metric #59",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_060": {
        "id": 60,
        "term_name": "Financial Reporting Metric #60",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_061": {
        "id": 61,
        "term_name": "Financial Reporting Metric #61",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_062": {
        "id": 62,
        "term_name": "Financial Reporting Metric #62",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_063": {
        "id": 63,
        "term_name": "Financial Reporting Metric #63",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_064": {
        "id": 64,
        "term_name": "Financial Reporting Metric #64",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_065": {
        "id": 65,
        "term_name": "Financial Reporting Metric #65",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_066": {
        "id": 66,
        "term_name": "Financial Reporting Metric #66",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_067": {
        "id": 67,
        "term_name": "Financial Reporting Metric #67",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_068": {
        "id": 68,
        "term_name": "Financial Reporting Metric #68",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_069": {
        "id": 69,
        "term_name": "Financial Reporting Metric #69",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_070": {
        "id": 70,
        "term_name": "Financial Reporting Metric #70",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_071": {
        "id": 71,
        "term_name": "Financial Reporting Metric #71",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_072": {
        "id": 72,
        "term_name": "Financial Reporting Metric #72",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_073": {
        "id": 73,
        "term_name": "Financial Reporting Metric #73",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_074": {
        "id": 74,
        "term_name": "Financial Reporting Metric #74",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_075": {
        "id": 75,
        "term_name": "Financial Reporting Metric #75",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_076": {
        "id": 76,
        "term_name": "Financial Reporting Metric #76",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_077": {
        "id": 77,
        "term_name": "Financial Reporting Metric #77",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_078": {
        "id": 78,
        "term_name": "Financial Reporting Metric #78",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_079": {
        "id": 79,
        "term_name": "Financial Reporting Metric #79",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_080": {
        "id": 80,
        "term_name": "Financial Reporting Metric #80",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_081": {
        "id": 81,
        "term_name": "Financial Reporting Metric #81",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_082": {
        "id": 82,
        "term_name": "Financial Reporting Metric #82",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_083": {
        "id": 83,
        "term_name": "Financial Reporting Metric #83",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_084": {
        "id": 84,
        "term_name": "Financial Reporting Metric #84",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_085": {
        "id": 85,
        "term_name": "Financial Reporting Metric #85",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_086": {
        "id": 86,
        "term_name": "Financial Reporting Metric #86",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_087": {
        "id": 87,
        "term_name": "Financial Reporting Metric #87",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_088": {
        "id": 88,
        "term_name": "Financial Reporting Metric #88",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_089": {
        "id": 89,
        "term_name": "Financial Reporting Metric #89",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_090": {
        "id": 90,
        "term_name": "Financial Reporting Metric #90",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_091": {
        "id": 91,
        "term_name": "Financial Reporting Metric #91",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_092": {
        "id": 92,
        "term_name": "Financial Reporting Metric #92",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_093": {
        "id": 93,
        "term_name": "Financial Reporting Metric #93",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_094": {
        "id": 94,
        "term_name": "Financial Reporting Metric #94",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_095": {
        "id": 95,
        "term_name": "Financial Reporting Metric #95",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_096": {
        "id": 96,
        "term_name": "Financial Reporting Metric #96",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_097": {
        "id": 97,
        "term_name": "Financial Reporting Metric #97",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_098": {
        "id": 98,
        "term_name": "Financial Reporting Metric #98",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_099": {
        "id": 99,
        "term_name": "Financial Reporting Metric #99",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_100": {
        "id": 100,
        "term_name": "Financial Reporting Metric #100",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_101": {
        "id": 101,
        "term_name": "Financial Reporting Metric #101",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_102": {
        "id": 102,
        "term_name": "Financial Reporting Metric #102",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_103": {
        "id": 103,
        "term_name": "Financial Reporting Metric #103",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_104": {
        "id": 104,
        "term_name": "Financial Reporting Metric #104",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_105": {
        "id": 105,
        "term_name": "Financial Reporting Metric #105",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_106": {
        "id": 106,
        "term_name": "Financial Reporting Metric #106",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_107": {
        "id": 107,
        "term_name": "Financial Reporting Metric #107",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_108": {
        "id": 108,
        "term_name": "Financial Reporting Metric #108",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_109": {
        "id": 109,
        "term_name": "Financial Reporting Metric #109",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_110": {
        "id": 110,
        "term_name": "Financial Reporting Metric #110",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_111": {
        "id": 111,
        "term_name": "Financial Reporting Metric #111",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_112": {
        "id": 112,
        "term_name": "Financial Reporting Metric #112",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_113": {
        "id": 113,
        "term_name": "Financial Reporting Metric #113",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_114": {
        "id": 114,
        "term_name": "Financial Reporting Metric #114",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_115": {
        "id": 115,
        "term_name": "Financial Reporting Metric #115",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_116": {
        "id": 116,
        "term_name": "Financial Reporting Metric #116",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_117": {
        "id": 117,
        "term_name": "Financial Reporting Metric #117",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_118": {
        "id": 118,
        "term_name": "Financial Reporting Metric #118",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_119": {
        "id": 119,
        "term_name": "Financial Reporting Metric #119",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_120": {
        "id": 120,
        "term_name": "Financial Reporting Metric #120",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_121": {
        "id": 121,
        "term_name": "Financial Reporting Metric #121",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_122": {
        "id": 122,
        "term_name": "Financial Reporting Metric #122",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_123": {
        "id": 123,
        "term_name": "Financial Reporting Metric #123",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_124": {
        "id": 124,
        "term_name": "Financial Reporting Metric #124",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_125": {
        "id": 125,
        "term_name": "Financial Reporting Metric #125",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_126": {
        "id": 126,
        "term_name": "Financial Reporting Metric #126",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_127": {
        "id": 127,
        "term_name": "Financial Reporting Metric #127",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_128": {
        "id": 128,
        "term_name": "Financial Reporting Metric #128",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_129": {
        "id": 129,
        "term_name": "Financial Reporting Metric #129",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_130": {
        "id": 130,
        "term_name": "Financial Reporting Metric #130",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_131": {
        "id": 131,
        "term_name": "Financial Reporting Metric #131",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_132": {
        "id": 132,
        "term_name": "Financial Reporting Metric #132",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_133": {
        "id": 133,
        "term_name": "Financial Reporting Metric #133",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_134": {
        "id": 134,
        "term_name": "Financial Reporting Metric #134",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_135": {
        "id": 135,
        "term_name": "Financial Reporting Metric #135",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_136": {
        "id": 136,
        "term_name": "Financial Reporting Metric #136",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_137": {
        "id": 137,
        "term_name": "Financial Reporting Metric #137",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_138": {
        "id": 138,
        "term_name": "Financial Reporting Metric #138",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_139": {
        "id": 139,
        "term_name": "Financial Reporting Metric #139",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_140": {
        "id": 140,
        "term_name": "Financial Reporting Metric #140",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_141": {
        "id": 141,
        "term_name": "Financial Reporting Metric #141",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_142": {
        "id": 142,
        "term_name": "Financial Reporting Metric #142",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_143": {
        "id": 143,
        "term_name": "Financial Reporting Metric #143",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_144": {
        "id": 144,
        "term_name": "Financial Reporting Metric #144",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_145": {
        "id": 145,
        "term_name": "Financial Reporting Metric #145",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_146": {
        "id": 146,
        "term_name": "Financial Reporting Metric #146",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_147": {
        "id": 147,
        "term_name": "Financial Reporting Metric #147",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_148": {
        "id": 148,
        "term_name": "Financial Reporting Metric #148",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_149": {
        "id": 149,
        "term_name": "Financial Reporting Metric #149",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_150": {
        "id": 150,
        "term_name": "Financial Reporting Metric #150",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_151": {
        "id": 151,
        "term_name": "Financial Reporting Metric #151",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_152": {
        "id": 152,
        "term_name": "Financial Reporting Metric #152",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_153": {
        "id": 153,
        "term_name": "Financial Reporting Metric #153",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_154": {
        "id": 154,
        "term_name": "Financial Reporting Metric #154",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_155": {
        "id": 155,
        "term_name": "Financial Reporting Metric #155",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_156": {
        "id": 156,
        "term_name": "Financial Reporting Metric #156",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_157": {
        "id": 157,
        "term_name": "Financial Reporting Metric #157",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_158": {
        "id": 158,
        "term_name": "Financial Reporting Metric #158",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_159": {
        "id": 159,
        "term_name": "Financial Reporting Metric #159",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_160": {
        "id": 160,
        "term_name": "Financial Reporting Metric #160",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_161": {
        "id": 161,
        "term_name": "Financial Reporting Metric #161",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_162": {
        "id": 162,
        "term_name": "Financial Reporting Metric #162",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_163": {
        "id": 163,
        "term_name": "Financial Reporting Metric #163",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_164": {
        "id": 164,
        "term_name": "Financial Reporting Metric #164",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_165": {
        "id": 165,
        "term_name": "Financial Reporting Metric #165",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_166": {
        "id": 166,
        "term_name": "Financial Reporting Metric #166",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_167": {
        "id": 167,
        "term_name": "Financial Reporting Metric #167",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_168": {
        "id": 168,
        "term_name": "Financial Reporting Metric #168",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_169": {
        "id": 169,
        "term_name": "Financial Reporting Metric #169",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_170": {
        "id": 170,
        "term_name": "Financial Reporting Metric #170",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_171": {
        "id": 171,
        "term_name": "Financial Reporting Metric #171",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_172": {
        "id": 172,
        "term_name": "Financial Reporting Metric #172",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_173": {
        "id": 173,
        "term_name": "Financial Reporting Metric #173",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_174": {
        "id": 174,
        "term_name": "Financial Reporting Metric #174",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_175": {
        "id": 175,
        "term_name": "Financial Reporting Metric #175",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_176": {
        "id": 176,
        "term_name": "Financial Reporting Metric #176",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_177": {
        "id": 177,
        "term_name": "Financial Reporting Metric #177",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_178": {
        "id": 178,
        "term_name": "Financial Reporting Metric #178",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_179": {
        "id": 179,
        "term_name": "Financial Reporting Metric #179",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_180": {
        "id": 180,
        "term_name": "Financial Reporting Metric #180",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_181": {
        "id": 181,
        "term_name": "Financial Reporting Metric #181",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_182": {
        "id": 182,
        "term_name": "Financial Reporting Metric #182",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_183": {
        "id": 183,
        "term_name": "Financial Reporting Metric #183",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_184": {
        "id": 184,
        "term_name": "Financial Reporting Metric #184",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_185": {
        "id": 185,
        "term_name": "Financial Reporting Metric #185",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_186": {
        "id": 186,
        "term_name": "Financial Reporting Metric #186",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_187": {
        "id": 187,
        "term_name": "Financial Reporting Metric #187",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_188": {
        "id": 188,
        "term_name": "Financial Reporting Metric #188",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_189": {
        "id": 189,
        "term_name": "Financial Reporting Metric #189",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_190": {
        "id": 190,
        "term_name": "Financial Reporting Metric #190",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_191": {
        "id": 191,
        "term_name": "Financial Reporting Metric #191",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_192": {
        "id": 192,
        "term_name": "Financial Reporting Metric #192",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_193": {
        "id": 193,
        "term_name": "Financial Reporting Metric #193",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_194": {
        "id": 194,
        "term_name": "Financial Reporting Metric #194",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_195": {
        "id": 195,
        "term_name": "Financial Reporting Metric #195",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_196": {
        "id": 196,
        "term_name": "Financial Reporting Metric #196",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_197": {
        "id": 197,
        "term_name": "Financial Reporting Metric #197",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_198": {
        "id": 198,
        "term_name": "Financial Reporting Metric #198",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_199": {
        "id": 199,
        "term_name": "Financial Reporting Metric #199",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
    "FIN_METRIC_200": {
        "id": 200,
        "term_name": "Financial Reporting Metric #200",
        "accounting_standard": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / IASB",
        "reporting_category": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Verify revenue recognition criteria are satisfied upon transfer of promised goods or services.",
            "Validate allowance for doubtful accounts and expected credit loss estimations.",
            "Ensure capitalization of research & development assets adheres to accounting standards.",
            "Inspect debt covenants, liquidity ratios, and working capital requirements.",
            "Confirm fair value measurement of financial instruments and goodwill impairment."
        ],
        "risk_rating": "HIGH" if idx % 4 == 0 else "NORMAL"
    },
}
