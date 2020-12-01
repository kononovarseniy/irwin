from abc import ABC, abstractmethod


class ApplicationModule(ABC):
    def __init__(self, gui):
        self.operators = self.create_operators()  # Save them in the field to protect against garbage collection
        for operator in self.operators:
            operator.connect_callback(gui)

    @abstractmethod
    def create_operators(self):
        pass
