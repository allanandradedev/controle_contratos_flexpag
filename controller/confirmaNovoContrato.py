from models.validaCNPJ import ValidadorDeCNPJ
from models.gerenciaBanco import BancoDeDados
from models.gerenciaAnexos import GerenciadorDeAnexos
from datetime import datetime, timedelta
from tkinter import messagebox
import re

from controller.formatacoesIO import FormatacoesIO


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
        self.cnpj = re.sub('[^A-Za-z0-9]+', '', cnpj)
        self.tipo_contrato = tipo_contrato
        self.area_gestora = area_gestora
        self.descricao_contrato = descricao_contrato
        self.inicio_vigencia = FormatacoesIO.formata_data_input(inicio_vigencia)
        self.data_vencimento = FormatacoesIO.formata_data_input(data_vencimento)
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
            '*Insira um CNPJ válido.',
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

    def verifica_datas(self) -> int:
        if datetime.strptime(self.inicio_vigencia, '%Y-%m-%d') >= datetime.strptime(self.data_vencimento, '%Y-%m-%d'):
            return 500
        else:
            return 200

    @staticmethod
    def retorna_duracao_contrato(inicio_vigencia: str, data_vencimento: str) -> int:
        data_inicio = datetime.strptime(inicio_vigencia, '%Y-%m-%d')
        data_fim = datetime.strptime(data_vencimento, '%Y-%m-%d')
        duracao = abs(data_inicio - data_fim).days + 1
        return duracao

    @staticmethod
    def retorna_situacao_contrato(data_vencimento: str) -> str:
        data_fim = datetime.strptime(data_vencimento, '%Y-%m-%d')
        dias_para_vencer = data_fim - datetime.today()

        if data_fim < datetime.today():
            situacao = 'Vencido'

        elif abs(dias_para_vencer.days) < 30:
            situacao = 'À Vencer'

        else:
            situacao = 'Vigente'

        return situacao

    def confirmar_inputs(self) -> int:
        if self.verificar_preenchimento() == 500:
            messagebox.showinfo('Campos Vazios', 'Preencha todos os campos corretamente para continuar.')
        elif self.verifica_datas() == 500:
            messagebox.showinfo('Preenchimento incorreto', 'A data de início da vigência é igual ou superior a data de'
                                                           ' vencimento do contrato, verifique e tente novamente.')
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
                                         self.inicio_vigencia,
                                         self.data_vencimento,
                                         duracao,
                                         situacao,
                                         self.observacoes,
                                         self.renovado)
                self.banco.commit()
                GerenciadorDeAnexos().anexar_contrato(self.anexo, self.banco.ver_ultimo_id())
                return 200
            else:
                return 500
