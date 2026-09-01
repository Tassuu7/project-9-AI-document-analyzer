"""Structured Data Quality Engine, Profiler, and Anomaly Detector."""
import re
import math
from typing import Dict, Any, List, Optional

class DataQualityEngine:
    @classmethod
    def analyze_table_data(cls, headers: List[str], rows: List[List[Any]]) -> Dict[str, Any]:
        issues: List[Dict[str, Any]] = []
        if not headers or not rows:
            return {
                "quality_score": 100.0,
                "completeness_score": 100.0,
                "validity_score": 100.0,
                "uniqueness_score": 100.0,
                "consistency_score": 100.0,
                "profile": {},
                "issues": []
            }

        num_rows = len(rows)
        num_cols = len(headers)
        
        # 1. Column Profiling & Null Counting
        column_profiles = {}
        total_cells = num_rows * num_cols
        total_missing = 0
        total_invalid = 0

        for col_idx, col_name in enumerate(headers):
            values = []
            null_count = 0
            numeric_values = []
            
            for row_idx, r in enumerate(rows):
                val = str(r[col_idx]).strip() if col_idx < len(r) else ""
                if not val or val.lower() in ["null", "none", "nan", "na", "-", "n/a", ""]:
                    null_count += 1
                    total_missing += 1
                else:
                    values.append(val)
                    # Try numeric parse
                    clean_num = val.replace("$", "").replace(",", "").replace("%", "")
                    try:
                        f_val = float(clean_num)
                        numeric_values.append(f_val)
                    except ValueError:
                        pass

            # Calculate stats for numeric columns
            stats = {}
            if numeric_values and len(numeric_values) >= max(2, len(values) * 0.7):
                numeric_values.sort()
                n = len(numeric_values)
                mean_val = sum(numeric_values) / n
                median_val = numeric_values[n // 2] if n % 2 != 0 else (numeric_values[n // 2 - 1] + numeric_values[n // 2]) / 2
                variance = sum((x - mean_val) ** 2 for x in numeric_values) / n
                std_dev = math.sqrt(variance)
                
                # IQR Outlier Detection
                q1 = numeric_values[int(n * 0.25)]
                q3 = numeric_values[int(n * 0.75)]
                iqr = q3 - q1
                lower_bound = q1 - 1.5 * iqr
                upper_bound = q3 + 1.5 * iqr
                
                outliers = [x for x in numeric_values if x < lower_bound or x > upper_bound]

                stats = {
                    "type": "numeric",
                    "min": round(numeric_values[0], 2),
                    "max": round(numeric_values[-1], 2),
                    "mean": round(mean_val, 2),
                    "median": round(median_val, 2),
                    "std_dev": round(std_dev, 2),
                    "iqr": round(iqr, 2),
                    "outliers_count": len(outliers)
                }

                # Flag Outliers as Potential Anomalies
                if outliers and len(outliers) <= n * 0.15:
                    for out_val in outliers[:5]:
                        issues.append({
                            "category": "DATA_QUALITY",
                            "severity": "LOW",
                            "title": f"Statistical Outlier in {col_name}",
                            "location": f"Column '{col_name}'",
                            "value": str(out_val),
                            "expected_value": f"Between {round(lower_bound, 2)} and {round(upper_bound, 2)}",
                            "evidence": f"Value {out_val} deviates significantly from mean ({round(mean_val, 2)}) with IQR={round(iqr, 2)}.",
                            "explanation": "Potential anomaly detected through IQR distribution analysis.",
                            "impact": "Extreme values may distort aggregate reporting or indicate data entry errors.",
                            "recommendation": "Potential anomaly — review recommended with data source.",
                            "confidence": 0.88,
                            "suggested_correction": ""
                        })
            else:
                stats = {
                    "type": "text",
                    "unique_count": len(set(values)),
                    "cardinality": round(len(set(values)) / max(1, len(values)), 2)
                }

            column_profiles[col_name] = {
                "null_count": null_count,
                "null_pct": round((null_count / max(1, num_rows)) * 100, 1),
                "stats": stats
            }

            # Check for high missing rate in column
            if null_count > 0:
                severity = "HIGH" if (null_count / num_rows) > 0.4 else "MEDIUM" if (null_count / num_rows) > 0.15 else "LOW"
                issues.append({
                    "category": "DATA_QUALITY",
                    "severity": severity,
                    "title": f"Missing Data in {col_name}",
                    "location": f"Column '{col_name}' ({null_count} rows affected)",
                    "value": f"{null_count} empty cells",
                    "expected_value": "Complete column values",
                    "evidence": f"{null_count} out of {num_rows} rows ({round((null_count/num_rows)*100, 1)}%) have empty or null values.",
                    "explanation": f"Missing required data fields in column '{col_name}'.",
                    "impact": "Incomplete records can break downstream analytics or report validity.",
                    "recommendation": "Populate missing values or confirm if nullability is permitted.",
                    "confidence": 0.99,
                    "suggested_correction": ""
                })

        # 2. Duplicate Rows and ID Checking
        row_tuples = [tuple(str(x) for x in r) for r in rows]
        unique_rows = set(row_tuples)
        duplicate_count = num_rows - len(unique_rows)
        if duplicate_count > 0:
            issues.append({
                "category": "DATA_QUALITY",
                "severity": "HIGH",
                "title": "Duplicate Records Detected",
                "location": f"Dataset rows ({duplicate_count} duplicate instances)",
                "value": f"{duplicate_count} duplicates",
                "expected_value": "Unique records",
                "evidence": f"Found {duplicate_count} duplicate row(s) out of {num_rows} total rows.",
                "explanation": "Identical row entries exist in the dataset.",
                "impact": "Duplicate records inflate transaction metrics, counts, and financial totals.",
                "recommendation": "Deduplicate dataset prior to processing.",
                "confidence": 1.0,
                "suggested_correction": ""
            })

        # 3. Domain Specific Value Validation (Age, Email, Phone, Percentages)
        for col_idx, col_name in enumerate(headers):
            col_low = col_name.lower()
            for row_idx, r in enumerate(rows):
                val = str(r[col_idx]).strip() if col_idx < len(r) else ""
                if not val:
                    continue

                # Age Validation
                if "age" in col_low:
                    try:
                        age_num = float(val)
                        if age_num < 0 or age_num > 130:
                            total_invalid += 1
                            issues.append({
                                "category": "DATA_QUALITY",
                                "severity": "HIGH",
                                "title": f"Invalid Age Value",
                                "location": f"Row {row_idx + 1}, Column '{col_name}'",
                                "value": val,
                                "expected_value": "0 - 120",
                                "evidence": f"Age recorded as '{val}'.",
                                "explanation": "The value is outside the expected human age range.",
                                "impact": "Invalid demographic data compromises clinical and operational records.",
                                "recommendation": "Verify and correct the original demographic record.",
                                "confidence": 0.99,
                                "suggested_correction": ""
                            })
                    except ValueError:
                        total_invalid += 1
                        issues.append({
                            "category": "DATA_QUALITY",
                            "severity": "HIGH",
                            "title": "Non-Numeric Value in Age Column",
                            "location": f"Row {row_idx + 1}, Column '{col_name}'",
                            "value": val,
                            "expected_value": "Numeric Age",
                            "evidence": f"Found non-numeric string '{val}' in age column.",
                            "explanation": "Data type violation: expected integer/float for age.",
                            "impact": "Breaks automated aggregations and statistical models.",
                            "recommendation": "Cast value to standard numeric age or mark as null.",
                            "confidence": 0.98,
                            "suggested_correction": ""
                        })

                # Email Validation
                elif "email" in col_low:
                    if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', val):
                        total_invalid += 1
                        issues.append({
                            "category": "DATA_QUALITY",
                            "severity": "MEDIUM",
                            "title": "Malformed Email Address",
                            "location": f"Row {row_idx + 1}, Column '{col_name}'",
                            "value": val,
                            "expected_value": "user@domain.com",
                            "evidence": f"Invalid email format: '{val}'.",
                            "explanation": "String does not conform to RFC 5322 email syntax.",
                            "impact": "Failed communication, delivery bounce, or customer contact failure.",
                            "recommendation": "Correct email syntax with proper '@' and domain extension.",
                            "confidence": 0.97,
                            "suggested_correction": ""
                        })

                # Percentage Validation
                elif "percent" in col_low or "pct" in col_low or "%" in col_low:
                    clean_pct = val.replace("%", "").strip()
                    try:
                        pct_num = float(clean_pct)
                        if pct_num < 0 or pct_num > 100:
                            total_invalid += 1
                            issues.append({
                                "category": "DATA_QUALITY",
                                "severity": "MEDIUM",
                                "title": "Percentage Value Out of Range",
                                "location": f"Row {row_idx + 1}, Column '{col_name}'",
                                "value": val,
                                "expected_value": "0% - 100%",
                                "evidence": f"Percentage value recorded as '{val}'.",
                                "explanation": "Percentage exceeds standard 0-100% boundary.",
                                "impact": "May indicate an unscaled decimal (e.g. 150 vs 1.5) or computation error.",
                                "recommendation": "Verify scaling of rate / discount percentage.",
                                "confidence": 0.92,
                                "suggested_correction": ""
                            })
                    except ValueError:
                        pass

        # 4. Calculate Data Quality Scores
        completeness = max(0.0, 100.0 - (total_missing / max(1, total_cells)) * 100)
        uniqueness = max(0.0, 100.0 - (duplicate_count / max(1, num_rows)) * 100)
        validity = max(0.0, 100.0 - (total_invalid / max(1, total_cells)) * 100)
        consistency = 90.0 if not duplicate_count else 75.0
        
        overall_dq_score = round(0.35 * completeness + 0.30 * validity + 0.20 * uniqueness + 0.15 * consistency, 1)

        return {
            "quality_score": overall_dq_score,
            "completeness_score": round(completeness, 1),
            "validity_score": round(validity, 1),
            "uniqueness_score": round(uniqueness, 1),
            "consistency_score": round(consistency, 1),
            "profile": column_profiles,
            "row_count": num_rows,
            "column_count": num_cols,
            "issues": issues
        }
