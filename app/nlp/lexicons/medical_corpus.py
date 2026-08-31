"""
Healthcare, Clinical Informatics and HIPAA PHI Corpus
Detailed clinical taxonomy for medical record classification and automated entity redaction.
"""

from typing import Dict, Any

CLINICAL_TERMS_CATALOG: Dict[str, Dict[str, Any]] = {
    f"MED_TERM_{idx}": {
        "term": term,
        "domain": domain,
        "phi_sensitivity": "HIGH" if domain in ["Identifiers", "Encounter Details", "Psychiatry"] else "MODERATE"
    }
    for idx, (term, domain) in enumerate([
        ("Medical Record Number (MRN)", "Identifiers"), ("Health Plan Beneficiary ID", "Identifiers"),
        ("Patient Full Legal Name", "Identifiers"), ("Date of Birth / Age", "Identifiers"),
        ("Social Security Number", "Identifiers"), ("Home Residential Address", "Identifiers"),
        ("Electronic Mail Address", "Identifiers"), ("Telephone / Fax Number", "Identifiers"),
        ("Biometric Identifiers", "Identifiers"), ("Full Face Photographic Images", "Identifiers"),
        ("Chief Complaint", "Clinical Evaluation"), ("History of Present Illness (HPI)", "Clinical Evaluation"),
        ("Past Medical History (PMH)", "Clinical Evaluation"), ("Family Medical History", "Clinical Evaluation"),
        ("Social History and Habits", "Clinical Evaluation"), ("Review of Systems (ROS)", "Clinical Evaluation"),
        ("Physical Examination Findings", "Clinical Evaluation"), ("Vital Signs (BP, HR, RR, Temp, SpO2)", "Clinical Evaluation"),
        ("Complete Blood Count (CBC)", "Diagnostic Lab"), ("Comprehensive Metabolic Panel (CMP)", "Diagnostic Lab"),
        ("Lipid Profile and Panel", "Diagnostic Lab"), ("Hemoglobin A1c", "Diagnostic Lab"),
        ("Prothrombin Time / INR", "Diagnostic Lab"), ("Urinalysis and Culture", "Diagnostic Lab"),
        ("Electrocardiogram (ECG/EKG)", "Diagnostic Imaging"), ("Chest Radiograph (X-Ray)", "Diagnostic Imaging"),
        ("Computed Tomography (CT Scan)", "Diagnostic Imaging"), ("Magnetic Resonance Imaging (MRI)", "Diagnostic Imaging"),
        ("Echocardiography (TTE/TEE)", "Diagnostic Imaging"), ("Ultrasound Sonography", "Diagnostic Imaging"),
        ("Pathology Biopsy Report", "Diagnostic Pathology"), ("Histopathology Examination", "Diagnostic Pathology"),
        ("Cytology Smear Examination", "Diagnostic Pathology"), ("Inpatient Admission Note", "Encounter Details"),
        ("Progress Note and SOAP", "Encounter Details"), ("Operative Procedure Report", "Encounter Details"),
        ("Anesthesia Administration Record", "Encounter Details"), ("Discharge Summary and Instructions", "Encounter Details"),
        ("Emergency Department Triage Note", "Encounter Details"), ("Outpatient Consultation Note", "Encounter Details"),
        ("Cardiovascular Pharmacology", "Therapeutics"), ("Antibiotic Regimen", "Therapeutics"),
        ("Anticoagulant Therapy", "Therapeutics"), ("Chemotherapy Protocol", "Therapeutics"),
        ("Analgesic Pain Management", "Therapeutics"), ("Immunosuppressive Regimen", "Therapeutics"),
        ("Endocrine Insulin Regimen", "Therapeutics"), ("Psychotropic Medication", "Therapeutics"),
        ("Psychotherapy Session Notes", "Psychiatry"), ("Informed Surgical Consent", "Legal Medical")
    ], 1)
}
