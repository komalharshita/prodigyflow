# evaluator_agent.py
class EvaluatorAgent:
    def __init__(self, memory):
        self.memory = memory

    def evaluate_quiz(self, user_id, quiz_results):
        # quiz_results: dict topic->score
        for topic, score in quiz_results.items():
            self.memory.append_mastery(user_id, topic, score)
        # compute overall mastery delta or average
        k = f"{user_id}:mastery"
        mastery = self.memory.store.get(k, {})
        avg = sum(mastery.values())/len(mastery) if mastery else 0
        return {"overall_mastery": avg, "per_topic": mastery}
