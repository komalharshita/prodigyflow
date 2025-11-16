from typing import Dict


class MasteryCheckerAgent:
def __init__(self, memory=None):
self.memory = memory


def evaluate_quiz(self, user_id: str, quiz_results: Dict[str, float]) -> Dict:
# quiz_results: {topic: score (0-100)}
# Update memory with scores
for topic, score in quiz_results.items():
if self.memory:
self.memory.append_mastery(user_id, topic, score)


# Compute overall mastery
k = f"{user_id}:mastery"
mastery = (self.memory.store.get(k, {}) if self.memory else {})
overall = sum(mastery.values()) / len(mastery) if mastery else 0
return {"overall_mastery": overall, "per_topic": mastery}
