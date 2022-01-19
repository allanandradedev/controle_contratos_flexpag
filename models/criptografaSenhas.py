from base64 import b64encode, b64decode


class Criptografia:
    # Criptografa a entrada da senha.
    @staticmethod
    def criptografa_senha(senha: str) -> bytes:
        senha = senha.encode("utf-8")
        senha_criptografada = b64encode(senha)
        return senha_criptografada

    # Descriptografa a entrada da senha.
    @staticmethod
    def descriptografa_senha(senha: bytes) -> str:
        senha_descriptografada = b64decode(senha)
        senha = senha_descriptografada.decode("utf-8")
        return senha
