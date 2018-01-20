import importlib
import settings


class ColorSchemeLoader:

    @staticmethod
    def load(scheme=settings.DEFAULT_COLOR_SCHEME):
        mod = importlib.import_module(ColorSchemeLoader.__get_import_name(scheme))
        return getattr(mod, scheme + 'ColorScheme')

    @staticmethod
    def __get_import_name(scheme):
        return '{PATH}.{FILE}'.format(
            PATH='view.gui.schemes',
            FILE=scheme.lower(),
        )
