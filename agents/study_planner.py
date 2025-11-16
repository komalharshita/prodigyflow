from core.tools import estimate_time

class StudyPlannerAgent:
    def create_plan(self, topics, hours):
        time_per_topic = estimate_time(hours, len(topics))
        plan = []

        for t in topics:
            plan.append({
                "topic": t,
                "allocated_time": f"{time_per_topic:.1f} hours"
            })

        return {
            "agent": "Study Planner",
            "message": "Here is your study plan:",
            "plan": plan
        }
