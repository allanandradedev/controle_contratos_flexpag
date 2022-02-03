from models.gerenciaBanco import BancoDeDados
from controller.confirmaNovoContrato import ConfirmaNovoContrato


class AtualizaContratos:
    @staticmethod
    def atualizar_situacao_contratos() -> None:
        contratos = BancoDeDados().pesquisar_por_contratado('')

        for contrato in contratos:
            id_contrato = contrato[0]
            vencimento_contrato = contrato[4]
            situacao_contrato = ConfirmaNovoContrato.retorna_situacao_contrato(vencimento_contrato)
            BancoDeDados().atualiza_situacao_contratos(id_contrato, situacao_contrato)

