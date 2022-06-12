import openpyxl.utils
from abc import ABC, abstractmethod


class Cell(ABC):
    def __init__(self, row, col, value):
        self._row = row
        self._col = col
        self.__value = value

    @abstractmethod
    def __str__(self):
        pass

    @property
    def value(self):
        return self.__value

    def _cell_from_string(self):
        return f"{openpyxl.utils.get_column_letter(self._col)}{self._row}"

    @abstractmethod
    def create_cell(self, sheet):
        pass


class SoloCell(Cell):
    def __init__(self, row, col, value):
        super().__init__(row, col, value)

    def __str__(self):
        return f"{self._cell_from_string()} {self.value}"

    def create_cell(self, sheet):
        sheet.cell(self._row, self._col).value = self.value


class MergeCell(Cell):
    def __init__(self, row_start, col_start, row_end, col_end, value):
        super().__init__(row_start, col_start, value)
        self.__row_end = row_end
        self.__col_end = col_end

    def __str__(self):
        return f"{self._cell_from_string()} {self.value}"

    def __cell_merge_from_string(self):
        return f"{self._cell_from_string()}:{openpyxl.utils.get_column_letter(self.__col_end)}{self.__row_end}"

    def create_cell(self, sheet):
        sheet.merge_cells(self.__cell_merge_from_string())
        sheet.cell(self._row, self._col).value = self.value