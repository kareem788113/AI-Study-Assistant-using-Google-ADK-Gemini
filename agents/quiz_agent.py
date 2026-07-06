from services.gemini_service import ask_gemini


class QuizAgent:

    def run(self, text):

        prompt = f"""
Generate 10 multiple choice questions from this PDF.

{text}
"""

        return ask_gemini(prompt)