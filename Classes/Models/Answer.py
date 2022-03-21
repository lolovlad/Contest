from pykson import JsonObject, IntegerField, StringField


class Task(JsonObject):
    id = IntegerField()

    date_send = StringField()
    id_contest = IntegerField()
    user_send = StringField()
    id_task = IntegerField()
    type_compiler = IntegerField()
    total = StringField()
    time = StringField()
    memory_size = IntegerField()
    number_test = IntegerField()
    points = IntegerField()

    path_report_file = StringField()
    path_programme_file = StringField()