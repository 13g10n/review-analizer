import os
import settings


class TemplateLoader:

    @staticmethod
    def load(template_name):
        file_path = os.path.join(settings.TEMPLATES_PATH, template_name)
        with open(file_path) as file:
            template = file.read()
        return template