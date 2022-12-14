import sqlite3


class BancoDeDados:

    def __init__(self):
        self.conexao = sqlite3.connect('utils\\Contracts.db')
        self.cursor = self.conexao.cursor()
        self.iniciar_banco()

    # Fecha a conexão com o banco de dados
    def desconectar(self) -> None:
        self.conexao.close()

    # Inicia o banco de dados, criando as tabelas necessárias para o funcionamento da aplicação

    def iniciar_banco(self) -> None:
        self.cursor.execute('''
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

        self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS users(
                    usuario varchar(255) PRIMARY KEY,
                    senha varchar(255) NOT NULL  
                );
                ''')

        self.cursor.execute('''
            DELETE FROM users;
        ''')

        self.cursor.execute('''
            INSERT INTO users VALUES(
            'socorro.cordeiro', 
            'pbkdf2:sha256:260000$AkqR38MGntnNa5Q4$07f18e176b2c0275d8de54671eea15fe896ac5574b7702261193045f3d201bee');
        ''')

        self.commit()

    # Realiza uma pesquisa na tabela contratos utilizando o contratado como parâmetro
    def pesquisar_por_contratado(self, contratado: str) -> list:
        self.cursor.execute(f'''
            SELECT id, contratado, cnpj, tipo_contrato, data_vencimento, situacao FROM contratos
                WHERE contratado LIKE '{contratado}%'
                    ORDER BY strftime('%s',data_vencimento);
        ''')
        return self.cursor.fetchall()

    # Realiza uma pesquisa na tabela contratos utilizando o CNPJ como parâmetro
    def pesquisar_por_cnpj(self, cnpj: str) -> list:

        self.cursor.execute(f'''
                            SELECT id, contratado, cnpj, tipo_contrato, data_vencimento, situacao FROM contratos
                                WHERE cnpj == {cnpj}
                                    ORDER BY strftime('%s',data_vencimento);
                        ''')
        return self.cursor.fetchall()

    # Gera o relatório completo utilizando o CNPJ como parâmetro
    def relatorio_por_cnpj(self, cnpj: str) -> list:
        self.cursor.execute(f'''
                            SELECT * FROM contratos
                                WHERE cnpj == {cnpj}
                                    ORDER BY strftime('%s',data_vencimento);
                        ''')
        return self.cursor.fetchall()

    # Retorna um contrato utilizando o ID como parâmetro
    def pesquisar_por_id(self, id_contrato: int) -> list:
        self.cursor.execute(f'''
                                    SELECT * FROM contratos
                                        WHERE id == {id_contrato}
                                            ORDER BY strftime('%s',data_vencimento);
                                ''')
        return self.cursor.fetchall()

    # Gera o relatório completo utilizando o nome do contratado como parâmetro
    def relatorio_por_contratado(self, contratado: str) -> list:
        self.cursor.execute(f'''
                            SELECT * FROM contratos
                                WHERE contratado LIKE '{contratado}%'
                                    ORDER BY strftime('%s',data_vencimento);
                        ''')
        return self.cursor.fetchall()

    def pesquisar_por_data(self) -> list:
        self.cursor.execute(f'''
            SELECT * FROM contratos
                WHERE data_vencimento
                    BETWEEN DATE('now') AND DATE('now', '+30 Day');
                            ''')
        return self.cursor.fetchall()

    # Realiza a inserção de um novo registro na tabela contratos.
    def novo_contrato(self,
                      contratado: str,
                      cnpj: int,
                      tipo_contrato: str,
                      area_gestora: str,
                      descricao_contrato: str,
                      inicio_vigencia: str,
                      data_vencimento: str,
                      duracao_contrato: int,
                      situacao: str,
                      observacoes: str,
                      renovado: str = 'Não') -> None:

        self.cursor.execute(f'''
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

    # Realiza a renovação de um contrato na tabela contratos, setando uma nova data de vencimento e mudando o status
    # para renovado, baseado no id
    def renovar_contrato(self,
                         id_contrato: int,
                         data_vencimento: str,
                         duracao_contrato: int,
                         situacao: str) -> None:
        self.cursor.execute(f'''
                            UPDATE contratos
                                SET
                                    data_vencimento = '{data_vencimento}',
                                    duracao_contrato = '{duracao_contrato}',
                                    situacao = '{situacao}',
                                    renovado = 'Sim'
                                WHERE
                                    id = {id_contrato};
                        ''')

    # Realiza a exclusão de um registro na tabela contratos, baseado no id
    def deletar_contrato(self, id_contrato: int) -> None:
        self.cursor.execute(f'''
                            DELETE FROM contratos
                                WHERE
                                    id = {id_contrato};
                        ''')

    # Torna o que foi executado pelo cursor permanente.
    def commit(self) -> None:
        self.conexao.commit()

    # Retorna o último registro realizado na tabela contratos.
    def ver_ultimo_id(self) -> int:
        self.cursor.execute('''
            SELECT last_insert_rowid();
        ''')
        registro = self.cursor.fetchall()
        ultimo_id = registro[0][0]
        return ultimo_id

    def adicionar_usuario(self, login: str, senha: str):
        self.cursor.execute(f'''
            INSERT INTO users VALUES(
                                    '{login}',
                                    '{senha}'
                                    )
        ''')

    def retorna_usuarios_e_senhas(self) -> list:
        self.cursor.execute('''
            SELECT * FROM users;
            ''')
        return self.cursor.fetchall()

    def pesquisar_usuario(self, usuario: str) -> list:
        self.cursor.execute(f'''
            SELECT * FROM users
                WHERE usuario = '{usuario}';
        ''')
        return self.cursor.fetchone()

    def atualiza_situacao_contratos(self, id_contrato: int, situacao: str) -> None:
        self.cursor.execute(f'''
                    UPDATE contratos
                        SET
                            situacao = '{situacao}'
                        WHERE
                            id = '{id_contrato}'
                ''')
        self.conexao.commit()
