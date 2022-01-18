from Controller.LoginController import LoginController
from Model.LoginModel import LoginModel

import eel

login = LoginController(LoginModel())


@eel.expose
def button_login():
    return login.login()


@eel.expose
def update_date(login_text, password_text):
    login.set_login(login_text)
    login.set_password(password_text)


@eel.expose
def retrieve():
    eel.show("main.html")


@eel.expose
def open_posl():
    eel.show("posl.html")


if __name__ == '__main__':
    eel.init('templates')
    login.show_view()



