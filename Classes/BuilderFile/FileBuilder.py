from abc import ABC, abstractmethod


class FileBuilder(ABC):
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def build_name_column(self):
        pass

    @abstractmethod
    def build_main_body(self):
        pass