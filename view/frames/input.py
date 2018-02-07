import settings

from tkinter import *
from models.loaders.color_scheme_loader import ColorSchemeLoader

SCHEME = ColorSchemeLoader.load(settings.DEFAULT_COLOR_SCHEME)


class InputFrame(Frame):
    def __init__(self, controller, **kwargs):
        super().__init__(**kwargs)
        self.__controller = controller
        self.__create()
        self.__place()

    def _activate_callback(self):
        self.input.delete(1.0, END)

    def __create(self):
        self.title = Label(self, text='INPUT STEP', font=SCHEME.title_font)
        self.description = Label(self, text='Enter the text which you want to analyze in the '
                                 'box below and click "Continue" button', font=SCHEME.description_font)
        self.input = Text(self, wrap=WORD)
        self.clear = Button(self, text="Clear", command=self.__clear_input)
        self.next = Button(self, text='Continue', command=self.__continue_callback)

    def __place(self):
        self.title.grid(row=0, column=0, columnspan=2)
        self.description.grid(row=1, column=0, columnspan=2)
        self.input.grid(row=2, column=0, sticky=W+E+S+N, pady=10, columnspan=2)
        self.grid_rowconfigure(2, weight=1)
        self.clear.grid(row=3, column=0, sticky=W+E+S+N, padx=(0, 5))
        self.next.grid(row=3, column=1, sticky=W+E+S+N, padx=(5, 0))

    def __clear_input(self):
        self.input.delete(0.0, END)

    def __continue_callback(self):
        self.__controller.input_text = self.input.get(1.0, END)[:-1]
        self.__controller.next_step()
