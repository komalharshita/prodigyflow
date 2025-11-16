from typing import Any, Dict, Optional
import time


try:
from memory.memory_bank import MemoryBank
except Exception:
# Fallback simple MemoryBank for standalone demos
class MemoryBank:
def __init__(self):
self.store = {}
def get(self, user_id, key):
return self.store.get(f"{user_id}:{key}")
def set(self, user_id, key, value):
self.store[f"{user_id}:{key}"] = value
def append_mastery(self, user_id, topic, score):
k = f"{user_id}:mastery"
self.store.setdefault(k, {})
self.store[k][topic] = score




class OrchestratorAgent:
def __init__(self, planner, researcher, tutor, evaluator, memory: Optional[MemoryBank] = None):
self.planner = planner
self.researcher = researcher
self.tutor = tutor
self.evaluator = evaluator
self.memory = memory or MemoryBank()


def handle_request(self, user_id: str, intent: str, payload: Dict[str, Any]):
"""Main entrypoint. Routes intents to agents and returns aggregated result."""
start = time.time()
if intent == "create_plan":
syllabus = payload.get("syllabus", {})
prefs = payload.get("preferences", {})
plan = self.planner.create_weekly_plan(user_id, syllabus, prefs)
self.memory.set(user_id, "last_plan", plan)
return {"status": "ok", "plan": plan}


if intent == "fetch_resources":
topic = payload.get("topic")
if not topic:
return {"status": "error", "error": "missing topic"}
resources = self.researcher.fetch_resources(topic)
return {"status": "ok", "resources": resources}


if intent == "summarize":
resource = payload.get("resource")
summary = self.tutor.summarize(resource)
return {"status": "ok", "summary": summary}


if intent == "quiz":
quiz_results = payload.get("quiz_results", {})
score_summary = self.evaluator.evaluate_quiz(user_id, quiz_results)
return {"status": "ok", "evaluation": score_summary}


return {"status": "error", "error": f"unknown intent {intent}"}

