try:
    from google.generativeai import GenerativeModel
    import google.generativeai as genai

    genai.configure(api_key="YOUR_API_KEY")

    GEMINI_AVAILABLE = True

except Exception:
    GEMINI_AVAILABLE = False


class ResearchAssistantAgent:
    def __init__(self):
        if GEMINI_AVAILABLE:
            self.model = GenerativeModel("gemini-1.5-flash")
        else:
            self.model = None   # fallback

    def generate_notes(self, topic):
        if GEMINI_AVAILABLE and self.model:
            try:
                response = self.model.generate_content(
                    f"Explain the topic '{topic}' in simple, beginner-friendly terms. "
                    f"Provide summary, key ideas, and one example."
                )

                return {
                    "agent": "Research Assistant (Gemini)",
                    "topic": topic,
                    "summary": response.text,
                    "source": "Gemini API"
                }

            except Exception as e:
                # Fallback to local simple explanation
                return {
                    "agent": "Research Assistant (Fallback)",
                    "topic": topic,
                    "summary": f"Gemini failed. Reason: {e}. Using fallback notes.",
                    "key_points": [
                        f"What is {topic}",
                        f"Why {topic} matters",
                        f"Example of {topic}"
                    ]
                }

        # Local fallback if Gemini not available
        return {
            "agent": "Research Assistant (Local)",
            "topic": topic,
            "summary": f"A simple explanation of {topic}.",
            "key_points": [
                f"Core idea of {topic}",
                f"Why {topic} matters",
                f"Example related to {topic}"
            ],
            "examples": [f"Example: Understanding {topic} in real life."]
        }
