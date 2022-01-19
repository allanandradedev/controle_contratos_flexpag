from validate_docbr import CNPJ


class ValidadorDeCNPJ:
    @staticmethod
    def valida_cnpj(cnpj: str) -> bool:
        return CNPJ().validate(cnpj)
