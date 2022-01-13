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

        self.title('Sistema de Automações Flexpag')
        self.geometry("630x390")
        self.configure(bg="#FFFFFF")
        self.resizable(False, False)

        global login_field_image_path
        global password_field_image_path
        global password_image
        global logo_image
        global enter_button_image

        self.canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=390,
            width=630,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)

        login_field_image_path = PhotoImage(
            file=relative_to_assets("lp_login_field_img.png"))

        self.canvas.create_image(
            315.0,
            163.0,
            image=login_field_image_path
        )
        login_field = PlaceHolderEntry(
            self.canvas,
            'Insert your login',
            bd=0,
            bg="#ECECEC",
            highlightthickness=0
        )

        login_field.place(
            x=118.0,
            y=142.0,
            width=394.0,
            height=40.0
        )

        password_field_image_path = PhotoImage(
            file=relative_to_assets("lp_password_field_img.png"))
        self.canvas.create_image(
            315.0,
            234.0,
            image=password_field_image_path
        )
        password_field = PlaceHolderEntry(
            self.canvas,
            'Insert your password',
            'gray',
            bd=0,
            type='password',
            bg="#ECECEC",
            highlightthickness=0
        )
        password_field.place(
            x=118.0,
            y=213.0,
            width=394.0,
            height=40.0
        )

        password_image = PhotoImage(
            file=relative_to_assets("lp_password_img.png"))
        self.canvas.create_image(
            141.5,
            200.0,
            image=password_image
        )
        password_label = Label(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0,
            text="Password"
        )
        password_label.place(
            x=108.0,
            y=191.0,
            width=67.0,
            height=16.0
        )

        logo_image = PhotoImage(
            file=relative_to_assets("lp_logo_blue.png"))
        self.canvas.create_image(
            315.0,
            73.0,
            image=logo_image
        )

        login_image = PhotoImage(
            file=relative_to_assets("lp_login_img.png"))
        self.canvas.create_image(
            127.0,
            126.0,
            image=login_image
        )
        login_label = Label(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0,
            text='Login'
        )
        login_label.place(
            x=108.0,
            y=117.0,
            width=38.0,
            height=16.0
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
            x=103.0,
            y=282.0,
            width=424.0,
            height=45.0
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
