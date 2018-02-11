import settings

from tkinter import *
from models.loaders.color_scheme_loader import ColorSchemeLoader
from models.processors.file import FileProcessor
from models.processors.word import WordProcessor
from view.grids.summary_categories import SummaryCategoriesGrid
from view.grids.summary_total import SummaryTotalGrid

SCHEME = ColorSchemeLoader.load(settings.DEFAULT_COLOR_SCHEME)


class SummaryFrame(Frame):
    def __init__(self, controller, **kwargs):
        super().__init__(**kwargs, bg=SCHEME.background)
        self.__controller = controller
        self.__create()
        self.__place()

    def _activate_callback(self):
        self.categories_table.update(self.__controller.get_summary_report())
        self.total_table.update(self.__controller.get_summary_report())

    def __create(self):
        self.title = Label(self, text='SUMMARY'.upper(),
                           background=SCHEME.background,
                           fg=SCHEME.text, font=SCHEME.title_font)
        self.description = Label(self, text='View or export the results of all reviews',
                                 background=SCHEME.background,
                                 fg=SCHEME.text, font=SCHEME.description_font)
        self.categories_table = SummaryCategoriesGrid(self, self.__controller.get_summary_report())
        self.total_table = SummaryTotalGrid(self, self.__controller.get_summary_report())
        self.back = Button(self, text='Back',
                           command=self.__back_callback)
        self.next = Button(self, text='Export .docx',
                           command=self.__docx_callback)

    def __place(self):
        for x in range(2):
            Grid.columnconfigure(self, x, weight=1)

        self.title.grid(row=0, column=0, columnspan=2)
        self.description.grid(row=1, column=0, columnspan=2)
        self.categories_table.grid(row=2, column=0, sticky=W+E+N, pady=(10, 5), columnspan=2)
        self.grid_rowconfigure(2, weight=2)
        self.total_table.grid(row=3, column=0, sticky=W+E+N, pady=(5, 10), columnspan=2)
        self.grid_rowconfigure(3, weight=2)
        self.back.grid(row=4, column=0, sticky=W + E + S + N, padx=(0, 5))
        self.next.grid(row=4, column=1, sticky=W + E + S + N, padx=(5, 0))

    def __back_callback(self):
        self.__controller.prev_step()

    def __docx_callback(self):
        document = WordProcessor.generate(self.__controller.get_summary_report())
        filename = FileProcessor.get_file_name(
            filetypes=(
                ("Document files", "*.doc;*.docx"),
                ("All files", "*.*")
            )
        )
        if filename:
            FileProcessor.save(document, filename)