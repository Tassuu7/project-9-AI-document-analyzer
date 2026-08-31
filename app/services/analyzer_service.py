"""Analyzer Service."""
import json
import time
import uuid
from typing import Dict, Any
from app.core.database import db
from app.services.document_service import DocumentService
from app.nlp.classification.doc_classifier import DocumentClassifier
from app.nlp.ner.entity_extractor import EntityExtractor
from app.nlp.summarizers.extractive_summarizer import ExtractiveSummarizer
from app.nlp.summarizers.executive_summarizer import ExecutiveSummarizer
from app.nlp.sentiment.sentiment_analyzer import SentimentAnalyzer
from app.nlp.readability.readability_metrics import ReadabilityMetrics
from app.nlp.compliance.compliance_engine import ComplianceEngine
from app.nlp.risk.risk_scorer import RiskScorer

class AnalyzerService:
    @classmethod
    def run_full_pipeline(cls, text: str, document_id: str = "") -> Dict[str, Any]:
        classification = DocumentClassifier.classify(text)
        entities = EntityExtractor.extract_entities(text)
        summary = ExtractiveSummarizer.summarize(text, max_sentences=5)
        exec_brief = ExecutiveSummarizer.generate_brief(text)
        sentiment = SentimentAnalyzer.analyze(text)
        readability = ReadabilityMetrics.analyze(text)
        compliance = ComplianceEngine.audit_document(text)
        risk = RiskScorer.evaluate_risk(text)

        report = {
            "classification": classification,
            "summary": {
                "extractive": summary["summary"],
                "compression_ratio": summary["compression_ratio"],
                "key_obligations": exec_brief["key_obligations"],
                "critical_risks": exec_brief["critical_risks"]
            },
            "entities": entities,
            "sentiment": sentiment,
            "readability": readability,
            "compliance": compliance,
            "risk": risk
        }

        if document_id:
            aid = str(uuid.uuid4())
            db.execute_non_query(
                """INSERT OR REPLACE INTO analyses 
                   (id, document_id, classification, classification_confidence, summary, risk_score, sentiment_polarity, sentiment_subjectivity, tone, readability_score, readability_grade, entities_json, compliance_json, risks_json, metrics_json, created_at)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (aid, document_id, classification["category"], classification["confidence"], summary["summary"], risk["overall_risk_score"], sentiment["polarity"], 0.0, sentiment["tone"], readability["flesch_reading_ease"], readability["reading_level"], json.dumps(entities), json.dumps(compliance), json.dumps(risk), json.dumps({}), time.time())
            )
            report["id"] = aid
        return report

    @classmethod
    def analyze_document_by_id(cls, document_id: str) -> Dict[str, Any]:
        text = DocumentService.get_document_text(document_id)
        return cls.run_full_pipeline(text, document_id=document_id)
