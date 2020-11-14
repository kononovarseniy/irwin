from abc import ABC, abstractmethod


class ApplicationModule(ABC):

    def __init__(self):
        self.main_window = None  # a class inherited from QMainWindow

    def run(self, main_window):
        self.main_window = main_window
        self.connect_all_callbacks()

    def connect_all_callbacks(self):
        for conn in self.callback_operators:
            conn.connect_callback(self.main_window)  # TODO: код в родителя


