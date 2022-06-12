from pykson import JsonObject, IntegerField, ObjectField, StringField, BooleanField, DateTimeField, ObjectListField
from Classes.Models.UserToTeam import UserToTeam


class ContestTeam(JsonObject):
    id = IntegerField()
    name_contest = StringField()
    datetime_registration = DateTimeField()
    datetime_start = DateTimeField()
    datetime_end = DateTimeField()
    type = IntegerField()


class Team(JsonObject):
    id = IntegerField()
    id_contest = IntegerField(default_value=0)
    name_team = StringField(default_value="")
    is_solo = BooleanField(default_value=False)
    state_contest = IntegerField(default_value=0)
    users = ObjectListField(UserToTeam)
    contest = ObjectField(ContestTeam)
