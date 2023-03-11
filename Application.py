from Classes.ControllersInit import ControllersInit
from Classes.EelModification import EelModification

from Controller.PackageController import PackageController
from Controller.MenuController import MenuController
from Controller.TotalWindowController import TotalWindowController

from Controller import UserController, TeamController, ContestController
from Classes.TaskPage import TaskPage
from Classes.ContestUserPage import ContestUserPage
from Classes.TotalPage import TotalPage

from tkinter import Tk, filedialog
from settings import settings
import eel

from typing import List

from random import randint


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


'''user'''


@eel.expose
def load_user():
    ControllersInit().user.load_user()


@eel.expose
def load_organization(type_edu: int):
    return ControllersInit().user.load_organization(type_edu)


@eel.expose
def button_login():
    return ControllersInit().login.login()


@eel.expose
def button_add_user(user: dict):
    ControllersInit().user.add_user(user)


@eel.expose
def button_update_user(user: dict):
    ControllersInit().user.update_user(user)


@eel.expose
def button_delete_user(id_user: int):
    ControllersInit().user.delete_user(id_user)


@eel.expose
def load_user_form_update(id_user: int):
    ControllersInit().user.show_view_form_update(id_user)


@eel.expose
def get_user_mode_update():
    return ControllersInit().user.get_mode_update()


@eel.expose
def load_form_user():
    return ControllersInit().user.load_form_user()

'''contest'''


@eel.expose
def load_contest_form_update(id_contest: int):
    return ControllersInit().contest.show_view_form_update(id_contest)


@eel.expose
def get_contest_mode_update():
    return ControllersInit().contest.get_mode_update()


@eel.expose
def load_form_contest():
    ControllersInit().contest.load_form_contest()


@eel.expose
def load_contest_form():
    return ControllersInit().contest.show_view_form()


@eel.expose
def button_add_contest(contest: dict):
    ControllersInit().contest.add_contest(contest)


@eel.expose
def button_update_contest(contest: dict):
    ControllersInit().contest.update_contest(contest)


@eel.expose
def button_delete_contest(id_contest: int):
    ControllersInit().contest.delete_contest(id_contest)


@eel.expose
def load_contests():
    ControllersInit().contest.load_contests()


@eel.expose
def load_menu_contest():
    return ControllersInit().menu.load_contest()


'''task'''

@eel.expose
def open_task_form():
    return ControllersInit().task.show_view_form()


@eel.expose
def open_task_update_form(id_task: int):
    return ControllersInit().task.show_view_form_update(id_task)


@eel.expose
def open_task_settings_form(id_task: int):
    return ControllersInit().task.show_view_form_settings(id_task)


@eel.expose
def load_form_task() -> dict:
    return ControllersInit().task.get_task()


@eel.expose
def get_task_mode_update():
    return ControllersInit().task.get_mode_update()


@eel.expose
def delete_file(name_file: str):
    ControllersInit().task.delete_file(name_file)


@eel.expose
def upload_json_file(file_name: str):
    return ControllersInit().task.upload_json_file(file_name)


@eel.expose
def get_list_task():
    return ControllersInit().task.get_list_task_in_contest()


@eel.expose
def get_setting_task():
    return ControllersInit().task.get_settings()


@eel.expose
def button_add_task(task: dict):
    ControllersInit().task.add_task(task)


@eel.expose
def button_update_settings(settings: dict):
    ControllersInit().task.update_setting(settings)


@eel.expose
def button_delete_task(id_task: int):
    ControllersInit().task.delete_task(id_task)


@eel.expose
def get_list_answers(id_task: int):
    return ControllersInit().main_window.get_list_answers(id_task)


@eel.expose
def update_field_login(val: dict):
    ControllersInit().login.set_login(val)


@eel.expose
def button_send_answer(id_task: int, id_compiler: int):
    return ControllersInit().main_window.send_answer(id_task, id_compiler)


@eel.expose
def file() -> str:
    root = Tk()
    root.withdraw()
    root.wm_attributes('-topmost', 1)
    filetypes = (
        ('json files', '*.json'),
    )
    try:
        folder = filedialog.askopenfile(
            title='Загрузить файл',
            initialdir='/',
            filetypes=filetypes
        )
        return str(folder.name)
    except AttributeError:
        return ""



@eel.expose
def open_window_contest_user(id_contest: int):
    ControllersInit().menu = None
    ControllersInit().main_window = ContestUserPage(id_contest)
    ControllersInit().main_window.show_view()


@eel.expose
def get_url_websocket():
    return ControllersInit().main_window.get_url_websocket()


@eel.expose
def load_compilation():
    return ControllersInit().main_window.load_compilation()


@eel.expose
def load_main_window_select_task(id_task: int):
    return ControllersInit().main_window.load_main_window_select_task(id_task)


@eel.expose
def get_report(id_answer: int):
    return ControllersInit().main_window.get_report(id_answer)


@eel.expose
def load_main_window_contest() -> str:
    return ControllersInit().main_window.load_contest()


@eel.expose
def load_main_window_list_task() -> str:
    return ControllersInit().main_window.load_main_window_list_task()


@eel.expose
def parser_message(message: str):
    ControllersInit().main_window.parser_message(message)

@eel.expose
def upload_file(value: dict):
    ControllersInit().main_window.set_file(value)


@eel.expose
def open_package_window():
    ControllersInit().package = PackageController()
    controller = ControllersInit().package
    ControllersInit().main_window.open_package_window(controller)


'''team'''


@eel.expose
def load_form_team():
    return ControllersInit().team.load_form_team()


@eel.expose
def get_team_mode_update():
    return ControllersInit().team.get_mode_update()


@eel.expose
def load_team_form():
    return ControllersInit().team.show_view_form()


@eel.expose
def load_team_form_update(id_team: int):
    return ControllersInit().team.show_view_form_update(id_team)


@eel.expose
def load_teams():
    ControllersInit().team.load_team()


@eel.expose
def button_add_team(team: dict):
    ControllersInit().team.add_team(team)


@eel.expose
def button_delete_team(id_team: int):
    ControllersInit().team.delete_team(id_team)


@eel.expose
def button_update_team(team: dict):
    ControllersInit().team.update_team(team)


@eel.expose
def close_contest():
    return ControllersInit().main_window.close_contest()


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
    ControllersInit().total = TotalPage()
    ControllersInit().total.show_view()
    ControllersInit().menu = None


@eel.expose
def select_contest_total(id_contest):
    return ControllersInit().total.load_total_report(id_contest)


@eel.expose
def load_contest_to_total():
    return ControllersInit().total.load_contest()


@eel.expose
def button_contest_create_report(settings_report: dict):
    ControllersInit().contest.create_report(settings_report)


@eel.expose
def load_user_in_team(id_team: int):
    return ControllersInit().team.load_user_in_team(id_team)


@eel.expose
def load_user_in_contest(id_contest: int):
    return ControllersInit().contest.load_user_in_contest(id_contest)


@eel.expose
def load_team_in_contest(id_contest: int):
    return ControllersInit().contest.load_team_in_contest(id_contest)


@eel.expose
def registration_users_contest(users):
    return ControllersInit().contest.registration_users_contest(users)


@eel.expose
def files_test() -> List[str]:
    root = Tk()
    root.withdraw()
    root.wm_attributes('-topmost', 1)
    try:
        files = filedialog.askopenfilenames(
            title='Загрузить файл',
            initialdir='/',
        )
        list_file = ControllersInit().task.add_files(list(root.splitlist(files)))
        return list(list_file)
    except AttributeError:
        return []


@eel.expose
def file_programme() -> str:
    root = Tk()
    root.withdraw()
    root.wm_attributes('-topmost', 1)
    filetypes = (
        ('python files', '*.py'),
        ('c++ files', '*.cpp'),
    )
    try:
        folder = filedialog.askopenfile(
            title='Загрузить файл',
            initialdir='/',
            filetypes=filetypes
        )
        return str(folder.name)
    except AttributeError:
        return ""


@eel.expose
def path_report() -> str:
    root = Tk()
    root.withdraw()
    root.wm_attributes('-topmost', 1)
    try:
        folder_selected = filedialog.askdirectory()
        return str(folder_selected)
    except AttributeError:
        return ""


@eel.expose
def open_window_menu():
    ControllersInit().menu = MenuController()
    ControllersInit().menu.show_view()
    ControllersInit().main_window = None
    ControllersInit().package = None


@eel.expose
def load_user_form():
    ControllersInit().user.show_view_form()


@eel.expose
def open_window_user():
    ControllersInit().contest = None
    ControllersInit().team = None
    ControllersInit().task = None
    ControllersInit().user = UserController()
    ControllersInit().user.show_view()


@eel.expose
def open_window_team():
    ControllersInit().contest = None
    ControllersInit().user = None
    ControllersInit().task = None
    ControllersInit().team = TeamController()
    ControllersInit().team.show_view()


@eel.expose
def open_window_contest():
    ControllersInit().team = None
    ControllersInit().user = None
    ControllersInit().task = None
    ControllersInit().contest = ContestController()
    ControllersInit().contest.show_view()


@eel.expose
def open_window_task(id_contest: int):
    ControllersInit().contest = None
    ControllersInit().task = TaskPage(id_contest)
    ControllersInit().task.show_view()


if __name__ == '__main__':
    eel.init('templates')
    geometry = {'size': (720, 760), 'position': (300, 50)}
    eel.start(settings.start_file, mode=settings.mode,
              size=geometry["size"], port=settings.port_app,
              position=geometry["position"], jinja_templates='templates',
              cmdline_args=[settings.path_browser, settings.args],
              shutdown_delay=500000)



