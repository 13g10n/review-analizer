import settings

from tkinter import *
from models.loaders.color_scheme_loader import ColorSchemeLoader

SCHEME = ColorSchemeLoader.load(settings.DEFAULT_COLOR_SCHEME)


class ProcessingFrame(Frame):
    def __init__(self, controller, **kwargs):
        super().__init__(**kwargs, bg=SCHEME.background)
        self.__controller = controller
        self.__create()
        self.__place()

    def _activate_callback(self):
        self.after(10, self.__process)

    def __process(self):
        self.__controller.process_text()
        self.__controller.next_step()

    def __create(self):
        self.title_label = Label(self, text='Processing...',
                                 background=SCHEME.background,
                                 fg=SCHEME.text, font=SCHEME.title_font)

    def __place(self):
        self.title_label.grid(row=0, column=0, sticky=W+E+S+N)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)


