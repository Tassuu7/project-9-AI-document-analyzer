"""Sentiment Lexicon."""
from typing import Dict

POSITIVE_POLARITY_LEXICON: Dict[str, float] = {
    "excellent": 0.95, "exceptional": 0.92, "outstanding": 0.90, "superior": 0.88, "perfect": 0.95,
    "favorable": 0.75, "benefit": 0.65, "beneficial": 0.70, "advantage": 0.68, "profit": 0.70,
    "profitable": 0.75, "success": 0.85, "successful": 0.82, "compliant": 0.80, "approved": 0.85,
    "certified": 0.82, "innovative": 0.78, "efficiency": 0.72, "efficient": 0.70, "robust": 0.75,
    "secure": 0.85, "safe": 0.70, "integrity": 0.85, "valuable": 0.72, "effective": 0.70
}

NEGATIVE_POLARITY_LEXICON: Dict[str, float] = {
    "breach": -0.90, "default": -0.85, "violation": -0.88, "terminate": -0.75, "termination": -0.78,
    "damages": -0.70, "liability": -0.65, "penalties": -0.80, "fraud": -0.95, "fraudulent": -0.95,
    "negligence": -0.88, "infringement": -0.85, "litigation": -0.75, "dispute": -0.65, "insolvency": -0.90,
    "bankruptcy": -0.92, "fail": -0.75, "failure": -0.78, "defect": -0.75, "vulnerability": -0.75,
    "threat": -0.80, "hazard": -0.75, "risk": -0.60, "severe": -0.70, "adverse": -0.75
}

URGENCY_LEXICON: Dict[str, float] = {
    "immediately": 0.95, "promptly": 0.85, "forthwith": 0.90, "urgently": 0.95, "urgent": 0.90,
    "critical": 0.92, "emergency": 0.98, "deadline": 0.80, "mandatory": 0.85, "imperative": 0.88
}

HEDGING_LEXICON: Dict[str, float] = {
    "may": 0.60, "might": 0.70, "could": 0.65, "possibly": 0.80, "perhaps": 0.75,
    "allegedly": 0.85, "uncertain": 0.75, "conditional": 0.60
}

LEGAL_ASSERTIVENESS_LEXICON: Dict[str, float] = {
    "shall": 0.90, "must": 0.95, "covenants": 0.85, "warrants": 0.88, "guarantees": 0.90,
    "irrevocable": 0.92, "unconditional": 0.95, "indemnify": 0.85, "hold harmless": 0.90, "strictly": 0.88
}
