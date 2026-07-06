from services.gemini_service import ask_gemini


class SummaryAgent:

    def run(self, text):

        prompt = f"""
You are an AI Study Assistant.

Summarize the following PDF into concise study notes.

{text}
"""

        return ask_gemini(prompt)