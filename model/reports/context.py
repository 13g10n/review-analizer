from .report import Report


class ContextReport(Report):
    def __init__(self, keyword=None, positive=0, negative=0, intensifier=None, inverted=False):
        super().__init__(
            content=keyword,
        )
        super().set_evaluation(positive=positive, negative=negative)
        self.category = None
        self.inverted = inverted
        self.intensifier = intensifier
