from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, Label
from controller.loginValidatorController import *
from controller.pathSelectorController import select_path
from view.placeHolder import *

OUTPUT_PATH = Path(__file__).parent.parent
ASSETS_PATH = OUTPUT_PATH


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class AppInterface(Tk):
    def __init__(self):
        super().__init__()
        self.canvas = Canvas(self)
        self.login_page()

    def login_page(self):

        self.title('Controle de Contratos FlexPag')
        self.geometry("1260x768")
        self.configure(bg="#005E9F")
        self.resizable(False, False)

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

    def switch_window(self):
        self.canvas.destroy()

    def validate_login(self, login_field, password_field):
        validation = login_page_validations(login_field, password_field)

        match validation:
            case 200:
                self.switch_window()
            case _:
                pass
