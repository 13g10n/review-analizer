import importlib
import settings

from tkinter import *
from models.loaders.color_scheme_loader import ColorSchemeLoader


class MainWindow(Tk):
    def __init__(self, controller):
        super().__init__()
        self.__controller = controller
        self.__scheme = ColorSchemeLoader.load(settings.DEFAULT_COLOR_SCHEME)
        self.__title = "Review analyzer"
        self.__setup_window()
        self.__setup_container()
        self.__setup_frames()

    def set_frame(self, frame_name):
        frame = self.__frames[frame_name]
        frame.tkraise()
        frame._activate_callback()

    def __setup_window(self):
        self.resizable(False, False)
        self.title('{TITLE} - v{VERSION}'.format(
            TITLE=self.__title,
            VERSION=settings.VERSION,
        ))
        self.__setup_scheme()

    def __setup_scheme(self):
        ColorSchemeLoader.apply(self, self.__scheme)

    def __setup_frames(self):
        self.__frames = {}
        for frame_name in self.__controller.steps:
            frame_class = self.__get_frame_class(frame_name)
            frame = frame_class(controller=self.__controller, master=self.__container)
            frame.pack_propagate(0)
            self.__frames[frame_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

    def __get_frame_class(self, frame_name):
        mod = importlib.import_module('{PATH}.{FILE}'.format(
            PATH='view.frames',
            FILE=frame_name.lower(),
        ))
        return getattr(mod, frame_name.capitalize() + 'Frame')

    def __setup_container(self):
        self.__container = Frame(self, padx=self.__scheme.window_padding, pady=self.__scheme.window_padding)
        self.__container.pack(side="top", fill="both", expand=True)
        self.__container.grid_rowconfigure(0, weight=1)
        self.__container.grid_columnconfigure(0, weight=1)
