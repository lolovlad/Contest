from Classes.ControllersInit import ControllersInit

import eel


@eel.expose
def button_login():
    return ControllersInit().login.login()


@eel.expose
def button_add_user():
    ControllersInit().admin_panel.add_user()


@eel.expose
def button_update_user():
    ControllersInit().admin_panel.update_user()


@eel.expose
def button_delete_user():
    ControllersInit().admin_panel.delete_user()


@eel.expose
def button_add_contest():
    ControllersInit().admin_panel.add_contest()


@eel.expose
def button_update_contest():
    ControllersInit().admin_panel.update_contest()


@eel.expose
def button_delete_contest():
    ControllersInit().admin_panel.delete_contest()


@eel.expose
def load_user():
    ControllersInit().admin_panel.load_users()


@eel.expose
def load_contest():
    ControllersInit().admin_panel.load_contest()


@eel.expose
def select_user(data):
    ControllersInit().admin_panel.set_select_user(data)


@eel.expose
def select_contest(data):
    ControllersInit().admin_panel.set_select_contest(data)


@eel.expose
def update_field_login(login_text, password_text):
    ControllersInit().login.set_login(login_text)
    ControllersInit().login.set_password(password_text)


if __name__ == '__main__':
    eel.init('templates')
    ControllersInit().login.show_view()



