from module.database import *
import xlsxwriter


class ReportGenerator:
    def __init__(self):
        self.__database = SQLiteDatabase()
        self.__connection = self.__database.connection()

    def model(self, path, search):

        workbook = xlsxwriter.Workbook(path)
        worksheet = workbook.add_worksheet()

        data = search
        last_line = len(data)+1
        worksheet.set_column('A:L', 20)

        worksheet.add_table(f'A1:L{last_line}',
                            {'data': data,
                             'columns': [{'header': 'Id contrato'},
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

        workbook.close()

    def generate_report(self, value, path):
        data = self.__database.search_by_input(value)
        self.model(path, data)


if __name__ == '__main__':
    ReportGenerator().generate_report('S','teste.xlsx')