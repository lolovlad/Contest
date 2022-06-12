import ctypes
from time import sleep
from threading import Thread


class CloseWindowWindows:
    def __init__(self):
        self.__enum_windows_proc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
        self.__get_window_text = ctypes.windll.user32.GetWindowTextW
        self.__get_window_text_length = ctypes.windll.user32.GetWindowTextLengthW
        self.__is_window_visible = ctypes.windll.user32.IsWindowVisible
        self.__enum_windows = ctypes.windll.user32.EnumWindows
        self.__WINDOW_CLOSE = 0x10
        self.__titles = []

    def __foreach_window(self, hwnd, lparam):
        if self.__is_window_visible(hwnd):
            length = self.__get_window_text_length(hwnd)
            buff = ctypes.create_unicode_buffer(length + 1)
            self.__get_window_text(hwnd, buff, length + 1)
            self.__titles.append((buff.value, hwnd))
        return True

    def close_window(self, name_window):
        def thread_close_window(window, window_close):
            sleep(0.9)
            hwnd = ctypes.windll.user32.FindWindowA(None, title[0])
            ctypes.windll.user32.PostMessageA(window, window_close, 0, 0)

        self.__enum_windows(self.__enum_windows_proc(self.__foreach_window), 0)
        for title, window in self.__titles:
            if title == name_window:
                thread = Thread(target=thread_close_window, args=(window, self.__WINDOW_CLOSE,))
                thread.start()