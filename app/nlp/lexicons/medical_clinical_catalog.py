"""Clinical Healthcare and Medical Taxonomy Catalog."""
from typing import Dict, Any

CLINICAL_TERMS_BANK: Dict[str, Dict[str, Any]] = {
    "CLINICAL_CODE_001": {
        "id": 1,
        "clinical_term": "Clinical Encounter Evaluation #1",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_002": {
        "id": 2,
        "clinical_term": "Clinical Encounter Evaluation #2",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_003": {
        "id": 3,
        "clinical_term": "Clinical Encounter Evaluation #3",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_004": {
        "id": 4,
        "clinical_term": "Clinical Encounter Evaluation #4",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_005": {
        "id": 5,
        "clinical_term": "Clinical Encounter Evaluation #5",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_006": {
        "id": 6,
        "clinical_term": "Clinical Encounter Evaluation #6",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_007": {
        "id": 7,
        "clinical_term": "Clinical Encounter Evaluation #7",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_008": {
        "id": 8,
        "clinical_term": "Clinical Encounter Evaluation #8",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_009": {
        "id": 9,
        "clinical_term": "Clinical Encounter Evaluation #9",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_010": {
        "id": 10,
        "clinical_term": "Clinical Encounter Evaluation #10",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_011": {
        "id": 11,
        "clinical_term": "Clinical Encounter Evaluation #11",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_012": {
        "id": 12,
        "clinical_term": "Clinical Encounter Evaluation #12",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_013": {
        "id": 13,
        "clinical_term": "Clinical Encounter Evaluation #13",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_014": {
        "id": 14,
        "clinical_term": "Clinical Encounter Evaluation #14",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_015": {
        "id": 15,
        "clinical_term": "Clinical Encounter Evaluation #15",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_016": {
        "id": 16,
        "clinical_term": "Clinical Encounter Evaluation #16",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_017": {
        "id": 17,
        "clinical_term": "Clinical Encounter Evaluation #17",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_018": {
        "id": 18,
        "clinical_term": "Clinical Encounter Evaluation #18",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_019": {
        "id": 19,
        "clinical_term": "Clinical Encounter Evaluation #19",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_020": {
        "id": 20,
        "clinical_term": "Clinical Encounter Evaluation #20",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_021": {
        "id": 21,
        "clinical_term": "Clinical Encounter Evaluation #21",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_022": {
        "id": 22,
        "clinical_term": "Clinical Encounter Evaluation #22",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_023": {
        "id": 23,
        "clinical_term": "Clinical Encounter Evaluation #23",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_024": {
        "id": 24,
        "clinical_term": "Clinical Encounter Evaluation #24",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_025": {
        "id": 25,
        "clinical_term": "Clinical Encounter Evaluation #25",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_026": {
        "id": 26,
        "clinical_term": "Clinical Encounter Evaluation #26",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_027": {
        "id": 27,
        "clinical_term": "Clinical Encounter Evaluation #27",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_028": {
        "id": 28,
        "clinical_term": "Clinical Encounter Evaluation #28",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_029": {
        "id": 29,
        "clinical_term": "Clinical Encounter Evaluation #29",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_030": {
        "id": 30,
        "clinical_term": "Clinical Encounter Evaluation #30",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_031": {
        "id": 31,
        "clinical_term": "Clinical Encounter Evaluation #31",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_032": {
        "id": 32,
        "clinical_term": "Clinical Encounter Evaluation #32",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_033": {
        "id": 33,
        "clinical_term": "Clinical Encounter Evaluation #33",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_034": {
        "id": 34,
        "clinical_term": "Clinical Encounter Evaluation #34",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_035": {
        "id": 35,
        "clinical_term": "Clinical Encounter Evaluation #35",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_036": {
        "id": 36,
        "clinical_term": "Clinical Encounter Evaluation #36",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_037": {
        "id": 37,
        "clinical_term": "Clinical Encounter Evaluation #37",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_038": {
        "id": 38,
        "clinical_term": "Clinical Encounter Evaluation #38",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_039": {
        "id": 39,
        "clinical_term": "Clinical Encounter Evaluation #39",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_040": {
        "id": 40,
        "clinical_term": "Clinical Encounter Evaluation #40",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_041": {
        "id": 41,
        "clinical_term": "Clinical Encounter Evaluation #41",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_042": {
        "id": 42,
        "clinical_term": "Clinical Encounter Evaluation #42",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_043": {
        "id": 43,
        "clinical_term": "Clinical Encounter Evaluation #43",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_044": {
        "id": 44,
        "clinical_term": "Clinical Encounter Evaluation #44",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_045": {
        "id": 45,
        "clinical_term": "Clinical Encounter Evaluation #45",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_046": {
        "id": 46,
        "clinical_term": "Clinical Encounter Evaluation #46",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_047": {
        "id": 47,
        "clinical_term": "Clinical Encounter Evaluation #47",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_048": {
        "id": 48,
        "clinical_term": "Clinical Encounter Evaluation #48",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_049": {
        "id": 49,
        "clinical_term": "Clinical Encounter Evaluation #49",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_050": {
        "id": 50,
        "clinical_term": "Clinical Encounter Evaluation #50",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_051": {
        "id": 51,
        "clinical_term": "Clinical Encounter Evaluation #51",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_052": {
        "id": 52,
        "clinical_term": "Clinical Encounter Evaluation #52",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_053": {
        "id": 53,
        "clinical_term": "Clinical Encounter Evaluation #53",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_054": {
        "id": 54,
        "clinical_term": "Clinical Encounter Evaluation #54",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_055": {
        "id": 55,
        "clinical_term": "Clinical Encounter Evaluation #55",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_056": {
        "id": 56,
        "clinical_term": "Clinical Encounter Evaluation #56",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_057": {
        "id": 57,
        "clinical_term": "Clinical Encounter Evaluation #57",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_058": {
        "id": 58,
        "clinical_term": "Clinical Encounter Evaluation #58",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_059": {
        "id": 59,
        "clinical_term": "Clinical Encounter Evaluation #59",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_060": {
        "id": 60,
        "clinical_term": "Clinical Encounter Evaluation #60",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_061": {
        "id": 61,
        "clinical_term": "Clinical Encounter Evaluation #61",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_062": {
        "id": 62,
        "clinical_term": "Clinical Encounter Evaluation #62",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_063": {
        "id": 63,
        "clinical_term": "Clinical Encounter Evaluation #63",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_064": {
        "id": 64,
        "clinical_term": "Clinical Encounter Evaluation #64",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_065": {
        "id": 65,
        "clinical_term": "Clinical Encounter Evaluation #65",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_066": {
        "id": 66,
        "clinical_term": "Clinical Encounter Evaluation #66",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_067": {
        "id": 67,
        "clinical_term": "Clinical Encounter Evaluation #67",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_068": {
        "id": 68,
        "clinical_term": "Clinical Encounter Evaluation #68",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_069": {
        "id": 69,
        "clinical_term": "Clinical Encounter Evaluation #69",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_070": {
        "id": 70,
        "clinical_term": "Clinical Encounter Evaluation #70",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_071": {
        "id": 71,
        "clinical_term": "Clinical Encounter Evaluation #71",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_072": {
        "id": 72,
        "clinical_term": "Clinical Encounter Evaluation #72",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_073": {
        "id": 73,
        "clinical_term": "Clinical Encounter Evaluation #73",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_074": {
        "id": 74,
        "clinical_term": "Clinical Encounter Evaluation #74",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_075": {
        "id": 75,
        "clinical_term": "Clinical Encounter Evaluation #75",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_076": {
        "id": 76,
        "clinical_term": "Clinical Encounter Evaluation #76",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_077": {
        "id": 77,
        "clinical_term": "Clinical Encounter Evaluation #77",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_078": {
        "id": 78,
        "clinical_term": "Clinical Encounter Evaluation #78",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_079": {
        "id": 79,
        "clinical_term": "Clinical Encounter Evaluation #79",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_080": {
        "id": 80,
        "clinical_term": "Clinical Encounter Evaluation #80",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_081": {
        "id": 81,
        "clinical_term": "Clinical Encounter Evaluation #81",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_082": {
        "id": 82,
        "clinical_term": "Clinical Encounter Evaluation #82",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_083": {
        "id": 83,
        "clinical_term": "Clinical Encounter Evaluation #83",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_084": {
        "id": 84,
        "clinical_term": "Clinical Encounter Evaluation #84",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_085": {
        "id": 85,
        "clinical_term": "Clinical Encounter Evaluation #85",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_086": {
        "id": 86,
        "clinical_term": "Clinical Encounter Evaluation #86",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_087": {
        "id": 87,
        "clinical_term": "Clinical Encounter Evaluation #87",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_088": {
        "id": 88,
        "clinical_term": "Clinical Encounter Evaluation #88",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_089": {
        "id": 89,
        "clinical_term": "Clinical Encounter Evaluation #89",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_090": {
        "id": 90,
        "clinical_term": "Clinical Encounter Evaluation #90",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_091": {
        "id": 91,
        "clinical_term": "Clinical Encounter Evaluation #91",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_092": {
        "id": 92,
        "clinical_term": "Clinical Encounter Evaluation #92",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_093": {
        "id": 93,
        "clinical_term": "Clinical Encounter Evaluation #93",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_094": {
        "id": 94,
        "clinical_term": "Clinical Encounter Evaluation #94",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_095": {
        "id": 95,
        "clinical_term": "Clinical Encounter Evaluation #95",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_096": {
        "id": 96,
        "clinical_term": "Clinical Encounter Evaluation #96",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_097": {
        "id": 97,
        "clinical_term": "Clinical Encounter Evaluation #97",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_098": {
        "id": 98,
        "clinical_term": "Clinical Encounter Evaluation #98",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_099": {
        "id": 99,
        "clinical_term": "Clinical Encounter Evaluation #99",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_100": {
        "id": 100,
        "clinical_term": "Clinical Encounter Evaluation #100",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_101": {
        "id": 101,
        "clinical_term": "Clinical Encounter Evaluation #101",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_102": {
        "id": 102,
        "clinical_term": "Clinical Encounter Evaluation #102",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_103": {
        "id": 103,
        "clinical_term": "Clinical Encounter Evaluation #103",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_104": {
        "id": 104,
        "clinical_term": "Clinical Encounter Evaluation #104",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_105": {
        "id": 105,
        "clinical_term": "Clinical Encounter Evaluation #105",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_106": {
        "id": 106,
        "clinical_term": "Clinical Encounter Evaluation #106",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_107": {
        "id": 107,
        "clinical_term": "Clinical Encounter Evaluation #107",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_108": {
        "id": 108,
        "clinical_term": "Clinical Encounter Evaluation #108",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_109": {
        "id": 109,
        "clinical_term": "Clinical Encounter Evaluation #109",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_110": {
        "id": 110,
        "clinical_term": "Clinical Encounter Evaluation #110",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_111": {
        "id": 111,
        "clinical_term": "Clinical Encounter Evaluation #111",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_112": {
        "id": 112,
        "clinical_term": "Clinical Encounter Evaluation #112",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_113": {
        "id": 113,
        "clinical_term": "Clinical Encounter Evaluation #113",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_114": {
        "id": 114,
        "clinical_term": "Clinical Encounter Evaluation #114",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_115": {
        "id": 115,
        "clinical_term": "Clinical Encounter Evaluation #115",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_116": {
        "id": 116,
        "clinical_term": "Clinical Encounter Evaluation #116",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_117": {
        "id": 117,
        "clinical_term": "Clinical Encounter Evaluation #117",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_118": {
        "id": 118,
        "clinical_term": "Clinical Encounter Evaluation #118",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_119": {
        "id": 119,
        "clinical_term": "Clinical Encounter Evaluation #119",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_120": {
        "id": 120,
        "clinical_term": "Clinical Encounter Evaluation #120",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_121": {
        "id": 121,
        "clinical_term": "Clinical Encounter Evaluation #121",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_122": {
        "id": 122,
        "clinical_term": "Clinical Encounter Evaluation #122",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_123": {
        "id": 123,
        "clinical_term": "Clinical Encounter Evaluation #123",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_124": {
        "id": 124,
        "clinical_term": "Clinical Encounter Evaluation #124",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_125": {
        "id": 125,
        "clinical_term": "Clinical Encounter Evaluation #125",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_126": {
        "id": 126,
        "clinical_term": "Clinical Encounter Evaluation #126",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_127": {
        "id": 127,
        "clinical_term": "Clinical Encounter Evaluation #127",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_128": {
        "id": 128,
        "clinical_term": "Clinical Encounter Evaluation #128",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_129": {
        "id": 129,
        "clinical_term": "Clinical Encounter Evaluation #129",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_130": {
        "id": 130,
        "clinical_term": "Clinical Encounter Evaluation #130",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_131": {
        "id": 131,
        "clinical_term": "Clinical Encounter Evaluation #131",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_132": {
        "id": 132,
        "clinical_term": "Clinical Encounter Evaluation #132",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_133": {
        "id": 133,
        "clinical_term": "Clinical Encounter Evaluation #133",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_134": {
        "id": 134,
        "clinical_term": "Clinical Encounter Evaluation #134",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_135": {
        "id": 135,
        "clinical_term": "Clinical Encounter Evaluation #135",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_136": {
        "id": 136,
        "clinical_term": "Clinical Encounter Evaluation #136",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_137": {
        "id": 137,
        "clinical_term": "Clinical Encounter Evaluation #137",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_138": {
        "id": 138,
        "clinical_term": "Clinical Encounter Evaluation #138",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_139": {
        "id": 139,
        "clinical_term": "Clinical Encounter Evaluation #139",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_140": {
        "id": 140,
        "clinical_term": "Clinical Encounter Evaluation #140",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_141": {
        "id": 141,
        "clinical_term": "Clinical Encounter Evaluation #141",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_142": {
        "id": 142,
        "clinical_term": "Clinical Encounter Evaluation #142",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_143": {
        "id": 143,
        "clinical_term": "Clinical Encounter Evaluation #143",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_144": {
        "id": 144,
        "clinical_term": "Clinical Encounter Evaluation #144",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_145": {
        "id": 145,
        "clinical_term": "Clinical Encounter Evaluation #145",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_146": {
        "id": 146,
        "clinical_term": "Clinical Encounter Evaluation #146",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_147": {
        "id": 147,
        "clinical_term": "Clinical Encounter Evaluation #147",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_148": {
        "id": 148,
        "clinical_term": "Clinical Encounter Evaluation #148",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_149": {
        "id": 149,
        "clinical_term": "Clinical Encounter Evaluation #149",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_150": {
        "id": 150,
        "clinical_term": "Clinical Encounter Evaluation #150",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_151": {
        "id": 151,
        "clinical_term": "Clinical Encounter Evaluation #151",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_152": {
        "id": 152,
        "clinical_term": "Clinical Encounter Evaluation #152",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_153": {
        "id": 153,
        "clinical_term": "Clinical Encounter Evaluation #153",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_154": {
        "id": 154,
        "clinical_term": "Clinical Encounter Evaluation #154",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_155": {
        "id": 155,
        "clinical_term": "Clinical Encounter Evaluation #155",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_156": {
        "id": 156,
        "clinical_term": "Clinical Encounter Evaluation #156",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_157": {
        "id": 157,
        "clinical_term": "Clinical Encounter Evaluation #157",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_158": {
        "id": 158,
        "clinical_term": "Clinical Encounter Evaluation #158",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_159": {
        "id": 159,
        "clinical_term": "Clinical Encounter Evaluation #159",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_160": {
        "id": 160,
        "clinical_term": "Clinical Encounter Evaluation #160",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_161": {
        "id": 161,
        "clinical_term": "Clinical Encounter Evaluation #161",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_162": {
        "id": 162,
        "clinical_term": "Clinical Encounter Evaluation #162",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_163": {
        "id": 163,
        "clinical_term": "Clinical Encounter Evaluation #163",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_164": {
        "id": 164,
        "clinical_term": "Clinical Encounter Evaluation #164",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_165": {
        "id": 165,
        "clinical_term": "Clinical Encounter Evaluation #165",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_166": {
        "id": 166,
        "clinical_term": "Clinical Encounter Evaluation #166",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_167": {
        "id": 167,
        "clinical_term": "Clinical Encounter Evaluation #167",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_168": {
        "id": 168,
        "clinical_term": "Clinical Encounter Evaluation #168",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_169": {
        "id": 169,
        "clinical_term": "Clinical Encounter Evaluation #169",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_170": {
        "id": 170,
        "clinical_term": "Clinical Encounter Evaluation #170",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_171": {
        "id": 171,
        "clinical_term": "Clinical Encounter Evaluation #171",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_172": {
        "id": 172,
        "clinical_term": "Clinical Encounter Evaluation #172",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_173": {
        "id": 173,
        "clinical_term": "Clinical Encounter Evaluation #173",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_174": {
        "id": 174,
        "clinical_term": "Clinical Encounter Evaluation #174",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_175": {
        "id": 175,
        "clinical_term": "Clinical Encounter Evaluation #175",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_176": {
        "id": 176,
        "clinical_term": "Clinical Encounter Evaluation #176",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_177": {
        "id": 177,
        "clinical_term": "Clinical Encounter Evaluation #177",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_178": {
        "id": 178,
        "clinical_term": "Clinical Encounter Evaluation #178",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_179": {
        "id": 179,
        "clinical_term": "Clinical Encounter Evaluation #179",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_180": {
        "id": 180,
        "clinical_term": "Clinical Encounter Evaluation #180",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_181": {
        "id": 181,
        "clinical_term": "Clinical Encounter Evaluation #181",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_182": {
        "id": 182,
        "clinical_term": "Clinical Encounter Evaluation #182",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_183": {
        "id": 183,
        "clinical_term": "Clinical Encounter Evaluation #183",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_184": {
        "id": 184,
        "clinical_term": "Clinical Encounter Evaluation #184",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_185": {
        "id": 185,
        "clinical_term": "Clinical Encounter Evaluation #185",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_186": {
        "id": 186,
        "clinical_term": "Clinical Encounter Evaluation #186",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_187": {
        "id": 187,
        "clinical_term": "Clinical Encounter Evaluation #187",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_188": {
        "id": 188,
        "clinical_term": "Clinical Encounter Evaluation #188",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_189": {
        "id": 189,
        "clinical_term": "Clinical Encounter Evaluation #189",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_190": {
        "id": 190,
        "clinical_term": "Clinical Encounter Evaluation #190",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_191": {
        "id": 191,
        "clinical_term": "Clinical Encounter Evaluation #191",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_192": {
        "id": 192,
        "clinical_term": "Clinical Encounter Evaluation #192",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_193": {
        "id": 193,
        "clinical_term": "Clinical Encounter Evaluation #193",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_194": {
        "id": 194,
        "clinical_term": "Clinical Encounter Evaluation #194",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_195": {
        "id": 195,
        "clinical_term": "Clinical Encounter Evaluation #195",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_196": {
        "id": 196,
        "clinical_term": "Clinical Encounter Evaluation #196",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_197": {
        "id": 197,
        "clinical_term": "Clinical Encounter Evaluation #197",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_198": {
        "id": 198,
        "clinical_term": "Clinical Encounter Evaluation #198",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_199": {
        "id": 199,
        "clinical_term": "Clinical Encounter Evaluation #199",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
    "CLINICAL_CODE_200": {
        "id": 200,
        "clinical_term": "Clinical Encounter Evaluation #200",
        "classification": "ICD-10-CM Concept" if idx % 2 == 0 else "CPT Procedure Concept",
        "phi_sensitivity": "HIGH" if idx % 3 == 0 else "MODERATE",
        "audit_rules": [
            "Ensure patient direct identifiers are redacted in secondary research datasets.",
            "Verify diagnostic codes correlate with documented clinical findings and laboratory markers.",
            "Validate informed consent forms are signed and archived prior to elective procedures.",
            "Inspect prescription dosage, frequency, and contraindication warning flags."
        ]
    },
}
