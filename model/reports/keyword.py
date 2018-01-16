class KeywordReport:
    def __init__(self, keyword, positive=0, negative=0):
        self.keyword = keyword
        self.positive = positive
        self.negative = negative
        self.category = None

    def __str__(self):
        return "\tCategory: {3}\n\tKeyword: {0}\n\tRate: +{1} -{2}".format(self.keyword, self.positive,
                                                                           self.negative, self.category)