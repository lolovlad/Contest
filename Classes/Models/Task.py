from pykson import JsonObject, IntegerField, StringField, ByteArrayField


class Task(JsonObject):

    id = IntegerField()

    time_work = IntegerField()
    size_raw = IntegerField()
    type_input = IntegerField()
    type_output = IntegerField()
    name_test = StringField()
    description = StringField()
    description_input = StringField()
    description_output = StringField()

    path_test_file = StringField()
    path_programme_file = StringField()

    type_task = IntegerField()

    test_file = ByteArrayField()
    programme_file = ByteArrayField()
