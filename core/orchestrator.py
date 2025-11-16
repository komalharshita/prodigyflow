import logging
logging.basicConfig(level=logging.INFO)

from agents.study_planner import StudyPlannerAgent
from agents.research_assistant import ResearchAssistantAgent
from agents.doubt_solver import DoubtSolverAgent
from memory.session_memory import SessionMemory
from agents.loop_agent import LoopAgent
from core.tools import evaluate_output, A2AProtocol


class Orchestrator:
    def __init__(self):
        self.memory = SessionMemory()

        self.study_planner = StudyPlannerAgent()
        self.researcher = ResearchAssistantAgent()
        self.doubt_solver = DoubtSolverAgent()

        self.loop_agent = LoopAgent()
        self.a2a = A2AProtocol()

    def route(self, user_input):
        logging.info(f"Routing input: {user_input}")
        self.memory.add_history("user", user_input)

        if "plan" in user_input.lower() or "study" in user_input.lower():
            response = self._handle_study(user_input)

        elif "explain" in user_input.lower() or "notes" in user_input.lower():
            response = self._handle_research(user_input)

        else:
            response = self._handle_doubt(user_input)

        final_response = evaluate_output(response)
        self.memory.add_history("system", final_response)

        return final_response

    def _handle_study(self, text):
        logging.info("Triggered Study Planner Agent")
        topics = ["Topic 1", "Topic 2", "Topic 3"]
        plan = self.study_planner.create_plan(topics, hours=4)

        refined = self.loop_agent.refine(plan)
        enriched = self.a2a.exchange(
            source_agent="StudyPlanner",
            target_agent="ResearchAssistant",
            content=refined
        )

        return enriched

    def _handle_research(self, text):
        logging.info("Triggered Research Agent")

        topic = text.lower().replace("explain", "").replace("notes", "").strip()
        if topic == "":
            topic = "general concept"

        notes = self.researcher.generate_notes(topic)
        enhanced = self.loop_agent.refine(notes)

        return enhanced

    def _handle_doubt(self, text):
        logging.info("Triggered Doubt Solver Agent")

        answer = self.doubt_solver.solve(text)

        merged = self.a2a.exchange(
            source_agent="DoubtSolver",
            target_agent="ResearchAssistant",
            content=answer
        )

        return merged
