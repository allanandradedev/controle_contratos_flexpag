from models.gerenciaBanco import BancoDeDados
import shutil


class ConfirmaExclusao:
    banco = BancoDeDados()

    def confirmar_exclusao(self, id_contrato: int):
        self.banco.deletar_contrato(id_contrato)
        self.banco.commit()
        shutil.rmtree(f'contracts\\{id_contrato}')
        return 200
