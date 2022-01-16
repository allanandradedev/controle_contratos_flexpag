from tkinter import messagebox
from module.validationService import *
from view.appInterfaceView import *


def add_contract_page_validations(hired_field,
                                  cnpj_field,
                                  contract_type_field,
                                  manager_area_field,
                                  contract_description_field,
                                  start_date_field,
                                  end_date_field,
                                  situation_field):
    fields = [
        hired_field,
        cnpj_field,
        contract_type_field,
        manager_area_field,
        contract_description_field,
        start_date_field,
        end_date_field,
        situation_field
    ]

    placeholders_list = [
        '*Nome do Contratado.',
        '*Insira o CNPJ sem as pontuações.',
        '*Tipo de Contrato.',
        '*Área Gestora.',
        '*Descrição do Contrato.',
        '*Início da Vigência.',
        '*Data de Vencimento.',
        '*Situação do Contrato.',
    ]

    for field in fields:
        if field not in placeholders_list:
            return 200
        else:
            return 500



