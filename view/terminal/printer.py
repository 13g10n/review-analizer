from model.reports.text import TextReport
from .templates import KEYWORD_REPORT, SENTENCE_REPORT, TEXT_REPORT


class TerminalPrinter:

    @staticmethod
    def out(report):
        if isinstance(report, TextReport):
            TerminalPrinter.__print_text_report(report)
        else:
            raise ValueError("Unsupported report type was passed!")

    @staticmethod
    def __print_text_report(report):
        print(TerminalPrinter.__get_text_report_string(report))

    @staticmethod
    def __get_text_report_string(report):
        return TEXT_REPORT.format(
            TITLE=report.excerpt,
            TEXT=report.content,
            SENTENCES_COUNT=report.sentences_count,
            POSITIVE=report.positive,
            NEGATIVE=report.negative,
            SUMMARY=report.summary,
            SENTENCE_REPORTS="".join([TerminalPrinter.__get_sentence_report_string(report) for report in report.reports])
        )

    @staticmethod
    def __get_sentence_report_string(report):
        return SENTENCE_REPORT.format(
            INDEX=report.index + 1,
            SENTENCE=report.sentence,
            KEYWORDS_COUNT=report.keywords_count,
            KEYWORD_REPORT="".join([TerminalPrinter.__get_keyword_report_string(report) for report in report.reports])
        )

    @staticmethod
    def __get_keyword_report_string(report):
        return KEYWORD_REPORT.format(
            CATEGORY=report.category,
            KEYWORD=report.content,
            POSITIVE=report.positive,
            NEGATIVE=report.negative,
            INVERTED=('Yes' if report.inverted else 'No'),
            INTENSIFIER=(report.intensifier if report.intensifier else '-'),
        )
