from Interfase.Subject import Subject
from Classes.Models.User import User
from Classes.Models.Contes import Contest
from Classes.Models.Task import Task
from Classes.Models.Team import Team
from datetime import datetime
from pykson import Pykson


class AdminPanelModel(Subject):
    def __init__(self):
        self.__observer = []
        self.__users = []
        self.__select_user = User()
        self.__select_contest = Contest()
        self.__select_task = Task()
        self.__select_team = {}
        self.__contests = []
        self.__tasks = []
        self.__teams = []

        self.__massage = ""
        self.__last_id_user = 0
        self.__last_id_contest = 0

    @property
    def users(self):
        return list(map(Pykson().to_dict_or_list, self.__users))

    @users.setter
    def users(self, val):
        self.__users = list(map(lambda x: Pykson().from_json(x, User), val))
        self.__last_id_user = self.__last_id(self.__users)
        self.notify("tab_user")

    @property
    def select_user(self):
        return self.__select_user

    @select_user.setter
    def select_user(self, val):

        self.__select_user = Pykson().from_json(val, User)
        self.notify("tab_user")

    def add_user(self, val):
        user = val
        self.__last_id_user = self.__last_id(self.__users)
        if isinstance(val, User) is False:
            user = Pykson().from_json(val, User)
            user.team = None
        user.id = self.__last_id_user + 1
        self.__users.append(user)
        self.__last_id_user = self.__last_id(self.__users)
        self.notify("tab_user")

    def delete_user(self, val):
        select_user = val
        if isinstance(val, User) is False:
            select_user = Pykson().from_json(val, User)
        for i, user in enumerate(self.__users):
            if user.id == select_user.id:
                self.__users.pop(i)
                break
        self.notify("tab_user")

    def update_user(self, val):
        select_user = val
        if isinstance(val, User) is False:
            select_user = Pykson().from_json(val, User)
            select_user.team = None
        for i, user in enumerate(self.__users):
            if user.id == select_user.id:
                self.__users[i] = select_user
                break
        self.notify("tab_user")

    @property
    def contests(self):
        return list(map(Pykson().to_dict_or_list, self.__contests))

    @contests.setter
    def contests(self, val):
        for contest in val:
            for key in contest:
                contest[key] = self.__conver_datetime_field(contest[key])
        self.__contests = list(map(lambda x: Pykson().from_json(x, Contest), val))
        self.__last_id_contest = self.__last_id(self.__contests)
        self.notify("tab_contest")

    @property
    def contest_select(self):
        return self.__select_contest

    @contest_select.setter
    def contest_select(self, val):
        start_datetime = datetime(val["dateStart"]["year"], val["dateStart"]["month"], val["dateStart"]["day"],
                                           val["timeStart"]["hours"],  val["timeStart"]["min"], 0)
        end_datetime = datetime(val["dateEnd"]["year"], val["dateEnd"]["month"], val["dateEnd"]["day"],
                                         val["timeEnd"]["hours"], val["timeEnd"]["min"], 0)
        val = {"id": val["id"],
               "name_contest": val["nameContest"],
               "type": val["typeSelectedContes"],
               "datetime_start": start_datetime,
               "datetime_end": end_datetime}
        self.__select_contest = Pykson().from_json(val, Contest)
        self.notify("tab_contest")

    def add_contest(self, val):
        contest = val
        self.__last_id_contest = self.__last_id(self.__contests)
        if isinstance(val, Contest) is False:
            contest = Pykson().from_json(val, Contest)
        contest.id = self.__last_id_contest + 1
        self.__contests.append(contest)
        self.__last_id_contest = self.__last_id(self.__contests)
        self.notify("tab_contest")

    def delete_contest(self, val):
        select_contest = val
        if isinstance(val, Contest) is False:
            select_contest = Pykson().from_json(val, Contest)
        for i, contest in enumerate(self.__contests):
            if contest.id == select_contest.id:
                self.__contests.pop(i)
                break
        self.notify("tab_contest")

    def update_contest(self, val):
        select_contest = val
        if isinstance(val, Contest) is False:
            select_contest = Pykson().from_json(val, Contest)
        for i, contest in enumerate(self.__contests):
            if contest.id == select_contest.id:
                self.__contests[i] = select_contest
                break
        self.notify("tab_contest")

    @property
    def select_task(self):
        return self.__select_task

    @select_task.setter
    def select_task(self, val):
        if val.get("type_response") == "selectChange":
            for task in self.__tasks:
                if task.id == val["id"]:
                    self.__select_task = task
                    self.notify("tab_task_to_form")
                    break
        else:
            val["id_contest"] = self.__select_contest.id
            self.__select_task = Pykson().from_json(val, Task)

    def add_task(self, val):
        task = val
        if isinstance(val, Task) is False:
            task = Pykson().from_json(val, Task)
        self.__tasks.append(task)
        self.notify("tab_task")

    def delete_task(self, val):
        select_task = val
        if isinstance(val, Task) is False:
            select_task = Pykson().from_json(val, Task)
        for i, task in enumerate(self.__tasks):
            if task.id == select_task.id:
                self.__tasks.pop(i)
                break
        self.notify("tab_task")

    def update_task(self, val):
        select_task = val
        if isinstance(val, Task) is False:
            select_task = Pykson().from_json(val, Task)
        for i, tasks in enumerate(self.__tasks):
            if tasks.id == select_task.id:
                self.__tasks[i] = select_task
                break
        self.notify("tab_task")

    @property
    def tasks(self):
        return list(map(Pykson().to_dict_or_list, self.__tasks))

    @tasks.setter
    def tasks(self, val):
        self.__tasks = list(map(lambda x: Pykson().from_json(x, Task), val))
        self.notify("tab_task")

    @property
    def teams(self):
        return list(map(Pykson().to_dict_or_list, self.__teams))

    @teams.setter
    def teams(self, val):
        self.__teams = list(map(lambda x: Pykson().from_json(x, Team), val))
        self.notify("tab_team")

    @property
    def select_team(self):
        return self.__select_team

    @select_team.setter
    def select_team(self, val):
        if val.get("type_response") == "selectChange":
            for team in self.__teams:
                if team.id == val["id"]:
                    self.__select_team = team
                    self.notify("tab_team_to_form")
                    break
        else:
            self.__select_team = Pykson().from_json(val, Team)

    def add_team(self, val):
        team = val
        if isinstance(val, Team) is False:
            team = Pykson().from_json(val, Team)
        self.__teams.append(team)
        self.notify("tab_team")

    def delete_team(self, val):
        select_team = val
        if isinstance(val, Team) is False:
            select_team = Pykson().from_json(val, Team)
        for i, team in enumerate(self.__teams):
            if team.id == select_team.id:
                self.__teams.pop(i)
                break
        self.notify("tab_team")

    def update_team(self, val):
        select_team = val
        if isinstance(val, Team) is False:
            select_team = Pykson().from_json(val, Team)
        for i, team in enumerate(self.__teams):
            if team.id == select_team.id:
                self.__teams[i] = select_team
                break
        self.notify("tab_team")

    @property
    def massage(self):
        return self.__massage

    @massage.setter
    def massage(self, val):
        self.__massage = val
        self.notify("massage")

    def __last_id(self, data):
        try:
            return data[-1].id
        except IndexError:
            return 0

    def __conver_datetime_field(self, val):
        try:
            return datetime.fromisoformat(val)
        except Exception:
            return val

    def attach(self, observer):
        self.__observer.append(observer)

    def detach(self, observer):
        self.__observer.remove(observer)

    def notify(self, type_notify):
        for observer in self.__observer:
            observer.update(type_notify)