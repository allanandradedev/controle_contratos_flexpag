from tkinter import Toplevel, Canvas, PhotoImage, Label, StringVar, Button, Entry
from views.placeholderEntry import PlaceHolder
from controller.copiaDestinoParaCampo import CopiaDestinoParaEntry
from controller.confirmaNovoContrato import ConfirmaNovoContrato

global title_label_image
global entry_field_image
global date_field_image
global observations_image
global path_picker_img


class JanelaAddContrato:
    def __init__(self, master):
        global title_label_image
        global entry_field_image
        global date_field_image
        global observations_image
        global path_picker_img

        self.master = master
        x_position = self.master.winfo_x() + 280
        y_position = self.master.winfo_y() + 60

        self.window = Toplevel(self.master)

        self.window.geometry(f"615x636+{x_position}+{y_position}")
        self.window.configure(bg="#FFFFFF")
        self.window.title('Adicionar Contrato.')
        self.canvas = Canvas(
            self.window,
            bg="#FFFFFF",
            height=636,
            width=615,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)

        title_label_image = PhotoImage(
            file="assets\\ac_title_label_img.png")
        self.canvas.create_image(
            308.0,
            59.0,
            image=title_label_image
        )
        title_label = Label(
            master=self.window,
            text='Registro de Contrato',
            font=('Roboto', 20),
            fg='#005E9F',
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        title_label.place(
            x=117.0,
            y=37.0,
            width=382.0,
            height=42.0
        )

        entry_field_image = PhotoImage(
            file="assets\\ac_entry_field_image.png")

        self.canvas.create_image(
            308.5,
            117.5,
            image=entry_field_image
        )
        hired_entry = PlaceHolder(
            self.canvas,
            placeholder='*Nome do Contratado.',
            default_fg_color='#2B2B2B',
            color='gray',
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0
        )
        hired_entry.place(
            x=62.0,
            y=98.0,
            width=493.0,
            height=37.0
        )

        self.canvas.create_image(
            306.5,
            166.5,
            image=entry_field_image
        )
        cnpj_entry = PlaceHolder(
            self.canvas,
            placeholder='Insira o CNPJ sem as pontuações.',
            default_fg_color='#2B2B2B',
            color='gray',
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0
        )
        cnpj_entry.place(
            x=60.0,
            y=147.0,
            width=493.0,
            height=37.0
        )

        self.canvas.create_image(
            308.5,
            215.5,
            image=entry_field_image
        )
        contract_type = PlaceHolder(
            self.canvas,
            placeholder='*Tipo de Contrato.',
            default_fg_color='#2B2B2B',
            color='gray',
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0
        )
        contract_type.place(
            x=62.0,
            y=196.0,
            width=493.0,
            height=37.0
        )

        self.canvas.create_image(
            308.5,
            264.5,
            image=entry_field_image
        )
        manager_area = PlaceHolder(
            self.canvas,
            placeholder='*Área Gestora.',
            default_fg_color='#2B2B2B',
            color='gray',
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0
        )
        manager_area.place(
            x=62.0,
            y=245.0,
            width=493.0,
            height=37.0
        )

        self.canvas.create_image(
            308.5,
            313.5,
            image=entry_field_image
        )
        contract_description = PlaceHolder(
            self.canvas,
            placeholder='*Descrição do Contrato.',
            default_fg_color='#2B2B2B',
            color='gray',
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0
        )
        contract_description.place(
            x=62.0,
            y=294.0,
            width=493.0,
            height=37.0
        )

        date_field_image = PhotoImage(
            file="assets\\ac_date_field_img.png")

        self.canvas.create_image(
            170.0,
            362.5,
            image=date_field_image
        )
        initial_date_entry = PlaceHolder(
            self.canvas,
            placeholder='*Início da Vigência.',
            default_fg_color='#2B2B2B',
            color='gray',
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0
        )
        initial_date_entry.place(
            x=62.0,
            y=343.0,
            width=216.0,
            height=37.0
        )

        self.canvas.create_image(
            447.0,
            362.5,
            image=date_field_image
        )
        end_date_entry = PlaceHolder(
            self.canvas,
            placeholder='*Data de Vencimento.',
            default_fg_color='#2B2B2B',
            color='gray',
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0
        )
        end_date_entry.place(
            x=339.0,
            y=343.0,
            width=216.0,
            height=37.0
        )

        self.canvas.create_image(
            308.5,
            411.5,
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
            x=62.0,
            y=392.0,
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
            command=lambda: CopiaDestinoParaEntry.copiar(self.window, attachment_text),
            relief='flat')

        path_picker_button.place(
            x=526.0, y=395.5,
            width=30,
            height=30)

        observations_image = PhotoImage(
            file="assets\\ac_observations_image.png")
        self.canvas.create_image(
            306.5,
            482.0,
            image=observations_image
        )
        observations = PlaceHolder(
            self.canvas,
            placeholder='Observações adicionais.',
            default_fg_color='#2B2B2B',
            color='gray',
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0
        )
        observations.place(
            x=60.0,
            y=441.0,
            width=493.0,
            height=80.0
        )

        add_contract_button_image = PhotoImage(
            file="assets\\ac_add_contract_button_img.png")

        add_contract_button = Button(
            master=self.window,
            image=add_contract_button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.confirma_contrato(hired_entry.get(),
                                                   cnpj_entry.get(),
                                                   contract_type.get(),
                                                   manager_area.get(),
                                                   contract_description.get(),
                                                   initial_date_entry.get(),
                                                   end_date_entry.get(),
                                                   attachment.get(),
                                                   observations.get()),
            relief="flat"
        )
        add_contract_button.place(
            x=157.0,
            y=540.0,
            width=303.0,
            height=59.01454162597656
        )
        self.window.resizable(False, False)
        self.window.mainloop()

    def confirma_contrato(self,
                          contratado,
                          cnpj,
                          tipo_contrato,
                          area_gestora,
                          descricao_contrato,
                          data_inicial,
                          data_final,
                          anexo,
                          observacoes):
        confirmação = ConfirmaNovoContrato(contratado,
                                           cnpj,
                                           tipo_contrato,
                                           area_gestora,
                                           descricao_contrato,
                                           data_inicial,
                                           data_final,
                                           anexo,
                                           observacoes).confirmar_inputs()
        match confirmação:
            case 200:
                self.window.destroy()
                self.master.focus_force()
            case 500:
                self.window.focus_force()
