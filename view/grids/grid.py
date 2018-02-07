from tkinter import *


class BasicGrid(Frame):
    def __init__(self, parent):
        super().__init__(parent, relief='solid', bd=1)
        self.update()

    def __create(self):
        raise NotImplementedError()

    def update(self, report=None):
        raise NotImplementedError()