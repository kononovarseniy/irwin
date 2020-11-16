from irwin.n_semiconductor_module.NCalculationParameters import NCalculationParameters
from irwin.common.Visualiser import Visualiser


class NDataVisualiser(Visualiser):
    def __init__(self, model, plot_canvas):
        super().__init__(model, plot_canvas)
        self._plotting_parameters = NCalculationParameters()

    def plot_resistivity(self):
        self._plot_canvas.plot(self._model.Nas, self._model.rho, title='Irwin Curve',
                               labels=['Acceptor concentrations', 'Resistivity'])

    def plot_conductivity(self):
        self._plot_canvas.plot(self._model.Nas, self._model.sigma, title='Irwin Curve',
                               labels=['Acceptor concentrations', 'Conductivity'])

    #  overriden
    def update_model(self):
        print(f'updating_model')

        if self._plotting_parameters.plot_resistivity:
            self.plot_resistivity()
        if self._plotting_parameters.plot_conductivity:
            self.plot_conductivity()
