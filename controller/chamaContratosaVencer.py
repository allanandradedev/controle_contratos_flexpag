from models.gerenciaBanco import BancoDeDados


class ContratosVencendo:
    def contratos_a_vencer(self):
        contratos = BancoDeDados().pesquisar_por_data()
        return f'Existem {len(contratos)} contratos à vencer nos próximos 30 dias.'
