from models.criptografaSenhas import Criptografia
from models.gerenciaBanco import BancoDeDados


class ValidadorDeLogin:

    criptografia = Criptografia()
    banco = BancoDeDados()

    def valida_usuario_e_senha(self, usuario: str, senha: bytes) -> int:
        usuario = usuario
        senha = self.criptografia.descriptografa_senha(senha)
        usuario_e_senha = (usuario, senha)
        tabela_de_usuarios = self.banco.retorna_usuarios_e_senhas()

        if usuario_e_senha in tabela_de_usuarios:
            return 200
        else:
            return 500
