import settings

from tkinter import *
from models.loaders.color_scheme_loader import ColorSchemeLoader
from models.processors.evaluation import EvaluationProcessor
from .grid import BasicGrid

SCHEME = ColorSchemeLoader.load(settings.DEFAULT_COLOR_SCHEME)


class SummaryCategoriesGrid(BasicGrid):

    def __init__(self, parent, report):
        super().__init__(parent)
        self.report = report

    def __create(self):
        if self.report:
            for x in range(2):
                Grid.columnconfigure(self, x, weight=1)

            Label(self, text="Report categories", bd=1, relief="solid")\
                .grid(row=0, column=0, columnspan=2, sticky=W + E + S + N, ipady=5)

            for i, (category, values) in enumerate(self.report.evaluation.items()):
                evaluation = EvaluationProcessor.get_evaluation(
                    values['positive'], values['negative'])
                fg, bg = EvaluationProcessor.get_evaluation_colors(evaluation)

                Label(self, text=category.capitalize(), bd=1, relief="solid")\
                    .grid(row=i+1, column=0, sticky=W + E + S + N, ipady=5)
                Label(self, text=evaluation, bd=1, relief="solid", bg=bg, fg=fg)\
                    .grid(row=i+1, column=1, sticky=W + E + S + N, ipady=5)

    def update(self, report=None):
        self.report = report
        self.__create()
