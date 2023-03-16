from typing import List
from Classes.BuilderFile.Cell import SoloCell, MergeCell
from Classes.BuilderFile.FileBuilder import FileBuilder
from Classes.BuilderFile.FileOutput import FileXlsx
from .TypeReport import TypeContest
from itertools import chain


class ReportBuilder(FileBuilder):
    def __init__(self, data: List[dict], type_report: int, file):
        self.__data = data
        self.__file = file
        self.__type_report = type_report

    @property
    def file(self):
        return self.__file

    def reset(self):
        self.__file = FileXlsx()

    def build_name_column(self):
        if self.__type_report == TypeContest.OLIMPIADA:
            self.__build_name_column_solo()
        else:
            self.__build_name_column_team()

    def build_main_body(self):
        if self.__type_report == TypeContest.OLIMPIADA:
            self.__build_main_body_solo()
        else:
            self.__build_main_body_team()

    def __build_name_column_team(self):
        self.__file.add_cells_name(SoloCell(1, 1, "№"))
        self.__file.add_cells_name(SoloCell(1, 2, "Название команды"))
        len_task = len(self.__data[0]["total"])
        col = self.__file.find_to_name_cell("Название команды").col
        for i in range(1, len_task + 1):
            col += 1
            self.__file.add_cells_name(SoloCell(1, col, f"Задани {i}"))
        self.__file.add_cells_name(SoloCell(1, col + 1, "Итог"))
        self.__file.add_cells_name(SoloCell(1, col + 2, "Место"))

    def __build_name_column_solo(self):
        self.__file.add_cells_name(SoloCell(1, 1, "№"))
        self.__file.add_cells_name(SoloCell(1, 2, "ФИО"))
        len_task = len(self.__data[0]["total"])
        col = self.__file.find_to_name_cell("ФИО").col
        for i in range(1, len_task + 1):
            col += 1
            self.__file.add_cells_name(SoloCell(1, col, f"Задани {i}"))
        self.__file.add_cells_name(SoloCell(1, col + 1, "Итог"))
        self.__file.add_cells_name(SoloCell(1, col + 2, "Место"))

    def __build_main_body_team(self):
        for i, row in enumerate(self.__converted_data()):
            self.__file.add_main_body(SoloCell(i + 2, 1, i + 1))
            for j, cell in enumerate(row):
                self.__file.add_main_body(SoloCell(i + 2, j + 2, cell))

    def __build_main_body_solo(self):
        for i, row in enumerate(self.__converted_data()):
            self.__file.add_main_body(SoloCell(i + 2, 1, i + 1))
            for j, cell in enumerate(row):
                self.__file.add_main_body(SoloCell(i + 2, j + 2, cell))

    def __converted_data(self):
        data_new = []
        for report in self.__data:
            del report["name_contest"]
            del report["type_contest"]
            report["total"] = list(report["total"].values())
            item = []
            for i in report.values():
                if isinstance(i, list):
                    item += i
                else:
                    item.append(i)
            data_new.append(tuple(item))
        return data_new
