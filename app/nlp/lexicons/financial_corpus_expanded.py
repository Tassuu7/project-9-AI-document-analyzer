"""Expanded Financial Taxonomy & Accounting Rules Catalog (500 Metrics)."""
from typing import Dict, Any

EXPANDED_FINANCIAL_METRICS: Dict[str, Dict[str, Any]] = {
    "FIN_METRIC_EXP_0001": {
        "metric_id": "FIN-0001",
        "name": "Financial Reporting Line Item #1",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0002": {
        "metric_id": "FIN-0002",
        "name": "Financial Reporting Line Item #2",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0003": {
        "metric_id": "FIN-0003",
        "name": "Financial Reporting Line Item #3",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0004": {
        "metric_id": "FIN-0004",
        "name": "Financial Reporting Line Item #4",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0005": {
        "metric_id": "FIN-0005",
        "name": "Financial Reporting Line Item #5",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0006": {
        "metric_id": "FIN-0006",
        "name": "Financial Reporting Line Item #6",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0007": {
        "metric_id": "FIN-0007",
        "name": "Financial Reporting Line Item #7",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0008": {
        "metric_id": "FIN-0008",
        "name": "Financial Reporting Line Item #8",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0009": {
        "metric_id": "FIN-0009",
        "name": "Financial Reporting Line Item #9",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0010": {
        "metric_id": "FIN-0010",
        "name": "Financial Reporting Line Item #10",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0011": {
        "metric_id": "FIN-0011",
        "name": "Financial Reporting Line Item #11",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0012": {
        "metric_id": "FIN-0012",
        "name": "Financial Reporting Line Item #12",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0013": {
        "metric_id": "FIN-0013",
        "name": "Financial Reporting Line Item #13",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0014": {
        "metric_id": "FIN-0014",
        "name": "Financial Reporting Line Item #14",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0015": {
        "metric_id": "FIN-0015",
        "name": "Financial Reporting Line Item #15",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0016": {
        "metric_id": "FIN-0016",
        "name": "Financial Reporting Line Item #16",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0017": {
        "metric_id": "FIN-0017",
        "name": "Financial Reporting Line Item #17",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0018": {
        "metric_id": "FIN-0018",
        "name": "Financial Reporting Line Item #18",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0019": {
        "metric_id": "FIN-0019",
        "name": "Financial Reporting Line Item #19",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0020": {
        "metric_id": "FIN-0020",
        "name": "Financial Reporting Line Item #20",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0021": {
        "metric_id": "FIN-0021",
        "name": "Financial Reporting Line Item #21",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0022": {
        "metric_id": "FIN-0022",
        "name": "Financial Reporting Line Item #22",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0023": {
        "metric_id": "FIN-0023",
        "name": "Financial Reporting Line Item #23",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0024": {
        "metric_id": "FIN-0024",
        "name": "Financial Reporting Line Item #24",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0025": {
        "metric_id": "FIN-0025",
        "name": "Financial Reporting Line Item #25",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0026": {
        "metric_id": "FIN-0026",
        "name": "Financial Reporting Line Item #26",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0027": {
        "metric_id": "FIN-0027",
        "name": "Financial Reporting Line Item #27",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0028": {
        "metric_id": "FIN-0028",
        "name": "Financial Reporting Line Item #28",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0029": {
        "metric_id": "FIN-0029",
        "name": "Financial Reporting Line Item #29",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0030": {
        "metric_id": "FIN-0030",
        "name": "Financial Reporting Line Item #30",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0031": {
        "metric_id": "FIN-0031",
        "name": "Financial Reporting Line Item #31",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0032": {
        "metric_id": "FIN-0032",
        "name": "Financial Reporting Line Item #32",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0033": {
        "metric_id": "FIN-0033",
        "name": "Financial Reporting Line Item #33",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0034": {
        "metric_id": "FIN-0034",
        "name": "Financial Reporting Line Item #34",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0035": {
        "metric_id": "FIN-0035",
        "name": "Financial Reporting Line Item #35",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0036": {
        "metric_id": "FIN-0036",
        "name": "Financial Reporting Line Item #36",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0037": {
        "metric_id": "FIN-0037",
        "name": "Financial Reporting Line Item #37",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0038": {
        "metric_id": "FIN-0038",
        "name": "Financial Reporting Line Item #38",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0039": {
        "metric_id": "FIN-0039",
        "name": "Financial Reporting Line Item #39",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0040": {
        "metric_id": "FIN-0040",
        "name": "Financial Reporting Line Item #40",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0041": {
        "metric_id": "FIN-0041",
        "name": "Financial Reporting Line Item #41",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0042": {
        "metric_id": "FIN-0042",
        "name": "Financial Reporting Line Item #42",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0043": {
        "metric_id": "FIN-0043",
        "name": "Financial Reporting Line Item #43",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0044": {
        "metric_id": "FIN-0044",
        "name": "Financial Reporting Line Item #44",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0045": {
        "metric_id": "FIN-0045",
        "name": "Financial Reporting Line Item #45",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0046": {
        "metric_id": "FIN-0046",
        "name": "Financial Reporting Line Item #46",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0047": {
        "metric_id": "FIN-0047",
        "name": "Financial Reporting Line Item #47",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0048": {
        "metric_id": "FIN-0048",
        "name": "Financial Reporting Line Item #48",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0049": {
        "metric_id": "FIN-0049",
        "name": "Financial Reporting Line Item #49",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0050": {
        "metric_id": "FIN-0050",
        "name": "Financial Reporting Line Item #50",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0051": {
        "metric_id": "FIN-0051",
        "name": "Financial Reporting Line Item #51",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0052": {
        "metric_id": "FIN-0052",
        "name": "Financial Reporting Line Item #52",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0053": {
        "metric_id": "FIN-0053",
        "name": "Financial Reporting Line Item #53",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0054": {
        "metric_id": "FIN-0054",
        "name": "Financial Reporting Line Item #54",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0055": {
        "metric_id": "FIN-0055",
        "name": "Financial Reporting Line Item #55",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0056": {
        "metric_id": "FIN-0056",
        "name": "Financial Reporting Line Item #56",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0057": {
        "metric_id": "FIN-0057",
        "name": "Financial Reporting Line Item #57",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0058": {
        "metric_id": "FIN-0058",
        "name": "Financial Reporting Line Item #58",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0059": {
        "metric_id": "FIN-0059",
        "name": "Financial Reporting Line Item #59",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0060": {
        "metric_id": "FIN-0060",
        "name": "Financial Reporting Line Item #60",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0061": {
        "metric_id": "FIN-0061",
        "name": "Financial Reporting Line Item #61",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0062": {
        "metric_id": "FIN-0062",
        "name": "Financial Reporting Line Item #62",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0063": {
        "metric_id": "FIN-0063",
        "name": "Financial Reporting Line Item #63",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0064": {
        "metric_id": "FIN-0064",
        "name": "Financial Reporting Line Item #64",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0065": {
        "metric_id": "FIN-0065",
        "name": "Financial Reporting Line Item #65",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0066": {
        "metric_id": "FIN-0066",
        "name": "Financial Reporting Line Item #66",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0067": {
        "metric_id": "FIN-0067",
        "name": "Financial Reporting Line Item #67",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0068": {
        "metric_id": "FIN-0068",
        "name": "Financial Reporting Line Item #68",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0069": {
        "metric_id": "FIN-0069",
        "name": "Financial Reporting Line Item #69",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0070": {
        "metric_id": "FIN-0070",
        "name": "Financial Reporting Line Item #70",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0071": {
        "metric_id": "FIN-0071",
        "name": "Financial Reporting Line Item #71",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0072": {
        "metric_id": "FIN-0072",
        "name": "Financial Reporting Line Item #72",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0073": {
        "metric_id": "FIN-0073",
        "name": "Financial Reporting Line Item #73",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0074": {
        "metric_id": "FIN-0074",
        "name": "Financial Reporting Line Item #74",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0075": {
        "metric_id": "FIN-0075",
        "name": "Financial Reporting Line Item #75",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0076": {
        "metric_id": "FIN-0076",
        "name": "Financial Reporting Line Item #76",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0077": {
        "metric_id": "FIN-0077",
        "name": "Financial Reporting Line Item #77",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0078": {
        "metric_id": "FIN-0078",
        "name": "Financial Reporting Line Item #78",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0079": {
        "metric_id": "FIN-0079",
        "name": "Financial Reporting Line Item #79",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0080": {
        "metric_id": "FIN-0080",
        "name": "Financial Reporting Line Item #80",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0081": {
        "metric_id": "FIN-0081",
        "name": "Financial Reporting Line Item #81",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0082": {
        "metric_id": "FIN-0082",
        "name": "Financial Reporting Line Item #82",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0083": {
        "metric_id": "FIN-0083",
        "name": "Financial Reporting Line Item #83",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0084": {
        "metric_id": "FIN-0084",
        "name": "Financial Reporting Line Item #84",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0085": {
        "metric_id": "FIN-0085",
        "name": "Financial Reporting Line Item #85",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0086": {
        "metric_id": "FIN-0086",
        "name": "Financial Reporting Line Item #86",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0087": {
        "metric_id": "FIN-0087",
        "name": "Financial Reporting Line Item #87",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0088": {
        "metric_id": "FIN-0088",
        "name": "Financial Reporting Line Item #88",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0089": {
        "metric_id": "FIN-0089",
        "name": "Financial Reporting Line Item #89",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0090": {
        "metric_id": "FIN-0090",
        "name": "Financial Reporting Line Item #90",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0091": {
        "metric_id": "FIN-0091",
        "name": "Financial Reporting Line Item #91",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0092": {
        "metric_id": "FIN-0092",
        "name": "Financial Reporting Line Item #92",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0093": {
        "metric_id": "FIN-0093",
        "name": "Financial Reporting Line Item #93",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0094": {
        "metric_id": "FIN-0094",
        "name": "Financial Reporting Line Item #94",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0095": {
        "metric_id": "FIN-0095",
        "name": "Financial Reporting Line Item #95",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0096": {
        "metric_id": "FIN-0096",
        "name": "Financial Reporting Line Item #96",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0097": {
        "metric_id": "FIN-0097",
        "name": "Financial Reporting Line Item #97",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0098": {
        "metric_id": "FIN-0098",
        "name": "Financial Reporting Line Item #98",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0099": {
        "metric_id": "FIN-0099",
        "name": "Financial Reporting Line Item #99",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0100": {
        "metric_id": "FIN-0100",
        "name": "Financial Reporting Line Item #100",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0101": {
        "metric_id": "FIN-0101",
        "name": "Financial Reporting Line Item #101",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0102": {
        "metric_id": "FIN-0102",
        "name": "Financial Reporting Line Item #102",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0103": {
        "metric_id": "FIN-0103",
        "name": "Financial Reporting Line Item #103",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0104": {
        "metric_id": "FIN-0104",
        "name": "Financial Reporting Line Item #104",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0105": {
        "metric_id": "FIN-0105",
        "name": "Financial Reporting Line Item #105",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0106": {
        "metric_id": "FIN-0106",
        "name": "Financial Reporting Line Item #106",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0107": {
        "metric_id": "FIN-0107",
        "name": "Financial Reporting Line Item #107",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0108": {
        "metric_id": "FIN-0108",
        "name": "Financial Reporting Line Item #108",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0109": {
        "metric_id": "FIN-0109",
        "name": "Financial Reporting Line Item #109",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0110": {
        "metric_id": "FIN-0110",
        "name": "Financial Reporting Line Item #110",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0111": {
        "metric_id": "FIN-0111",
        "name": "Financial Reporting Line Item #111",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0112": {
        "metric_id": "FIN-0112",
        "name": "Financial Reporting Line Item #112",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0113": {
        "metric_id": "FIN-0113",
        "name": "Financial Reporting Line Item #113",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0114": {
        "metric_id": "FIN-0114",
        "name": "Financial Reporting Line Item #114",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0115": {
        "metric_id": "FIN-0115",
        "name": "Financial Reporting Line Item #115",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0116": {
        "metric_id": "FIN-0116",
        "name": "Financial Reporting Line Item #116",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0117": {
        "metric_id": "FIN-0117",
        "name": "Financial Reporting Line Item #117",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0118": {
        "metric_id": "FIN-0118",
        "name": "Financial Reporting Line Item #118",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0119": {
        "metric_id": "FIN-0119",
        "name": "Financial Reporting Line Item #119",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0120": {
        "metric_id": "FIN-0120",
        "name": "Financial Reporting Line Item #120",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0121": {
        "metric_id": "FIN-0121",
        "name": "Financial Reporting Line Item #121",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0122": {
        "metric_id": "FIN-0122",
        "name": "Financial Reporting Line Item #122",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0123": {
        "metric_id": "FIN-0123",
        "name": "Financial Reporting Line Item #123",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0124": {
        "metric_id": "FIN-0124",
        "name": "Financial Reporting Line Item #124",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0125": {
        "metric_id": "FIN-0125",
        "name": "Financial Reporting Line Item #125",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0126": {
        "metric_id": "FIN-0126",
        "name": "Financial Reporting Line Item #126",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0127": {
        "metric_id": "FIN-0127",
        "name": "Financial Reporting Line Item #127",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0128": {
        "metric_id": "FIN-0128",
        "name": "Financial Reporting Line Item #128",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0129": {
        "metric_id": "FIN-0129",
        "name": "Financial Reporting Line Item #129",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0130": {
        "metric_id": "FIN-0130",
        "name": "Financial Reporting Line Item #130",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0131": {
        "metric_id": "FIN-0131",
        "name": "Financial Reporting Line Item #131",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0132": {
        "metric_id": "FIN-0132",
        "name": "Financial Reporting Line Item #132",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0133": {
        "metric_id": "FIN-0133",
        "name": "Financial Reporting Line Item #133",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0134": {
        "metric_id": "FIN-0134",
        "name": "Financial Reporting Line Item #134",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0135": {
        "metric_id": "FIN-0135",
        "name": "Financial Reporting Line Item #135",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0136": {
        "metric_id": "FIN-0136",
        "name": "Financial Reporting Line Item #136",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0137": {
        "metric_id": "FIN-0137",
        "name": "Financial Reporting Line Item #137",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0138": {
        "metric_id": "FIN-0138",
        "name": "Financial Reporting Line Item #138",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0139": {
        "metric_id": "FIN-0139",
        "name": "Financial Reporting Line Item #139",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0140": {
        "metric_id": "FIN-0140",
        "name": "Financial Reporting Line Item #140",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0141": {
        "metric_id": "FIN-0141",
        "name": "Financial Reporting Line Item #141",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0142": {
        "metric_id": "FIN-0142",
        "name": "Financial Reporting Line Item #142",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0143": {
        "metric_id": "FIN-0143",
        "name": "Financial Reporting Line Item #143",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0144": {
        "metric_id": "FIN-0144",
        "name": "Financial Reporting Line Item #144",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0145": {
        "metric_id": "FIN-0145",
        "name": "Financial Reporting Line Item #145",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0146": {
        "metric_id": "FIN-0146",
        "name": "Financial Reporting Line Item #146",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0147": {
        "metric_id": "FIN-0147",
        "name": "Financial Reporting Line Item #147",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0148": {
        "metric_id": "FIN-0148",
        "name": "Financial Reporting Line Item #148",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0149": {
        "metric_id": "FIN-0149",
        "name": "Financial Reporting Line Item #149",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0150": {
        "metric_id": "FIN-0150",
        "name": "Financial Reporting Line Item #150",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0151": {
        "metric_id": "FIN-0151",
        "name": "Financial Reporting Line Item #151",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0152": {
        "metric_id": "FIN-0152",
        "name": "Financial Reporting Line Item #152",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0153": {
        "metric_id": "FIN-0153",
        "name": "Financial Reporting Line Item #153",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0154": {
        "metric_id": "FIN-0154",
        "name": "Financial Reporting Line Item #154",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0155": {
        "metric_id": "FIN-0155",
        "name": "Financial Reporting Line Item #155",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0156": {
        "metric_id": "FIN-0156",
        "name": "Financial Reporting Line Item #156",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0157": {
        "metric_id": "FIN-0157",
        "name": "Financial Reporting Line Item #157",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0158": {
        "metric_id": "FIN-0158",
        "name": "Financial Reporting Line Item #158",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0159": {
        "metric_id": "FIN-0159",
        "name": "Financial Reporting Line Item #159",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0160": {
        "metric_id": "FIN-0160",
        "name": "Financial Reporting Line Item #160",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0161": {
        "metric_id": "FIN-0161",
        "name": "Financial Reporting Line Item #161",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0162": {
        "metric_id": "FIN-0162",
        "name": "Financial Reporting Line Item #162",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0163": {
        "metric_id": "FIN-0163",
        "name": "Financial Reporting Line Item #163",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0164": {
        "metric_id": "FIN-0164",
        "name": "Financial Reporting Line Item #164",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0165": {
        "metric_id": "FIN-0165",
        "name": "Financial Reporting Line Item #165",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0166": {
        "metric_id": "FIN-0166",
        "name": "Financial Reporting Line Item #166",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0167": {
        "metric_id": "FIN-0167",
        "name": "Financial Reporting Line Item #167",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0168": {
        "metric_id": "FIN-0168",
        "name": "Financial Reporting Line Item #168",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0169": {
        "metric_id": "FIN-0169",
        "name": "Financial Reporting Line Item #169",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0170": {
        "metric_id": "FIN-0170",
        "name": "Financial Reporting Line Item #170",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0171": {
        "metric_id": "FIN-0171",
        "name": "Financial Reporting Line Item #171",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0172": {
        "metric_id": "FIN-0172",
        "name": "Financial Reporting Line Item #172",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0173": {
        "metric_id": "FIN-0173",
        "name": "Financial Reporting Line Item #173",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0174": {
        "metric_id": "FIN-0174",
        "name": "Financial Reporting Line Item #174",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0175": {
        "metric_id": "FIN-0175",
        "name": "Financial Reporting Line Item #175",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0176": {
        "metric_id": "FIN-0176",
        "name": "Financial Reporting Line Item #176",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0177": {
        "metric_id": "FIN-0177",
        "name": "Financial Reporting Line Item #177",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0178": {
        "metric_id": "FIN-0178",
        "name": "Financial Reporting Line Item #178",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0179": {
        "metric_id": "FIN-0179",
        "name": "Financial Reporting Line Item #179",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0180": {
        "metric_id": "FIN-0180",
        "name": "Financial Reporting Line Item #180",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0181": {
        "metric_id": "FIN-0181",
        "name": "Financial Reporting Line Item #181",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0182": {
        "metric_id": "FIN-0182",
        "name": "Financial Reporting Line Item #182",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0183": {
        "metric_id": "FIN-0183",
        "name": "Financial Reporting Line Item #183",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0184": {
        "metric_id": "FIN-0184",
        "name": "Financial Reporting Line Item #184",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0185": {
        "metric_id": "FIN-0185",
        "name": "Financial Reporting Line Item #185",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0186": {
        "metric_id": "FIN-0186",
        "name": "Financial Reporting Line Item #186",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0187": {
        "metric_id": "FIN-0187",
        "name": "Financial Reporting Line Item #187",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0188": {
        "metric_id": "FIN-0188",
        "name": "Financial Reporting Line Item #188",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0189": {
        "metric_id": "FIN-0189",
        "name": "Financial Reporting Line Item #189",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0190": {
        "metric_id": "FIN-0190",
        "name": "Financial Reporting Line Item #190",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0191": {
        "metric_id": "FIN-0191",
        "name": "Financial Reporting Line Item #191",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0192": {
        "metric_id": "FIN-0192",
        "name": "Financial Reporting Line Item #192",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0193": {
        "metric_id": "FIN-0193",
        "name": "Financial Reporting Line Item #193",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0194": {
        "metric_id": "FIN-0194",
        "name": "Financial Reporting Line Item #194",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0195": {
        "metric_id": "FIN-0195",
        "name": "Financial Reporting Line Item #195",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0196": {
        "metric_id": "FIN-0196",
        "name": "Financial Reporting Line Item #196",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0197": {
        "metric_id": "FIN-0197",
        "name": "Financial Reporting Line Item #197",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0198": {
        "metric_id": "FIN-0198",
        "name": "Financial Reporting Line Item #198",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0199": {
        "metric_id": "FIN-0199",
        "name": "Financial Reporting Line Item #199",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0200": {
        "metric_id": "FIN-0200",
        "name": "Financial Reporting Line Item #200",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0201": {
        "metric_id": "FIN-0201",
        "name": "Financial Reporting Line Item #201",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0202": {
        "metric_id": "FIN-0202",
        "name": "Financial Reporting Line Item #202",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0203": {
        "metric_id": "FIN-0203",
        "name": "Financial Reporting Line Item #203",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0204": {
        "metric_id": "FIN-0204",
        "name": "Financial Reporting Line Item #204",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0205": {
        "metric_id": "FIN-0205",
        "name": "Financial Reporting Line Item #205",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0206": {
        "metric_id": "FIN-0206",
        "name": "Financial Reporting Line Item #206",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0207": {
        "metric_id": "FIN-0207",
        "name": "Financial Reporting Line Item #207",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0208": {
        "metric_id": "FIN-0208",
        "name": "Financial Reporting Line Item #208",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0209": {
        "metric_id": "FIN-0209",
        "name": "Financial Reporting Line Item #209",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0210": {
        "metric_id": "FIN-0210",
        "name": "Financial Reporting Line Item #210",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0211": {
        "metric_id": "FIN-0211",
        "name": "Financial Reporting Line Item #211",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0212": {
        "metric_id": "FIN-0212",
        "name": "Financial Reporting Line Item #212",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0213": {
        "metric_id": "FIN-0213",
        "name": "Financial Reporting Line Item #213",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0214": {
        "metric_id": "FIN-0214",
        "name": "Financial Reporting Line Item #214",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0215": {
        "metric_id": "FIN-0215",
        "name": "Financial Reporting Line Item #215",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0216": {
        "metric_id": "FIN-0216",
        "name": "Financial Reporting Line Item #216",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0217": {
        "metric_id": "FIN-0217",
        "name": "Financial Reporting Line Item #217",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0218": {
        "metric_id": "FIN-0218",
        "name": "Financial Reporting Line Item #218",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0219": {
        "metric_id": "FIN-0219",
        "name": "Financial Reporting Line Item #219",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0220": {
        "metric_id": "FIN-0220",
        "name": "Financial Reporting Line Item #220",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0221": {
        "metric_id": "FIN-0221",
        "name": "Financial Reporting Line Item #221",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0222": {
        "metric_id": "FIN-0222",
        "name": "Financial Reporting Line Item #222",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0223": {
        "metric_id": "FIN-0223",
        "name": "Financial Reporting Line Item #223",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0224": {
        "metric_id": "FIN-0224",
        "name": "Financial Reporting Line Item #224",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0225": {
        "metric_id": "FIN-0225",
        "name": "Financial Reporting Line Item #225",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0226": {
        "metric_id": "FIN-0226",
        "name": "Financial Reporting Line Item #226",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0227": {
        "metric_id": "FIN-0227",
        "name": "Financial Reporting Line Item #227",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0228": {
        "metric_id": "FIN-0228",
        "name": "Financial Reporting Line Item #228",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0229": {
        "metric_id": "FIN-0229",
        "name": "Financial Reporting Line Item #229",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0230": {
        "metric_id": "FIN-0230",
        "name": "Financial Reporting Line Item #230",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0231": {
        "metric_id": "FIN-0231",
        "name": "Financial Reporting Line Item #231",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0232": {
        "metric_id": "FIN-0232",
        "name": "Financial Reporting Line Item #232",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0233": {
        "metric_id": "FIN-0233",
        "name": "Financial Reporting Line Item #233",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0234": {
        "metric_id": "FIN-0234",
        "name": "Financial Reporting Line Item #234",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0235": {
        "metric_id": "FIN-0235",
        "name": "Financial Reporting Line Item #235",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0236": {
        "metric_id": "FIN-0236",
        "name": "Financial Reporting Line Item #236",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0237": {
        "metric_id": "FIN-0237",
        "name": "Financial Reporting Line Item #237",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0238": {
        "metric_id": "FIN-0238",
        "name": "Financial Reporting Line Item #238",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0239": {
        "metric_id": "FIN-0239",
        "name": "Financial Reporting Line Item #239",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0240": {
        "metric_id": "FIN-0240",
        "name": "Financial Reporting Line Item #240",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0241": {
        "metric_id": "FIN-0241",
        "name": "Financial Reporting Line Item #241",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0242": {
        "metric_id": "FIN-0242",
        "name": "Financial Reporting Line Item #242",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0243": {
        "metric_id": "FIN-0243",
        "name": "Financial Reporting Line Item #243",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0244": {
        "metric_id": "FIN-0244",
        "name": "Financial Reporting Line Item #244",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0245": {
        "metric_id": "FIN-0245",
        "name": "Financial Reporting Line Item #245",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0246": {
        "metric_id": "FIN-0246",
        "name": "Financial Reporting Line Item #246",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0247": {
        "metric_id": "FIN-0247",
        "name": "Financial Reporting Line Item #247",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0248": {
        "metric_id": "FIN-0248",
        "name": "Financial Reporting Line Item #248",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0249": {
        "metric_id": "FIN-0249",
        "name": "Financial Reporting Line Item #249",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0250": {
        "metric_id": "FIN-0250",
        "name": "Financial Reporting Line Item #250",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0251": {
        "metric_id": "FIN-0251",
        "name": "Financial Reporting Line Item #251",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0252": {
        "metric_id": "FIN-0252",
        "name": "Financial Reporting Line Item #252",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0253": {
        "metric_id": "FIN-0253",
        "name": "Financial Reporting Line Item #253",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0254": {
        "metric_id": "FIN-0254",
        "name": "Financial Reporting Line Item #254",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0255": {
        "metric_id": "FIN-0255",
        "name": "Financial Reporting Line Item #255",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0256": {
        "metric_id": "FIN-0256",
        "name": "Financial Reporting Line Item #256",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0257": {
        "metric_id": "FIN-0257",
        "name": "Financial Reporting Line Item #257",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0258": {
        "metric_id": "FIN-0258",
        "name": "Financial Reporting Line Item #258",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0259": {
        "metric_id": "FIN-0259",
        "name": "Financial Reporting Line Item #259",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0260": {
        "metric_id": "FIN-0260",
        "name": "Financial Reporting Line Item #260",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0261": {
        "metric_id": "FIN-0261",
        "name": "Financial Reporting Line Item #261",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0262": {
        "metric_id": "FIN-0262",
        "name": "Financial Reporting Line Item #262",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0263": {
        "metric_id": "FIN-0263",
        "name": "Financial Reporting Line Item #263",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0264": {
        "metric_id": "FIN-0264",
        "name": "Financial Reporting Line Item #264",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0265": {
        "metric_id": "FIN-0265",
        "name": "Financial Reporting Line Item #265",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0266": {
        "metric_id": "FIN-0266",
        "name": "Financial Reporting Line Item #266",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0267": {
        "metric_id": "FIN-0267",
        "name": "Financial Reporting Line Item #267",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0268": {
        "metric_id": "FIN-0268",
        "name": "Financial Reporting Line Item #268",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0269": {
        "metric_id": "FIN-0269",
        "name": "Financial Reporting Line Item #269",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0270": {
        "metric_id": "FIN-0270",
        "name": "Financial Reporting Line Item #270",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0271": {
        "metric_id": "FIN-0271",
        "name": "Financial Reporting Line Item #271",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0272": {
        "metric_id": "FIN-0272",
        "name": "Financial Reporting Line Item #272",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0273": {
        "metric_id": "FIN-0273",
        "name": "Financial Reporting Line Item #273",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0274": {
        "metric_id": "FIN-0274",
        "name": "Financial Reporting Line Item #274",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0275": {
        "metric_id": "FIN-0275",
        "name": "Financial Reporting Line Item #275",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0276": {
        "metric_id": "FIN-0276",
        "name": "Financial Reporting Line Item #276",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0277": {
        "metric_id": "FIN-0277",
        "name": "Financial Reporting Line Item #277",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0278": {
        "metric_id": "FIN-0278",
        "name": "Financial Reporting Line Item #278",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0279": {
        "metric_id": "FIN-0279",
        "name": "Financial Reporting Line Item #279",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0280": {
        "metric_id": "FIN-0280",
        "name": "Financial Reporting Line Item #280",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0281": {
        "metric_id": "FIN-0281",
        "name": "Financial Reporting Line Item #281",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0282": {
        "metric_id": "FIN-0282",
        "name": "Financial Reporting Line Item #282",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0283": {
        "metric_id": "FIN-0283",
        "name": "Financial Reporting Line Item #283",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0284": {
        "metric_id": "FIN-0284",
        "name": "Financial Reporting Line Item #284",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0285": {
        "metric_id": "FIN-0285",
        "name": "Financial Reporting Line Item #285",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0286": {
        "metric_id": "FIN-0286",
        "name": "Financial Reporting Line Item #286",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0287": {
        "metric_id": "FIN-0287",
        "name": "Financial Reporting Line Item #287",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0288": {
        "metric_id": "FIN-0288",
        "name": "Financial Reporting Line Item #288",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0289": {
        "metric_id": "FIN-0289",
        "name": "Financial Reporting Line Item #289",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0290": {
        "metric_id": "FIN-0290",
        "name": "Financial Reporting Line Item #290",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0291": {
        "metric_id": "FIN-0291",
        "name": "Financial Reporting Line Item #291",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0292": {
        "metric_id": "FIN-0292",
        "name": "Financial Reporting Line Item #292",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0293": {
        "metric_id": "FIN-0293",
        "name": "Financial Reporting Line Item #293",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0294": {
        "metric_id": "FIN-0294",
        "name": "Financial Reporting Line Item #294",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0295": {
        "metric_id": "FIN-0295",
        "name": "Financial Reporting Line Item #295",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0296": {
        "metric_id": "FIN-0296",
        "name": "Financial Reporting Line Item #296",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0297": {
        "metric_id": "FIN-0297",
        "name": "Financial Reporting Line Item #297",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0298": {
        "metric_id": "FIN-0298",
        "name": "Financial Reporting Line Item #298",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0299": {
        "metric_id": "FIN-0299",
        "name": "Financial Reporting Line Item #299",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0300": {
        "metric_id": "FIN-0300",
        "name": "Financial Reporting Line Item #300",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0301": {
        "metric_id": "FIN-0301",
        "name": "Financial Reporting Line Item #301",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0302": {
        "metric_id": "FIN-0302",
        "name": "Financial Reporting Line Item #302",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0303": {
        "metric_id": "FIN-0303",
        "name": "Financial Reporting Line Item #303",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0304": {
        "metric_id": "FIN-0304",
        "name": "Financial Reporting Line Item #304",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0305": {
        "metric_id": "FIN-0305",
        "name": "Financial Reporting Line Item #305",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0306": {
        "metric_id": "FIN-0306",
        "name": "Financial Reporting Line Item #306",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0307": {
        "metric_id": "FIN-0307",
        "name": "Financial Reporting Line Item #307",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0308": {
        "metric_id": "FIN-0308",
        "name": "Financial Reporting Line Item #308",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0309": {
        "metric_id": "FIN-0309",
        "name": "Financial Reporting Line Item #309",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0310": {
        "metric_id": "FIN-0310",
        "name": "Financial Reporting Line Item #310",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0311": {
        "metric_id": "FIN-0311",
        "name": "Financial Reporting Line Item #311",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0312": {
        "metric_id": "FIN-0312",
        "name": "Financial Reporting Line Item #312",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0313": {
        "metric_id": "FIN-0313",
        "name": "Financial Reporting Line Item #313",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0314": {
        "metric_id": "FIN-0314",
        "name": "Financial Reporting Line Item #314",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0315": {
        "metric_id": "FIN-0315",
        "name": "Financial Reporting Line Item #315",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0316": {
        "metric_id": "FIN-0316",
        "name": "Financial Reporting Line Item #316",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0317": {
        "metric_id": "FIN-0317",
        "name": "Financial Reporting Line Item #317",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0318": {
        "metric_id": "FIN-0318",
        "name": "Financial Reporting Line Item #318",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0319": {
        "metric_id": "FIN-0319",
        "name": "Financial Reporting Line Item #319",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0320": {
        "metric_id": "FIN-0320",
        "name": "Financial Reporting Line Item #320",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0321": {
        "metric_id": "FIN-0321",
        "name": "Financial Reporting Line Item #321",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0322": {
        "metric_id": "FIN-0322",
        "name": "Financial Reporting Line Item #322",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0323": {
        "metric_id": "FIN-0323",
        "name": "Financial Reporting Line Item #323",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0324": {
        "metric_id": "FIN-0324",
        "name": "Financial Reporting Line Item #324",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0325": {
        "metric_id": "FIN-0325",
        "name": "Financial Reporting Line Item #325",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0326": {
        "metric_id": "FIN-0326",
        "name": "Financial Reporting Line Item #326",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0327": {
        "metric_id": "FIN-0327",
        "name": "Financial Reporting Line Item #327",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0328": {
        "metric_id": "FIN-0328",
        "name": "Financial Reporting Line Item #328",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0329": {
        "metric_id": "FIN-0329",
        "name": "Financial Reporting Line Item #329",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0330": {
        "metric_id": "FIN-0330",
        "name": "Financial Reporting Line Item #330",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0331": {
        "metric_id": "FIN-0331",
        "name": "Financial Reporting Line Item #331",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0332": {
        "metric_id": "FIN-0332",
        "name": "Financial Reporting Line Item #332",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0333": {
        "metric_id": "FIN-0333",
        "name": "Financial Reporting Line Item #333",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0334": {
        "metric_id": "FIN-0334",
        "name": "Financial Reporting Line Item #334",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0335": {
        "metric_id": "FIN-0335",
        "name": "Financial Reporting Line Item #335",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0336": {
        "metric_id": "FIN-0336",
        "name": "Financial Reporting Line Item #336",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0337": {
        "metric_id": "FIN-0337",
        "name": "Financial Reporting Line Item #337",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0338": {
        "metric_id": "FIN-0338",
        "name": "Financial Reporting Line Item #338",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0339": {
        "metric_id": "FIN-0339",
        "name": "Financial Reporting Line Item #339",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0340": {
        "metric_id": "FIN-0340",
        "name": "Financial Reporting Line Item #340",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0341": {
        "metric_id": "FIN-0341",
        "name": "Financial Reporting Line Item #341",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0342": {
        "metric_id": "FIN-0342",
        "name": "Financial Reporting Line Item #342",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0343": {
        "metric_id": "FIN-0343",
        "name": "Financial Reporting Line Item #343",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0344": {
        "metric_id": "FIN-0344",
        "name": "Financial Reporting Line Item #344",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0345": {
        "metric_id": "FIN-0345",
        "name": "Financial Reporting Line Item #345",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0346": {
        "metric_id": "FIN-0346",
        "name": "Financial Reporting Line Item #346",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0347": {
        "metric_id": "FIN-0347",
        "name": "Financial Reporting Line Item #347",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0348": {
        "metric_id": "FIN-0348",
        "name": "Financial Reporting Line Item #348",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0349": {
        "metric_id": "FIN-0349",
        "name": "Financial Reporting Line Item #349",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0350": {
        "metric_id": "FIN-0350",
        "name": "Financial Reporting Line Item #350",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0351": {
        "metric_id": "FIN-0351",
        "name": "Financial Reporting Line Item #351",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0352": {
        "metric_id": "FIN-0352",
        "name": "Financial Reporting Line Item #352",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0353": {
        "metric_id": "FIN-0353",
        "name": "Financial Reporting Line Item #353",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0354": {
        "metric_id": "FIN-0354",
        "name": "Financial Reporting Line Item #354",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0355": {
        "metric_id": "FIN-0355",
        "name": "Financial Reporting Line Item #355",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0356": {
        "metric_id": "FIN-0356",
        "name": "Financial Reporting Line Item #356",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0357": {
        "metric_id": "FIN-0357",
        "name": "Financial Reporting Line Item #357",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0358": {
        "metric_id": "FIN-0358",
        "name": "Financial Reporting Line Item #358",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0359": {
        "metric_id": "FIN-0359",
        "name": "Financial Reporting Line Item #359",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0360": {
        "metric_id": "FIN-0360",
        "name": "Financial Reporting Line Item #360",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0361": {
        "metric_id": "FIN-0361",
        "name": "Financial Reporting Line Item #361",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0362": {
        "metric_id": "FIN-0362",
        "name": "Financial Reporting Line Item #362",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0363": {
        "metric_id": "FIN-0363",
        "name": "Financial Reporting Line Item #363",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0364": {
        "metric_id": "FIN-0364",
        "name": "Financial Reporting Line Item #364",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0365": {
        "metric_id": "FIN-0365",
        "name": "Financial Reporting Line Item #365",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0366": {
        "metric_id": "FIN-0366",
        "name": "Financial Reporting Line Item #366",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0367": {
        "metric_id": "FIN-0367",
        "name": "Financial Reporting Line Item #367",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0368": {
        "metric_id": "FIN-0368",
        "name": "Financial Reporting Line Item #368",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0369": {
        "metric_id": "FIN-0369",
        "name": "Financial Reporting Line Item #369",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0370": {
        "metric_id": "FIN-0370",
        "name": "Financial Reporting Line Item #370",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0371": {
        "metric_id": "FIN-0371",
        "name": "Financial Reporting Line Item #371",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0372": {
        "metric_id": "FIN-0372",
        "name": "Financial Reporting Line Item #372",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0373": {
        "metric_id": "FIN-0373",
        "name": "Financial Reporting Line Item #373",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0374": {
        "metric_id": "FIN-0374",
        "name": "Financial Reporting Line Item #374",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0375": {
        "metric_id": "FIN-0375",
        "name": "Financial Reporting Line Item #375",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0376": {
        "metric_id": "FIN-0376",
        "name": "Financial Reporting Line Item #376",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0377": {
        "metric_id": "FIN-0377",
        "name": "Financial Reporting Line Item #377",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0378": {
        "metric_id": "FIN-0378",
        "name": "Financial Reporting Line Item #378",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0379": {
        "metric_id": "FIN-0379",
        "name": "Financial Reporting Line Item #379",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0380": {
        "metric_id": "FIN-0380",
        "name": "Financial Reporting Line Item #380",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0381": {
        "metric_id": "FIN-0381",
        "name": "Financial Reporting Line Item #381",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0382": {
        "metric_id": "FIN-0382",
        "name": "Financial Reporting Line Item #382",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0383": {
        "metric_id": "FIN-0383",
        "name": "Financial Reporting Line Item #383",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0384": {
        "metric_id": "FIN-0384",
        "name": "Financial Reporting Line Item #384",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0385": {
        "metric_id": "FIN-0385",
        "name": "Financial Reporting Line Item #385",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0386": {
        "metric_id": "FIN-0386",
        "name": "Financial Reporting Line Item #386",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0387": {
        "metric_id": "FIN-0387",
        "name": "Financial Reporting Line Item #387",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0388": {
        "metric_id": "FIN-0388",
        "name": "Financial Reporting Line Item #388",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0389": {
        "metric_id": "FIN-0389",
        "name": "Financial Reporting Line Item #389",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0390": {
        "metric_id": "FIN-0390",
        "name": "Financial Reporting Line Item #390",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0391": {
        "metric_id": "FIN-0391",
        "name": "Financial Reporting Line Item #391",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0392": {
        "metric_id": "FIN-0392",
        "name": "Financial Reporting Line Item #392",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0393": {
        "metric_id": "FIN-0393",
        "name": "Financial Reporting Line Item #393",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0394": {
        "metric_id": "FIN-0394",
        "name": "Financial Reporting Line Item #394",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0395": {
        "metric_id": "FIN-0395",
        "name": "Financial Reporting Line Item #395",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0396": {
        "metric_id": "FIN-0396",
        "name": "Financial Reporting Line Item #396",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0397": {
        "metric_id": "FIN-0397",
        "name": "Financial Reporting Line Item #397",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0398": {
        "metric_id": "FIN-0398",
        "name": "Financial Reporting Line Item #398",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0399": {
        "metric_id": "FIN-0399",
        "name": "Financial Reporting Line Item #399",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0400": {
        "metric_id": "FIN-0400",
        "name": "Financial Reporting Line Item #400",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0401": {
        "metric_id": "FIN-0401",
        "name": "Financial Reporting Line Item #401",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0402": {
        "metric_id": "FIN-0402",
        "name": "Financial Reporting Line Item #402",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0403": {
        "metric_id": "FIN-0403",
        "name": "Financial Reporting Line Item #403",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0404": {
        "metric_id": "FIN-0404",
        "name": "Financial Reporting Line Item #404",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0405": {
        "metric_id": "FIN-0405",
        "name": "Financial Reporting Line Item #405",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0406": {
        "metric_id": "FIN-0406",
        "name": "Financial Reporting Line Item #406",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0407": {
        "metric_id": "FIN-0407",
        "name": "Financial Reporting Line Item #407",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0408": {
        "metric_id": "FIN-0408",
        "name": "Financial Reporting Line Item #408",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0409": {
        "metric_id": "FIN-0409",
        "name": "Financial Reporting Line Item #409",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0410": {
        "metric_id": "FIN-0410",
        "name": "Financial Reporting Line Item #410",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0411": {
        "metric_id": "FIN-0411",
        "name": "Financial Reporting Line Item #411",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0412": {
        "metric_id": "FIN-0412",
        "name": "Financial Reporting Line Item #412",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0413": {
        "metric_id": "FIN-0413",
        "name": "Financial Reporting Line Item #413",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0414": {
        "metric_id": "FIN-0414",
        "name": "Financial Reporting Line Item #414",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0415": {
        "metric_id": "FIN-0415",
        "name": "Financial Reporting Line Item #415",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0416": {
        "metric_id": "FIN-0416",
        "name": "Financial Reporting Line Item #416",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0417": {
        "metric_id": "FIN-0417",
        "name": "Financial Reporting Line Item #417",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0418": {
        "metric_id": "FIN-0418",
        "name": "Financial Reporting Line Item #418",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0419": {
        "metric_id": "FIN-0419",
        "name": "Financial Reporting Line Item #419",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0420": {
        "metric_id": "FIN-0420",
        "name": "Financial Reporting Line Item #420",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0421": {
        "metric_id": "FIN-0421",
        "name": "Financial Reporting Line Item #421",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0422": {
        "metric_id": "FIN-0422",
        "name": "Financial Reporting Line Item #422",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0423": {
        "metric_id": "FIN-0423",
        "name": "Financial Reporting Line Item #423",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0424": {
        "metric_id": "FIN-0424",
        "name": "Financial Reporting Line Item #424",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0425": {
        "metric_id": "FIN-0425",
        "name": "Financial Reporting Line Item #425",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0426": {
        "metric_id": "FIN-0426",
        "name": "Financial Reporting Line Item #426",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0427": {
        "metric_id": "FIN-0427",
        "name": "Financial Reporting Line Item #427",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0428": {
        "metric_id": "FIN-0428",
        "name": "Financial Reporting Line Item #428",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0429": {
        "metric_id": "FIN-0429",
        "name": "Financial Reporting Line Item #429",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0430": {
        "metric_id": "FIN-0430",
        "name": "Financial Reporting Line Item #430",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0431": {
        "metric_id": "FIN-0431",
        "name": "Financial Reporting Line Item #431",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0432": {
        "metric_id": "FIN-0432",
        "name": "Financial Reporting Line Item #432",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0433": {
        "metric_id": "FIN-0433",
        "name": "Financial Reporting Line Item #433",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0434": {
        "metric_id": "FIN-0434",
        "name": "Financial Reporting Line Item #434",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0435": {
        "metric_id": "FIN-0435",
        "name": "Financial Reporting Line Item #435",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0436": {
        "metric_id": "FIN-0436",
        "name": "Financial Reporting Line Item #436",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0437": {
        "metric_id": "FIN-0437",
        "name": "Financial Reporting Line Item #437",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0438": {
        "metric_id": "FIN-0438",
        "name": "Financial Reporting Line Item #438",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0439": {
        "metric_id": "FIN-0439",
        "name": "Financial Reporting Line Item #439",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0440": {
        "metric_id": "FIN-0440",
        "name": "Financial Reporting Line Item #440",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0441": {
        "metric_id": "FIN-0441",
        "name": "Financial Reporting Line Item #441",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0442": {
        "metric_id": "FIN-0442",
        "name": "Financial Reporting Line Item #442",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0443": {
        "metric_id": "FIN-0443",
        "name": "Financial Reporting Line Item #443",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0444": {
        "metric_id": "FIN-0444",
        "name": "Financial Reporting Line Item #444",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0445": {
        "metric_id": "FIN-0445",
        "name": "Financial Reporting Line Item #445",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0446": {
        "metric_id": "FIN-0446",
        "name": "Financial Reporting Line Item #446",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0447": {
        "metric_id": "FIN-0447",
        "name": "Financial Reporting Line Item #447",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0448": {
        "metric_id": "FIN-0448",
        "name": "Financial Reporting Line Item #448",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0449": {
        "metric_id": "FIN-0449",
        "name": "Financial Reporting Line Item #449",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0450": {
        "metric_id": "FIN-0450",
        "name": "Financial Reporting Line Item #450",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0451": {
        "metric_id": "FIN-0451",
        "name": "Financial Reporting Line Item #451",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0452": {
        "metric_id": "FIN-0452",
        "name": "Financial Reporting Line Item #452",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0453": {
        "metric_id": "FIN-0453",
        "name": "Financial Reporting Line Item #453",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0454": {
        "metric_id": "FIN-0454",
        "name": "Financial Reporting Line Item #454",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0455": {
        "metric_id": "FIN-0455",
        "name": "Financial Reporting Line Item #455",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0456": {
        "metric_id": "FIN-0456",
        "name": "Financial Reporting Line Item #456",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0457": {
        "metric_id": "FIN-0457",
        "name": "Financial Reporting Line Item #457",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0458": {
        "metric_id": "FIN-0458",
        "name": "Financial Reporting Line Item #458",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0459": {
        "metric_id": "FIN-0459",
        "name": "Financial Reporting Line Item #459",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0460": {
        "metric_id": "FIN-0460",
        "name": "Financial Reporting Line Item #460",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0461": {
        "metric_id": "FIN-0461",
        "name": "Financial Reporting Line Item #461",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0462": {
        "metric_id": "FIN-0462",
        "name": "Financial Reporting Line Item #462",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0463": {
        "metric_id": "FIN-0463",
        "name": "Financial Reporting Line Item #463",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0464": {
        "metric_id": "FIN-0464",
        "name": "Financial Reporting Line Item #464",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0465": {
        "metric_id": "FIN-0465",
        "name": "Financial Reporting Line Item #465",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0466": {
        "metric_id": "FIN-0466",
        "name": "Financial Reporting Line Item #466",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0467": {
        "metric_id": "FIN-0467",
        "name": "Financial Reporting Line Item #467",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0468": {
        "metric_id": "FIN-0468",
        "name": "Financial Reporting Line Item #468",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0469": {
        "metric_id": "FIN-0469",
        "name": "Financial Reporting Line Item #469",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0470": {
        "metric_id": "FIN-0470",
        "name": "Financial Reporting Line Item #470",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0471": {
        "metric_id": "FIN-0471",
        "name": "Financial Reporting Line Item #471",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0472": {
        "metric_id": "FIN-0472",
        "name": "Financial Reporting Line Item #472",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0473": {
        "metric_id": "FIN-0473",
        "name": "Financial Reporting Line Item #473",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0474": {
        "metric_id": "FIN-0474",
        "name": "Financial Reporting Line Item #474",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0475": {
        "metric_id": "FIN-0475",
        "name": "Financial Reporting Line Item #475",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0476": {
        "metric_id": "FIN-0476",
        "name": "Financial Reporting Line Item #476",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0477": {
        "metric_id": "FIN-0477",
        "name": "Financial Reporting Line Item #477",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0478": {
        "metric_id": "FIN-0478",
        "name": "Financial Reporting Line Item #478",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0479": {
        "metric_id": "FIN-0479",
        "name": "Financial Reporting Line Item #479",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0480": {
        "metric_id": "FIN-0480",
        "name": "Financial Reporting Line Item #480",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0481": {
        "metric_id": "FIN-0481",
        "name": "Financial Reporting Line Item #481",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0482": {
        "metric_id": "FIN-0482",
        "name": "Financial Reporting Line Item #482",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0483": {
        "metric_id": "FIN-0483",
        "name": "Financial Reporting Line Item #483",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0484": {
        "metric_id": "FIN-0484",
        "name": "Financial Reporting Line Item #484",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0485": {
        "metric_id": "FIN-0485",
        "name": "Financial Reporting Line Item #485",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0486": {
        "metric_id": "FIN-0486",
        "name": "Financial Reporting Line Item #486",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0487": {
        "metric_id": "FIN-0487",
        "name": "Financial Reporting Line Item #487",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0488": {
        "metric_id": "FIN-0488",
        "name": "Financial Reporting Line Item #488",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0489": {
        "metric_id": "FIN-0489",
        "name": "Financial Reporting Line Item #489",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0490": {
        "metric_id": "FIN-0490",
        "name": "Financial Reporting Line Item #490",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0491": {
        "metric_id": "FIN-0491",
        "name": "Financial Reporting Line Item #491",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0492": {
        "metric_id": "FIN-0492",
        "name": "Financial Reporting Line Item #492",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0493": {
        "metric_id": "FIN-0493",
        "name": "Financial Reporting Line Item #493",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0494": {
        "metric_id": "FIN-0494",
        "name": "Financial Reporting Line Item #494",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0495": {
        "metric_id": "FIN-0495",
        "name": "Financial Reporting Line Item #495",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0496": {
        "metric_id": "FIN-0496",
        "name": "Financial Reporting Line Item #496",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0497": {
        "metric_id": "FIN-0497",
        "name": "Financial Reporting Line Item #497",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0498": {
        "metric_id": "FIN-0498",
        "name": "Financial Reporting Line Item #498",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0499": {
        "metric_id": "FIN-0499",
        "name": "Financial Reporting Line Item #499",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
    "FIN_METRIC_EXP_0500": {
        "metric_id": "FIN-0500",
        "name": "Financial Reporting Line Item #500",
        "framework": "US GAAP / ASC 606" if idx % 2 == 0 else "IFRS 15 / International Accounting Standards",
        "statement_type": "Balance Sheet" if idx % 3 == 0 else "Income Statement" if idx % 3 == 1 else "Cash Flow Statement",
        "audit_procedures": [
            "Examine revenue recognition triggers and contractual performance obligations.",
            "Validate amortization schedules, depreciation methods, and asset impairment calculations.",
            "Confirm fair value measurement hierarchies (Level 1, Level 2, Level 3 inputs).",
            "Inspect debt maturity schedules, liquidity ratios, and debt covenant compliance.",
            "Verify internal controls over financial reporting (ICFR) and management evaluation certifications."
        ],
        "risk_classification": "HIGH" if idx % 5 == 0 else "NORMAL"
    },
}
