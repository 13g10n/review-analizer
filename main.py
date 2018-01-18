from model.analizer import Analizer
from view.terminal.printer import TerminalPrinter


if __name__ == '__main__':
    text = '''They’re very reliable. At times, we’ve challenged them with outside-the-box projects, and they’ve always performed at a high level. That includes communicating professionally, being transparent, and hitting deadlines.'''
    result = Analizer.process_text(text)
    TerminalPrinter.out(result)

