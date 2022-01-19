from tkinter import Menu, FLAT, messagebox
from views.janelaRenovacao import JanelaRenovacao
from controller.confirmaExclusao import ConfirmaExclusao


class PopUpMenu:
    def __init__(self, master, event, id_contrato):
        self.master = master
        self.id_contrato = id_contrato
        popup_menu = Menu(master,
                          tearoff=False,
                          bg='#FFFFFF',
                          font=('Roboto', 11),
                          bd=0,
                          activeborderwidth=0,
                          fg='#2B2B2B',
                          relief=FLAT)
        popup_menu.add_command(label='Renovar Contrato', command=lambda: JanelaRenovacao(self.master, self.id_contrato))
        popup_menu.add_separator()
        popup_menu.add_command(label='Excluir Contrato', command=lambda: self.confirma_exclusao(popup_menu,
                                                                                                self.id_contrato))
        popup_menu.tk_popup(event.x_root, event.y_root)

    def confirma_exclusao(self, master, id_contrato):
        opcao = messagebox.askyesno('Tem certeza', 'Você está prestes a excluir um contrato e os anexos ligados a ele,'
                                                   'você tem certeza? Esta ação não podera ser desfeita.')
        if opcao:
            ConfirmaExclusao().confirmar_exclusao(id_contrato)
            messagebox.showinfo('Sucesso', 'O Contrato e todos os seus anexos foram excluído com sucesso.')
            master.destroy()
            self.master.focus_force()
        else:
            master.focus_force()
