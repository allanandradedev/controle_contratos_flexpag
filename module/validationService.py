import validate_docbr as docbr
import datetime as dt


class Validations:
    def __init__(self):
        pass

    @staticmethod
    def validate_cnpj(value: str):
        if docbr.CNPJ().validate(value):
            return docbr.CNPJ().mask(value)
        else:
            return False

    @staticmethod
    def validate_dates(date):
        return dt.datetime.strptime(date,'%d/%m/%Y')

