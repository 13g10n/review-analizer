import settings

from tkinter import *
from models.loaders.color_scheme_loader import ColorSchemeLoader
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
        self.output.config(state=NORMAL)
        self.output.delete(1.0, END)
        self.output.insert(0.0, self.__controller.output_text)
        self.output.config(state=DISABLED)

    def __create(self):
        self.title = Label(self, text='SUMMARY'.upper(),
                           background=SCHEME.background,
                           fg=SCHEME.text, font=SCHEME.title_font)
        self.description = Label(self, text='You can view or export the result of text processing',
                                 background=SCHEME.background,
                                 fg=SCHEME.text, font=SCHEME.description_font)
        self.output = Text(self, relief='flat', wrap=WORD,
                           background=SCHEME.background_light,
                           foreground=SCHEME.text,
                           insertbackground=SCHEME.text,
                           font=SCHEME.font)
        self.back = Button(self, text='Back',
                           command=self.__back_callback)
        self.next = Button(self, text='Export .docx',
                           command=self.__docx_callback)

    def __place(self):
        self.title.grid(row=0, column=0, columnspan=2)
        self.description.grid(row=1, column=0, columnspan=2)
        self.output.grid(row=2, column=0, sticky=W + E + S + N, pady=10, columnspan=2)
        self.grid_rowconfigure(2, weight=1)
        self.back.grid(row=3, column=0, sticky=W + E + S + N, padx=(0, 5))
        self.next.grid(row=3, column=1, sticky=W + E + S + N, padx=(5, 0))

    def __back_callback(self):
        self.__controller.prev_step()

    def __docx_callback(self):
        document = WordProcessor.generate(self.__controller.report)
        filename = FileProcessor.get_file_name(
            filetypes=(
                ("Document files", "*.doc;*.docx"),
                ("All files", "*.*")
            )
        )
        if filename:
            FileProcessor.save(document, filename)