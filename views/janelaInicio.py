from tkinter import Canvas, PhotoImage, Frame, ttk, VERTICAL, RIGHT, Y, Button, messagebox
from controller.confirmaPesquisa import ConfirmaPesquisa
from controller.chamaGeraRelatorios import ChamaGeraRelatorios
from views.janelaAddContrato import JanelaAddContrato
from views.placeholderEntry import PlaceHolder
from controller.mascaraCnpj import MascaraCNPJ
from controller.abreContrato import AbreAnexos
from views.popupBotaoDireito import PopUpMenu
from controller.mascaraDatas import MascaraDatas

global upper_field_image
global search_field_image
global add_contract_image
global search_button_image
global treeview_field_image
global download_report_button_image


class JanelaInicial:

    def __init__(self, master: vars):

        global upper_field_image
        global search_field_image
        global add_contract_image
        global search_button_image
        global treeview_field_image
        global download_report_button_image

        self.master = master

        self.canvas = Canvas(
            self.master,
            bg="#005E9F",
            height=768,
            width=1260,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)
        upper_field_image = PhotoImage(
            file="assets\\ti_upper_field_img.png")
        self.canvas.create_image(
            629.0,
            53.0,
            image=upper_field_image
        )

        search_field_image = PhotoImage(
            file="assets\\ti_search_field_img.png")
        self.canvas.create_image(
            265.5,
            52.0,
            image=search_field_image
        )
        search_field = PlaceHolder(
            self.canvas,
            placeholder='Insira o contratado ou CNPJ.',
            default_fg_color='#FFFFFF',
            color='#FFFFFF',
            bd=0,
            bg="#2082C5",
            highlightthickness=0
        )
        search_field.place(
            x=66.0,
            y=34.0,
            width=399.0,
            height=34.0
        )

        treeview_field_image = PhotoImage(
            file="assets\\ti_treeview_field_img.png")
        self.canvas.create_image(
            629.0,
            432.0,
            image=treeview_field_image
        )

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
                  background=[('selected', '#56AFEC')])

        treeview_frame = Frame(self.canvas)
        treeview_frame.place(
            x=24.0 + 15,
            y=135.0,
            width=1208.0 - 20,
            height=600.0
        )

        treeview_scrollbar = ttk.Scrollbar(treeview_frame, orient=VERTICAL)
        treeview_scrollbar.pack(side=RIGHT, fill=Y)

        tree = ttk.Treeview(treeview_frame, columns=(1, 2, 3, 4, 5, 6), height='7', show='headings',
                            yscrollcommand=treeview_scrollbar.set)
        tree.place(
            width=1208.0 - 40,
            height=600.0
        )

        treeview_scrollbar.config(command=tree.yview)

        tree.heading(1, text='Id')
        tree.heading(2, text='Contratado')
        tree.heading(3, text='CNPJ')
        tree.heading(4, text='Inicio Vigência')
        tree.heading(5, text='Data Vencimento')
        tree.heading(6, text='Situação')

        tree.column(1, anchor='center')
        tree.column(3, anchor='center')
        tree.column(4, anchor='center')
        tree.column(5, anchor='center')
        tree.column(6, anchor='center')

        self.inserir_pesquisa_na_tabela(tree, '')

        search_button_image = PhotoImage(
            file="assets\\ti_search_button_img.png")
        search_button = Button(
            image=search_button_image,
            borderwidth=0,
            bg=None,
            highlightthickness=0,
            command=lambda: self.inserir_pesquisa_na_tabela(tree, search_field.get()),
            relief="flat"
        )
        search_button.place(
            x=440.0,
            y=37.0,
            width=29.0,
            height=30.0
        )

        download_report_button_image = PhotoImage(
            file="assets\\ti_donwload_report_buttom_img.png")
        download_report_button = Button(
            image=download_report_button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.gera_relatorios(search_field.get()),
            relief="flat"
        )
        download_report_button.place(
            x=778.0,
            y=34.0,
            width=223.0,
            height=39.0
        )

        add_contract_image = PhotoImage(
            file="assets\\ti_add_contract_button_img.png")
        add_contract_button = Button(
            image=add_contract_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: JanelaAddContrato(self.master),
            relief="flat"
        )
        add_contract_button.place(
            x=1001.0,
            y=34.0,
            width=223.0,
            height=39.0
        )

        def chama_pesquisa(e):
            self.inserir_pesquisa_na_tabela(tree, search_field.get())

        def chama_double_click(e):
            self.abrir_anexo(tree)

        def chama_botao_direito(e):
            self.abrir_menu_botao_direito(self.master, tree, e)

        self.master.bind('<Return>', chama_pesquisa)
        tree.bind('<Double-1>', chama_double_click)
        tree.bind('<Button-3>', chama_botao_direito)

    @staticmethod
    def inserir_pesquisa_na_tabela(tabela: ttk.Treeview, pesquisa: str) -> None:
        contador = 0

        tabela.tag_configure('impar', background='#0B74BC')
        tabela.tag_configure('par', background='#2083C6')

        dados = ConfirmaPesquisa().pesquisar(pesquisa)

        tabela.delete(*tabela.get_children())

        for linha in dados:

            linha = list(linha)
            linha[2] = MascaraCNPJ.mascarar(linha[2])
            linha[3] = MascaraDatas.mascarar_datas(linha[3])
            linha[4] = MascaraDatas.mascarar_datas(linha[4])

            if contador % 2 == 0:
                tabela.insert('', 'end', values=linha, tags='par')
            else:
                tabela.insert('', 'end', values=linha, tags='impar')
            contador += 1

    def gera_relatorios(self, pesquisa: str) -> None:
        ChamaGeraRelatorios.gerar_relatorio(pesquisa)
        messagebox.showinfo(title='Donwload Concluído', message='O donwload do relatório foi concluído')
        self.canvas.focus_force()

    def abrir_anexo(self, tree) -> None:
        id_contrato = self.retorna_id_da_tree(tree)
        AbreAnexos.abre_anexo(id_contrato)

    @staticmethod
    def retorna_id_da_tree(tree: ttk.Treeview) -> int:
        selection = tree.selection()
        item = tree.item(selection)
        id_contrato = item['values'][0]
        return id_contrato

    def abrir_menu_botao_direito(self, master, tree,  event) -> None:
        id_contrato = self.retorna_id_da_tree(tree)
        PopUpMenu(master, event, id_contrato)
