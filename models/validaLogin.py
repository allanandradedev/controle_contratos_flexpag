from models.criptografaSenhas import Criptografia
from models.gerenciaBanco import BancoDeDados


class ValidadorDeLogin:

    criptografia = Criptografia()
    banco = BancoDeDados()

    def valida_usuario_e_senha(self, usuario: str, senha: str) -> int:
        if len(self.banco.pesquisar_usuario(usuario)) > 0:
            usuario = self.banco.pesquisar_usuario(usuario)
            if self.criptografia.checa_senha(usuario[1], senha):
                return 200
            else:
                return 500
        else:
            return 500