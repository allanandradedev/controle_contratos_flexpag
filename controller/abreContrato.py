from models.gerenciaAnexos import GerenciadorDeAnexos


class AbreAnexos:
    @staticmethod
    def abre_anexo(id_contrato: int) -> None:
        GerenciadorDeAnexos().abrir_anexo(id_contrato)
