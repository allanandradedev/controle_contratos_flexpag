from models.validaCNPJ import ValidadorDeCNPJ
from models.gerenciaBanco import BancoDeDados
from models.gerenciaAnexos import GerenciadorDeAnexos
from datetime import datetime
from tkinter import messagebox


class ConfirmaNovoContrato:
    def __init__(self,
                 contratado: str,
                 cnpj: int,
                 tipo_contrato: str,
                 area_gestora: str,
                 descricao_contrato: str,
                 inicio_vigencia: str,
                 data_vencimento: str,
                 anexo: str,
                 observacoes: str,
                 renovado: str = 'Não'
                 ):
        self.contratado = contratado
        self.cnpj = cnpj
        self.tipo_contrato = tipo_contrato
        self.area_gestora = area_gestora
        self.descricao_contrato = descricao_contrato
        self.inicio_vigencia = inicio_vigencia
        self.data_vencimento = data_vencimento
        self.anexo = anexo
        self.observacoes = observacoes
        self.renovado = renovado
        self.banco = BancoDeDados()

    def verificar_preenchimento(self) -> int:
        campos = [
            self.contratado,
            self.cnpj,
            self.tipo_contrato,
            self.area_gestora,
            self.descricao_contrato,
            self.inicio_vigencia,
            self.data_vencimento,
            self.anexo,
            self.observacoes,
            self.renovado
        ]

        placeholders = [
            '*Nome do Contratado.',
            '*Insira o CNPJ sem as pontuações.',
            '*Tipo de Contrato.',
            '*Área Gestora.',
            '*Descrição do Contrato.',
            '*Início da Vigência.',
            '*Data de Vencimento.',
            '*Situação do Contrato.',
            '*Clique no ícone para escolher o arquivo.'
        ]

        for campo in campos:
            if not campo or campo in placeholders:
                return 500
            elif not ValidadorDeCNPJ().valida_cnpj(str(self.cnpj)):
                return 404
            else:
                return 200

    def formatar_inputs(self) -> None:
        self.contratado = self.contratado.title()
        self.tipo_contrato = self.tipo_contrato.title()
        self.area_gestora = self.area_gestora.title()
        self.descricao_contrato = self.descricao_contrato.title()
        self.observacoes = self.observacoes.title()
        self.renovado = self.renovado.title()

    def formatar_datas(self, data) -> str:
        dia = data[:2]
        mes = data[3:5]
        ano = data[6:]
        data = '-'.join([ano, mes, dia])
        return data

    @staticmethod
    def retorna_duracao_contrato(inicio_vigencia: str, data_vencimento: str) -> int:
        data_inicio = datetime.strptime(inicio_vigencia, '%d/%m/%Y')
        data_fim = datetime.strptime(data_vencimento, '%d/%m/%Y')
        duracao = abs(data_inicio - data_fim).days + 1
        return duracao

    @staticmethod
    def retorna_situacao_contrato(data_vencimento: str) -> str:
        data_fim = datetime.strptime(data_vencimento, '%d/%m/%Y')

        if data_fim < datetime.today():
            situacao = 'Vencido'
        else:
            situacao = 'Vigente'
        return situacao

    def confirmar_inputs(self) -> int:
        if self.verificar_preenchimento() == 500:
            messagebox.showinfo('Campos Vazios', 'Preencha todos os campos corretamente para continuar.')
        elif self.verificar_preenchimento() == 404:
            messagebox.showinfo(title='CNPJ Inválido', message='Verifique o CNPJ e tente novamente.')
        else:
            self.formatar_inputs()
            duracao = self.retorna_duracao_contrato(self.inicio_vigencia, self.data_vencimento)
            situacao = self.retorna_situacao_contrato(self.data_vencimento)
            opcao = messagebox.askyesno('Tem certeza?', 'Deseja tornar a inserção permanente?')
            if opcao:
                self.banco.novo_contrato(self.contratado,
                                         self.cnpj,
                                         self.tipo_contrato,
                                         self.area_gestora,
                                         self.descricao_contrato,
                                         self.formatar_datas(self.inicio_vigencia),
                                         self.formatar_datas(self.data_vencimento),
                                         duracao,
                                         situacao,
                                         self.observacoes,
                                         situacao)
                self.banco.commit()
                GerenciadorDeAnexos().anexar_contrato(self.anexo, self.banco.ver_ultimo_id())
                return 200
            else:
                return 500

