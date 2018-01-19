import os

from model.analizer import Analizer
from view.terminal.printer import TerminalPrinter

 
if __name__ == '__main__':
    text = input("Enter text to process: ")
    result = Analizer.process_text(text)
    TerminalPrinter.out(result)
    os.system("pause")
