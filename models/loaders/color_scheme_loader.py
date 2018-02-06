import importlib
import settings


class ColorSchemeLoader:

    @staticmethod
    def load(scheme=settings.DEFAULT_COLOR_SCHEME):
        mod = importlib.import_module(ColorSchemeLoader.__get_import_name(scheme))
        return getattr(mod, scheme + 'ColorScheme')

    @staticmethod
    def apply(root, scheme=settings.DEFAULT_COLOR_SCHEME):
        root.option_add("*Background", scheme.background)
        root.option_add("*Font", scheme.font)

        root.option_add("*Button.Background", scheme.button_background)
        root.option_add("*Button.Foreground", scheme.button_text)
        root.option_add("*Button.Background", scheme.button_background)
        root.option_add("*Button.activeBackground", scheme.button_active)
        root.option_add("*Button.activeForeground", scheme.button_text)
        root.option_add("*Button.Font", scheme.button_font)
        root.option_add("*Button.Relief", scheme.button_relief)
        root.option_add("*Button.Cursor", scheme.button_cursor)
        root.option_add("*Button.Border", 0)

        root.option_add("*Text.Relief", scheme.text_relief)
        root.option_add("*Text.Foreground", scheme.text_foreground)
        root.option_add("*Text.Background", scheme.text_background)
        root.option_add("*Text.Font", scheme.font)
        root.option_add("*Text.insertBackground", scheme.text_insertbackground)

        root.option_add("*Label.Foreground", scheme.label_foreground)
        root.option_add("*Label.Background", scheme.label_background)

    @staticmethod
    def __get_import_name(scheme):
        return '{PATH}.{FILE}'.format(
            PATH='view.schemes',
            FILE=scheme.lower(),
        )
