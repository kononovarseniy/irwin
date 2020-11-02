from irwin.p_semiconductor_module.Visualiser import Visualiser
import matplotlib.pyplot as plt
from irwin.CalculationParameters import CalculationParameters

class PDataVisualiser(Visualiser):
    def __init__(self, controller, model):
        super().__init__(controller, model)
        self._figure = plt.figure()
        self._graph = self._figure.add_subplot(111)
        self._plotting_parameters = CalculationParameters()

    def plot_resistivity(self):
        self._graph.plot(
            x=self.Model.Nds, y=self.Model.rho
        )
        plt.title('Irwin Curve')
        plt.ylabel('Resistivity')
        plt.xlabel('Donor concentrations')

    def plot_conductivity(self):
        self._graph.plot(
            x=self.Model.Nds, y=self.Model.sigma
        )
        plt.title('Irwin Curve')
        plt.ylabel('Conductivity')
        plt.xlabel('Donor concentrations')

    #  overriden
    def update_model(self):
        print(f'updating_model')
        self._graph.clear()

        if self._plotting_parameters.plot_resistivity:
            self.plot_resistivity()
        if self._plotting_parameters.plot_conductivity:
            self.plot_conductivity()
