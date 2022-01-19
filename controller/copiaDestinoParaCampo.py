from views.selecaoArquivo import Selecoes
from tkinter import StringVar

class CopiaDestinoParaEntry:
    @staticmethod
    def copiar(master, entry: StringVar) -> None:
        destino = Selecoes.seleciona_arquivo()
        entry.set(destino)
        master.focus_force()
