from view.gui.window import MainWindow
from model.analizer import Analizer
from model.processors.template import TemplateProcessor


class Application:
    __steps = {
        1: 'input',
        2: 'output'
    }

    def __init__(self):
        self.__input_text = ''
        self.__output_text = ''

        self.__current_step = 1
        self.window = MainWindow(controller=self)
        self.window.set_frame(self.__steps[self.__current_step])

    def run(self):
        self.window.mainloop()

    @property
    def steps(self):
        return self.__steps.values()

    @property
    def input_text(self):
        return self.__input_text

    @input_text.setter
    def input_text(self, text):
        self.__input_text = text

    @property
    def output_text(self):
        return self.__output_text

    def next_step(self):
        self.__current_step += 1
        self.window.set_frame(self.__steps[self.__current_step])

    def prev_step(self):
        self.__current_step -= 1
        self.window.set_frame(self.__steps[self.__current_step])

    def process_text(self):
        self.__output_text = TemplateProcessor.get_text_report_string(
            Analizer.process_text(self.__input_text))
