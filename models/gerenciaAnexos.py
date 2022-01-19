from subprocess import Popen
from shutil import copy
import os


class GerenciadorDeAnexos:
    contratos = 'contracts'

    # Anexa o contrato ao registro adicionado no banco de dados.
    def anexar_contrato(self, origem: str, id_contrato: int) -> None:
        if os.path.isdir(f'{self.contratos}\\{id_contrato}'):
            contratos = os.listdir(f'{self.contratos}\\{id_contrato}')
            ultimo_contrato = contratos[-1]
            ponto = ultimo_contrato.find('.')
            valor_ultimo_contrato = ultimo_contrato[0:ponto]
            novo_contrato = int(valor_ultimo_contrato) + 1
            destino = f'{self.contratos}\\{id_contrato}\\{novo_contrato}.pdf'

        else:
            os.mkdir(f'{self.contratos}\\{id_contrato}')
            destino = f'{self.contratos}\\{id_contrato}\\1.pdf'

        copy(origem, destino)

    # Abre o contrato relacionado à um id registrado no banco de dados.
    def abrir_anexo(self, id_contrato: int) -> None:
        contratos = os.listdir(f'{self.contratos}\\{id_contrato}')
        for contrato in contratos:
            Popen(f'{self.contratos}\\{id_contrato}\\{contrato}', shell=True)
