from services.gemini_service import ask_gemini


class PlannerAgent:

    def run(self, text):

        prompt = f"""
Create a 7-day study plan for this material.

{text}
"""

        return ask_gemini(prompt)