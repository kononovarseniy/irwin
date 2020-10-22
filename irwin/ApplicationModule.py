from abc import ABC, abstractmethod


class ApplicationModule(ABC):

    def __init__(self):
        self.main_window = None  # a class inherited from QMainWindow

    @abstractmethod
    def run(self, window):
        pass

    def connect_all_callbacks(self):
        for conn in self.callback_operators:
            conn.connect_callback(self.main_window)  # TODO: код в родителя
