from agents.summary_agent import SummaryAgent
from agents.quiz_agent import QuizAgent
from agents.planner_agent import PlannerAgent
from agents.tutor_agent import TutorAgent

from utils.pdf_reader import extract_text_from_pdf


class Orchestrator:

    def __init__(self):

        self.summary = SummaryAgent()
        self.quiz = QuizAgent()
        self.planner = PlannerAgent()
        self.tutor = TutorAgent()

    def process_pdf(self, pdf):

        return extract_text_from_pdf(pdf)