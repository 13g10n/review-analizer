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

            for i, (category, value) in enumerate(self.report.evaluation.items()):
                if value > 0:
                    bg = SCHEME.success_color
                elif value < 0:
                    bg = SCHEME.danger_color
                else:
                    bg = SCHEME.background
                Label(self, text=category.capitalize(), bd=1, relief="solid")\
                    .grid(row=i+1, column=0, sticky=W + E + S + N, ipady=5)
                Label(self, text=EvaluationProcessor.get_evaluation(value), bd=1, relief="solid", bg=bg)\
                    .grid(row=i+1, column=1, sticky=W + E + S + N, ipady=5)

    def update(self, report=None):
        self.report = report
        self.__create()
