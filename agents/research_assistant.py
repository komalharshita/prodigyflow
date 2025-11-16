import logging
logging.basicConfig(level=logging.INFO)

class ResearchAssistantAgent:
    def generate_notes(self, topic):
        return {
            "agent": "Research Assistant",
            "topic": topic,
            "summary": f"A simple explanation of {topic}.",
            "key_points": [
                f"Core idea of {topic}",
                f"Why {topic} matters",
                f"Example related to {topic}"
            ],
            "examples": [
                f"Example: Understanding {topic} in real life."
            ]
        }
