from abc import ABC, abstractmethod

class ApplicationModule(ABC):

    def __init(self):
        self.MainWindow = None # a class inherited from QMainWindow

    @abstractmethod
    def Run(self, window):
        pass

    def ConnectAllCallBacks(self):
        for conn in self.callback_operators:
            conn.ConnectCallBack(self.UserInterface)  # TODO: код в родителя


