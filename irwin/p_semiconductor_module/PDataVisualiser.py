from irwin.p_semiconductor_module.PCalculationParameters import PCalculationParameters
from irwin.common.Visualiser import Visualiser


class PDataVisualiser(Visualiser):
    def __init__(self, model, plot_canvas):
        super().__init__(model, plot_canvas)
        self._plotting_parameters = PCalculationParameters()

    def plot_resistivity(self):
        self._plot_canvas.plot(self._model.Nds, self._model.rho, title='Irwin Curve',
                               labels=['Donor concentrations', 'Resistivity'])

    def plot_conductivity(self):
        self._plot_canvas.plot(self._model.Nds, self._model.sigma, title='Irwin Curve',
                               labels=['Donor concentrations', 'Conductivity'])

    #  overriden

    def update_model(self):
        print(f'updating_model')

        if self._plotting_parameters.plot_resistivity:
            self.plot_resistivity()
        if self._plotting_parameters.plot_conductivity:
            self.plot_conductivity()
