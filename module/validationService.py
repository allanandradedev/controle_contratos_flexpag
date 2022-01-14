import validate_docbr as docbr
from tkinter import messagebox


class Validations:
    def __init__(self):
        pass

    def validate_doc(self, value: str):
        if docbr.CNPJ().validate(value):
            return docbr.CNPJ().mask(value)
        elif docbr.CPF().validate(value):
            return docbr.CPF().mask(value)
        else:
            messagebox.showerror(title='Valor Invalido', message='Insira um valor válido.')





if __name__ == '__main__':
    Validations().validate_doc('000000000')