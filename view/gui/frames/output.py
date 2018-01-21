import settings

from tkinter import *
from model.loaders.color_scheme_loader import ColorSchemeLoader
from view.gui.widgets.text_input import ScrollableTextInput

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
        self.output_field.set_text(self.__controller.output_text)

    def __create(self):
        self.title_label = Label(self, text='OUTPUT STEP'.upper(),
                                 background=SCHEME.background,
                                 fg=SCHEME.text, font=SCHEME.title_font)
        self.title_label.pack(fill=X, pady=(20, 0))

        self.description_label = Label(self, text='You can view or export the result of text processing',
                                       background=SCHEME.background,
                                       fg=SCHEME.text, font=SCHEME.description_font)
        self.description_label.pack(fill=X, pady=(0, 10))

        self.output_field = ScrollableTextInput(self)
        self.output_field.pack(fill=X, padx=self.__padding)

        self.continue_button = Button(self, text='Back', relief='flat', bd=0,
                                      background=SCHEME.button_background,
                                      font=SCHEME.button_font,
                                      foreground=SCHEME.button_text,
                                      activebackground=SCHEME.button_active,
                                      activeforeground=SCHEME.button_text,
                                      command=self.__back_callback
                                      )
        self.continue_button.pack(fill=X, padx=self.__padding, pady=15)

    def __back_callback(self):
        self.__controller.restart_steps()