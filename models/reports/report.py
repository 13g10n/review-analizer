from models.processors.evaluation import EvaluationProcessor


class Report:
    """Abstract report class, all type of reports must inherit
    from this one.
    """

    def __init__(self, content=None, acceptable_types=None):
        self.__reports = []
        self.__content = content
        self.__add_acceptable_type(acceptable_types)
        self.__positive = 0
        self.__negative = 0

    @property
    def content(self):
        return self.__content

    @property
    def positive(self):
        return self.__positive

    @property
    def negative(self):
        return self.__negative

    @property
    def reports(self):
        return self.__reports

    @property
    def summary(self):
        return EvaluationProcessor.get_evaluation(self.positive + self.negative)

    def add(self, item):
        if item and isinstance(item, self.__acceptable_types):
            self.__update_stat(item)
            self.__reports.append(item)
        else:
            raise ValueError("Only {0} instances can be added to {1}!".format(
                repr(self.__acceptable_types),
                self.__class__
            ))

    def set_evaluation(self, positive, negative):
        self.__positive = positive
        self.__negative = negative

    def __update_stat(self, report):
        self.__positive += report.positive
        self.__negative += report.negative

    def __add_acceptable_type(self, types):
        self.__acceptable_types = types if types else ()

