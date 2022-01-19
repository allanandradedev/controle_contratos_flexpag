from tkinter import messagebox, Canvas, PhotoImage, Label, Button, StringVar, Entry
from views.placeholderEntry import PlaceHolder
from controller.confirmaLogin import ConfirmaLogin
from views.janelaInicio import JanelaInicial

global login_field_image_path
global password_field_image_path
global password_image
global logo_image
global enter_button_image
global woman_image_path
global login_image_path


class JanelaLogin:

    def __init__(self, master: vars):

        global login_field_image_path
        global password_field_image_path
        global password_image
        global logo_image
        global enter_button_image
        global woman_image_path
        global login_image_path

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

        logo_image = PhotoImage(
            file="assets\\lp_logo_white.png")

        self.canvas.create_image(
            313.0,
            157.0,
            image=logo_image
        )

        woman_image_path = PhotoImage(
            file="assets\\lp_woman_image.png")
        self.canvas.create_image(
            313.0,
            461.0,
            image=woman_image_path
        )

        self.canvas.create_rectangle(
            630.0,
            0.0,
            1260.0,
            768.0,
            fill="#FFFFFF",
            outline="")

        login_field_image_path = PhotoImage(
            file="assets\\lp_login_field_img.png")

        self.canvas.create_image(
            944.5,
            318.0,
            image=login_field_image_path
        )

        login_field = PlaceHolder(
            self.canvas,
            color='gray',
            placeholder='Insira seu nome de usuário.',
            bd=0,
            default_fg_color='#000000',
            bg="#ECECEC",
            highlightthickness=0
        )

        login_field.place(
            x=698.0,
            y=293.0,
            width=493.0,
            height=48.0
        )

        password_field_image_path = PhotoImage(
            file="assets\\lp_password_field_img.png")

        self.canvas.create_image(
            944.5,
            409.0,
            image=password_field_image_path
        )
        password_field = PlaceHolder(
            self.canvas,
            color='gray',
            placeholder='Insira sua senha.',
            entry_type='password',
            bd=0,
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

        caps_aviso_texto = StringVar()
        caps_aviso_texto.set('')

        caps_aviso = Label(
            master=self.canvas,
            fg='gray',
            bd=0,
            background="#FFFFFF",
            textvariable=caps_aviso_texto,
            font=('Roboto', '10'),
            highlightthickness=0,
            anchor="w"
        )
        caps_aviso.place(
            x=698.0,
            y=384.0 + 60,
            width=493.0,
            height=25.0
        )

        login_title_image_path = PhotoImage(
            file="assets\\lp_login_title_img.png")

        self.canvas.create_image(
            945.0,
            206.0,
            image=login_title_image_path
        )

        login_title = Label(
            master=self.canvas,
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
            file="assets\\lp_password_img.png")

        self.canvas.create_image(
            718.0,
            363.5,
            image=password_image
        )

        login_image_path = PhotoImage(
            file="assets\\lp_login_img.png")
        self.canvas.create_image(
            715.0,
            269.5,
            image=login_image_path
        )
        login_label = Label(
            master=self.canvas,
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
            master=self.canvas,
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
            file="assets\\lp_enter_button.png")
        enter_button = Button(
            master=self.canvas,
            image=enter_button_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.confirma_login(login_field.get(), password_field.get()),
            relief="flat"
        )
        enter_button.place(
            x=773.0,
            y=478.0,
            width=344.0,
            height=67.0
        )

        def chama_confirmacao(e):
            self.confirma_login(login_field.get(), password_field.get())

        def chama_caps_aviso(e):
            if e.keycode == 20 and e.state == 8:
                self.caps_lock_aviso(caps_aviso_texto)
            else:
                caps_aviso_texto.set('')

        self.master.bind('<Return>', chama_confirmacao)

        self.master.bind('<Key>', chama_caps_aviso)

    def confirma_login(self, usuario: str, senha: str) -> None:

        confirmacao = ConfirmaLogin.confirma_login(usuario, senha)

        placeholders = [
            'Insira seu nome de usuário.',
            'Insira sua senha.'
        ]

        if not usuario or not senha or usuario in placeholders or senha in placeholders:
            messagebox.showerror(title='Campos Vazios', message='Preencha todos os campos e tente novamente.')
        elif confirmacao == 500:
            messagebox.showerror(title='Senha Incorreta', message='Verifique os dados e tente novamente.')
        else:
            self.canvas.destroy()
            JanelaInicial(self.master)

    def caps_lock_aviso(self, label):
            label.set('O Caps Lock está ligado!')

