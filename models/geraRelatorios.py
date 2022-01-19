from xlsxwriter import Workbook


class GeradorDeRelatorios:

    # Gera um relatório em excel baseado nos dados que recebe.
    @staticmethod
    def gerar_relatorio(destino: str, dados: list) -> None:
        arquivo = Workbook(f'{destino}\\Controle de Contratos.xlsx')
        planilha = arquivo.add_worksheet()

        dados = dados
        if len(dados) > 0:
            ultima_linha = len(dados)+1
        else:
            ultima_linha = 2

        planilha.set_column('A:L', 20)
        planilha.add_table(f'A1:L{ultima_linha}',
                           {'data': dados,
                            'columns': [{'header': 'Id'},
                                         {'header': 'Contratado'},
                                         {'header': 'CNPJ'},
                                         {'header': 'Tipo de Contrato'},
                                         {'header': 'Área Gestora'},
                                         {'header': 'Descricao do Contrato'},
                                         {'header': 'Início da Vigência'},
                                         {'header': 'Data de Vencimento'},
                                         {'header': 'Duracão do Contrato'},
                                         {'header': 'Situação'},
                                         {'header': 'Observações'},
                                         {'header': 'Renovado?'}
                                         ]})
        arquivo.close()
