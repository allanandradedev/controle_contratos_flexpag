from models.gerenciaBanco import BancoDeDados


class AtualizaLista:
    banco = BancoDeDados()

    def atualizar(self) -> list:
        dados = self.banco.atualizar_lista()
        return dados
