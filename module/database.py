import sqlite3
import string

from module.validationService import *
from utils.datesUtil import *

class SQLiteDatabase:
    # -------------------- INITIALIZATION METHODS ------------------------------------------
    def __init__(self):
        self.__conexao = sqlite3.connect('module\\Contracts.db')
        self.initiate_db()

    def connection(self):
        return self.__conexao

    @property
    def connect(self):
        if not self.__conexao:
            self.__conexao = sqlite3.connect('module\\Contracts.db')
        return self.__conexao

    def drop_table(self):
        self.__conexao.cursor().execute('DROP TABLE contratos;')

    def initiate_db(self):
        cursor = self.__conexao.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS contratos(
            id INTEGER PRIMARY KEY NOT NULL,
            contratado VARCHAR(255) NOT NULL,
            cnpj char(11) NOT NULL,
            tipo_contrato VARCHAR(255) NOT NULL,
            area_gestora VARCHAR(255) NOT NULL,
            descricao_contrato VARCHAR(255) NOT NULL,
            inicio_vigencia DATE NOT NULL,
            data_vencimento DATE NOT NULL,
            duracao_contrato VARCHAR(255) NOT NULL,
            situacao VARCHAR(255) NOT NULL,
            observacoes VARCHAR(255),
            renovado VARCHAR(255)              
        );
        ''')

    # ------------------------------------------------------------------------------

    # -------------------- SEARCH METHODS ------------------------------------------

    def update_list(self):
        cursor = self.__conexao.cursor()
        cursor.execute('''
            SELECT * FROM contratos
            ORDER BY data_vencimento;
        ''')
        print(cursor.fetchall())

    def search_by_input(self, value):
        if Validations.validate_cnpj(value):
            if '.' in value:
                value = ''.join([i for i in value if i not in string.punctuation])
            return self.search_by_cnpj(value)
        else:
            return self.search_by_hired(value)

    def search_by_hired(self, hired):
        cursor = self.__conexao.cursor()
        cursor.execute(f'''
            SELECT id, contratado, cnpj, inicio_vigencia, data_vencimento, situacao FROM contratos
                WHERE contratado LIKE '{hired}%'
                    ORDER BY strftime('%Y-%m-%d', data_vencimento);
        ''')
        return cursor.fetchall()

    def search_by_cnpj(self, cnpj):
        cursor = self.__conexao.cursor()
        cursor.execute(f'''
                    SELECT id, contratado, cnpj, inicio_vigencia, data_vencimento, situacao FROM contratos
                        WHERE cnpj == {cnpj}
                            ORDER BY strftime('%Y-%m-%d', data_vencimento);
                ''')
        return cursor.fetchall()

    # ------------------------------------------------------------------------------

    # -------------------- ADD, TRANSFORM AND EXCLUDE DATA METHODS -----------------

    def new_contract(self,
                     contratado,
                     cnpj,
                     tipo_contrato,
                     area_gestora,
                     descricao_contrato,
                     inicio_vigencia,
                     data_vencimento,
                     observacoes,
                     renovado='Não'):

        if Validations.validate_dates(data_vencimento) < TODAY:
            situacao = 'Vencido'
        else:
            situacao = 'Vigente'

        if observacoes == 'Observações adicionais.' or not observacoes:
            observacoes = None

        duracao_contrato = (abs(
                    Validations.validate_dates(inicio_vigencia) - Validations.validate_dates(data_vencimento)).days) + 1
        cursor = self.__conexao.cursor()
        cursor.execute(f'''
            INSERT INTO contratos(contratado,
                                  cnpj,
                                  tipo_contrato,
                                  area_gestora,
                                  descricao_contrato,
                                  inicio_vigencia,
                                  data_vencimento,
                                  duracao_contrato,
                                  situacao,
                                  observacoes,
                                  renovado) 
                          VALUES ('{contratado}',
                                  '{cnpj}',
                                  '{tipo_contrato}',
                                  '{area_gestora}',
                                  '{descricao_contrato}',
                                  '{inicio_vigencia}',
                                  '{data_vencimento}',
                                  '{duracao_contrato}',
                                  '{situacao}',
                                  '{observacoes}',
                                  '{renovado}');
        ''')

    def edit_contract(self,
                      id,
                      contratado,
                      cnpj,
                      tipo_contrato,
                      area_gestora,
                      descricao_contrato,
                      inicio_vigencia,
                      data_vencimento,
                      situacao,
                      observacoes = None):

        duracao_contrato = (abs(
            Validations.validate_dates(inicio_vigencia) - Validations.validate_dates(data_vencimento)).days) + 1

        self.__conexao.cursor().execute(f'''
            UPDATE contratos
                SET 
                    contratado = '{contratado}',
                    cnpj = '{cnpj}',
                    tipo_contrato = '{tipo_contrato}',
                    area_gestora = '{area_gestora}',
                    descricao_contrato = '{descricao_contrato}',
                    inicio_vigencia = '{inicio_vigencia}',
                    data_vencimento = '{data_vencimento}',
                    duracao_contrato = '{duracao_contrato}',
                    situacao = '{situacao}',
                    observacoes = '{observacoes}'    
                WHERE
                    id = '{id}';
        ''')

    def renovate_contract(self, id, new_end_date):
        cursor = self.__conexao.cursor()

        cursor.execute(f'''
            SELECT inicio_vigencia FROM contratos
                WHERE id = {id}
        ''')
        inicio_vigencia = cursor.fetchone()

        duracao_contrato = (abs(
            Validations.validate_dates(str(inicio_vigencia[0])) - Validations.validate_dates(new_end_date)).days) + 1

        self.__conexao.cursor().execute(f'''
                    UPDATE contratos
                        SET
                            data_vencimento = '{new_end_date}',
                            duracao_contrato = '{duracao_contrato}',
                            renovado = 'Sim'
                        WHERE
                            id = {id};
                ''')

    def delete_contract(self, id):
        self.__conexao.cursor().execute(f'''
                            DELETE FROM contratos
                                WHERE
                                    id = {id};
                        ''')

    # ------------------------------------------------------------------------------

    def commit(self):
        self.__conexao.commit()

    def get_last_id(self):
        cursor = self.__conexao.cursor()
        cursor.execute('SELECT last_insert_rowid()')
        id = cursor.fetchall()
        id = id[0][0]
        return id

if __name__ == '__main__':
    banco = SQLiteDatabase()
    banco.new_contract('Companie Update', '12345678911111', 'teste', 'teste', 'teste', '15/01/2021', '15/01/2025',
                       'teste')
    banco.commit()