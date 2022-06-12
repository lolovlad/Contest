from Classes.BuilderFile.Cell import SoloCell, MergeCell
from Classes.BuilderFile.FileBuilder import FileBuilder
from Classes.BuilderFile.FileOutput import FileXlsx


class ReportXlsx(FileBuilder):
    def __init__(self, data):
        self.__data = data['reports_total']
        self.__file = FileXlsx()

    @property
    def file(self):
        return self.__file

    def reset(self):
        self.__file = FileXlsx()

    def build_name_column(self):

        self.__file.add_cells_name(SoloCell(1, 1, "№"))
        self.__file.add_cells_name(SoloCell(1, 2, "Имя"))
        self.__file.add_cells_name(SoloCell(1, 3, "Фамилия"))
        self.__file.add_cells_name(SoloCell(1, 4, "Отчество"))
        self.__file.add_cells_name(SoloCell(1, 5, "Имя команды"))
        name_contest = list(self.__data.keys())[0]
        len_task = len(self.__data[name_contest][0]["total"])
        col = 5
        for i in range(1, len_task + 1):
            col += 1
            self.__file.add_cells_name(SoloCell(1, col, f"Задани {i}"))
        self.__file.add_cells_name(SoloCell(1, col + 1, "Итог"))
        self.__file.add_cells_name(SoloCell(1, col + 2, "Место"))

    def build_main_body(self):
        name_contest = list(self.__data.keys())[0]
        task = self.__data[name_contest]
        for i, user in enumerate(task):
            col = 5
            name_users = user['name_users'].split()
            self.__file.add_main_body(SoloCell(i + 2, 1, i + 1))
            self.__file.add_main_body(SoloCell(i + 2, 2, name_users[0]))
            self.__file.add_main_body(SoloCell(i + 2, 3, name_users[1]))
            self.__file.add_main_body(SoloCell(i + 2, 4, name_users[2]))
            self.__file.add_main_body(SoloCell(i + 2, 5, user["name_team"]))
            for j, points in enumerate(user["total"]):
                col += 1
                self.__file.add_main_body(SoloCell(i + 2, col, user["total"][points]["points"]))
            self.__file.add_main_body(SoloCell(i + 2, col + 1, user["sum_point"]))