from pykson import IntegerField, ObjectField, StringField, JsonObject, DateTimeField
from Classes.Models.TeamToUser import TeamToUser
from Classes.Models.UserToTeam import UserToTeam
from Classes.Models.Task import Task

from datetime import datetime


class Answer(JsonObject):
    date_send = DateTimeField()
    id = IntegerField()
    team = ObjectField(TeamToUser)
    user = ObjectField(UserToTeam)
    task = ObjectField(Task)
    type_compiler = IntegerField()
    total = StringField()
    time = StringField()
    memory_size = IntegerField()
    number_test = IntegerField()
    points = IntegerField()

    path_report_file = StringField()
    path_programme_file = StringField()