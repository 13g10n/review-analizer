from .report import Report
from .sentence import SentenceReport


class TextReport(Report):

    def __init__(self, text):
        super().__init__(
            content=text,
            acceptable_types=(SentenceReport, ),
        )
        self.__sentences_count = text.count('.') + text.count('?') + text.count('!')

    @property
    def excerpt(self):
        return self.content[:30] + "..."

    @property
    def sentences_count(self):
        return self.__sentences_count

    @property
    def summary(self):
        summary = self.positive + self.negative
        if summary > 0:
            return "Positive"
        elif summary < 0:
            return "Negative"
        else:
            return "Neutral"
