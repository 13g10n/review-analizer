from .report import Report
from .context import ContextReport


class SentenceReport(Report):

    def __init__(self, sentence=None, index=None):
        super().__init__(
            content=sentence,
            acceptable_types=(ContextReport,),
        )
        self.__sentence = sentence
        self.__index = index

    @property
    def sentence(self):
        return self.__sentence

    @property
    def index(self):
        return self.__index

    @property
    def keywords_count(self):
        return len(self.reports)