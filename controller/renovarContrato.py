from models.gerenciaAnexos import GerenciadorDeAnexos
from models.gerenciaBanco import BancoDeDados
from controller.confirmaNovoContrato import ConfirmaNovoContrato


class RenovaContrato:

    banco = BancoDeDados()

    def renovar(self, id_contrato: int, data_vencimento: str, novo_anexo: str) -> int:
            contrato = self.banco.pesquisar_por_id(id_contrato)
            inicio_vigencia = contrato[0][6]
            duracao = ConfirmaNovoContrato.retorna_duracao_contrato(inicio_vigencia, data_vencimento)
            situacao = ConfirmaNovoContrato.retorna_situacao_contrato(data_vencimento)
            self.banco.renovar_contrato(id_contrato, data_vencimento, duracao, situacao)
            self.banco.commit()
            GerenciadorDeAnexos().anexar_contrato(novo_anexo, id_contrato)
