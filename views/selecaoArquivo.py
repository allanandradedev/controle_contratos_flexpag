from tkinter import filedialog


class Selecoes:

    @staticmethod
    def seleciona_pasta():
        global destino
        destino = filedialog.askdirectory()
        return destino

    @staticmethod
    def seleciona_arquivo():
        global destino
        destino = filedialog.askopenfilename(filetype=(('pdf', '*.pdf'), ('All Files', '*.*')))
        return destino
