import settings

from tkinter import *
from model.loaders.color_scheme_loader import ColorSchemeLoader

SCHEME = ColorSchemeLoader.load(settings.DEFAULT_COLOR_SCHEME)


class ProcessingFrame(Frame):
    def __init__(self, controller, **kwargs):
        super().__init__(**kwargs, bg=SCHEME.background)
        self.__controller = controller
        self.__height = kwargs['height']
        self.__width = kwargs['width']
        self.__padding = 50
        self.__text = 'Processing'
        self.__current_text = 'Processing...'
        self.__text_apdater = False
        self.__create()
        self.pack_propagate(0)

    def _activate_callback(self):
        self.__text_apdater = True
        self.__update_text()
        self.__controller.process_text()
        self.after(1600, self.__controller.next_step)
        self.after(1600, self.__stop_text_updater)

    def __create(self):
        self.title_label = Label(self, text=self.__text.upper(),
                                 background=SCHEME.background,
                                 fg=SCHEME.text, font=SCHEME.title_font)
        self.title_label.pack(fill=BOTH, expand=1)

    def __update_text(self):
        i = self.__current_text.count('.') + 1
        e = 0 if i == 4 else i
        self.__current_text = self.__text + '.' * e + ' ' * (3-e)
        self.title_label.config(text=self.__current_text)
        if self.__text_apdater:
            self.after(500, self.__update_text)

    def __stop_text_updater(self):
        self.__text_apdater = False
