"""Analysis Result Model."""
from dataclasses import dataclass, field
from typing import List, Dict, Any
import time
import uuid

@dataclass
class AnalysisResult:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    document_id: str = ""
    classification: str = "Unknown"
    classification_confidence: float = 0.0
    summary: str = ""
    risk_score: float = 0.0
    sentiment_polarity: float = 0.0
    sentiment_subjectivity: float = 0.0
    tone: str = "Neutral"
    readability_score: float = 0.0
    readability_grade: str = "N/A"
    entities: List[Dict[str, Any]] = field(default_factory=list)
    compliance_violations: List[Dict[str, Any]] = field(default_factory=list)
    risk_factors: List[Dict[str, Any]] = field(default_factory=list)
    metrics: Dict[str, Any] = field(default_factory=dict)
    created_at: float = field(default_factory=time.time)
