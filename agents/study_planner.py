from datetime import datetime, timedelta
from typing import Dict, List


class StudyPlannerAgent:
def __init__(self, memory=None):
self.memory = memory


def create_weekly_plan(self, user_id: str, syllabus: Dict[str, List[Dict]], preferences: Dict):
"""Return a dict with days of week mapped to topic lists.
syllabus example: {"CS101": [{"topic":"Arrays", "weight":3}, ...]}
preferences example: {"daily_hours": 2, "study_days": ["Mon","Tue",...]}
"""
study_days = preferences.get("study_days", ["Mon","Tue","Wed","Thu","Fri"])[:7]
daily_hours = preferences.get("daily_hours", 2)


# Flatten topics
topics = []
for course, items in syllabus.items():
for itm in items:
topics.append({
"course": course,
"topic": itm.get("topic"),
"weight": itm.get("weight", 1)
})


# Sort by weight descending (more important topics first)
topics.sort(key=lambda x: -x["weight"]) if topics else None


plan = {day: [] for day in study_days}
idx = 0
for t in topics:
day = study_days[idx % len(study_days)]
plan[day].append(t)
idx += 1


# Assign estimated durations (simple heuristic)
for day in plan:
items = plan[day]
n = max(1, len(items))
for it in items:
it["duration_hours"] = round(daily_hours / n, 2)


if self.memory:
self.memory.set(user_id, "last_plan", plan)
return plan
