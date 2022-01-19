from views.selecaoArquivo import Selecoes
from models.geraRelatorios import GeradorDeRelatorios
from controller.confirmaPesquisa import ConfirmaPesquisa


class ChamaGeraRelatorios:
    @staticmethod
    def gerar_relatorio(dados: str) -> None:
        dados = ConfirmaPesquisa().pesquisa_completa(dados)
        destino = Selecoes.seleciona_pasta()
        GeradorDeRelatorios.gerar_relatorio(destino, dados)