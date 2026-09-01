"""Central Inspection & Intelligence Coordinator."""
import json
import time
import uuid
from typing import Dict, Any, List
from app.core.database import db
from app.services.document_service import DocumentService
from app.services.notification_service import NotificationService
from app.nlp.classification.doc_classifier import DocumentClassifier
from app.nlp.ner.entity_extractor import EntityExtractor
from app.nlp.summarizers.extractive_summarizer import ExtractiveSummarizer
from app.nlp.summarizers.executive_summarizer import ExecutiveSummarizer
from app.nlp.sentiment.sentiment_analyzer import SentimentAnalyzer
from app.nlp.readability.readability_metrics import ReadabilityMetrics
from app.nlp.compliance.compliance_engine import ComplianceEngine

# Specialized Inspection Engines
from app.inspection.text_error_detector import TextErrorDetector
from app.inspection.data_quality_engine import DataQualityEngine
from app.inspection.calculation_validator import CalculationValidator
from app.inspection.consistency_engine import ConsistencyEngine
from app.inspection.risk_analyzer import RiskAnalyzer
from app.inspection.pii_inspector import PIIInspector
from app.inspection.health_scorer import HealthScorer

# Linguistic, Writing Quality, and Paraphrasing Engines
from app.inspection.passive_voice_detector import PassiveVoiceDetector
from app.inspection.complexity_detector import ComplexityDetector
from app.inspection.filler_detector import FillerDetector
from app.inspection.structure_analyzer import StructureAnalyzer
from app.inspection.duplicate_sentence_detector import DuplicateSentenceDetector
from app.inspection.writing_quality_scorer import WritingQualityScorer
from app.inspection.paraphrase_engine import ParaphraseEngine

class AnalyzerService:
    @classmethod
    def inspect_document(cls, text: str, document_id: str = "", user_id: str = "user_default", headers: List[str] = None, rows: List[List[Any]] = None) -> Dict[str, Any]:
        now = time.time()

        # 1. Base NLP Classifiers & Summaries
        classification = DocumentClassifier.classify(text)
        entities = EntityExtractor.extract_entities(text)
        summary = ExtractiveSummarizer.summarize(text, max_sentences=5)
        exec_brief = ExecutiveSummarizer.generate_brief(text)
        sentiment = SentimentAnalyzer.analyze(text)
        readability = ReadabilityMetrics.analyze(text)
        compliance = ComplianceEngine.audit_document(text)

        # 2. Advanced Error & Risk Detection Engines
        text_errors = TextErrorDetector.detect_errors(text)
        data_quality_res = DataQualityEngine.analyze_table_data(headers or [], rows or [])
        calc_errors = CalculationValidator.validate_calculations(text)
        consistency_errors = ConsistencyEngine.check_consistency(text)
        risk_res = RiskAnalyzer.evaluate_risks(text)
        pii_res = PIIInspector.inspect_pii(text)

        # 3. Linguistic & Style Inspection
        passive_findings = PassiveVoiceDetector.detect_passive_voice(text)
        complexity_findings = ComplexityDetector.detect_complex_sentences(text)
        filler_findings = FillerDetector.detect_fillers(text)
        structure_res = StructureAnalyzer.analyze_structure(text)
        duplicate_findings = DuplicateSentenceDetector.detect_duplicate_sentences(text)
        writing_quality = WritingQualityScorer.score_writing_quality(text)
        paraphrase_preview = ParaphraseEngine.paraphrase_text(text, mode="professional")

        # 4. Aggregate all structured issues
        all_issues = []
        all_issues.extend(text_errors)
        all_issues.extend(data_quality_res.get("issues", []))
        all_issues.extend(calc_errors)
        all_issues.extend(consistency_errors)
        all_issues.extend(risk_res.get("findings", []))
        all_issues.extend(pii_res.get("findings", []))
        all_issues.extend(passive_findings)
        all_issues.extend(complexity_findings)
        all_issues.extend(filler_findings)
        all_issues.extend(duplicate_findings)

        # Add Compliance Violations as Issues
        for v in compliance.get("violations_found", []):
            all_issues.append({
                "category": "COMPLIANCE",
                "severity": v.get("severity", "HIGH"),
                "title": f"[{v.get('standard')}] {v.get('rule')}",
                "location": "Policy Clause",
                "value": v.get("clause", ""),
                "expected_value": f"Compliant under {v.get('standard')}",
                "evidence": f"Violation of {v.get('standard')}: '{v.get('clause')}'",
                "explanation": f"Non-compliance detected against statutory standard {v.get('standard')}.",
                "impact": f"Risk of regulatory penalties, audit failure, and fines.",
                "recommendation": v.get("remediation", "Review and adjust terms to satisfy statutory requirement."),
                "confidence": 0.96,
                "suggested_correction": ""
            })

        # 5. Calculate Overall Health Score
        health = HealthScorer.calculate_health_score(
            text_errors=text_errors,
            data_quality_res=data_quality_res,
            consistency_errors=consistency_errors,
            calc_errors=calc_errors,
            risk_res=risk_res,
            compliance_res=compliance,
            word_count=len(text.split())
        )

        # Generate Auto-Corrected Document Text
        corrected_text = cls._generate_corrected_text(text, text_errors + filler_findings)

        report = {
            "document_id": document_id,
            "classification": classification,
            "health": health,
            "writing_quality": writing_quality,
            "structure": structure_res,
            "data_quality": data_quality_res,
            "summary": {
                "extractive": summary["summary"],
                "compression_ratio": summary["compression_ratio"],
                "key_obligations": exec_brief["key_obligations"],
                "critical_risks": exec_brief["critical_risks"],
                "keywords": [w for w in set(text.split()) if len(w) > 5][:10]
            },
            "sentiment": sentiment,
            "readability": readability,
            "risk": risk_res,
            "pii": pii_res,
            "compliance": compliance,
            "entities": entities,
            "issues": all_issues,
            "corrected_text": corrected_text,
            "paraphrased_text": paraphrase_preview.get("paraphrased_text", ""),
            "created_at": now
        }

        # 6. Persist to Database if document_id is present
        if document_id:
            aid = str(uuid.uuid4())
            try:
                db.execute_non_query(
                    """INSERT OR REPLACE INTO analyses 
                       (id, document_id, version_num, classification, classification_confidence, health_score, text_quality_score, data_quality_score, consistency_score, risk_score, compliance_score, summary, metrics_json, created_at)
                       VALUES (?, ?, 1, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                    (aid, document_id, classification["category"], classification["confidence"], health["overall_health_score"], health["text_quality_score"], health["data_quality_score"], health["consistency_score"], risk_res["overall_risk_score"], health["compliance_score"], summary["summary"], json.dumps(report), now)
                )

                db.execute_non_query(
                    "UPDATE documents SET health_score = ?, risk_level = ?, status = 'COMPLETED' WHERE id = ?",
                    (health["overall_health_score"], risk_res["risk_level"], document_id)
                )

                db.execute_non_query("DELETE FROM issues WHERE document_id = ?", (document_id,))
                for iss in all_issues:
                    iss_id = str(uuid.uuid4())
                    db.execute_non_query(
                        """INSERT INTO issues 
                           (id, document_id, analysis_id, category, severity, title, location, value, expected_value, evidence, explanation, impact, recommendation, confidence, status, suggested_correction, created_at, updated_at)
                           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'OPEN', ?, ?, ?)""",
                        (iss_id, document_id, aid, iss.get("category", "GENERAL"), iss.get("severity", "LOW"), iss.get("title", "Issue"), iss.get("location", ""), str(iss.get("value", "")), str(iss.get("expected_value", "")), str(iss.get("evidence", "")), str(iss.get("explanation", "")), str(iss.get("impact", "")), str(iss.get("recommendation", "")), iss.get("confidence", 0.9), str(iss.get("suggested_correction", "")), now, now)
                    )
            except Exception:
                pass

            report["id"] = aid

        return report

    @classmethod
    def _generate_corrected_text(cls, original_text: str, fixable_issues: List[Dict[str, Any]]) -> str:
        corrected = original_text
        for iss in fixable_issues:
            target = iss.get("value", "")
            repl = iss.get("suggested_correction", "")
            if target and repl and target in corrected:
                corrected = corrected.replace(target, repl, 1)
        return corrected

    @classmethod
    def inspect_document_by_id(cls, document_id: str, user_id: str = "user_default") -> Dict[str, Any]:
        text = DocumentService.get_document_text(document_id)
        doc = DocumentService.get_document(document_id)
        headers, rows = None, None
        if doc and doc.get("file_type") in ["csv", "xlsx"]:
            from app.parsers.csv_parser import CSVParser
            res = CSVParser.parse(text)
            headers = res.get("headers")
            rows = res.get("rows")
            
        return cls.inspect_document(text, document_id=document_id, user_id=user_id, headers=headers, rows=rows)

AnalyzerService.run_full_pipeline = AnalyzerService.inspect_document
AnalyzerService.analyze_document_by_id = AnalyzerService.inspect_document_by_id
