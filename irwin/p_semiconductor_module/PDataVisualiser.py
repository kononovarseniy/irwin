from irwin.common.Visualiser import Visualiser
from irwin.config import Units
from irwin.p_semiconductor_module.PCalculationParameters import PCalculationParameters


class PDataVisualiser(Visualiser):
    def __init__(self, model, plot_canvas):
        super().__init__(model, plot_canvas)
        self._plotting_parameters = PCalculationParameters()

    def plot_resistivity(self):
        self._plot_canvas.plot(
            self._model.Nds / Units.CONCENTRATION,
            self._model.rho / Units.RESISTIVITY,
            title='Irwin Curve',
            labels=['Donor concentrations', 'Resistivity'])

    def plot_conductivity(self):
        self._plot_canvas.plot(
            self._model.Nds / Units.CONCENTRATION,
            self._model.sigma / Units.CONDUCTIVITY,
            title='Irwin Curve',
            labels=['Donor concentrations', 'Conductivity'])

    #  overriden

    def update_model(self):
        print(f'updating_model')

        if self._plotting_parameters.plot_resistivity:
            self.plot_resistivity()
        if self._plotting_parameters.plot_conductivity:
            self.plot_conductivity()
