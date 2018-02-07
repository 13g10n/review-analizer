import settings

from tkinter import *
from models.loaders.color_scheme_loader import ColorSchemeLoader

SCHEME = ColorSchemeLoader.load(settings.DEFAULT_COLOR_SCHEME)


class OutputFrame(Frame):
    def __init__(self, controller, **kwargs):
        super().__init__(**kwargs)
        self.__controller = controller
        self.__create()
        self.__place()

    def _activate_callback(self):
        self.output.config(state=NORMAL)
        self.output.delete(1.0, END)
        self.output.insert(0.0, self.__controller.output_text)
        self.output.config(state=DISABLED)

    def __create(self):
        self.title = Label(self, text='OUTPUT STEP'.upper(),
                                 background=SCHEME.background,
                                 fg=SCHEME.text, font=SCHEME.title_font)
        self.description = Label(self, text='You can view or export the result of text processing',
                                       background=SCHEME.background,
                                       fg=SCHEME.text, font=SCHEME.description_font)
        self.output = Text(self, wrap=WORD)
        self.back = Button(self, text='Add another',
                                      command=self.__back_callback)
        self.next = Button(self, text='Summary',
                                      command=self.__continue_callback)

    def __place(self):
        self.title.grid(row=0, column=0, columnspan=2)
        self.description.grid(row=1, column=0, columnspan=2)
        self.output.grid(row=2, column=0, sticky=W + E + S + N, pady=10, columnspan=2)
        self.grid_rowconfigure(2, weight=1)
        self.back.grid(row=3, column=0, sticky=W + E + S + N, padx=(0, 5))
        self.next.grid(row=3, column=1, sticky=W + E + S + N, padx=(5, 0))

    def __back_callback(self):
        self.__controller.restart_steps()

    def __continue_callback(self):
        self.__controller.next_step()