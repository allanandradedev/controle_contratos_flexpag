from module.database import *
import xlsxwriter


class ReportGenerator(SQLiteDatabase):
    def __init__(self):
        super().__init__()

    def search_by_input(self, value):
        if Validations.validate_cnpj(value):
            return self.search_by_cnpj(value)
        else:
            return self.search_by_hired(value)

    def search_by_cnpj(self, cnpj):
        cursor = self.__conexao.cursor()
        cursor.execute(f'''
                            SELECT * FROM contratos
                                WHERE cnpj == {cnpj}
                                    ORDER BY id;
                        ''')
        return cursor.fetchall()

    def search_by_hired(self, hired):
        cursor = self.__conexao.cursor()
        cursor.execute(f'''
                    SELECT * FROM contratos
                        WHERE contratado LIKE '{hired}%'
                            ORDER BY id;
                ''')

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
        data = self.search_by_input(value)
        self.model(path, data)
