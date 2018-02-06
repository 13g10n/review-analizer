import settings

from tkinter import *
from models.loaders.color_scheme_loader import ColorSchemeLoader
from models.processors.evaluation import EvaluationProcessor
from models.processors.file import FileProcessor
from models.processors.word import WordProcessor

SCHEME = ColorSchemeLoader.load(settings.DEFAULT_COLOR_SCHEME)


class SummaryFrame(Frame):
    def __init__(self, controller, **kwargs):
        super().__init__(**kwargs, bg=SCHEME.background)
        self.__controller = controller
        self.__create()
        self.__place()

    def _activate_callback(self):
        self.__create_table(self.table)
        # self.output.config(state=NORMAL)
        # self.output.delete(1.0, END)
        # self.output.insert(0.0, self.__controller.summary)
        # self.output.config(state=DISABLED)

    def __create(self):
        self.title = Label(self, text='SUMMARY'.upper(),
                           background=SCHEME.background,
                           fg=SCHEME.text, font=SCHEME.title_font)
        self.description = Label(self, text='You can view or export the result of text processing',
                                 background=SCHEME.background,
                                 fg=SCHEME.text, font=SCHEME.description_font)
        self.table = Frame(self)

        self.__create_table(self.table)

        self.back = Button(self, text='Back',
                           command=self.__back_callback)
        self.next = Button(self, text='Export .docx',
                           command=self.__docx_callback)

    def __place(self):
        for x in range(2):
            Grid.columnconfigure(self, x, weight=1)

        self.title.grid(row=0, column=0, columnspan=2)
        self.description.grid(row=1, column=0, columnspan=2)
        self.table.grid(row=2, column=0, sticky=W+E+S+N, pady=10, columnspan=2)
        self.grid_rowconfigure(2, weight=2)
        self.back.grid(row=3, column=0, sticky=W + E + S + N, padx=(0, 5))
        self.next.grid(row=3, column=1, sticky=W + E + S + N, padx=(5, 0))

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

    def __create_table(self, root):
        for x in range(2):
            Grid.columnconfigure(root, x, weight=1)

        Label(root, text="Report categories", bd=1, relief="solid")\
            .grid(row=0, column=0, columnspan=2, sticky=W + E + S + N, ipady=5)

        e = 0
        for i, (category, value) in enumerate(self.__controller.get_summary_report().evaluation.items()):
            Label(root, text=category.capitalize(), bd=1, relief="solid")\
                .grid(row=i+1, column=0, sticky=W + E + S + N, ipady=5)
            Label(root, text=EvaluationProcessor.get_evaluation(value), bd=1, relief="solid")\
                .grid(row=i+1, column=1, sticky=W + E + S + N, ipady=5)
            e = i + 2

        Label(root, text="Reviews summary", bd=1, relief="solid") \
            .grid(row=e, column=0, columnspan=2, sticky=W + E + S + N, ipady=5, pady=(10, 0))

        Label(root, text="Keywords", bd=1, relief="solid") \
            .grid(row=e + 1, column=0, sticky=W + E + S + N, ipady=5)
        Label(root, text=str(len(self.__controller.get_summary_report().reports)), bd=1, relief="solid") \
            .grid(row=e + 1, column=1, sticky=W + E + S + N, ipady=5)
        Label(root, text="Evaluation", bd=1, relief="solid") \
            .grid(row=e + 2, column=0, sticky=W + E + S + N, ipady=5)
        Label(root, text=self.__controller.get_summary_report().summary, bd=1, relief="solid") \
            .grid(row=e + 2, column=1, sticky=W + E + S + N, ipady=5)