from models.processors.evaluation import EvaluationProcessor
from .report import Report
from .text import TextReport
from data import ASPECT_CATEGORIES


class SummaryReport(Report):

    def __init__(self):
        super().__init__(
            content=None,
            acceptable_types=(TextReport, ),
        )
        self.evaluation = {}

        for key in ASPECT_CATEGORIES.keys():
            self.evaluation[key] = 0

    def add(self, item):
        super().add(item)
        for sentence_report in item.reports:
            for context_report in sentence_report.reports:
                category = context_report.category
                total = context_report.positive + context_report.negative
                if category in self.evaluation:
                    self.evaluation[category] += total
