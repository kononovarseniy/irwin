from abc import ABCMeta, abstractmethod


class Visualiser(metaclass=ABCMeta):
    def __init__(self, model, plot_canvas):
        self._model = model
        self._model.add_visualiser(self)
        self._plot_canvas = plot_canvas

    @abstractmethod
    def update_model(self):
        pass
