from tkinter import filedialog


class FileProcessor:

    @staticmethod
    def save(document, filename):
        document.save('{}'.format(filename))

    @staticmethod
    def get_file_name(filetypes):
        return filedialog.asksaveasfilename(
            initialdir='/',
            initialfile='report.docx',
            title='Save report as',
            filetypes=filetypes
        )
