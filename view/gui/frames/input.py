import settings

from tkinter import *
from model.loaders.color_scheme_loader import ColorSchemeLoader

SCHEME = ColorSchemeLoader.load(settings.DEFAULT_COLOR_SCHEME)


class InputFrame(Frame):
    def __init__(self, controller, **kwargs):
        super().__init__(**kwargs, bg=SCHEME.background)
        self.__controller = controller
        self.__height = kwargs['height']
        self.__width = kwargs['width']
        self.__padding = 50
        self.__create()
        self.pack_propagate(0)

    def _activate_callback(self):
        self.input_field.delete(0.0, END)
        self.input_field.insert(0.0, self.__controller.input_text)

    def __create(self):
        self.title_label = Label(self, text='Step 1: input'.upper(),
                                 background=SCHEME.background,
                                 fg=SCHEME.text, font=SCHEME.title_font)
        self.title_label.pack(fill=X)

        self.description_label = Label(self, text='Enter the text which you want to analyze in the '
                                                  'box below and click "Continue" button',
                                       background=SCHEME.background,
                                       fg=SCHEME.text, font=SCHEME.description_font)
        self.description_label.pack(fill=X)

        self.input_field = Text(self, height=15,
                                background=SCHEME.background_light,
                                font=SCHEME.description_font)
        self.input_field.pack(fill=X, padx=self.__padding)

        self.continue_button = Button(self, text='Continue', relief='flat', bd=0,
                                      background=SCHEME.button_background,
                                      foreground=SCHEME.button_text,
                                      activebackground=SCHEME.button_active,
                                      activeforeground=SCHEME.button_text,
                                      command=self.__continue_callback
                                      )
        self.continue_button.pack(fill=X, padx=self.__padding, pady=15)

    def __continue_callback(self):
        self.__controller.input_text = self.input_field.get(0.0, END)
        self.__controller.process_text()
        self.__controller.next_step()
