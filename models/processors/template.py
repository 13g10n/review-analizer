from models.loaders.template_loader import TemplateLoader
from models.processors.evaluation import EvaluationProcessor

SUMMARY_REPORT = TemplateLoader.load('summary_report.txt')
TEXT_REPORT = TemplateLoader.load('text_report.txt')
SENTENCE_REPORT = TemplateLoader.load('sentence_report.txt')
CONTEXT_REPORT = TemplateLoader.load('context_report.txt')
CATEGORY_LINE = TemplateLoader.load('category_line.txt')


class TemplateProcessor:

    @staticmethod
    def get_summary_report_string(report):
        return SUMMARY_REPORT.format(
            POSITIVE=report.positive,
            NEGATIVE=report.negative,
            SUMMARY=report.summary,
            COUNTER=len(report.reports),
            TABLE="".join([CATEGORY_LINE.format(
                CATEGORY=category,
                VALUE=EvaluationProcessor.get_evaluation(value)
            ) for (category, value) in report.evaluation.items()])
        )

    @staticmethod
    def get_text_report_string(report):
        return TEXT_REPORT.format(
            TITLE=report.excerpt,
            TEXT=report.content,
            SENTENCES_COUNT=report.sentences_count,
            POSITIVE=report.positive,
            NEGATIVE=report.negative,
            SUMMARY=report.summary,
            SENTENCE_REPORTS="".join([TemplateProcessor.__get_sentence_report_string(report) for report in report.reports])
        )

    @staticmethod
    def __get_sentence_report_string(report):
        return SENTENCE_REPORT.format(
            INDEX=report.index + 1,
            SENTENCE=report.sentence,
            KEYWORDS_COUNT=report.keywords_count,
            KEYWORD_REPORT="".join([TemplateProcessor.__get_keyword_report_string(report) for report in report.reports])
        )

    @staticmethod
    def __get_keyword_report_string(report):
        return CONTEXT_REPORT.format(
            CATEGORY=report.category,
            KEYWORD=report.content,
            POSITIVE=report.positive,
            NEGATIVE=report.negative,
            INVERTED=('Yes' if report.inverted else 'No'),
            INTENSIFIER=(report.intensifier if report.intensifier else '-'),
            EVALUATOR=(report.evaluator if report.evaluator else '-'),
        )