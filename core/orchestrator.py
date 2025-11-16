from agents.study_planner import StudyPlannerAgent
from agents.research_assistant import ResearchAssistantAgent
from agents.doubt_solver import DoubtSolverAgent
from memory.session_memory import SessionMemory

class Orchestrator:
    def __init__(self):
        self.memory = SessionMemory()
        self.study_planner = StudyPlannerAgent()
        self.researcher = ResearchAssistantAgent()
        self.doubt_solver = DoubtSolverAgent()

    def route(self, user_input):
        self.memory.add_history("user", user_input)

        if "plan" in user_input.lower() or "study" in user_input.lower():
            return self._handle_study(user_input)

        elif "explain" in user_input.lower() or "notes" in user_input.lower():
            return self._handle_research(user_input)

        else:
            return self._handle_doubt(user_input)

    def _handle_study(self, text):
        topics = ["Topic 1", "Topic 2", "Topic 3"]
        response = self.study_planner.create_plan(topics, hours=4)
        self.memory.add_history("study_agent", response)
        return response

    def _handle_research(self, text):
        topic = text.replace("explain", "").strip()
        response = self.researcher.generate_notes(topic)
        self.memory.add_history("research_agent", response)
        return response

    def _handle_doubt(self, text):
        response = self.doubt_solver.solve(text)
        self.memory.add_history("doubt_agent", response)
        return response
