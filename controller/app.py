from view.window import MainWindow
from models.analizer import Analizer
from models.processors.template import TemplateProcessor


class Application:
    __steps = {
        1: 'input',
        2: 'processing',
        3: 'output',
        4: 'summary',
    }

    def __init__(self):
        self.__input_text = ''
        self.__output_text = ''
        self.__report = None

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

    @property
    def report(self):
        return self.__report

    def next_step(self):
        self.__current_step += 1
        self.window.set_frame(self.__steps[self.__current_step])

    def prev_step(self):
        self.__current_step -= 1
        self.window.set_frame(self.__steps[self.__current_step])

    def restart_steps(self):
        self.__current_step = 1
        self.window.set_frame(self.__steps[1])

    def process_text(self):
        self.__report = Analizer.process_text(self.__input_text)
        self.__output_text = TemplateProcessor.get_text_report_string(self.__report)
