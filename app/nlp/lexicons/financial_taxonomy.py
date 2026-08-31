"""
Financial, Accounting and Regulatory Reporting Taxonomy
Covers US GAAP, IFRS, SEC reporting (10-K, 10-Q), EBITDA, liquidity metrics, and financial risk markers.
"""

from typing import Dict, List

FINANCIAL_METRICS_TAXONOMY: Dict[str, List[str]] = {
    "Revenue & Top-Line": [
        "gross revenue", "net sales", "operating revenue", "recurring revenue",
        "annual recurring revenue", "arr", "monthly recurring revenue", "mrr",
        "deferred revenue", "revenue recognition", "asc 606", "ifrs 15"
    ],
    "Profitability & Margins": [
        "gross profit", "gross margin", "operating income", "operating margin",
        "ebitda", "adjusted ebitda", "ebit", "net income", "earnings per share",
        "eps", "diluted eps", "return on equity", "roe", "return on assets", "roa"
    ],
    "Balance Sheet & Assets": [
        "current assets", "cash and cash equivalents", "marketable securities",
        "accounts receivable", "allowance for doubtful accounts", "inventory",
        "property, plant and equipment", "goodwill", "intangible assets", "total assets"
    ],
    "Liabilities & Debt": [
        "current liabilities", "accounts payable", "accrued expenses", "short-term debt",
        "long-term debt", "senior secured notes", "convertible debentures", "deferred tax liability",
        "contingent liabilities", "total liabilities", "working capital"
    ],
    "Cash Flow & Capital Allocation": [
        "cash flow from operations", "free cash flow", "capital expenditures", "capex",
        "operating expenditures", "opex", "financing cash flow", "dividends paid",
        "share repurchases", "stock buyback program"
    ],
    "Financial Risk & Distress Signals": [
        "going concern warning", "material weakness in internal controls", "debt covenant breach",
        "liquidity deficit", "restructuring charges", "impairment of goodwill",
        "sec investigation", "restatement of financial statements", "default on credit facility"
    ]
}
