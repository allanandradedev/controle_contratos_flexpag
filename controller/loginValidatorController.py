from tkinter import messagebox
from utils.registeredUsersUtil import *
from view.appInterfaceView import *


def login_page_validations(login_field, password_field):
    login_info = {
        login_field.get(): password_field.get()
    }
    if login_field.get() == 'Insira seu nome de usuário':
        messagebox.showinfo(title='Empty fields', message='Login em falta, por favor preencha o campo e'
                                                          ' tente novamente')
        return 500
    elif password_field.get() == 'Insira sua senha':
        messagebox.showinfo(title='Empty fields', message='Senha em falta, por favor preencha o campo e'
                                                          ' tente novamente')
        return 500
    elif not login_field.get():
        messagebox.showinfo(title='Empty fields', message='Login em falta, por favor preencha o campo e'
                                                          ' tente novamente')
        return 500
    elif not password_field.get():
        messagebox.showinfo(title='Empty fields', message='Senha em falta, por favor preencha o campo e'
                                                          ' tente novamente')
        return 500
    elif login_field.get() not in USERS_LIST:
        messagebox.showinfo(title='User not found', message='Usuário não cadastrado, contate o '
                                                            'administrador do sistema')
        return 404
    elif USERS_LIST[login_field.get()] == '':
        messagebox.showinfo(title='Password not found', message='Senha não cadastrada, contate o '
                                                                'administrador do sistema')
        return 404
    else:
        if login_info[login_field.get()] == USERS_LIST[login_field.get()]:
            return 200
        else:
            messagebox.showinfo(title='Wrong Password', message='Senha Incorreta.')
            return 500
