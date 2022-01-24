from Classes.ControllersInit import ControllersInit

import eel


@eel.expose
def button_login():
    return ControllersInit().login.login()


@eel.expose
def button_add_user():
    ControllersInit().admin_panel.add_user()


@eel.expose
def update_field_login(login_text, password_text):
    ControllersInit().login.set_login(login_text)
    ControllersInit().login.set_password(password_text)


if __name__ == '__main__':
    eel.init('templates')
    ControllersInit().login.show_view()



