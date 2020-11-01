from abc import ABCMeta, abstractmethod

class Visualiser(metaclass=ABCMeta):
    def __init__(self, controller, model):
        self._controller = controller
        self._model = model

    @abstractmethod
    def update_model(self):
        pass