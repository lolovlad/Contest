from pykson import JsonObject, IntegerField, StringField, DateTimeField, ObjectListField
from Classes.Models.Task import Task
from datetime import datetime


class Contest(JsonObject):
    id = IntegerField()
    name_contest = StringField()

    datetime_start = DateTimeField()
    datetime_end = DateTimeField()
    datetime_registration = DateTimeField(default_value=datetime.now())

    type = IntegerField()

    state_contest = IntegerField()

    tasks = ObjectListField(Task)
