import settings

from tkinter import *
from model.loaders.color_scheme_loader import ColorSchemeLoader
from model.processors.file import FileProcessor
from model.processors.word import WordProcessor
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

        self.buttons_frame = Frame(self)
        self.buttons_frame.columnconfigure(0, weight=2)
        self.buttons_frame.columnconfigure(1, weight=3)
        self.buttons_frame.pack(fill=X, padx=self.__padding, pady=(15, 0))

        self.back_button = Button(self.buttons_frame, text='Export to .docx', relief='flat', bd=0,
                                      background=SCHEME.button_background,
                                      font=SCHEME.button_font,
                                      foreground=SCHEME.button_text,
                                      activebackground=SCHEME.button_active,
                                      activeforeground=SCHEME.button_text,
                                      command=self.__docx_callback
                                      )
        self.back_button.grid(row=0, column=0, sticky=W+E+S+N)

        self.back_button = Button(self.buttons_frame, text='Back', relief='flat', bd=0,
                                      background=SCHEME.button_background,
                                      font=SCHEME.button_font,
                                      foreground=SCHEME.button_text,
                                      activebackground=SCHEME.button_active,
                                      activeforeground=SCHEME.button_text,
                                      command=self.__back_callback
                                      )
        self.back_button.grid(row=0, column=1, sticky=W+E+S+N, padx=(15, 0))

    def __back_callback(self):
        self.__controller.restart_steps()

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