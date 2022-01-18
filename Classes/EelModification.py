import ctypes


class EelModification:
    __enum_windows_proc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
    __get_window_text = ctypes.windll.user32.GetWindowTextW
    __get_window_text_length = ctypes.windll.user32.GetWindowTextLengthW
    __is_window_visible = ctypes.windll.user32.IsWindowVisible
    __enum_windows = ctypes.windll.user32.EnumWindows
    __WINDOW_CLOSE = 0x10

    __titles = []

    @classmethod
    def __foreach_window(cls, hwnd, lparam):
        if cls.__is_window_visible(hwnd):
            length = cls.__get_window_text_length(hwnd)
            buff = ctypes.create_unicode_buffer(length + 1)
            cls.__get_window_text(hwnd, buff, length + 1)
            cls.__titles.append((buff.value, hwnd))
        return True

    @classmethod
    def close_window(cls, name_window):
        cls.__enum_windows(cls.__enum_windows_proc(cls.__foreach_window), 0)
        for title, window in cls.__titles:
            if title == name_window:
                hwnd = ctypes.windll.user32.FindWindowA(None, title[0])
                ctypes.windll.user32.PostMessageA(window, cls.__WINDOW_CLOSE, 0, 0)