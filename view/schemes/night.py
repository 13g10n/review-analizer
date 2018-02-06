from .scheme import ColorScheme


class NightColorScheme(ColorScheme):
    # Background
    background = '#34495e'
    background_light = '#2c3e50'
    background_dark = '#2c3e50'

    # Text
    text = '#ecf0f1'

    # Buttons
    button_background = '#3498db'
    button_active = '#2980b9'
    button_text = '#f7f7f7'

    # Fonts
    font = ('Calibri', 10)
    title_font = ('Calibri', 14, 'bold')
    description_font = ('Calibri', 8, 'italic')
    button_font = ('Calibri', 11)