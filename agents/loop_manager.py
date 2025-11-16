from typing import Dict, Any


class LoopManager:
def __init__(self, orchestrator: OrchestratorAgent, memory=None):
self.orch = orchestrator
self.memory = memory or orchestrator.memory


def run_feedback_cycle(self, user_id: str, topic: str, simulate_score_after_study: int = 85) -> Dict[str, Any]:
# 1) fetch resources
res = self.orch.handle_request(user_id, "fetch_resources", {"topic": topic})
resources = res.get("resources", [])


# 2) summarize first resource
if resources:
summary = self.orch.handle_request(user_id, "summarize", {"resource": resources[0]})
else:
summary = {"summary": "No resources found"}


# 3) simulate quiz and evaluation
quiz_results = {topic: simulate_score_after_study}
eval_res = self.orch.handle_request(user_id, "quiz", {"quiz_results": quiz_results})


return {
"resources": resources,
"summary": summary.get("summary") if isinstance(summary, dict) else summary,
"evaluation": eval_res.get("evaluation") if isinstance(eval_res, dict) else eval_res
}
