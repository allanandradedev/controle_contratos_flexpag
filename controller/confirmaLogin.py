from models.criptografaSenhas import Criptografia
from models.validaLogin import ValidadorDeLogin


class ConfirmaLogin:

    @staticmethod
    def confirma_login(usuario: str, senha: str) -> int:
        usuario = usuario
        senha = Criptografia.criptografa_senha(senha)
        confirmacao = ValidadorDeLogin().valida_usuario_e_senha(usuario, senha)
        return confirmacao
