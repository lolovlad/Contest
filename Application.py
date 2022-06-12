from Classes.ControllersInit import ControllersInit
from Classes.EelModification import EelModification
from tkinter import Tk, filedialog
import eel

root = Tk()
root.withdraw()
root.wm_attributes('-topmost', 1)


@eel.expose
def button_exit_window():
    ControllersInit().admin_panel.close_window()
    ControllersInit().total.close_window()
    ControllersInit().login.show_view()


@eel.expose
def button_exit_menu():
    ControllersInit().menu.close_window()
    ControllersInit().login.show_view()


@eel.expose
def title_window():
    return ControllersInit().target.name_window


@eel.expose
def load_user():
    ControllersInit().admin_panel.load_users()


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
def select_user(data):
    ControllersInit().admin_panel.set_select_user(data)


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
def select_contest(data):
    ControllersInit().admin_panel.set_select_contest(data)


@eel.expose
def load_contest(mode):
    ControllersInit().admin_panel.load_contest(mode)


@eel.expose
def load_menu_contest():
    ControllersInit().menu.load_contest()


@eel.expose
def select_task(task):
    ControllersInit().admin_panel.set_select_task(task)


@eel.expose
def load_tasks():
    ControllersInit().admin_panel.load_task()


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
def load_answer():
    ControllersInit().main_window.load_answer()


@eel.expose
def update_field_login(login_text, password_text):
    ControllersInit().login.set_login(login_text)
    ControllersInit().login.set_password(password_text)


@eel.expose
def button_send_answer():
    ControllersInit().main_window.send_answer()


@eel.expose
def file():
    try:
        folder = filedialog.askopenfile()
        return str(folder.name)
    except AttributeError:
        return ""


@eel.expose
def update_tasks(val):
    ControllersInit().admin_panel.update_tasks(val)


@eel.expose
def set_file(val):
    ControllersInit().main_window.set_file(val)


@eel.expose
def user_load_contest(id_contest):
    contest = ControllersInit().menu.get_select_contest(id_contest)
    ControllersInit().menu.close_window()
    ControllersInit().main_window.show_view(contest)


@eel.expose
def user_load_tasks():
    ControllersInit().main_window.load_tasks_on_contest()


@eel.expose
def user_select_task(id_task):
    ControllersInit().main_window.select_task(id_task)


@eel.expose
def load_report(id_report):
    task = ControllersInit().main_window.load_report(id_report)


@eel.expose
def load_main_window_contest():
    ControllersInit().main_window.load_contest()


@eel.expose
def open_package_window():
    ControllersInit().main_window.open_package_window(ControllersInit().package)


@eel.expose
def load_teams():
    ControllersInit().admin_panel.load_team()


@eel.expose
def button_add_team():
    ControllersInit().admin_panel.add_team()


@eel.expose
def button_delete_team():
    ControllersInit().admin_panel.delete_team()


@eel.expose
def button_update_team():
    ControllersInit().admin_panel.update_team()


@eel.expose
def select_team(val):
    ControllersInit().admin_panel.set_select_team(val)


@eel.expose
def registration_user_event(data):
    ControllersInit().admin_panel.registration_user_event(data)


@eel.expose
def close_contest():
    ControllersInit().main_window.close_contest()


@eel.expose
def is_close():
    return ControllersInit().main_window.is_close_contest()


@eel.expose
def load_answer_package():
    ControllersInit().package.load_answer_package()


@eel.expose
def load_report_package(id_report):
    ControllersInit().package.load_report_package(id_report)


@eel.expose
def open_window_total():
    ControllersInit().menu.close_window()
    ControllersInit().total.show_view(ControllersInit().menu.get_contest())


@eel.expose
def open_window_contest():
    ControllersInit().total.close_window()
    ControllersInit().menu.show_view()


@eel.expose
def select_contest_total(id_contest):
    ControllersInit().total.set_select_contest(id_contest)


@eel.expose
def load_report_total():
    ControllersInit().total.load_contest()


@eel.expose
def button_contest_create_report():
    ControllersInit().admin_panel.create_report()


if __name__ == '__main__':
    eel.init('templates')
    ControllersInit().login.show_view()



