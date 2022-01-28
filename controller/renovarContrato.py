import datetime
from tkinter import messagebox
from models.gerenciaAnexos import GerenciadorDeAnexos
from models.gerenciaBanco import BancoDeDados
from controller.confirmaNovoContrato import ConfirmaNovoContrato
from controller.formatacoesIO import FormatacoesIO


class RenovaContrato:

    banco = BancoDeDados()

    def renovar(self, id_contrato: int, data_vencimento: str, novo_anexo: str) -> int:
            contrato = self.banco.pesquisar_por_id(id_contrato)
            data_vencimento = FormatacoesIO.formata_data_input(data_vencimento)
            inicio_vigencia_banco = contrato[0][6]
            data_vencimento_banco = datetime.datetime.strptime(contrato[0][7], '%Y-%m-%d')
            data_vencimento_input = datetime.datetime.strptime(data_vencimento,
                                                               '%Y-%m-%d')

            if data_vencimento_banco > data_vencimento_input:
                messagebox.showinfo('Preenchimento incorreto',
                                    'A data de início da vigência é igual ou superior a data de'
                                    ' vencimento do contrato, verifique e tente novamente.')
                return 500
            else:
                opcao = messagebox.askyesno('Tem certeza', 'Deseja tornar a alteração permanente?')
                if opcao:
                    duracao = ConfirmaNovoContrato.retorna_duracao_contrato(inicio_vigencia_banco, data_vencimento)
                    situacao = ConfirmaNovoContrato.retorna_situacao_contrato(data_vencimento)
                    self.banco.renovar_contrato(id_contrato, data_vencimento, duracao, situacao)
                    self.banco.commit()
                    GerenciadorDeAnexos().anexar_contrato(novo_anexo, id_contrato)
                    return 200
                else:
                    return 500
