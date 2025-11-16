import logging
logging.basicConfig(level=logging.INFO)

from core.tools import estimate_time

from google.generativeai import GenerativeModel

model = GenerativeModel("gemini-1.5-flash")


class StudyPlannerAgent:
    def create_plan(self, topics, hours):
        time_per_topic = estimate_time(hours, len(topics))
        plan = []
        # Gemini-generated plan description (bonus feature)
        gemini_summary = model.generate_content(
            f"Create a short motivational study overview for: {topics}").text


        for t in topics:
            plan.append({
                "topic": t,
                "allocated_time": f"{time_per_topic:.1f} hours"
            })

        return {
            "agent": "Study Planner",
            "message": "Here is your study plan:",
            "plan": plan,
            "gemini_summary": gemini_summary
        }
