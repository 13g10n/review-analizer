from .sentence import SentenceReport


class TextReport:

    def __init__(self, text):
        self.__text = text
        self.__sentences_count = text.count('.') + text.count('?') + text.count('!')
        self.__sentence_reports = []
        self.__positive = 0
        self.__negative = 0

    def add(self, item):
        if isinstance(item, SentenceReport):
            self.__update_stat(item)
            self.__sentence_reports.append(item)
        else:
            raise ValueError("Only SentenceReport instances can be added to TextReport!")

    def __update_stat(self, report):
        self.__positive += report.positive
        self.__negative += report.negative

    def get_excerpt(self):
        return self.__text[:30] + "..."

    def get_sentences(self):
        return self.__sentence_reports

    @property
    def sentences_count(self):
        return self.__sentences_count

    @property
    def positive(self):
        return self.__positive

    @property
    def negative(self):
        return self.__negative

    @property
    def summary(self):
        summary = self.__positive + self.__negative
        if summary > 0:
            return "Positive"
        elif summary < 0:
            return "Negative"
        else:
            return "Neutral"
