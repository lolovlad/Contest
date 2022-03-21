from Classes.ControllersInit import ControllersInit
from Classes.EelModification import EelModification
from tkinter import Tk, filedialog
import eel

root = Tk()
root.withdraw()
root.wm_attributes('-topmost', 1)


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
def load_menu_contest():
    ControllersInit().menu.load_contest()


@eel.expose
def select_task(id_task):
    return ControllersInit().admin_panel.select_task(id_task)


@eel.expose
def load_tasks():
    ControllersInit().admin_panel.load_tasks()


@eel.expose
def load_answer():
    ControllersInit().main_window.load_answer()


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


@eel.expose
def button_add_task():
    ControllersInit().admin_panel.add_task()


@eel.expose
def button_delete_task():
    ControllersInit().admin_panel.delete_task()


@eel.expose
def button_update_task():
    ControllersInit().admin_panel.update_task()


@eel.expose
def button_send_answer():
    ControllersInit().main_window.send_answer()


@eel.expose
def file():
    folder = filedialog.askopenfile()
    return str(folder.name)


@eel.expose
def update_tasks(val):
    ControllersInit().admin_panel.update_tasks(val)


@eel.expose
def set_file(val):
    ControllersInit().main_window.set_file(val)


@eel.expose
def user_load_contest(id_contest):
    EelModification.close_window('localhost:3000/menu.html')
    ControllersInit().main_window.show_view(id_contest)


@eel.expose
def user_load_tasks():
    ControllersInit().main_window.load_tasks_on_contest()


@eel.expose
def user_upload_task(id_task):
    task = ControllersInit().main_window.upload_task(id_task)
    return task


@eel.expose
def load_report(id_report):
    task = ControllersInit().main_window.load_report(id_report)


@eel.expose
def load_main_window_contest():
    task = ControllersInit().main_window.load_contest()


if __name__ == '__main__':
    eel.init('templates')
    ControllersInit().login.show_view()



