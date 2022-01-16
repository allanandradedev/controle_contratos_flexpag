from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, Label, ttk
from controller.loginValidatorController import *
from controller.pathSelectorController import select_path
from view.placeHolder import *
from module.database import *
from controller.addContractValidatorController import *
from module.reportGeneratorService import *

OUTPUT_PATH = Path(__file__).parent.parent
ASSETS_PATH = OUTPUT_PATH


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class AppInterface(Tk):
    def __init__(self):
        super().__init__()
        self.canvas = Canvas(self)
        self.login_page()
        self.title('Controle de Contratos FlexPag')
        self.geometry("1260x768")
        self.configure(bg="#005E9F")
        self.resizable(False, False)
        self.database = SQLiteDatabase()
        self.report_generator = ReportGenerator()

    def login_page(self):

        global login_field_image_path
        global password_field_image_path
        global password_image
        global logo_image
        global enter_button_image
        global woman_image_path
        global login_image_path

        self.canvas = Canvas(
            self,
            bg="#005E9F",
            height=768,
            width=1260,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)

        logo_image = PhotoImage(
            file=relative_to_assets("lp_logo_white.png"))
        self.canvas.create_image(
            313.0,
            157.0,
            image=logo_image
        )

        woman_image_path = PhotoImage(
            file=relative_to_assets("lp_woman_image.png"))
        self.canvas.create_image(
            313.0,
            461.0,
            image=woman_image_path
        )

        # Frame do login
        self.canvas.create_rectangle(
            630.0,
            0.0,
            1260.0,
            768.0,
            fill="#FFFFFF",
            outline="")

        login_field_image_path = PhotoImage(
            file=relative_to_assets("lp_login_field_img.png"))

        self.canvas.create_image(
            944.5,
            318.0,
            image=login_field_image_path
        )

        login_field = PlaceHolderEntry(
            self.canvas,
            'Insira seu nome de usuário',
            bd=0,
            bg="#EFEFEF",
            default_fg_color='#000000',
            highlightthickness=0
        )

        login_field.place(
            x=698.0,
            y=293.0,
            width=493.0,
            height=48.0
        )

        password_field_image_path = PhotoImage(
            file=relative_to_assets("lp_password_field_img.png"))
        self.canvas.create_image(
            944.5,
            409.0,
            image=password_field_image_path
        )
        password_field = PlaceHolderEntry(
            self.canvas,
            'Insira sua senha',
            'gray',
            bd=0,
            type='password',
            default_fg_color='#000000',
            bg="#ECECEC",
            highlightthickness=0
        )
        password_field.place(
            x=698.0,
            y=384.0,
            width=493.0,
            height=48.0
        )

        login_title_image_path = PhotoImage(
            file=relative_to_assets("lp_login_title_img.png"))
        self.canvas.create_image(
            945.0,
            206.0,
            image=login_title_image_path
        )

        login_title = Label(
            text='Faça o Login para Continuar',
            bd=0,
            font=("Roboto Bold", '20'),
            fg='#005E9F',
            bg="#FFFFFF",
            highlightthickness=0
        )
        login_title.place(
            x=754.0,
            y=184.0,
            width=382.0,
            height=42.0
        )

        password_image = PhotoImage(
            file=relative_to_assets("lp_password_img.png"))

        self.canvas.create_image(
            718.0,
            363.5,
            image=password_image
        )

        login_image_path = PhotoImage(
            file=relative_to_assets("lp_login_img.png"))
        self.canvas.create_image(
            715.0,
            269.5,
            image=login_image_path
        )
        login_label = Label(
            text='Login',
            font=("Roboto", '12'),
            bd=0,
            bg="#FFFFFF",
            fg='#818181',
            highlightthickness=0
        )
        login_label.place(
            x=690.0,
            y=261.0,
            width=50.0,
            height=21.0
        )

        password_label = Label(
            text='Senha',
            font=("Roboto", '12'),
            bd=0,
            bg="#FFFFFF",
            fg='#808080',
            highlightthickness=0
        )
        password_label.place(
            x=690.0,
            y=355.0,
            width=56.0,
            height=21.0
        )

        enter_button_image = PhotoImage(
            file=relative_to_assets("lp_enter_button.png"))
        enter_button = Button(
            image=enter_button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.validate_login(login_field, password_field),
            relief="flat"
        )
        enter_button.place(
            x=773.0,
            y=478.0,
            width=344.0,
            height=67.0
        )

    def ui_screen(self):

        global upper_field_image
        global search_field_image
        global add_contract_image
        global search_button_image
        global treeview_field_image
        global download_report_button_image

        self.canvas = Canvas(
            self,
            bg="#005E9F",
            height=768,
            width=1260,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)
        upper_field_image = PhotoImage(
            file=relative_to_assets("ti_upper_field_img.png"))
        self.canvas.create_image(
            629.0,
            53.0,
            image=upper_field_image
        )

        search_field_image = PhotoImage(
            file=relative_to_assets("ti_search_field_img.png"))
        self.canvas.create_image(
            265.5,
            52.0,
            image=search_field_image
        )
        search_field = PlaceHolderEntry(
            self.canvas,
            placeholder='Insira o contratado ou CNPJ.',
            color='#EFEFEF',
            bd=0,
            bg="#2082C5",
            default_fg_color='#FFFFFF',
            highlightthickness=0
        )
        search_field.place(
            x=66.0,
            y=34.0,
            width=399.0,
            height=34.0
        )

        treeview_field_image = PhotoImage(
            file=relative_to_assets("ti_treeview_field_img.png"))
        self.canvas.create_image(
            629.0,
            432.0,
            image=treeview_field_image
        )

        # -------- Treeview Settings ----------------------------------

        style = ttk.Style()

        style.theme_use("clam")

        style.configure("Treeview",
                        background="#0B74BC",
                        foreground="white",
                        font=('Roboto', 12),
                        rowheight=40,
                        fieldbackground="#0B74BC",
                        )
        style.configure('Treeview.Heading',
                        font=('Arial Bold', 13),
                        foreground='White',
                        background='#0B74BC',
                        fieldbackground='#0B74BC',
                        rowheight=30,
                        borderwidth=0,
                        padding=15)

        style.configure("Vertical.TScrollbar", gripcount=0,
                        arrowsize=20, arrowcolor="#0B74BC",
                        background="#0B74BC", darkcolor="#0B74BC",
                        lightcolor="#0B74BC", troughcolor="#0B74BC",
                        bordercolor="#0B74BC", )

        style.map('Treeview.Heading',
                  background=[('pressed', '!focus', '#0B74BC'),
                              ('active', '#0B74BC'),
                              ('disabled', '#0B74BC')]
                  )

        style.map('Vertical.TScrollbar',
                  background=[('pressed', '!focus', '#005E9F'),
                              ('active', '#005E9F')]
                  )

        style.layout("Treeview",
                     [('mystyle.Treeview.treearea',
                       {'sticky': 'nswe'})])

        style.map("Treeview",
                  background=[('selected', '#2285CA')])

        # ---------------------------------------------------------

        # ------- Treeview Frame Settings -------------------------

        treeview_frame = Frame(self.canvas)
        treeview_frame.place(
            x=24.0 + 15,
            y=135.0,
            width=1208.0 - 20,
            height=600.0
        )

        treeview_scrollbar = ttk.Scrollbar(treeview_frame, orient=VERTICAL)
        treeview_scrollbar.pack(side=RIGHT, fill=Y)

        tv = ttk.Treeview(treeview_frame, columns=(1, 2, 3, 4, 5, 6), height='7', show='headings',
                          yscrollcommand=treeview_scrollbar.set)
        tv.place(
            width=1208.0 - 40,
            height=600.0
        )

        treeview_scrollbar.config(command=tv.yview)

        tv.heading(1, text='Id')
        tv.heading(2, text='Contratado')
        tv.heading(3, text='CNPJ')
        tv.heading(4, text='Inicio Vigência')
        tv.heading(5, text='Data Vencimento')
        tv.heading(6, text='Situação')

        tv.column(1, anchor='center')
        tv.column(3, anchor='center')
        tv.column(4, anchor='center')
        tv.column(5, anchor='center')
        tv.column(6, anchor='center')

        # ------------------------------------------------------------------------

        search_button_image = PhotoImage(
            file=relative_to_assets("ti_search_button_img.png"))
        search_button = Button(
            image=search_button_image,
            borderwidth=0,
            bg=None,
            highlightthickness=0,
            command=lambda: self.insert_search_into_treeview(tv, self.database, search_field.get()),
            relief="flat"
        )
        search_button.place(
            x=440.0,
            y=37.0,
            width=29.0,
            height=30.0
        )

        download_report_button_image = PhotoImage(
            file=relative_to_assets("ti_donwload_report_buttom_img.png"))
        download_report_button = Button(
            image=download_report_button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.report_generator.generate_report(search_field.get()),
            relief="flat"
        )
        download_report_button.place(
            x=778.0,
            y=34.0,
            width=223.0,
            height=39.0
        )

        add_contract_image = PhotoImage(
            file=relative_to_assets("ti_add_contract_button_img.png"))
        add_contract_button = Button(
            image=add_contract_image,
            borderwidth=0,
            highlightthickness=0,
            command=self.add_contract_page,
            relief="flat"
        )
        add_contract_button.place(
            x=1001.0,
            y=34.0,
            width=223.0,
            height=39.0
        )

        self.insert_search_into_treeview(tv, self.database, search_field.get())

    def add_contract_page(self):

        global title_label_image
        global entry_field_image
        global date_field_image
        global observations_image

        window = Toplevel()

        window.geometry("615x636")
        window.configure(bg="#FFFFFF")
        window.title('Adicionar Contrato.')

        canvas = Canvas(
            window,
            bg="#FFFFFF",
            height=636,
            width=615,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        canvas.place(x=0, y=0)

        title_label_image = PhotoImage(
            file=relative_to_assets("ac_title_label_img.png"))
        canvas.create_image(
            308.0,
            59.0,
            image=title_label_image
        )
        title_label = Label(
            master=window,
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
            file=relative_to_assets("ac_entry_field_image.png"))

        canvas.create_image(
            308.5,
            117.5,
            image=entry_field_image
        )
        hired_entry = PlaceHolderEntry(
            master=window,
            placeholder='*Nome do Contratado.',
            default_fg_color='#2B2B2B',
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

        canvas.create_image(
            306.5,
            166.5,
            image=entry_field_image
        )
        cnpj_entry = PlaceHolderEntry(
            master=window,
            placeholder='*Insira o CNPJ sem as pontuações.',
            default_fg_color='#2B2B2B',
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

        canvas.create_image(
            308.5,
            215.5,
            image=entry_field_image
        )
        contract_type = PlaceHolderEntry(
            master=window,
            placeholder='*Tipo de Contrato.',
            default_fg_color='#2B2B2B',
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

        canvas.create_image(
            308.5,
            264.5,
            image=entry_field_image
        )
        manager_area = PlaceHolderEntry(
            master=window,
            placeholder='*Área Gestora.',
            default_fg_color='#2B2B2B',
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

        canvas.create_image(
            308.5,
            313.5,
            image=entry_field_image
        )
        contract_description = PlaceHolderEntry(
            master=window,
            placeholder='*Descrição do Contrato.',
            default_fg_color='#2B2B2B',
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
            file=relative_to_assets("ac_date_field_img.png"))

        canvas.create_image(
            170.0,
            362.5,
            image=date_field_image
        )
        initial_date_entry = PlaceHolderEntry(
            master=window,
            placeholder='*Início da Vigência.',
            default_fg_color='#2B2B2B',
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

        canvas.create_image(
            447.0,
            362.5,
            image=date_field_image
        )
        end_date_entry = PlaceHolderEntry(
            master=window,
            placeholder='*Data de Vencimento.',
            default_fg_color='#2B2B2B',
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

        canvas.create_image(
            308.5,
            411.5,
            image=entry_field_image
        )
        situation = PlaceHolderEntry(
            master=window,
            placeholder='*Situação do Contrato.',
            default_fg_color='#2B2B2B',
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0
        )
        situation.place(
            x=62.0,
            y=392.0,
            width=493.0,
            height=37.0
        )

        observations_image = PhotoImage(
            file=relative_to_assets("ac_observations_image.png"))
        canvas.create_image(
            306.5,
            482.0,
            image=observations_image
        )
        observations = PlaceHolderEntry(
            master=window,
            placeholder='Observações adicionais.',
            default_fg_color='#2B2B2B',
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
            file=relative_to_assets("ac_add_contract_button_img.png"))

        add_contract_button = Button(
            master=window,
            image=add_contract_button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.validate_contract_adittion(window,
                                                            hired_entry.get(),
                                                            cnpj_entry.get(),
                                                            contract_type.get(),
                                                            manager_area.get(),
                                                            contract_description.get(),
                                                            initial_date_entry.get(),
                                                            end_date_entry.get(),
                                                            situation.get(),
                                                            observations.get()),
            relief="flat"
        )
        add_contract_button.place(
            x=157.0,
            y=540.0,
            width=303.0,
            height=59.01454162597656
        )
        window.resizable(False, False)
        window.mainloop()

    def insert_search_into_treeview(self, treeview, database, search=''):
        global count
        count = 0

        treeview.tag_configure('oddrow', background='#0B74BC')
        treeview.tag_configure('evenrow', background='#2083C6')

        if search == 'Insira o contratado ou CNPJ.' or not search:
            search = ''
        else:
            search = search

        rows = database.search_by_input(search)

        treeview.delete(*treeview.get_children())

        for i in rows:
            if count % 2 == 0:
                treeview.insert('', 'end', values=i, tags='evenrow')
            else:
                treeview.insert('', 'end', values=i, tags='oddrow')
            count += 1

    def switch_window(self):
        self.canvas.destroy()
        self.ui_screen()

    def validate_contract_adittion(self,
                                   master,
                                   hired_field,
                                   cnpj_field,
                                   contract_type_field,
                                   manager_area_field,
                                   contract_description_field,
                                   start_date_field,
                                   end_date_field,
                                   situation_field,
                                   observation_field
                                   ):

        if add_contract_page_validations(hired_field,
                                         cnpj_field,
                                         contract_type_field,
                                         manager_area_field,
                                         contract_description_field,
                                         start_date_field,
                                         end_date_field,
                                         situation_field) and Validations.validate_cnpj(cnpj_field):

            option = messagebox.askyesno(title='Informação Adicional', message='Deseja tornar a adição permanente?')

            if option:
                self.database.new_contract(hired_field,
                                           cnpj_field,
                                           contract_type_field,
                                           manager_area_field,
                                           contract_description_field,
                                           start_date_field,
                                           end_date_field,
                                           situation_field,
                                           observation_field)
                self.database.commit()
                master.destroy()
                self.canvas.focus_force()
            if not option:
                master.focus_force()

        elif add_contract_page_validations(hired_field,
                                           cnpj_field,
                                           contract_type_field,
                                           manager_area_field,
                                           contract_description_field,
                                           start_date_field,
                                           end_date_field,
                                           situation_field) == 500:
            messagebox.showinfo(title='Campos Vazios', message='Preencha todos os campos obrigatórios para continuar')
            master.focus_force()
        else:
            messagebox.showinfo(title='CNPJ Inválido', message='Verifique o CNPJ e tente novamente')
            master.focus_force()

    def validate_login(self, login_field, password_field):
        validation = login_page_validations(login_field, password_field)

        match validation:
            case 200:
                self.switch_window()
            case _:
                pass
