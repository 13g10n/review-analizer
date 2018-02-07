class EvaluationProcessor:
    @staticmethod
    def get_evaluation(value):
        if value > 0:
            return "Positive"
        elif value < 0:
            return "Negative"
        else:
            return "Neutral"
