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
        self.input_field.delete(1.0, END)
        self.input_field.insert(0.0, self.__controller.input_text)

    def __create(self):
        self.title_label = Label(self, text='INPUT STEP'.upper(),
                                 background=SCHEME.background,
                                 fg=SCHEME.text, font=SCHEME.title_font)
        self.title_label.pack(fill=X, pady=(20, 0))

        self.description_label = Label(self, text='Enter the text which you want to analyze in the '
                                                  'box below and click "Continue" button',
                                       background=SCHEME.background,
                                       fg=SCHEME.text, font=SCHEME.description_font)
        self.description_label.pack(fill=X, pady=(0, 10))

        self.input_field = Text(self, height=13, bd=5,
                                relief='flat', wrap=WORD,
                                background=SCHEME.background_light,
                                foreground=SCHEME.text,
                                insertbackground=SCHEME.text,
                                font=SCHEME.font)
        self.input_field.pack(fill=X, padx=self.__padding)

        self.continue_button = Button(self, text='Continue', relief='flat', bd=0,
                                      font=SCHEME.button_font,
                                      background=SCHEME.button_background,
                                      foreground=SCHEME.button_text,
                                      activebackground=SCHEME.button_active,
                                      activeforeground=SCHEME.button_text,
                                      command=self.__continue_callback
                                      )
        self.continue_button.pack(fill=X, padx=self.__padding, pady=15)

    def __continue_callback(self):
        self.__controller.input_text = self.input_field.get(1.0, END)[:-1]
        self.__controller.next_step()
