from werkzeug.security import generate_password_hash, check_password_hash


class Criptografia:
    # Criptografa a entrada da senha.
    @staticmethod
    def criptografa_senha(senha: str) -> str:
        senha_criptografada = generate_password_hash(senha)
        return senha_criptografada

    def checa_senha(self, senha_hash: str, senha) -> bool:
        confirmacao = check_password_hash(senha_hash, senha)
        return confirmacao
