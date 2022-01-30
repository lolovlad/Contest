from pykson import JsonObject, IntegerField, StringField


class User(JsonObject):

    id = IntegerField()
    login = StringField()
    name = StringField()
    sename = StringField()

    password = StringField()

    type = IntegerField()
