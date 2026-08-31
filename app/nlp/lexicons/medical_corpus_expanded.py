"""Expanded Clinical Informatics & HIPAA PHI Catalog (500 Entities)."""
from typing import Dict, Any

EXPANDED_CLINICAL_ENTITIES: Dict[str, Dict[str, Any]] = {
    "MED_ENTITY_EXP_0001": {
        "entity_id": "MED-0001",
        "medical_term": "Clinical Diagnostic Code & Procedure #1",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0002": {
        "entity_id": "MED-0002",
        "medical_term": "Clinical Diagnostic Code & Procedure #2",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0003": {
        "entity_id": "MED-0003",
        "medical_term": "Clinical Diagnostic Code & Procedure #3",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0004": {
        "entity_id": "MED-0004",
        "medical_term": "Clinical Diagnostic Code & Procedure #4",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0005": {
        "entity_id": "MED-0005",
        "medical_term": "Clinical Diagnostic Code & Procedure #5",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0006": {
        "entity_id": "MED-0006",
        "medical_term": "Clinical Diagnostic Code & Procedure #6",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0007": {
        "entity_id": "MED-0007",
        "medical_term": "Clinical Diagnostic Code & Procedure #7",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0008": {
        "entity_id": "MED-0008",
        "medical_term": "Clinical Diagnostic Code & Procedure #8",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0009": {
        "entity_id": "MED-0009",
        "medical_term": "Clinical Diagnostic Code & Procedure #9",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0010": {
        "entity_id": "MED-0010",
        "medical_term": "Clinical Diagnostic Code & Procedure #10",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0011": {
        "entity_id": "MED-0011",
        "medical_term": "Clinical Diagnostic Code & Procedure #11",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0012": {
        "entity_id": "MED-0012",
        "medical_term": "Clinical Diagnostic Code & Procedure #12",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0013": {
        "entity_id": "MED-0013",
        "medical_term": "Clinical Diagnostic Code & Procedure #13",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0014": {
        "entity_id": "MED-0014",
        "medical_term": "Clinical Diagnostic Code & Procedure #14",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0015": {
        "entity_id": "MED-0015",
        "medical_term": "Clinical Diagnostic Code & Procedure #15",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0016": {
        "entity_id": "MED-0016",
        "medical_term": "Clinical Diagnostic Code & Procedure #16",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0017": {
        "entity_id": "MED-0017",
        "medical_term": "Clinical Diagnostic Code & Procedure #17",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0018": {
        "entity_id": "MED-0018",
        "medical_term": "Clinical Diagnostic Code & Procedure #18",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0019": {
        "entity_id": "MED-0019",
        "medical_term": "Clinical Diagnostic Code & Procedure #19",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0020": {
        "entity_id": "MED-0020",
        "medical_term": "Clinical Diagnostic Code & Procedure #20",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0021": {
        "entity_id": "MED-0021",
        "medical_term": "Clinical Diagnostic Code & Procedure #21",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0022": {
        "entity_id": "MED-0022",
        "medical_term": "Clinical Diagnostic Code & Procedure #22",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0023": {
        "entity_id": "MED-0023",
        "medical_term": "Clinical Diagnostic Code & Procedure #23",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0024": {
        "entity_id": "MED-0024",
        "medical_term": "Clinical Diagnostic Code & Procedure #24",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0025": {
        "entity_id": "MED-0025",
        "medical_term": "Clinical Diagnostic Code & Procedure #25",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0026": {
        "entity_id": "MED-0026",
        "medical_term": "Clinical Diagnostic Code & Procedure #26",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0027": {
        "entity_id": "MED-0027",
        "medical_term": "Clinical Diagnostic Code & Procedure #27",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0028": {
        "entity_id": "MED-0028",
        "medical_term": "Clinical Diagnostic Code & Procedure #28",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0029": {
        "entity_id": "MED-0029",
        "medical_term": "Clinical Diagnostic Code & Procedure #29",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0030": {
        "entity_id": "MED-0030",
        "medical_term": "Clinical Diagnostic Code & Procedure #30",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0031": {
        "entity_id": "MED-0031",
        "medical_term": "Clinical Diagnostic Code & Procedure #31",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0032": {
        "entity_id": "MED-0032",
        "medical_term": "Clinical Diagnostic Code & Procedure #32",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0033": {
        "entity_id": "MED-0033",
        "medical_term": "Clinical Diagnostic Code & Procedure #33",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0034": {
        "entity_id": "MED-0034",
        "medical_term": "Clinical Diagnostic Code & Procedure #34",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0035": {
        "entity_id": "MED-0035",
        "medical_term": "Clinical Diagnostic Code & Procedure #35",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0036": {
        "entity_id": "MED-0036",
        "medical_term": "Clinical Diagnostic Code & Procedure #36",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0037": {
        "entity_id": "MED-0037",
        "medical_term": "Clinical Diagnostic Code & Procedure #37",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0038": {
        "entity_id": "MED-0038",
        "medical_term": "Clinical Diagnostic Code & Procedure #38",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0039": {
        "entity_id": "MED-0039",
        "medical_term": "Clinical Diagnostic Code & Procedure #39",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0040": {
        "entity_id": "MED-0040",
        "medical_term": "Clinical Diagnostic Code & Procedure #40",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0041": {
        "entity_id": "MED-0041",
        "medical_term": "Clinical Diagnostic Code & Procedure #41",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0042": {
        "entity_id": "MED-0042",
        "medical_term": "Clinical Diagnostic Code & Procedure #42",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0043": {
        "entity_id": "MED-0043",
        "medical_term": "Clinical Diagnostic Code & Procedure #43",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0044": {
        "entity_id": "MED-0044",
        "medical_term": "Clinical Diagnostic Code & Procedure #44",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0045": {
        "entity_id": "MED-0045",
        "medical_term": "Clinical Diagnostic Code & Procedure #45",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0046": {
        "entity_id": "MED-0046",
        "medical_term": "Clinical Diagnostic Code & Procedure #46",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0047": {
        "entity_id": "MED-0047",
        "medical_term": "Clinical Diagnostic Code & Procedure #47",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0048": {
        "entity_id": "MED-0048",
        "medical_term": "Clinical Diagnostic Code & Procedure #48",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0049": {
        "entity_id": "MED-0049",
        "medical_term": "Clinical Diagnostic Code & Procedure #49",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0050": {
        "entity_id": "MED-0050",
        "medical_term": "Clinical Diagnostic Code & Procedure #50",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0051": {
        "entity_id": "MED-0051",
        "medical_term": "Clinical Diagnostic Code & Procedure #51",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0052": {
        "entity_id": "MED-0052",
        "medical_term": "Clinical Diagnostic Code & Procedure #52",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0053": {
        "entity_id": "MED-0053",
        "medical_term": "Clinical Diagnostic Code & Procedure #53",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0054": {
        "entity_id": "MED-0054",
        "medical_term": "Clinical Diagnostic Code & Procedure #54",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0055": {
        "entity_id": "MED-0055",
        "medical_term": "Clinical Diagnostic Code & Procedure #55",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0056": {
        "entity_id": "MED-0056",
        "medical_term": "Clinical Diagnostic Code & Procedure #56",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0057": {
        "entity_id": "MED-0057",
        "medical_term": "Clinical Diagnostic Code & Procedure #57",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0058": {
        "entity_id": "MED-0058",
        "medical_term": "Clinical Diagnostic Code & Procedure #58",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0059": {
        "entity_id": "MED-0059",
        "medical_term": "Clinical Diagnostic Code & Procedure #59",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0060": {
        "entity_id": "MED-0060",
        "medical_term": "Clinical Diagnostic Code & Procedure #60",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0061": {
        "entity_id": "MED-0061",
        "medical_term": "Clinical Diagnostic Code & Procedure #61",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0062": {
        "entity_id": "MED-0062",
        "medical_term": "Clinical Diagnostic Code & Procedure #62",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0063": {
        "entity_id": "MED-0063",
        "medical_term": "Clinical Diagnostic Code & Procedure #63",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0064": {
        "entity_id": "MED-0064",
        "medical_term": "Clinical Diagnostic Code & Procedure #64",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0065": {
        "entity_id": "MED-0065",
        "medical_term": "Clinical Diagnostic Code & Procedure #65",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0066": {
        "entity_id": "MED-0066",
        "medical_term": "Clinical Diagnostic Code & Procedure #66",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0067": {
        "entity_id": "MED-0067",
        "medical_term": "Clinical Diagnostic Code & Procedure #67",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0068": {
        "entity_id": "MED-0068",
        "medical_term": "Clinical Diagnostic Code & Procedure #68",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0069": {
        "entity_id": "MED-0069",
        "medical_term": "Clinical Diagnostic Code & Procedure #69",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0070": {
        "entity_id": "MED-0070",
        "medical_term": "Clinical Diagnostic Code & Procedure #70",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0071": {
        "entity_id": "MED-0071",
        "medical_term": "Clinical Diagnostic Code & Procedure #71",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0072": {
        "entity_id": "MED-0072",
        "medical_term": "Clinical Diagnostic Code & Procedure #72",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0073": {
        "entity_id": "MED-0073",
        "medical_term": "Clinical Diagnostic Code & Procedure #73",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0074": {
        "entity_id": "MED-0074",
        "medical_term": "Clinical Diagnostic Code & Procedure #74",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0075": {
        "entity_id": "MED-0075",
        "medical_term": "Clinical Diagnostic Code & Procedure #75",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0076": {
        "entity_id": "MED-0076",
        "medical_term": "Clinical Diagnostic Code & Procedure #76",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0077": {
        "entity_id": "MED-0077",
        "medical_term": "Clinical Diagnostic Code & Procedure #77",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0078": {
        "entity_id": "MED-0078",
        "medical_term": "Clinical Diagnostic Code & Procedure #78",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0079": {
        "entity_id": "MED-0079",
        "medical_term": "Clinical Diagnostic Code & Procedure #79",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0080": {
        "entity_id": "MED-0080",
        "medical_term": "Clinical Diagnostic Code & Procedure #80",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0081": {
        "entity_id": "MED-0081",
        "medical_term": "Clinical Diagnostic Code & Procedure #81",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0082": {
        "entity_id": "MED-0082",
        "medical_term": "Clinical Diagnostic Code & Procedure #82",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0083": {
        "entity_id": "MED-0083",
        "medical_term": "Clinical Diagnostic Code & Procedure #83",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0084": {
        "entity_id": "MED-0084",
        "medical_term": "Clinical Diagnostic Code & Procedure #84",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0085": {
        "entity_id": "MED-0085",
        "medical_term": "Clinical Diagnostic Code & Procedure #85",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0086": {
        "entity_id": "MED-0086",
        "medical_term": "Clinical Diagnostic Code & Procedure #86",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0087": {
        "entity_id": "MED-0087",
        "medical_term": "Clinical Diagnostic Code & Procedure #87",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0088": {
        "entity_id": "MED-0088",
        "medical_term": "Clinical Diagnostic Code & Procedure #88",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0089": {
        "entity_id": "MED-0089",
        "medical_term": "Clinical Diagnostic Code & Procedure #89",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0090": {
        "entity_id": "MED-0090",
        "medical_term": "Clinical Diagnostic Code & Procedure #90",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0091": {
        "entity_id": "MED-0091",
        "medical_term": "Clinical Diagnostic Code & Procedure #91",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0092": {
        "entity_id": "MED-0092",
        "medical_term": "Clinical Diagnostic Code & Procedure #92",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0093": {
        "entity_id": "MED-0093",
        "medical_term": "Clinical Diagnostic Code & Procedure #93",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0094": {
        "entity_id": "MED-0094",
        "medical_term": "Clinical Diagnostic Code & Procedure #94",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0095": {
        "entity_id": "MED-0095",
        "medical_term": "Clinical Diagnostic Code & Procedure #95",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0096": {
        "entity_id": "MED-0096",
        "medical_term": "Clinical Diagnostic Code & Procedure #96",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0097": {
        "entity_id": "MED-0097",
        "medical_term": "Clinical Diagnostic Code & Procedure #97",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0098": {
        "entity_id": "MED-0098",
        "medical_term": "Clinical Diagnostic Code & Procedure #98",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0099": {
        "entity_id": "MED-0099",
        "medical_term": "Clinical Diagnostic Code & Procedure #99",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0100": {
        "entity_id": "MED-0100",
        "medical_term": "Clinical Diagnostic Code & Procedure #100",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0101": {
        "entity_id": "MED-0101",
        "medical_term": "Clinical Diagnostic Code & Procedure #101",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0102": {
        "entity_id": "MED-0102",
        "medical_term": "Clinical Diagnostic Code & Procedure #102",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0103": {
        "entity_id": "MED-0103",
        "medical_term": "Clinical Diagnostic Code & Procedure #103",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0104": {
        "entity_id": "MED-0104",
        "medical_term": "Clinical Diagnostic Code & Procedure #104",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0105": {
        "entity_id": "MED-0105",
        "medical_term": "Clinical Diagnostic Code & Procedure #105",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0106": {
        "entity_id": "MED-0106",
        "medical_term": "Clinical Diagnostic Code & Procedure #106",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0107": {
        "entity_id": "MED-0107",
        "medical_term": "Clinical Diagnostic Code & Procedure #107",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0108": {
        "entity_id": "MED-0108",
        "medical_term": "Clinical Diagnostic Code & Procedure #108",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0109": {
        "entity_id": "MED-0109",
        "medical_term": "Clinical Diagnostic Code & Procedure #109",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0110": {
        "entity_id": "MED-0110",
        "medical_term": "Clinical Diagnostic Code & Procedure #110",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0111": {
        "entity_id": "MED-0111",
        "medical_term": "Clinical Diagnostic Code & Procedure #111",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0112": {
        "entity_id": "MED-0112",
        "medical_term": "Clinical Diagnostic Code & Procedure #112",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0113": {
        "entity_id": "MED-0113",
        "medical_term": "Clinical Diagnostic Code & Procedure #113",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0114": {
        "entity_id": "MED-0114",
        "medical_term": "Clinical Diagnostic Code & Procedure #114",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0115": {
        "entity_id": "MED-0115",
        "medical_term": "Clinical Diagnostic Code & Procedure #115",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0116": {
        "entity_id": "MED-0116",
        "medical_term": "Clinical Diagnostic Code & Procedure #116",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0117": {
        "entity_id": "MED-0117",
        "medical_term": "Clinical Diagnostic Code & Procedure #117",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0118": {
        "entity_id": "MED-0118",
        "medical_term": "Clinical Diagnostic Code & Procedure #118",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0119": {
        "entity_id": "MED-0119",
        "medical_term": "Clinical Diagnostic Code & Procedure #119",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0120": {
        "entity_id": "MED-0120",
        "medical_term": "Clinical Diagnostic Code & Procedure #120",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0121": {
        "entity_id": "MED-0121",
        "medical_term": "Clinical Diagnostic Code & Procedure #121",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0122": {
        "entity_id": "MED-0122",
        "medical_term": "Clinical Diagnostic Code & Procedure #122",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0123": {
        "entity_id": "MED-0123",
        "medical_term": "Clinical Diagnostic Code & Procedure #123",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0124": {
        "entity_id": "MED-0124",
        "medical_term": "Clinical Diagnostic Code & Procedure #124",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0125": {
        "entity_id": "MED-0125",
        "medical_term": "Clinical Diagnostic Code & Procedure #125",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0126": {
        "entity_id": "MED-0126",
        "medical_term": "Clinical Diagnostic Code & Procedure #126",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0127": {
        "entity_id": "MED-0127",
        "medical_term": "Clinical Diagnostic Code & Procedure #127",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0128": {
        "entity_id": "MED-0128",
        "medical_term": "Clinical Diagnostic Code & Procedure #128",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0129": {
        "entity_id": "MED-0129",
        "medical_term": "Clinical Diagnostic Code & Procedure #129",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0130": {
        "entity_id": "MED-0130",
        "medical_term": "Clinical Diagnostic Code & Procedure #130",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0131": {
        "entity_id": "MED-0131",
        "medical_term": "Clinical Diagnostic Code & Procedure #131",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0132": {
        "entity_id": "MED-0132",
        "medical_term": "Clinical Diagnostic Code & Procedure #132",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0133": {
        "entity_id": "MED-0133",
        "medical_term": "Clinical Diagnostic Code & Procedure #133",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0134": {
        "entity_id": "MED-0134",
        "medical_term": "Clinical Diagnostic Code & Procedure #134",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0135": {
        "entity_id": "MED-0135",
        "medical_term": "Clinical Diagnostic Code & Procedure #135",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0136": {
        "entity_id": "MED-0136",
        "medical_term": "Clinical Diagnostic Code & Procedure #136",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0137": {
        "entity_id": "MED-0137",
        "medical_term": "Clinical Diagnostic Code & Procedure #137",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0138": {
        "entity_id": "MED-0138",
        "medical_term": "Clinical Diagnostic Code & Procedure #138",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0139": {
        "entity_id": "MED-0139",
        "medical_term": "Clinical Diagnostic Code & Procedure #139",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0140": {
        "entity_id": "MED-0140",
        "medical_term": "Clinical Diagnostic Code & Procedure #140",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0141": {
        "entity_id": "MED-0141",
        "medical_term": "Clinical Diagnostic Code & Procedure #141",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0142": {
        "entity_id": "MED-0142",
        "medical_term": "Clinical Diagnostic Code & Procedure #142",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0143": {
        "entity_id": "MED-0143",
        "medical_term": "Clinical Diagnostic Code & Procedure #143",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0144": {
        "entity_id": "MED-0144",
        "medical_term": "Clinical Diagnostic Code & Procedure #144",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0145": {
        "entity_id": "MED-0145",
        "medical_term": "Clinical Diagnostic Code & Procedure #145",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0146": {
        "entity_id": "MED-0146",
        "medical_term": "Clinical Diagnostic Code & Procedure #146",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0147": {
        "entity_id": "MED-0147",
        "medical_term": "Clinical Diagnostic Code & Procedure #147",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0148": {
        "entity_id": "MED-0148",
        "medical_term": "Clinical Diagnostic Code & Procedure #148",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0149": {
        "entity_id": "MED-0149",
        "medical_term": "Clinical Diagnostic Code & Procedure #149",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0150": {
        "entity_id": "MED-0150",
        "medical_term": "Clinical Diagnostic Code & Procedure #150",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0151": {
        "entity_id": "MED-0151",
        "medical_term": "Clinical Diagnostic Code & Procedure #151",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0152": {
        "entity_id": "MED-0152",
        "medical_term": "Clinical Diagnostic Code & Procedure #152",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0153": {
        "entity_id": "MED-0153",
        "medical_term": "Clinical Diagnostic Code & Procedure #153",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0154": {
        "entity_id": "MED-0154",
        "medical_term": "Clinical Diagnostic Code & Procedure #154",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0155": {
        "entity_id": "MED-0155",
        "medical_term": "Clinical Diagnostic Code & Procedure #155",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0156": {
        "entity_id": "MED-0156",
        "medical_term": "Clinical Diagnostic Code & Procedure #156",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0157": {
        "entity_id": "MED-0157",
        "medical_term": "Clinical Diagnostic Code & Procedure #157",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0158": {
        "entity_id": "MED-0158",
        "medical_term": "Clinical Diagnostic Code & Procedure #158",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0159": {
        "entity_id": "MED-0159",
        "medical_term": "Clinical Diagnostic Code & Procedure #159",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0160": {
        "entity_id": "MED-0160",
        "medical_term": "Clinical Diagnostic Code & Procedure #160",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0161": {
        "entity_id": "MED-0161",
        "medical_term": "Clinical Diagnostic Code & Procedure #161",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0162": {
        "entity_id": "MED-0162",
        "medical_term": "Clinical Diagnostic Code & Procedure #162",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0163": {
        "entity_id": "MED-0163",
        "medical_term": "Clinical Diagnostic Code & Procedure #163",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0164": {
        "entity_id": "MED-0164",
        "medical_term": "Clinical Diagnostic Code & Procedure #164",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0165": {
        "entity_id": "MED-0165",
        "medical_term": "Clinical Diagnostic Code & Procedure #165",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0166": {
        "entity_id": "MED-0166",
        "medical_term": "Clinical Diagnostic Code & Procedure #166",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0167": {
        "entity_id": "MED-0167",
        "medical_term": "Clinical Diagnostic Code & Procedure #167",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0168": {
        "entity_id": "MED-0168",
        "medical_term": "Clinical Diagnostic Code & Procedure #168",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0169": {
        "entity_id": "MED-0169",
        "medical_term": "Clinical Diagnostic Code & Procedure #169",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0170": {
        "entity_id": "MED-0170",
        "medical_term": "Clinical Diagnostic Code & Procedure #170",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0171": {
        "entity_id": "MED-0171",
        "medical_term": "Clinical Diagnostic Code & Procedure #171",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0172": {
        "entity_id": "MED-0172",
        "medical_term": "Clinical Diagnostic Code & Procedure #172",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0173": {
        "entity_id": "MED-0173",
        "medical_term": "Clinical Diagnostic Code & Procedure #173",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0174": {
        "entity_id": "MED-0174",
        "medical_term": "Clinical Diagnostic Code & Procedure #174",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0175": {
        "entity_id": "MED-0175",
        "medical_term": "Clinical Diagnostic Code & Procedure #175",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0176": {
        "entity_id": "MED-0176",
        "medical_term": "Clinical Diagnostic Code & Procedure #176",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0177": {
        "entity_id": "MED-0177",
        "medical_term": "Clinical Diagnostic Code & Procedure #177",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0178": {
        "entity_id": "MED-0178",
        "medical_term": "Clinical Diagnostic Code & Procedure #178",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0179": {
        "entity_id": "MED-0179",
        "medical_term": "Clinical Diagnostic Code & Procedure #179",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0180": {
        "entity_id": "MED-0180",
        "medical_term": "Clinical Diagnostic Code & Procedure #180",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0181": {
        "entity_id": "MED-0181",
        "medical_term": "Clinical Diagnostic Code & Procedure #181",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0182": {
        "entity_id": "MED-0182",
        "medical_term": "Clinical Diagnostic Code & Procedure #182",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0183": {
        "entity_id": "MED-0183",
        "medical_term": "Clinical Diagnostic Code & Procedure #183",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0184": {
        "entity_id": "MED-0184",
        "medical_term": "Clinical Diagnostic Code & Procedure #184",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0185": {
        "entity_id": "MED-0185",
        "medical_term": "Clinical Diagnostic Code & Procedure #185",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0186": {
        "entity_id": "MED-0186",
        "medical_term": "Clinical Diagnostic Code & Procedure #186",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0187": {
        "entity_id": "MED-0187",
        "medical_term": "Clinical Diagnostic Code & Procedure #187",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0188": {
        "entity_id": "MED-0188",
        "medical_term": "Clinical Diagnostic Code & Procedure #188",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0189": {
        "entity_id": "MED-0189",
        "medical_term": "Clinical Diagnostic Code & Procedure #189",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0190": {
        "entity_id": "MED-0190",
        "medical_term": "Clinical Diagnostic Code & Procedure #190",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0191": {
        "entity_id": "MED-0191",
        "medical_term": "Clinical Diagnostic Code & Procedure #191",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0192": {
        "entity_id": "MED-0192",
        "medical_term": "Clinical Diagnostic Code & Procedure #192",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0193": {
        "entity_id": "MED-0193",
        "medical_term": "Clinical Diagnostic Code & Procedure #193",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0194": {
        "entity_id": "MED-0194",
        "medical_term": "Clinical Diagnostic Code & Procedure #194",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0195": {
        "entity_id": "MED-0195",
        "medical_term": "Clinical Diagnostic Code & Procedure #195",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0196": {
        "entity_id": "MED-0196",
        "medical_term": "Clinical Diagnostic Code & Procedure #196",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0197": {
        "entity_id": "MED-0197",
        "medical_term": "Clinical Diagnostic Code & Procedure #197",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0198": {
        "entity_id": "MED-0198",
        "medical_term": "Clinical Diagnostic Code & Procedure #198",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0199": {
        "entity_id": "MED-0199",
        "medical_term": "Clinical Diagnostic Code & Procedure #199",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0200": {
        "entity_id": "MED-0200",
        "medical_term": "Clinical Diagnostic Code & Procedure #200",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0201": {
        "entity_id": "MED-0201",
        "medical_term": "Clinical Diagnostic Code & Procedure #201",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0202": {
        "entity_id": "MED-0202",
        "medical_term": "Clinical Diagnostic Code & Procedure #202",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0203": {
        "entity_id": "MED-0203",
        "medical_term": "Clinical Diagnostic Code & Procedure #203",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0204": {
        "entity_id": "MED-0204",
        "medical_term": "Clinical Diagnostic Code & Procedure #204",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0205": {
        "entity_id": "MED-0205",
        "medical_term": "Clinical Diagnostic Code & Procedure #205",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0206": {
        "entity_id": "MED-0206",
        "medical_term": "Clinical Diagnostic Code & Procedure #206",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0207": {
        "entity_id": "MED-0207",
        "medical_term": "Clinical Diagnostic Code & Procedure #207",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0208": {
        "entity_id": "MED-0208",
        "medical_term": "Clinical Diagnostic Code & Procedure #208",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0209": {
        "entity_id": "MED-0209",
        "medical_term": "Clinical Diagnostic Code & Procedure #209",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0210": {
        "entity_id": "MED-0210",
        "medical_term": "Clinical Diagnostic Code & Procedure #210",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0211": {
        "entity_id": "MED-0211",
        "medical_term": "Clinical Diagnostic Code & Procedure #211",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0212": {
        "entity_id": "MED-0212",
        "medical_term": "Clinical Diagnostic Code & Procedure #212",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0213": {
        "entity_id": "MED-0213",
        "medical_term": "Clinical Diagnostic Code & Procedure #213",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0214": {
        "entity_id": "MED-0214",
        "medical_term": "Clinical Diagnostic Code & Procedure #214",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0215": {
        "entity_id": "MED-0215",
        "medical_term": "Clinical Diagnostic Code & Procedure #215",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0216": {
        "entity_id": "MED-0216",
        "medical_term": "Clinical Diagnostic Code & Procedure #216",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0217": {
        "entity_id": "MED-0217",
        "medical_term": "Clinical Diagnostic Code & Procedure #217",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0218": {
        "entity_id": "MED-0218",
        "medical_term": "Clinical Diagnostic Code & Procedure #218",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0219": {
        "entity_id": "MED-0219",
        "medical_term": "Clinical Diagnostic Code & Procedure #219",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0220": {
        "entity_id": "MED-0220",
        "medical_term": "Clinical Diagnostic Code & Procedure #220",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0221": {
        "entity_id": "MED-0221",
        "medical_term": "Clinical Diagnostic Code & Procedure #221",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0222": {
        "entity_id": "MED-0222",
        "medical_term": "Clinical Diagnostic Code & Procedure #222",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0223": {
        "entity_id": "MED-0223",
        "medical_term": "Clinical Diagnostic Code & Procedure #223",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0224": {
        "entity_id": "MED-0224",
        "medical_term": "Clinical Diagnostic Code & Procedure #224",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0225": {
        "entity_id": "MED-0225",
        "medical_term": "Clinical Diagnostic Code & Procedure #225",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0226": {
        "entity_id": "MED-0226",
        "medical_term": "Clinical Diagnostic Code & Procedure #226",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0227": {
        "entity_id": "MED-0227",
        "medical_term": "Clinical Diagnostic Code & Procedure #227",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0228": {
        "entity_id": "MED-0228",
        "medical_term": "Clinical Diagnostic Code & Procedure #228",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0229": {
        "entity_id": "MED-0229",
        "medical_term": "Clinical Diagnostic Code & Procedure #229",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0230": {
        "entity_id": "MED-0230",
        "medical_term": "Clinical Diagnostic Code & Procedure #230",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0231": {
        "entity_id": "MED-0231",
        "medical_term": "Clinical Diagnostic Code & Procedure #231",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0232": {
        "entity_id": "MED-0232",
        "medical_term": "Clinical Diagnostic Code & Procedure #232",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0233": {
        "entity_id": "MED-0233",
        "medical_term": "Clinical Diagnostic Code & Procedure #233",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0234": {
        "entity_id": "MED-0234",
        "medical_term": "Clinical Diagnostic Code & Procedure #234",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0235": {
        "entity_id": "MED-0235",
        "medical_term": "Clinical Diagnostic Code & Procedure #235",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0236": {
        "entity_id": "MED-0236",
        "medical_term": "Clinical Diagnostic Code & Procedure #236",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0237": {
        "entity_id": "MED-0237",
        "medical_term": "Clinical Diagnostic Code & Procedure #237",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0238": {
        "entity_id": "MED-0238",
        "medical_term": "Clinical Diagnostic Code & Procedure #238",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0239": {
        "entity_id": "MED-0239",
        "medical_term": "Clinical Diagnostic Code & Procedure #239",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0240": {
        "entity_id": "MED-0240",
        "medical_term": "Clinical Diagnostic Code & Procedure #240",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0241": {
        "entity_id": "MED-0241",
        "medical_term": "Clinical Diagnostic Code & Procedure #241",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0242": {
        "entity_id": "MED-0242",
        "medical_term": "Clinical Diagnostic Code & Procedure #242",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0243": {
        "entity_id": "MED-0243",
        "medical_term": "Clinical Diagnostic Code & Procedure #243",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0244": {
        "entity_id": "MED-0244",
        "medical_term": "Clinical Diagnostic Code & Procedure #244",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0245": {
        "entity_id": "MED-0245",
        "medical_term": "Clinical Diagnostic Code & Procedure #245",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0246": {
        "entity_id": "MED-0246",
        "medical_term": "Clinical Diagnostic Code & Procedure #246",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0247": {
        "entity_id": "MED-0247",
        "medical_term": "Clinical Diagnostic Code & Procedure #247",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0248": {
        "entity_id": "MED-0248",
        "medical_term": "Clinical Diagnostic Code & Procedure #248",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0249": {
        "entity_id": "MED-0249",
        "medical_term": "Clinical Diagnostic Code & Procedure #249",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0250": {
        "entity_id": "MED-0250",
        "medical_term": "Clinical Diagnostic Code & Procedure #250",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0251": {
        "entity_id": "MED-0251",
        "medical_term": "Clinical Diagnostic Code & Procedure #251",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0252": {
        "entity_id": "MED-0252",
        "medical_term": "Clinical Diagnostic Code & Procedure #252",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0253": {
        "entity_id": "MED-0253",
        "medical_term": "Clinical Diagnostic Code & Procedure #253",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0254": {
        "entity_id": "MED-0254",
        "medical_term": "Clinical Diagnostic Code & Procedure #254",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0255": {
        "entity_id": "MED-0255",
        "medical_term": "Clinical Diagnostic Code & Procedure #255",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0256": {
        "entity_id": "MED-0256",
        "medical_term": "Clinical Diagnostic Code & Procedure #256",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0257": {
        "entity_id": "MED-0257",
        "medical_term": "Clinical Diagnostic Code & Procedure #257",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0258": {
        "entity_id": "MED-0258",
        "medical_term": "Clinical Diagnostic Code & Procedure #258",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0259": {
        "entity_id": "MED-0259",
        "medical_term": "Clinical Diagnostic Code & Procedure #259",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0260": {
        "entity_id": "MED-0260",
        "medical_term": "Clinical Diagnostic Code & Procedure #260",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0261": {
        "entity_id": "MED-0261",
        "medical_term": "Clinical Diagnostic Code & Procedure #261",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0262": {
        "entity_id": "MED-0262",
        "medical_term": "Clinical Diagnostic Code & Procedure #262",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0263": {
        "entity_id": "MED-0263",
        "medical_term": "Clinical Diagnostic Code & Procedure #263",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0264": {
        "entity_id": "MED-0264",
        "medical_term": "Clinical Diagnostic Code & Procedure #264",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0265": {
        "entity_id": "MED-0265",
        "medical_term": "Clinical Diagnostic Code & Procedure #265",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0266": {
        "entity_id": "MED-0266",
        "medical_term": "Clinical Diagnostic Code & Procedure #266",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0267": {
        "entity_id": "MED-0267",
        "medical_term": "Clinical Diagnostic Code & Procedure #267",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0268": {
        "entity_id": "MED-0268",
        "medical_term": "Clinical Diagnostic Code & Procedure #268",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0269": {
        "entity_id": "MED-0269",
        "medical_term": "Clinical Diagnostic Code & Procedure #269",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0270": {
        "entity_id": "MED-0270",
        "medical_term": "Clinical Diagnostic Code & Procedure #270",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0271": {
        "entity_id": "MED-0271",
        "medical_term": "Clinical Diagnostic Code & Procedure #271",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0272": {
        "entity_id": "MED-0272",
        "medical_term": "Clinical Diagnostic Code & Procedure #272",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0273": {
        "entity_id": "MED-0273",
        "medical_term": "Clinical Diagnostic Code & Procedure #273",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0274": {
        "entity_id": "MED-0274",
        "medical_term": "Clinical Diagnostic Code & Procedure #274",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0275": {
        "entity_id": "MED-0275",
        "medical_term": "Clinical Diagnostic Code & Procedure #275",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0276": {
        "entity_id": "MED-0276",
        "medical_term": "Clinical Diagnostic Code & Procedure #276",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0277": {
        "entity_id": "MED-0277",
        "medical_term": "Clinical Diagnostic Code & Procedure #277",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0278": {
        "entity_id": "MED-0278",
        "medical_term": "Clinical Diagnostic Code & Procedure #278",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0279": {
        "entity_id": "MED-0279",
        "medical_term": "Clinical Diagnostic Code & Procedure #279",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0280": {
        "entity_id": "MED-0280",
        "medical_term": "Clinical Diagnostic Code & Procedure #280",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0281": {
        "entity_id": "MED-0281",
        "medical_term": "Clinical Diagnostic Code & Procedure #281",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0282": {
        "entity_id": "MED-0282",
        "medical_term": "Clinical Diagnostic Code & Procedure #282",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0283": {
        "entity_id": "MED-0283",
        "medical_term": "Clinical Diagnostic Code & Procedure #283",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0284": {
        "entity_id": "MED-0284",
        "medical_term": "Clinical Diagnostic Code & Procedure #284",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0285": {
        "entity_id": "MED-0285",
        "medical_term": "Clinical Diagnostic Code & Procedure #285",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0286": {
        "entity_id": "MED-0286",
        "medical_term": "Clinical Diagnostic Code & Procedure #286",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0287": {
        "entity_id": "MED-0287",
        "medical_term": "Clinical Diagnostic Code & Procedure #287",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0288": {
        "entity_id": "MED-0288",
        "medical_term": "Clinical Diagnostic Code & Procedure #288",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0289": {
        "entity_id": "MED-0289",
        "medical_term": "Clinical Diagnostic Code & Procedure #289",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0290": {
        "entity_id": "MED-0290",
        "medical_term": "Clinical Diagnostic Code & Procedure #290",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0291": {
        "entity_id": "MED-0291",
        "medical_term": "Clinical Diagnostic Code & Procedure #291",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0292": {
        "entity_id": "MED-0292",
        "medical_term": "Clinical Diagnostic Code & Procedure #292",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0293": {
        "entity_id": "MED-0293",
        "medical_term": "Clinical Diagnostic Code & Procedure #293",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0294": {
        "entity_id": "MED-0294",
        "medical_term": "Clinical Diagnostic Code & Procedure #294",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0295": {
        "entity_id": "MED-0295",
        "medical_term": "Clinical Diagnostic Code & Procedure #295",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0296": {
        "entity_id": "MED-0296",
        "medical_term": "Clinical Diagnostic Code & Procedure #296",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0297": {
        "entity_id": "MED-0297",
        "medical_term": "Clinical Diagnostic Code & Procedure #297",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0298": {
        "entity_id": "MED-0298",
        "medical_term": "Clinical Diagnostic Code & Procedure #298",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0299": {
        "entity_id": "MED-0299",
        "medical_term": "Clinical Diagnostic Code & Procedure #299",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0300": {
        "entity_id": "MED-0300",
        "medical_term": "Clinical Diagnostic Code & Procedure #300",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0301": {
        "entity_id": "MED-0301",
        "medical_term": "Clinical Diagnostic Code & Procedure #301",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0302": {
        "entity_id": "MED-0302",
        "medical_term": "Clinical Diagnostic Code & Procedure #302",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0303": {
        "entity_id": "MED-0303",
        "medical_term": "Clinical Diagnostic Code & Procedure #303",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0304": {
        "entity_id": "MED-0304",
        "medical_term": "Clinical Diagnostic Code & Procedure #304",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0305": {
        "entity_id": "MED-0305",
        "medical_term": "Clinical Diagnostic Code & Procedure #305",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0306": {
        "entity_id": "MED-0306",
        "medical_term": "Clinical Diagnostic Code & Procedure #306",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0307": {
        "entity_id": "MED-0307",
        "medical_term": "Clinical Diagnostic Code & Procedure #307",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0308": {
        "entity_id": "MED-0308",
        "medical_term": "Clinical Diagnostic Code & Procedure #308",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0309": {
        "entity_id": "MED-0309",
        "medical_term": "Clinical Diagnostic Code & Procedure #309",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0310": {
        "entity_id": "MED-0310",
        "medical_term": "Clinical Diagnostic Code & Procedure #310",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0311": {
        "entity_id": "MED-0311",
        "medical_term": "Clinical Diagnostic Code & Procedure #311",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0312": {
        "entity_id": "MED-0312",
        "medical_term": "Clinical Diagnostic Code & Procedure #312",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0313": {
        "entity_id": "MED-0313",
        "medical_term": "Clinical Diagnostic Code & Procedure #313",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0314": {
        "entity_id": "MED-0314",
        "medical_term": "Clinical Diagnostic Code & Procedure #314",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0315": {
        "entity_id": "MED-0315",
        "medical_term": "Clinical Diagnostic Code & Procedure #315",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0316": {
        "entity_id": "MED-0316",
        "medical_term": "Clinical Diagnostic Code & Procedure #316",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0317": {
        "entity_id": "MED-0317",
        "medical_term": "Clinical Diagnostic Code & Procedure #317",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0318": {
        "entity_id": "MED-0318",
        "medical_term": "Clinical Diagnostic Code & Procedure #318",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0319": {
        "entity_id": "MED-0319",
        "medical_term": "Clinical Diagnostic Code & Procedure #319",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0320": {
        "entity_id": "MED-0320",
        "medical_term": "Clinical Diagnostic Code & Procedure #320",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0321": {
        "entity_id": "MED-0321",
        "medical_term": "Clinical Diagnostic Code & Procedure #321",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0322": {
        "entity_id": "MED-0322",
        "medical_term": "Clinical Diagnostic Code & Procedure #322",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0323": {
        "entity_id": "MED-0323",
        "medical_term": "Clinical Diagnostic Code & Procedure #323",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0324": {
        "entity_id": "MED-0324",
        "medical_term": "Clinical Diagnostic Code & Procedure #324",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0325": {
        "entity_id": "MED-0325",
        "medical_term": "Clinical Diagnostic Code & Procedure #325",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0326": {
        "entity_id": "MED-0326",
        "medical_term": "Clinical Diagnostic Code & Procedure #326",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0327": {
        "entity_id": "MED-0327",
        "medical_term": "Clinical Diagnostic Code & Procedure #327",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0328": {
        "entity_id": "MED-0328",
        "medical_term": "Clinical Diagnostic Code & Procedure #328",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0329": {
        "entity_id": "MED-0329",
        "medical_term": "Clinical Diagnostic Code & Procedure #329",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0330": {
        "entity_id": "MED-0330",
        "medical_term": "Clinical Diagnostic Code & Procedure #330",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0331": {
        "entity_id": "MED-0331",
        "medical_term": "Clinical Diagnostic Code & Procedure #331",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0332": {
        "entity_id": "MED-0332",
        "medical_term": "Clinical Diagnostic Code & Procedure #332",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0333": {
        "entity_id": "MED-0333",
        "medical_term": "Clinical Diagnostic Code & Procedure #333",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0334": {
        "entity_id": "MED-0334",
        "medical_term": "Clinical Diagnostic Code & Procedure #334",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0335": {
        "entity_id": "MED-0335",
        "medical_term": "Clinical Diagnostic Code & Procedure #335",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0336": {
        "entity_id": "MED-0336",
        "medical_term": "Clinical Diagnostic Code & Procedure #336",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0337": {
        "entity_id": "MED-0337",
        "medical_term": "Clinical Diagnostic Code & Procedure #337",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0338": {
        "entity_id": "MED-0338",
        "medical_term": "Clinical Diagnostic Code & Procedure #338",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0339": {
        "entity_id": "MED-0339",
        "medical_term": "Clinical Diagnostic Code & Procedure #339",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0340": {
        "entity_id": "MED-0340",
        "medical_term": "Clinical Diagnostic Code & Procedure #340",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0341": {
        "entity_id": "MED-0341",
        "medical_term": "Clinical Diagnostic Code & Procedure #341",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0342": {
        "entity_id": "MED-0342",
        "medical_term": "Clinical Diagnostic Code & Procedure #342",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0343": {
        "entity_id": "MED-0343",
        "medical_term": "Clinical Diagnostic Code & Procedure #343",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0344": {
        "entity_id": "MED-0344",
        "medical_term": "Clinical Diagnostic Code & Procedure #344",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0345": {
        "entity_id": "MED-0345",
        "medical_term": "Clinical Diagnostic Code & Procedure #345",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0346": {
        "entity_id": "MED-0346",
        "medical_term": "Clinical Diagnostic Code & Procedure #346",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0347": {
        "entity_id": "MED-0347",
        "medical_term": "Clinical Diagnostic Code & Procedure #347",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0348": {
        "entity_id": "MED-0348",
        "medical_term": "Clinical Diagnostic Code & Procedure #348",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0349": {
        "entity_id": "MED-0349",
        "medical_term": "Clinical Diagnostic Code & Procedure #349",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0350": {
        "entity_id": "MED-0350",
        "medical_term": "Clinical Diagnostic Code & Procedure #350",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0351": {
        "entity_id": "MED-0351",
        "medical_term": "Clinical Diagnostic Code & Procedure #351",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0352": {
        "entity_id": "MED-0352",
        "medical_term": "Clinical Diagnostic Code & Procedure #352",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0353": {
        "entity_id": "MED-0353",
        "medical_term": "Clinical Diagnostic Code & Procedure #353",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0354": {
        "entity_id": "MED-0354",
        "medical_term": "Clinical Diagnostic Code & Procedure #354",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0355": {
        "entity_id": "MED-0355",
        "medical_term": "Clinical Diagnostic Code & Procedure #355",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0356": {
        "entity_id": "MED-0356",
        "medical_term": "Clinical Diagnostic Code & Procedure #356",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0357": {
        "entity_id": "MED-0357",
        "medical_term": "Clinical Diagnostic Code & Procedure #357",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0358": {
        "entity_id": "MED-0358",
        "medical_term": "Clinical Diagnostic Code & Procedure #358",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0359": {
        "entity_id": "MED-0359",
        "medical_term": "Clinical Diagnostic Code & Procedure #359",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0360": {
        "entity_id": "MED-0360",
        "medical_term": "Clinical Diagnostic Code & Procedure #360",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0361": {
        "entity_id": "MED-0361",
        "medical_term": "Clinical Diagnostic Code & Procedure #361",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0362": {
        "entity_id": "MED-0362",
        "medical_term": "Clinical Diagnostic Code & Procedure #362",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0363": {
        "entity_id": "MED-0363",
        "medical_term": "Clinical Diagnostic Code & Procedure #363",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0364": {
        "entity_id": "MED-0364",
        "medical_term": "Clinical Diagnostic Code & Procedure #364",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0365": {
        "entity_id": "MED-0365",
        "medical_term": "Clinical Diagnostic Code & Procedure #365",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0366": {
        "entity_id": "MED-0366",
        "medical_term": "Clinical Diagnostic Code & Procedure #366",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0367": {
        "entity_id": "MED-0367",
        "medical_term": "Clinical Diagnostic Code & Procedure #367",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0368": {
        "entity_id": "MED-0368",
        "medical_term": "Clinical Diagnostic Code & Procedure #368",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0369": {
        "entity_id": "MED-0369",
        "medical_term": "Clinical Diagnostic Code & Procedure #369",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0370": {
        "entity_id": "MED-0370",
        "medical_term": "Clinical Diagnostic Code & Procedure #370",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0371": {
        "entity_id": "MED-0371",
        "medical_term": "Clinical Diagnostic Code & Procedure #371",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0372": {
        "entity_id": "MED-0372",
        "medical_term": "Clinical Diagnostic Code & Procedure #372",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0373": {
        "entity_id": "MED-0373",
        "medical_term": "Clinical Diagnostic Code & Procedure #373",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0374": {
        "entity_id": "MED-0374",
        "medical_term": "Clinical Diagnostic Code & Procedure #374",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0375": {
        "entity_id": "MED-0375",
        "medical_term": "Clinical Diagnostic Code & Procedure #375",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0376": {
        "entity_id": "MED-0376",
        "medical_term": "Clinical Diagnostic Code & Procedure #376",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0377": {
        "entity_id": "MED-0377",
        "medical_term": "Clinical Diagnostic Code & Procedure #377",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0378": {
        "entity_id": "MED-0378",
        "medical_term": "Clinical Diagnostic Code & Procedure #378",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0379": {
        "entity_id": "MED-0379",
        "medical_term": "Clinical Diagnostic Code & Procedure #379",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0380": {
        "entity_id": "MED-0380",
        "medical_term": "Clinical Diagnostic Code & Procedure #380",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0381": {
        "entity_id": "MED-0381",
        "medical_term": "Clinical Diagnostic Code & Procedure #381",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0382": {
        "entity_id": "MED-0382",
        "medical_term": "Clinical Diagnostic Code & Procedure #382",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0383": {
        "entity_id": "MED-0383",
        "medical_term": "Clinical Diagnostic Code & Procedure #383",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0384": {
        "entity_id": "MED-0384",
        "medical_term": "Clinical Diagnostic Code & Procedure #384",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0385": {
        "entity_id": "MED-0385",
        "medical_term": "Clinical Diagnostic Code & Procedure #385",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0386": {
        "entity_id": "MED-0386",
        "medical_term": "Clinical Diagnostic Code & Procedure #386",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0387": {
        "entity_id": "MED-0387",
        "medical_term": "Clinical Diagnostic Code & Procedure #387",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0388": {
        "entity_id": "MED-0388",
        "medical_term": "Clinical Diagnostic Code & Procedure #388",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0389": {
        "entity_id": "MED-0389",
        "medical_term": "Clinical Diagnostic Code & Procedure #389",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0390": {
        "entity_id": "MED-0390",
        "medical_term": "Clinical Diagnostic Code & Procedure #390",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0391": {
        "entity_id": "MED-0391",
        "medical_term": "Clinical Diagnostic Code & Procedure #391",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0392": {
        "entity_id": "MED-0392",
        "medical_term": "Clinical Diagnostic Code & Procedure #392",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0393": {
        "entity_id": "MED-0393",
        "medical_term": "Clinical Diagnostic Code & Procedure #393",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0394": {
        "entity_id": "MED-0394",
        "medical_term": "Clinical Diagnostic Code & Procedure #394",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0395": {
        "entity_id": "MED-0395",
        "medical_term": "Clinical Diagnostic Code & Procedure #395",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0396": {
        "entity_id": "MED-0396",
        "medical_term": "Clinical Diagnostic Code & Procedure #396",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0397": {
        "entity_id": "MED-0397",
        "medical_term": "Clinical Diagnostic Code & Procedure #397",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0398": {
        "entity_id": "MED-0398",
        "medical_term": "Clinical Diagnostic Code & Procedure #398",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0399": {
        "entity_id": "MED-0399",
        "medical_term": "Clinical Diagnostic Code & Procedure #399",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0400": {
        "entity_id": "MED-0400",
        "medical_term": "Clinical Diagnostic Code & Procedure #400",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0401": {
        "entity_id": "MED-0401",
        "medical_term": "Clinical Diagnostic Code & Procedure #401",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0402": {
        "entity_id": "MED-0402",
        "medical_term": "Clinical Diagnostic Code & Procedure #402",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0403": {
        "entity_id": "MED-0403",
        "medical_term": "Clinical Diagnostic Code & Procedure #403",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0404": {
        "entity_id": "MED-0404",
        "medical_term": "Clinical Diagnostic Code & Procedure #404",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0405": {
        "entity_id": "MED-0405",
        "medical_term": "Clinical Diagnostic Code & Procedure #405",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0406": {
        "entity_id": "MED-0406",
        "medical_term": "Clinical Diagnostic Code & Procedure #406",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0407": {
        "entity_id": "MED-0407",
        "medical_term": "Clinical Diagnostic Code & Procedure #407",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0408": {
        "entity_id": "MED-0408",
        "medical_term": "Clinical Diagnostic Code & Procedure #408",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0409": {
        "entity_id": "MED-0409",
        "medical_term": "Clinical Diagnostic Code & Procedure #409",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0410": {
        "entity_id": "MED-0410",
        "medical_term": "Clinical Diagnostic Code & Procedure #410",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0411": {
        "entity_id": "MED-0411",
        "medical_term": "Clinical Diagnostic Code & Procedure #411",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0412": {
        "entity_id": "MED-0412",
        "medical_term": "Clinical Diagnostic Code & Procedure #412",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0413": {
        "entity_id": "MED-0413",
        "medical_term": "Clinical Diagnostic Code & Procedure #413",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0414": {
        "entity_id": "MED-0414",
        "medical_term": "Clinical Diagnostic Code & Procedure #414",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0415": {
        "entity_id": "MED-0415",
        "medical_term": "Clinical Diagnostic Code & Procedure #415",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0416": {
        "entity_id": "MED-0416",
        "medical_term": "Clinical Diagnostic Code & Procedure #416",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0417": {
        "entity_id": "MED-0417",
        "medical_term": "Clinical Diagnostic Code & Procedure #417",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0418": {
        "entity_id": "MED-0418",
        "medical_term": "Clinical Diagnostic Code & Procedure #418",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0419": {
        "entity_id": "MED-0419",
        "medical_term": "Clinical Diagnostic Code & Procedure #419",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0420": {
        "entity_id": "MED-0420",
        "medical_term": "Clinical Diagnostic Code & Procedure #420",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0421": {
        "entity_id": "MED-0421",
        "medical_term": "Clinical Diagnostic Code & Procedure #421",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0422": {
        "entity_id": "MED-0422",
        "medical_term": "Clinical Diagnostic Code & Procedure #422",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0423": {
        "entity_id": "MED-0423",
        "medical_term": "Clinical Diagnostic Code & Procedure #423",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0424": {
        "entity_id": "MED-0424",
        "medical_term": "Clinical Diagnostic Code & Procedure #424",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0425": {
        "entity_id": "MED-0425",
        "medical_term": "Clinical Diagnostic Code & Procedure #425",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0426": {
        "entity_id": "MED-0426",
        "medical_term": "Clinical Diagnostic Code & Procedure #426",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0427": {
        "entity_id": "MED-0427",
        "medical_term": "Clinical Diagnostic Code & Procedure #427",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0428": {
        "entity_id": "MED-0428",
        "medical_term": "Clinical Diagnostic Code & Procedure #428",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0429": {
        "entity_id": "MED-0429",
        "medical_term": "Clinical Diagnostic Code & Procedure #429",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0430": {
        "entity_id": "MED-0430",
        "medical_term": "Clinical Diagnostic Code & Procedure #430",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0431": {
        "entity_id": "MED-0431",
        "medical_term": "Clinical Diagnostic Code & Procedure #431",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0432": {
        "entity_id": "MED-0432",
        "medical_term": "Clinical Diagnostic Code & Procedure #432",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0433": {
        "entity_id": "MED-0433",
        "medical_term": "Clinical Diagnostic Code & Procedure #433",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0434": {
        "entity_id": "MED-0434",
        "medical_term": "Clinical Diagnostic Code & Procedure #434",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0435": {
        "entity_id": "MED-0435",
        "medical_term": "Clinical Diagnostic Code & Procedure #435",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0436": {
        "entity_id": "MED-0436",
        "medical_term": "Clinical Diagnostic Code & Procedure #436",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0437": {
        "entity_id": "MED-0437",
        "medical_term": "Clinical Diagnostic Code & Procedure #437",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0438": {
        "entity_id": "MED-0438",
        "medical_term": "Clinical Diagnostic Code & Procedure #438",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0439": {
        "entity_id": "MED-0439",
        "medical_term": "Clinical Diagnostic Code & Procedure #439",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0440": {
        "entity_id": "MED-0440",
        "medical_term": "Clinical Diagnostic Code & Procedure #440",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0441": {
        "entity_id": "MED-0441",
        "medical_term": "Clinical Diagnostic Code & Procedure #441",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0442": {
        "entity_id": "MED-0442",
        "medical_term": "Clinical Diagnostic Code & Procedure #442",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0443": {
        "entity_id": "MED-0443",
        "medical_term": "Clinical Diagnostic Code & Procedure #443",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0444": {
        "entity_id": "MED-0444",
        "medical_term": "Clinical Diagnostic Code & Procedure #444",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0445": {
        "entity_id": "MED-0445",
        "medical_term": "Clinical Diagnostic Code & Procedure #445",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0446": {
        "entity_id": "MED-0446",
        "medical_term": "Clinical Diagnostic Code & Procedure #446",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0447": {
        "entity_id": "MED-0447",
        "medical_term": "Clinical Diagnostic Code & Procedure #447",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0448": {
        "entity_id": "MED-0448",
        "medical_term": "Clinical Diagnostic Code & Procedure #448",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0449": {
        "entity_id": "MED-0449",
        "medical_term": "Clinical Diagnostic Code & Procedure #449",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0450": {
        "entity_id": "MED-0450",
        "medical_term": "Clinical Diagnostic Code & Procedure #450",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0451": {
        "entity_id": "MED-0451",
        "medical_term": "Clinical Diagnostic Code & Procedure #451",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0452": {
        "entity_id": "MED-0452",
        "medical_term": "Clinical Diagnostic Code & Procedure #452",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0453": {
        "entity_id": "MED-0453",
        "medical_term": "Clinical Diagnostic Code & Procedure #453",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0454": {
        "entity_id": "MED-0454",
        "medical_term": "Clinical Diagnostic Code & Procedure #454",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0455": {
        "entity_id": "MED-0455",
        "medical_term": "Clinical Diagnostic Code & Procedure #455",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0456": {
        "entity_id": "MED-0456",
        "medical_term": "Clinical Diagnostic Code & Procedure #456",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0457": {
        "entity_id": "MED-0457",
        "medical_term": "Clinical Diagnostic Code & Procedure #457",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0458": {
        "entity_id": "MED-0458",
        "medical_term": "Clinical Diagnostic Code & Procedure #458",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0459": {
        "entity_id": "MED-0459",
        "medical_term": "Clinical Diagnostic Code & Procedure #459",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0460": {
        "entity_id": "MED-0460",
        "medical_term": "Clinical Diagnostic Code & Procedure #460",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0461": {
        "entity_id": "MED-0461",
        "medical_term": "Clinical Diagnostic Code & Procedure #461",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0462": {
        "entity_id": "MED-0462",
        "medical_term": "Clinical Diagnostic Code & Procedure #462",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0463": {
        "entity_id": "MED-0463",
        "medical_term": "Clinical Diagnostic Code & Procedure #463",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0464": {
        "entity_id": "MED-0464",
        "medical_term": "Clinical Diagnostic Code & Procedure #464",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0465": {
        "entity_id": "MED-0465",
        "medical_term": "Clinical Diagnostic Code & Procedure #465",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0466": {
        "entity_id": "MED-0466",
        "medical_term": "Clinical Diagnostic Code & Procedure #466",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0467": {
        "entity_id": "MED-0467",
        "medical_term": "Clinical Diagnostic Code & Procedure #467",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0468": {
        "entity_id": "MED-0468",
        "medical_term": "Clinical Diagnostic Code & Procedure #468",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0469": {
        "entity_id": "MED-0469",
        "medical_term": "Clinical Diagnostic Code & Procedure #469",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0470": {
        "entity_id": "MED-0470",
        "medical_term": "Clinical Diagnostic Code & Procedure #470",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0471": {
        "entity_id": "MED-0471",
        "medical_term": "Clinical Diagnostic Code & Procedure #471",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0472": {
        "entity_id": "MED-0472",
        "medical_term": "Clinical Diagnostic Code & Procedure #472",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0473": {
        "entity_id": "MED-0473",
        "medical_term": "Clinical Diagnostic Code & Procedure #473",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0474": {
        "entity_id": "MED-0474",
        "medical_term": "Clinical Diagnostic Code & Procedure #474",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0475": {
        "entity_id": "MED-0475",
        "medical_term": "Clinical Diagnostic Code & Procedure #475",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0476": {
        "entity_id": "MED-0476",
        "medical_term": "Clinical Diagnostic Code & Procedure #476",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0477": {
        "entity_id": "MED-0477",
        "medical_term": "Clinical Diagnostic Code & Procedure #477",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0478": {
        "entity_id": "MED-0478",
        "medical_term": "Clinical Diagnostic Code & Procedure #478",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0479": {
        "entity_id": "MED-0479",
        "medical_term": "Clinical Diagnostic Code & Procedure #479",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0480": {
        "entity_id": "MED-0480",
        "medical_term": "Clinical Diagnostic Code & Procedure #480",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0481": {
        "entity_id": "MED-0481",
        "medical_term": "Clinical Diagnostic Code & Procedure #481",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0482": {
        "entity_id": "MED-0482",
        "medical_term": "Clinical Diagnostic Code & Procedure #482",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0483": {
        "entity_id": "MED-0483",
        "medical_term": "Clinical Diagnostic Code & Procedure #483",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0484": {
        "entity_id": "MED-0484",
        "medical_term": "Clinical Diagnostic Code & Procedure #484",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0485": {
        "entity_id": "MED-0485",
        "medical_term": "Clinical Diagnostic Code & Procedure #485",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0486": {
        "entity_id": "MED-0486",
        "medical_term": "Clinical Diagnostic Code & Procedure #486",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0487": {
        "entity_id": "MED-0487",
        "medical_term": "Clinical Diagnostic Code & Procedure #487",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0488": {
        "entity_id": "MED-0488",
        "medical_term": "Clinical Diagnostic Code & Procedure #488",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0489": {
        "entity_id": "MED-0489",
        "medical_term": "Clinical Diagnostic Code & Procedure #489",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0490": {
        "entity_id": "MED-0490",
        "medical_term": "Clinical Diagnostic Code & Procedure #490",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0491": {
        "entity_id": "MED-0491",
        "medical_term": "Clinical Diagnostic Code & Procedure #491",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0492": {
        "entity_id": "MED-0492",
        "medical_term": "Clinical Diagnostic Code & Procedure #492",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0493": {
        "entity_id": "MED-0493",
        "medical_term": "Clinical Diagnostic Code & Procedure #493",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0494": {
        "entity_id": "MED-0494",
        "medical_term": "Clinical Diagnostic Code & Procedure #494",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0495": {
        "entity_id": "MED-0495",
        "medical_term": "Clinical Diagnostic Code & Procedure #495",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0496": {
        "entity_id": "MED-0496",
        "medical_term": "Clinical Diagnostic Code & Procedure #496",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0497": {
        "entity_id": "MED-0497",
        "medical_term": "Clinical Diagnostic Code & Procedure #497",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0498": {
        "entity_id": "MED-0498",
        "medical_term": "Clinical Diagnostic Code & Procedure #498",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0499": {
        "entity_id": "MED-0499",
        "medical_term": "Clinical Diagnostic Code & Procedure #499",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
    "MED_ENTITY_EXP_0500": {
        "entity_id": "MED-0500",
        "medical_term": "Clinical Diagnostic Code & Procedure #500",
        "taxonomy_class": "ICD-10-CM Clinical Diagnosis" if idx % 2 == 0 else "CPT Surgical / Diagnostic Code",
        "hipaa_phi_type": "Direct Identifier" if idx % 4 == 0 else "Clinical Attribute",
        "privacy_handling": [
            "Mandatory de-identification under HIPAA Safe Harbor Method prior to analytical export.",
            "Ensure minimum necessary disclosure principles are strictly applied to clinical datasets.",
            "Validate patient authorization records and psychotherapy session note restrictions.",
            "Inspect audit trails for unauthorized electronic medical record (EMR) lookups."
        ]
    },
}
