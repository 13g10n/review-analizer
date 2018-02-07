from tkinter import *

import settings
from models.loaders.color_scheme_loader import ColorSchemeLoader
from .grid import BasicGrid

SCHEME = ColorSchemeLoader.load(settings.DEFAULT_COLOR_SCHEME)


class SummaryTotalGrid(BasicGrid):

    def __init__(self, parent, report):
        super().__init__(parent)
        self.report = report

    def __create(self):
        if self.report:
            for x in range(2):
                Grid.columnconfigure(self, x, weight=1)

            Label(self, text="Reviews summary", bd=1, relief="solid") \
                .grid(row=0, column=0, columnspan=2, sticky=W + E + S + N, ipady=5)

            Label(self, text="Items", bd=1, relief="solid") \
                .grid(row=1, column=0, sticky=W + E + S + N, ipady=5)
            Label(self, text=str(len(self.report.reports)), bd=1, relief="solid") \
                .grid(row=1, column=1, sticky=W + E + S + N, ipady=5)
            Label(self, text="Evaluation", bd=1, relief="solid") \
                .grid(row=2, column=0, sticky=W + E + S + N, ipady=5)

            bg = {
                "Positive": SCHEME.success_color,
                "Negative": SCHEME.danger_color,
                "Neutral": SCHEME.background
            }[self.report.summary]
            Label(self, text=self.report.summary, bd=1, relief="solid", bg=bg) \
                .grid(row=2, column=1, sticky=W + E + S + N, ipady=5)

    def update(self, report=None):
        self.report = report
        self.__create()