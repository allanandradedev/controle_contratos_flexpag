import sqlite3
import pandas as pd


class SQLiteDatabase:

    def __init__(self):
        self.__conexao = sqlite3.connect('Contracts.db')
        self.initiate_db()

    @property
    def connect(self):
        if not self.__conexao:
            self.__conexao = sqlite3.connect('Contracts.db')
        return self.__conexao

    def initiate_db(self):
        cursor = self.__conexao.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS contratos(
            id INTEGER PRIMARY KEY NOT NULL,
            contratado VARCHAR(255) NOT NULL,
            cnpj char(18) NOT NULL,
            tipo_contrato VARCHAR(255) NOT NULL,
            area_gestora VARCHAR(255) NOT NULL,
            descricao_contrato VARCHAR(255) NOT NULL,
            inicio_vigencia DATE NOT NULL,
            data_vencimento DATE NOT NULL,
            duracao_contrato VARCHAR(255) NOT NULL,
            situacao VARCHAR(255) NOT NULL,
            observacoes VARCHAR(255)                
        );
        ''')

    def update_list(self):
        self.__conexao.cursor().execute('''
            SELECT * FROM contratos
            ORDER BY data_vencimento;
        ''')

    def search_by_hired(self, hired):
        self.__conexao.cursor().execute(f'''
            SELECT * FROM contratos
                WHERE contratado LIKE '%{hired}%';
        ''')

    def search_by_cnpj(self, cnpj):
        self.__conexao.cursor().execute(f'''
                    SELECT * FROM contratos
                        WHERE cnpj = {cnpj};
                ''')

    def new_contract(self,
                     contratado,
                     cnpj,
                     tipo_contrato,
                     area_gestora,
                     descricao_contrato,
                     inicio_vigencia,
                     data_vencimento,
                     situacao,
                     observacoes):
        duracao_contrato = inicio_vigencia - data_vencimento
        self.__conexao.cursor().execute(f'''
            INSERT INTO contratos(contratado,
                                  cnpj,
                                  tipo_contrato,
                                  area_gestora,
                                  descricao_contrato,
                                  inicio_vigencia,
                                  data_vencimento,
                                  duracao_contrato,
                                  situacao,
                                  observacoes) 
                          VALUES ('{contratado}',
                                  '{cnpj}',
                                  '{tipo_contrato}',
                                  '{area_gestora}',
                                  '{descricao_contrato}',
                                  '{inicio_vigencia}',
                                  '{data_vencimento}',
                                  '{duracao_contrato}'
                                  '{situacao}',
                                  '{observacoes}'
                                  );
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
                      observacoes):
        duracao_contrato = inicio_vigencia - data_vencimento

        self.__conexao.cursor().execute(f'''
            UPDATE contratos
                SET 
                    contratado = {contratado},
                    cnpj = {cnpj},
                    tipo_contrato = {tipo_contrato},
                    area_gestora = {area_gestora},
                    descricao_contrato = {descricao_contrato},
                    inicio_vigencia = {inicio_vigencia},
                    data_vencimento = {data_vencimento},
                    duracao_contrato = {duracao_contrato},
                    situacao = {situacao},
                    observacoes = {observacoes}    
                WHERE
                    id = {id};
        ''')

    def renovate_contract(self, id, new_end_date):
        self.__conexao.cursor().execute(f'''
                    UPDATE contratos
                        SET 
                            data_vencimento = {new_end_date},
                        WHERE
                            id = {id};
                ''')

    def delete_contract(self, id):
        self.__conexao.cursor().execute(f'''
                            DELETE FROM contratos
                                WHERE
                                    id = {id};
                        ''')


if __name__ == '__main__':
    banco = SQLiteDatabase()
