import openpyxl


class FileXlsx:
    def __init__(self):
        self.__cells_name = []
        self.__main_body_cells = []
        self.__workbook = openpyxl.Workbook()
        self.__sheet = self.__workbook.active

    def add_main_body(self, cell):
        self.__main_body_cells.append(cell)

    def add_cells_name(self, cell):
        self.__cells_name.append(cell)

    def return_file(self, name_file):
        for cell in self.__cells_name + self.__main_body_cells:
            cell.create_cell(self.__sheet)
        self.__workbook.save(name_file)
