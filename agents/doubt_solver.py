import logging
logging.basicConfig(level=logging.INFO)

class DoubtSolverAgent:
    def solve(self, question):
        return {
            "agent": "Doubt Solver",
            "question": question,
            "explanation": f"Here is a clear explanation for your doubt about '{question}'.",
            "tip": "Break the concept into smaller steps to understand better."
        }
