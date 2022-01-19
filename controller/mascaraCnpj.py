from validate_docbr import CNPJ


class MascaraCNPJ:
    @staticmethod
    def mascarar(cnpj):
        cnpj = CNPJ().mask(cnpj)
        return cnpj