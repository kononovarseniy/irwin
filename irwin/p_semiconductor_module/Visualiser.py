from abc import ABCMeta, abstractmethod
import matplotlib.pyplot as plt


class Visualiser(metaclass=ABCMeta):
    def __init__(self, controller, model):
        self._controller = controller
        self._model = model
        self._model.add_visualiser(self)

    def draw_grid(self):
        plt.grid(True, which='both', axis='both')
        plt.xscale('log')
        plt.yscale('log')
        plt.show(block=False)
        self._figure.canvas.draw()
        self._figure.canvas.flush_events()

    @abstractmethod
    def update_model(self):
        pass
