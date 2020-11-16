from irwin.p_semiconductor_module.Visualiser import Visualiser
import matplotlib.pyplot as plt
from irwin.PCalculationParameters import PCalculationParameters
from irwin.p_semiconductor_module.PPlotCanvas import PPlotCanvas


class PDataVisualiser(Visualiser):
    def __init__(self, controller, model):
        super().__init__(controller, model)
        self.PlotCanvas = PPlotCanvas()
        self._plotting_parameters = PCalculationParameters()

    def plot_resistivity(self):
        self.PlotCanvas.plot(self._model.Nds, self._model.rho, title='Irwin Curve',
                             labels=['Donor concentrations', 'Resistivity'])

    def plot_conductivity(self):
        self.PlotCanvas.plot(self._model.Nds, self._model.sigma, title='Irwin Curve',
                             labels=['Donor concentrations', 'Conductivity'])

    #  overriden

    def update_model(self):
        print(f'updating_model')

        if self._plotting_parameters.plot_resistivity:
            self.plot_resistivity()
        if self._plotting_parameters.plot_conductivity:
            self.plot_conductivity()
