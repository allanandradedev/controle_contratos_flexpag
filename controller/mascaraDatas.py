class MascaraDatas:
    @staticmethod
    def mascarar_datas(data) -> str:
        ano = data[:4]
        print(ano)
        mes = data[5:7]
        print(mes)
        dia = data[8:]
        print(dia)
        data = '/'.join([dia, mes, ano])
        return data