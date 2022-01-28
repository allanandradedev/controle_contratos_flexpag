class FormatacoesIO:

    @staticmethod
    def formata_data_input(data) -> str:
        dia = data[:2]
        mes = data[3:5]
        ano = data[6:]
        data = '-'.join([ano, mes, dia])
        return data

    @staticmethod
    def formata_data_output(data) -> str:
        ano = data[:4]
        mes = data[5:7]
        dia = data[8:]
        data = '/'.join([dia, mes, ano])
        return data

