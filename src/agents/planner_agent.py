# planner_agent.py
from datetime import datetime, timedelta

class PlannerAgent:
    def __init__(self, memory: "MemoryBank", calendar_tool=None):
        self.memory = memory
        self.calendar = calendar_tool

    def create_weekly_plan(self, user_id, syllabus: dict, preferences: dict):
        # syllabus: {"Course": [{"topic":"Arrays", "weight":3}, ...]}
        # preferences: {"daily_hours": 2, "study_days": ["Mon","Tue",...]}
        # simplified greedy planner
        daily_hours = preferences.get("daily_hours", 2)
        topics = []
        for course, tlist in syllabus.items():
            for t in tlist:
                topics.append({"course": course, "topic": t["topic"], "weight": t.get("weight",1)})
        # sort by weight desc
        topics.sort(key=lambda x: -x["weight"])
        plan = {}
        day = 0
        for item in topics:
            d = (day % 7)
            day_name = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"][d]
            plan.setdefault(day_name, []).append(item)
            day += 1
        # attach estimated durations
        for day_name, items in plan.items():
            for it in items:
                it["duration_hours"] = round(daily_hours / max(1, len(items)), 2)
        # persist plan
        self.memory.set(user_id, "last_plan", plan)
        return plan
