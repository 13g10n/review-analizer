import settings

from tkinter import *
from model.loaders.color_scheme_loader import ColorSchemeLoader

SCHEME = ColorSchemeLoader.load(settings.DEFAULT_COLOR_SCHEME)


class ScrollableTextInput(Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        self.output_field_scrollbar = Scrollbar(self, bg=SCHEME.background_light, relief='flat')
        self.output_field_scrollbar.pack(side=RIGHT, fill=Y)

        self.output_field = Text(self, height=10, wrap=WORD, bd=5,
                                 relief='flat',
                                 background=SCHEME.background_light,
                                 foreground=SCHEME.text,
                                 font=SCHEME.font,
                                 yscrollcommand=self.output_field_scrollbar.set)
        self.output_field.pack(fill=Y)
        self.output_field_scrollbar.config(command=self.output_field.yview)

    def set_text(self, text):
        self.output_field.config(state=NORMAL)
        self.output_field.delete(1.0, END)
        self.output_field.insert(0.0, text)
        self.output_field.config(state=DISABLED)