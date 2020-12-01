from irwin.common.Visualiser import Visualiser
from irwin.config import Units
from irwin.p_semiconductor_module.PInputData import PInputData


class PDataVisualiser(Visualiser):
    def __init__(self, model, plot_canvas):
        super().__init__(model, plot_canvas)
        self._plotting_parameters = PInputData()

    def plot_resistivity(self):
        self._plot_canvas.plot(
            self._model.Ns / Units.CONCENTRATION,
            self._model.rho / Units.RESISTIVITY,
            labels=['Donor concentrations', f'Resistivity, {Units.RESISTIVITY_TEXT}'])

    def plot_conductivity(self):
        self._plot_canvas.plot(
            self._model.Ns / Units.CONCENTRATION,
            self._model.sigma / Units.CONDUCTIVITY,
            labels=['Donor concentrations', f'Conductivity, {Units.CONDUCTIVITY_TEXT}'])

    #  overriden

    def update_model(self):
        print(f'updating_model')

        if self._plotting_parameters.plot_resistivity:
            self.plot_resistivity()
        if self._plotting_parameters.plot_conductivity:
            self.plot_conductivity()
