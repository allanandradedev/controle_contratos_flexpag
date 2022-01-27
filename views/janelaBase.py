from tkinter import Tk

from views.janelaLogin import JanelaLogin


class JanelaBase(Tk):
    def __init__(self):
        super().__init__()
        self.title('Controle de Contratos FlexPag')
        self.geometry("1260x768")
        self.configure(bg="#005E9F")
        self.iconbitmap('assets\icone_flexpag.ico')
        self.resizable(False, False)
        JanelaLogin(self)
