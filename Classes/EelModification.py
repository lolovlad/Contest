from Classes.CloseWindowWindows import CloseWindowWindows
from sys import platform


class EelModification:
    __windows = CloseWindowWindows()
    __linux = None

    @classmethod
    def close_window(cls, name_window):
        if platform == "linux" or platform == "linux2":
            pass
        elif platform == "darwin":
            pass
        elif platform == "win32":
            cls.__windows.close_window(name_window)