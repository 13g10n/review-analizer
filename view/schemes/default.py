from .scheme import ColorScheme


class DefaultColorScheme(ColorScheme):
    # Background
    background = '#ecf0f1'
    background_light = '#f7f7f7'
    background_dark = '#bdc3c7'

    # Text
    text = '#34495e'

    # Buttons
    button_background = '#3498db'
    button_active = '#2980b9'
    button_text = '#f7f7f7'

    # Fonts
    font = ('Calibri', 10)
    title_font = ('Calibri', 14, 'bold')
    description_font = ('Calibri', 8, 'italic')
    button_font = ('Calibri', 11)
