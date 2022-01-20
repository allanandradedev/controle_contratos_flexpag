from tkinter import Toplevel, Canvas, PhotoImage, Button, Entry, StringVar, messagebox
from views.placeholderEntry import PlaceHolder
from controller.copiaDestinoParaCampo import CopiaDestinoParaEntry
from controller.renovarContrato import RenovaContrato

global title_field_image
global entry_field_image
global observations_image
global renovate_button_image
global path_picker_img


class JanelaRenovacao:

    def __init__(self, master: vars, id_contrato: int):

        global title_field_image
        global entry_field_image
        global observations_image
        global renovate_button_image
        global path_picker_img

        self.master = master
        self.id_contrato = id_contrato

        x_position = self.master.winfo_x()+270
        y_position = self.master.winfo_y()+140

        self.window = Toplevel()

        self.window.geometry(f"630x394+{x_position}+{y_position}")
        self.window.configure(bg="#FFFFFF")
        self.window.iconbitmap('assets\icone_flexpag.ico')
        self.window.title('Renovar Contrato')

        canvas = Canvas(
            self.window,
            bg="#FFFFFF",
            height=394,
            width=630,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        canvas.place(x=0, y=0)
        title_field_image = PhotoImage(
            file="assets\\rs_title_field_image.png")
        canvas.create_image(
            315.0,
            61.0,
            image=title_field_image
        )

        entry_field_image = PhotoImage(
            file="assets\\rs_entry_field_img.png")
        canvas.create_image(
            315.5,
            118.5,
            image=entry_field_image
        )
        end_date = PlaceHolder(
            master=self.window,
            placeholder='*Nova data de vigência.',
            bd=0,
            default_fg_color='#2B2B2B',
            bg="#EFEFEF",
            highlightthickness=0
        )
        end_date.place(
            x=69.0,
            y=99.0,
            width=493.0,
            height=37.0
        )

        canvas.create_image(
            314.5,
            167.5,
            image=entry_field_image
        )

        attachment_text = StringVar()
        attachment_text.set('*Clique no ícone para escolher o arquivo.')

        attachment = Entry(
            master=self.window,
            fg='gray',
            bd=0,
            bg="#EFEFEF",
            textvariable=attachment_text,
            font=('Roboto', 11),
            state='disabled',
            highlightthickness=0
        )
        attachment.place(
            x=68.0,
            y=148.0,
            width=493.0,
            height=37.0
        )

        path_picker_img = PhotoImage(file="assets\\path_picker.png")

        path_picker_button = Button(
            master=self.window,
            image=path_picker_img,
            text='',
            compound='center',
            fg='white',
            borderwidth=0,
            highlightthickness=0,
            command=lambda: CopiaDestinoParaEntry().copiar(self.window, attachment_text),
            relief='flat')

        path_picker_button.place(
            x=529.0, y=151.5,
            width=30,
            height=30)

        observations_image = PhotoImage(
            file="assets\\rs_observation_field_img.png")
        canvas.create_image(
            315.5,
            238.0,
            image=observations_image
        )

        observations_field = PlaceHolder(
            master=self.window,
            placeholder='Observações adicionais.',
            bd=0,
            default_fg_color='#2B2B2B',
            bg="#EFEFEF",
            highlightthickness=0
        )
        observations_field.place(
            x=69.0,
            y=197.0,
            width=493.0,
            height=80.0
        )

        renovate_button_image = PhotoImage(
            file="assets\\rs_renovate_button_img.png")
        renovate_button = Button(
            master=self.window,
            image=renovate_button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.renovar_contrato(self.id_contrato, end_date.get(), attachment.get()),
            relief="flat"
        )
        renovate_button.place(
            x=164.0,
            y=295.0,
            width=303.0,
            height=59.01454162597656
        )

        self.window.resizable(False, False)
        self.window.mainloop()

    def renovar_contrato(self, id_contrato, data_vencimento, anexo):
        campos = [
            data_vencimento,
            anexo
        ]

        placeholders = [
            '*Nova data de vigência.',
            '*Clique no ícone para escolher o arquivo.',
        ]

        for campo in campos:
            if not campo or campo in placeholders:
                messagebox.showinfo('Campos Vazios', 'Preencha todos os campos e tente novamente.')
                break
            else:
                pass

        opcao = messagebox.askyesno('Tem certeza', 'Deseja tornar a alteração permanente?')
        if opcao:
            RenovaContrato().renovar(id_contrato, data_vencimento, anexo)
            messagebox.showinfo('Sucesso', 'Contrato renovado.')
            self.window.destroy()
            self.master.focus_force()
        else:
            self.window.focus_force()
