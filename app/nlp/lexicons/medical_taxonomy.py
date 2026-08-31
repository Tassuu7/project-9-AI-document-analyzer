"""
Healthcare and Medical Terminology Taxonomy
Identifiers for Protected Health Information (PHI), clinical classifications, and diagnostic terminology.
"""

from typing import Dict, List

MEDICAL_TAXONOMY: Dict[str, List[str]] = {
    "PHI Identifiers": [
        "patient name", "medical record number", "mrn", "health plan beneficiary number",
        "account number", "certificate/license number", "vehicle identifiers",
        "device identifiers and serial numbers", "biometric identifiers", "full face photos",
        "date of birth", "admission date", "discharge date", "date of death"
    ],
    "Clinical Encounters": [
        "inpatient admission", "outpatient consultation", "emergency department", "icu",
        "triage", "history of present illness", "physical examination", "chief complaint",
        "review of systems", "discharge summary", "operative report"
    ],
    "Diagnostic & Lab Findings": [
        "complete blood count", "cbc", "basic metabolic panel", "bmp", "hemoglobin a1c",
        "electrocardiogram", "ecg", "ekg", "magnetic resonance imaging", "mri",
        "computed tomography", "ct scan", "ultrasound", "biopsy pathology"
    ],
    "Pharmacological Categories": [
        "antibiotics", "antihypertensives", "analgesics", "anticoagulants", "corticosteroids",
        "insulin therapy", "chemotherapy", "immunosuppressants", "dosage", "contraindications"
    ]
}
