from pykson import JsonObject, IntegerField, StringField, DateTimeField


class Contest(JsonObject):

    id = IntegerField()
    name_contest = StringField()

    datetime_start = DateTimeField()
    datetime_end = DateTimeField()
    datetime_registration = DateTimeField()

    type = IntegerField()
