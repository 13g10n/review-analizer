import settings

from tkinter import *
from model.loaders.color_scheme_loader import ColorSchemeLoader

SCHEME = ColorSchemeLoader.load(settings.DEFAULT_COLOR_SCHEME)


class OutputFrame(Frame):
    def __init__(self, controller, **kwargs):
        super().__init__(**kwargs, bg=SCHEME.background)
        self.__controller = controller
        self.__height = kwargs['height']
        self.__width = kwargs['width']
        self.__padding = 50
        self.__create()
        self.pack_propagate(0)

    def _activate_callback(self):
        self.output_field.config(state=NORMAL)
        self.output_field.delete(0.0, END)
        self.output_field.insert(0.0, self.__controller.output_text)
        self.output_field.config(state=DISABLED)

    def __create(self):
        self.title_label = Label(self, text='Step 2: output'.upper(),
                                 background=SCHEME.background,
                                 fg=SCHEME.text, font=SCHEME.title_font)
        self.title_label.pack(fill=X)

        self.output_field = Text(self, height=18, bd=0,
                                 background=SCHEME.background,
                                 foreground=SCHEME.text,
                                 font=SCHEME.description_font)
        self.output_field.pack(fill=X, padx=self.__padding)

        self.continue_button = Button(self, text='Back', relief='flat', bd=0,
                                      background=SCHEME.button_background,
                                      foreground=SCHEME.button_text,
                                      activebackground=SCHEME.button_active,
                                      activeforeground=SCHEME.button_text,
                                      command=self.__back_callback
                                      )
        self.continue_button.pack(fill=X, padx=self.__padding, pady=15)

    def __back_callback(self):
        self.__controller.prev_step()