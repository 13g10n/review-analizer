from .keyword import KeywordReport


class SentenceReport:

    def __init__(self, sentence, index=None):
        self.__sentence = sentence
        self.__index = index
        self.__keyword_reports = []
        self.__positive = 0
        self.__negative = 0

    def add(self, item):
        if isinstance(item, KeywordReport):
            self.__positive += item.positive
            self.__negative += item.negative
            self.__keyword_reports.append(item)
        else:
            raise ValueError("Only KeywordReport instances can be added to SentenceReport!")

    @property
    def sentence(self):
        return self.__sentence

    @property
    def index(self):
        return self.__index

    def get_reports(self):
        return self.__keyword_reports

    @property
    def positive(self):
        return self.__positive

    @property
    def negative(self):
        return self.__negative

    @property
    def keywords_count(self):
        return len(self.__keyword_reports)