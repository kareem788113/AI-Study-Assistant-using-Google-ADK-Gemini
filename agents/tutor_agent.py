from services.gemini_service import ask_gemini


class TutorAgent:

    def run(self, text, question):

        prompt = f"""
You are a tutor.

Material:

{text}

Student Question:

{question}

Answer only using the material.
"""

        return ask_gemini(prompt)