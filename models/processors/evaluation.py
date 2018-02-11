import settings
from models.loaders.color_scheme_loader import ColorSchemeLoader

SCHEME = ColorSchemeLoader.load(settings.DEFAULT_COLOR_SCHEME)


class EvaluationProcessor:

    @staticmethod
    def get_evaluation(positive, negative):
        if positive == 0 and negative == 0:
            return "Unknown"

        value = positive + negative
        if value > 0:
            return "Positive"
        elif value < 0:
            return "Negative"
        else:
            return "Neutral"

    @staticmethod
    def get_evaluation_colors(evaluation):
        bg = {
            "Positive": SCHEME.success_color,
            "Negative": SCHEME.danger_color,
            "Neutral": SCHEME.warning_color,
            "Unknown": SCHEME.background
        }[evaluation]
        fg = {
            "Positive": SCHEME.button_text,
            "Negative": SCHEME.button_text,
            "Neutral": SCHEME.button_text,
            "Unknown": SCHEME.text
        }[evaluation]
        return fg, bg