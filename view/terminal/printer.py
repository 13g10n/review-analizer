from model.loaders.template_loader import TemplateLoader
from model.processors.template import TemplateProcessor
from model.reports.text import TextReport

TEXT_REPORT = TemplateLoader.load('text_report.txt')
SENTENCE_REPORT = TemplateLoader.load('sentence_report.txt')
CONTEXT_REPORT = TemplateLoader.load('context_report.txt')


class TerminalPrinter:

    @staticmethod
    def out(report):
        if isinstance(report, TextReport):
            TerminalPrinter.__print_text_report(report)
        else:
            raise ValueError("Unsupported report type was passed!")

    @staticmethod
    def __print_text_report(report):
        print(TemplateProcessor.get_text_report_string(report))
