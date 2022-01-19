from models.gerenciaBanco import BancoDeDados
from models.validaCNPJ import ValidadorDeCNPJ


class ConfirmaPesquisa:
    def __init__(self):
        self.banco = BancoDeDados()

    @staticmethod
    def confirmar_preenchimento(pesquisa: str) -> str:
        if pesquisa == 'Insira o contratado ou CNPJ.' or not pesquisa:
            pesquisa = ''
        else:
            pesquisa = pesquisa

        return pesquisa

    def pesquisar(self, pesquisa: str) -> list:
        pesquisa = self.confirmar_preenchimento(pesquisa)
        if ValidadorDeCNPJ.valida_cnpj(pesquisa):
            return self.banco.pesquisar_por_cnpj(pesquisa)
        else:
            return self.banco.pesquisar_por_contratado(pesquisa)

    def pesquisa_completa(self, pesquisa: str) -> list:
        pesquisa = self.confirmar_preenchimento(pesquisa)
        if ValidadorDeCNPJ.valida_cnpj(pesquisa):
            return self.banco.relatorio_por_cnpj(pesquisa)
        else:
            return self.banco.relatorio_por_contratado(pesquisa)
