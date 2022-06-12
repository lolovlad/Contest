from pykson import JsonObject, IntegerField, StringField, ObjectField
from Classes.Models.TeamToUser import TeamToUser


class User(JsonObject):

    id = IntegerField()
    login = StringField()
    name = StringField()
    sename = StringField()
    secondname = StringField()
    password = StringField()
    team = ObjectField(TeamToUser)

    type = IntegerField()
