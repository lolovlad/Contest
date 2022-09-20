from Classes.ControllersInit import ControllersInit
from Classes.EelModification import EelModification

from Controller.PackageController import PackageController
from Controller.MainWindowController import MainWindowController
from Controller.MenuController import MenuController
from Controller.TotalWindowController import TotalWindowController

from Controller import UserController, TeamController, ContestController

from tkinter import Tk, filedialog
from settings import settings
import eel


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
def load_organization():
    return ControllersInit().user.load_organization()


@eel.expose
def button_login():
    return ControllersInit().login.login()


@eel.expose
def button_add_user():
    ControllersInit().user.add_user()


@eel.expose
def button_update_user():
    ControllersInit().user.update_user()


@eel.expose
def button_delete_user():
    ControllersInit().user.delete_user()


@eel.expose
def select_user(data: dict):
    ControllersInit().user.set_select_user(data)


@eel.expose
def update_select_user(data: dict):
    ControllersInit().user.update_select_user(data)


'''contest'''


@eel.expose
def button_add_contest():
    ControllersInit().contest.add_contest()


@eel.expose
def button_update_contest():
    ControllersInit().contest.update_contest()


@eel.expose
def button_delete_contest():
    ControllersInit().contest.delete_contest()


@eel.expose
def select_contest(data: dict):
    ControllersInit().contest.set_select_contest(data)


@eel.expose
def update_select_contest(data: dict):
    ControllersInit().contest.update_select_contest(data)


@eel.expose
def load_contests():
    ControllersInit().contest.load_contests()


@eel.expose
def load_menu_contest():
    ControllersInit().menu.load_contest()


'''task'''


@eel.expose
def select_task(task: dict):
    ControllersInit().contest.set_select_task(task)


@eel.expose
def update_select_task(task: dict):
    ControllersInit().contest.update_select_task(task)


@eel.expose
def load_tasks():
    ControllersInit().contest.load_tasks()


@eel.expose
def button_add_task():
    ControllersInit().contest.add_task()


@eel.expose
def button_delete_task():
    ControllersInit().contest.delete_task()


@eel.expose
def button_update_task():
    ControllersInit().contest.update_task()


@eel.expose
def load_answer(data: dict):
    ControllersInit().main_window.load_answer(data)


@eel.expose
def update_field_login(val: dict):
    ControllersInit().login.set_login(val)


@eel.expose
def button_send_answer():
    ControllersInit().main_window.send_answer()


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
def update_tasks():
    ControllersInit().contest.update_task()


@eel.expose
def user_load_contest(id_contest):
    contest = ControllersInit().menu.get_select_contest(id_contest)
    ControllersInit().menu = None
    ControllersInit().main_window = MainWindowController()
    ControllersInit().main_window.show_view(contest)


@eel.expose
def load_compilation():
    return ControllersInit().main_window.load_compilation()


@eel.expose
def user_select_task(id_task: int):
    ControllersInit().main_window.select_task(id_task)


@eel.expose
def load_report(id_answer: int):
    ControllersInit().main_window.load_report(id_answer)


@eel.expose
def load_main_window_contest():
    ControllersInit().main_window.load_contest()


@eel.expose
def select_answer(value: dict):
    ControllersInit().main_window.set_select_answer(value)


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
def load_teams():
    ControllersInit().team.load_team()


@eel.expose
def update_select_team(data: dict):
    ControllersInit().team.update_select_team(data)


@eel.expose
def button_add_team():
    ControllersInit().team.add_team()


@eel.expose
def button_delete_team():
    ControllersInit().team.delete_team()


@eel.expose
def button_update_team():
    ControllersInit().team.update_team()


@eel.expose
def select_team(data: dict):
    ControllersInit().team.set_select_team(data)


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
    ControllersInit().total = TotalWindowController()
    ControllersInit().total.show_view(ControllersInit().menu.get_contest())
    ControllersInit().menu = None


@eel.expose
def select_contest_total(id_contest):
    ControllersInit().total.load_total_report(id_contest)


@eel.expose
def load_contest_to_total():
    ControllersInit().total.load_contest()


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
def registration_users_contest():
    return ControllersInit().contest.registration_users_contest()


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
def clear_select_user():
    ControllersInit().user.clear_select_user()


@eel.expose
def clear_select_team():
    ControllersInit().team.clear_select_team()


@eel.expose
def clear_select_contest():
    ControllersInit().contest.clear_select_contest()


@eel.expose
def clear_select_task():
    ControllersInit().contest.clear_select_task()


@eel.expose
def open_window_user():
    ControllersInit().contest = None
    ControllersInit().team = None
    ControllersInit().user = UserController()
    ControllersInit().user.show_view()


'''@eel.expose
def open_window_contest():
    pass
'''


@eel.expose
def open_window_team():
    ControllersInit().contest = None
    ControllersInit().user = None
    ControllersInit().team = TeamController()
    ControllersInit().team.show_view()


@eel.expose
def open_window_contest():
    ControllersInit().team = None
    ControllersInit().user = None
    ControllersInit().contest = ContestController()
    ControllersInit().contest.show_view()


if __name__ == '__main__':
    eel.init('templates')
    geometry = {'size': (720, 760), 'position': (300, 50)}
    eel.start(settings.start_file, mode=settings.path_browser,
              size=geometry["size"], port=settings.port_app,
              position=geometry["position"], jinja_templates='templates')



