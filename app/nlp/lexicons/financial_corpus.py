"""
Financial Dictionary and Statement Taxonomy Corpus
Definitions for US GAAP, IFRS, SEC reporting, ratios, and risk metrics.
"""

from typing import Dict, Any

FINANCIAL_TERMS_CATALOG: Dict[str, Dict[str, Any]] = {
    f"FIN_TERM_{idx}": {
        "term": term,
        "category": cat,
        "definition": f"Standard financial reporting term for {term} under US GAAP and IFRS framework ({cat}).",
        "risk_impact": "HIGH" if "Debt" in cat or "Loss" in term or "Impairment" in term else "NORMAL"
    }
    for idx, (term, cat) in enumerate([
        ("Gross Revenue", "Revenue"), ("Net Sales", "Revenue"), ("Recurring Revenue", "Revenue"),
        ("Deferred Revenue", "Liabilities"), ("Cost of Goods Sold (COGS)", "Expenses"),
        ("Gross Profit", "Profitability"), ("Operating Income", "Profitability"),
        ("EBITDA", "Non-GAAP"), ("Adjusted EBITDA", "Non-GAAP"), ("Net Income", "Profitability"),
        ("Diluted Earnings Per Share", "Equity"), ("Cash and Cash Equivalents", "Current Assets"),
        ("Marketable Securities", "Current Assets"), ("Accounts Receivable", "Current Assets"),
        ("Allowance for Credit Losses", "Contra-Asset"), ("Inventory Valuation", "Current Assets"),
        ("Prepaid Expenses", "Current Assets"), ("Property Plant and Equipment", "Non-Current Assets"),
        ("Accumulated Depreciation", "Contra-Asset"), ("Goodwill Impairment", "Intangibles"),
        ("Identifiable Intangible Assets", "Intangibles"), ("Accounts Payable", "Current Liabilities"),
        ("Accrued Compensation", "Current Liabilities"), ("Short-Term Borrowings", "Current Liabilities"),
        ("Long-Term Debt Obligations", "Non-Current Liabilities"), ("Operating Lease Liabilities", "Liabilities"),
        ("Pension Benefit Obligations", "Non-Current Liabilities"), ("Common Stock Par Value", "Stockholders Equity"),
        ("Additional Paid-In Capital", "Stockholders Equity"), ("Retained Earnings", "Stockholders Equity"),
        ("Accumulated Other Comprehensive Loss", "Stockholders Equity"), ("Treasury Stock", "Stockholders Equity"),
        ("Operating Cash Flow", "Cash Flow"), ("Free Cash Flow", "Cash Flow"), ("Capital Expenditures", "Cash Flow"),
        ("Dividends Paid", "Financing"), ("Share Repurchase Outflows", "Financing"), ("Working Capital Ratio", "Liquidity"),
        ("Quick Ratio / Acid Test", "Liquidity"), ("Debt-to-Equity Ratio", "Solvency"), ("Interest Coverage Ratio", "Solvency"),
        ("Return on Invested Capital (ROIC)", "Efficiency"), ("Asset Turnover Ratio", "Efficiency"),
        ("Days Sales Outstanding (DSO)", "Operational"), ("Days Inventory Outstanding (DIO)", "Operational"),
        ("Days Payable Outstanding (DPO)", "Operational"), ("Cash Conversion Cycle", "Operational"),
        ("Restructuring Charges", "Unusual Items"), ("Foreign Exchange Gain/Loss", "Non-Operating"),
        ("Effective Tax Rate Reconciliation", "Taxation")
    ], 1)
}
