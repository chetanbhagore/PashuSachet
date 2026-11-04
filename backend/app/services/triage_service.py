import os
import json
from typing import Dict, Any, List, Optional
from pydantic import BaseModel

class TriageInput(BaseModel):
    species: str # 'cattle', 'buffalo', 'goat', 'sheep', 'poultry'
    breed: Optional[str] = "Indigenous"
    age_months: Optional[int] = 36
    rectal_temp_f: Optional[float] = None
    symptoms: List[str] # e.g. ["nodules", "high_fever", "off_feed"]
    duration_days: int = 1
    red_flags: Dict[str, bool] = {} # e.g. {"severe_bloat": False}

class ConditionAssessment(BaseModel):
    condition_id: str
    name_en: str
    name_mr: str
    likelihood_band: str # 'Likely', 'Possible', 'Less Likely'
    notifiable: bool
    urgency: str

class TriageOutput(BaseModel):
    rules_version: str
    red_flag_triggered: bool
    emergency_message: Optional[str] = None
    urgency: str
    primary_condition: Optional[ConditionAssessment] = None
    differential_conditions: List[ConditionAssessment] = []
    safe_first_aid: List[str] = []
    suggested_action: str

class TriageEngine:
    def __init__(self, rules_path: Optional[str] = None):
        if not rules_path:
            # Resolve relative to backend/app/services/../../shared/rules/triage_rules_v1.json
            base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            rules_path = os.path.join(os.path.dirname(base_dir), "shared", "rules", "triage_rules_v1.json")
            if not os.path.exists(rules_path):
                # Fallback to local check
                rules_path = os.path.join(base_dir, "shared", "rules", "triage_rules_v1.json")
        
        self.rules_path = rules_path
        self._load_rules()

    def _load_rules(self):
        if os.path.exists(self.rules_path):
            with open(self.rules_path, "r", encoding="utf-8") as f:
                self.rules_data = json.load(f)
        else:
            self.rules_data = {
                "version": "1.0.0",
                "red_flag_triggers": [],
                "species_rules": {}
            }

    def evaluate(self, payload: TriageInput) -> TriageOutput:
        rules_ver = self.rules_data.get("version", "v1.0.0")

        # 1. Check Red Flags (Hardcoded Circuit Breaker)
        for rf_id, is_active in payload.red_flags.items():
            if is_active:
                for rf in self.rules_data.get("red_flag_triggers", []):
                    if rf.get("id") == rf_id:
                        return TriageOutput(
                            rules_version=rules_ver,
                            red_flag_triggered=True,
                            emergency_message=rf.get("message"),
                            urgency="CRITICAL",
                            primary_condition=None,
                            differential_conditions=[],
                            safe_first_aid=[
                                "EMERGENCY: Do not delay for online processing.",
                                "Keep the animal in a safe resting position; do not force movement.",
                                "Call 1962 toll-free government veterinary ambulance immediately."
                            ],
                            suggested_action="EMERGENCY_OVERRIDE_1962"
                        )

        species_key = payload.species.lower()
        species_rules = self.rules_data.get("species_rules", {}).get(species_key, [])
        input_symptoms = set(s.lower() for s in payload.symptoms)

        likely_matches = []
        possible_matches = []
        less_likely_matches = []

        for rule in species_rules:
            cardinal = set(rule.get("cardinal_symptoms", []))
            supporting = set(rule.get("supporting_symptoms", []))
            min_fever = rule.get("min_fever_f", 102.5)
            cardinal_min = rule.get("cardinal_match_min", 1)
            supporting_min = rule.get("supporting_match_min", 1)

            card_matches = len(input_symptoms & cardinal)
            supp_matches = len(input_symptoms & supporting)
            fever_met = (payload.rectal_temp_f is not None and payload.rectal_temp_f >= min_fever) or ("high_fever" in input_symptoms)

            cond = ConditionAssessment(
                condition_id=rule.get("condition_id"),
                name_en=rule.get("name_en"),
                name_mr=rule.get("name_mr"),
                likelihood_band="Less Likely",
                notifiable=rule.get("notifiable", False),
                urgency=rule.get("default_urgency", "MODERATE")
            )

            if card_matches >= cardinal_min and (fever_met or supp_matches >= supporting_min):
                cond.likelihood_band = "Likely"
                likely_matches.append((cond, rule, card_matches * 2 + supp_matches))
            elif card_matches >= 1 or supp_matches >= supporting_min:
                cond.likelihood_band = "Possible"
                possible_matches.append((cond, rule, card_matches + supp_matches))
            else:
                less_likely_matches.append((cond, rule, 0))

        # Determine primary condition
        primary = None
        first_aid = []
        action = "BOOK_LOCAL_DISPENSARY"
        urgency = "MODERATE"

        if likely_matches:
            likely_matches.sort(key=lambda x: x[2], reverse=True)
            primary = likely_matches[0][0]
            first_aid = likely_matches[0][1].get("safe_first_aid", [])
            action = likely_matches[0][1].get("suggested_action", "BOOK_LOCAL_DISPENSARY")
            urgency = primary.urgency
            differentials = [m[0] for m in likely_matches[1:]] + [m[0] for m in possible_matches]
        elif possible_matches:
            possible_matches.sort(key=lambda x: x[2], reverse=True)
            primary = possible_matches[0][0]
            first_aid = possible_matches[0][1].get("safe_first_aid", [])
            action = possible_matches[0][1].get("suggested_action", "BOOK_LOCAL_DISPENSARY")
            urgency = primary.urgency
            differentials = [m[0] for m in possible_matches[1:]]
        else:
            # Fallback routine/general check
            first_aid = [
                "Keep animal in clean dry shelter with access to fresh drinking water.",
                "Monitor feed intake and body temperature twice daily.",
                "If animal goes completely off feed or shows new symptoms, consult dispensary."
            ]
            action = "MONITOR_OR_BOOK"
            urgency = "ROUTINE"
            differentials = [m[0] for m in less_likely_matches[:2]]

        return TriageOutput(
            rules_version=rules_ver,
            red_flag_triggered=False,
            urgency=urgency,
            primary_condition=primary,
            differential_conditions=differentials[:3],
            safe_first_aid=first_aid,
            suggested_action=action
        )

# Global engine singleton
triage_engine = TriageEngine()

