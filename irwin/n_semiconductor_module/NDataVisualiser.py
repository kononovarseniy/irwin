from irwin.p_semiconductor_module.Visualiser import Visualiser
import matplotlib.pyplot as plt
from irwin.NCalculationParameters import NCalculationParameters


class NDataVisualiser(Visualiser):
    def __init__(self, controller, model):
        super().__init__(controller, model)
        self._figure = plt.figure()
        self._graph = self._figure.add_subplot(111)
        self._plotting_parameters = NCalculationParameters()

    def plot_resistivity(self):
        self._graph.plot(
            self._model.Nas, self._model.rho
        )
        plt.title('Irwin Curve P type')
        plt.ylabel('Resistivity')
        plt.xlabel('Acceptor concentrations')
        self.draw_grid()

    def plot_conductivity(self):
        self._graph.plot(
            self._model.Nas, self._model.sigma
        )
        plt.title('Irwin Curve P type')
        plt.ylabel('Conductivity')
        plt.xlabel('Acceptor concentrations')
        self.draw_grid()

    #  overriden
    def update_model(self):
        print(f'updating_model')
        self._graph.clear()
        plt.ion()

        if self._plotting_parameters.plot_resistivity:
            self.plot_resistivity()
        if self._plotting_parameters.plot_conductivity:
            self.plot_conductivity()
