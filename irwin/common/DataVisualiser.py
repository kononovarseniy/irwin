from irwin.config import Units


class DataVisualiser:
    def __init__(self, output_data, plot_canvas, input_data, concentration_label):
        self._canvas = plot_canvas

        self.output_data = output_data
        self.output_data.add_visualiser(self)
        self.input_data = input_data

        self.concentration_label = concentration_label
        self.resistivity_label = f'Resistivity, {Units.RESISTIVITY_TEXT}'
        self.conductivity_label = f'Conductivity, {Units.CONDUCTIVITY_TEXT}'

    def plot_resistivity(self):
        self._canvas.plot(
            self.output_data.Ns / Units.CONCENTRATION,
            self.output_data.rho / Units.RESISTIVITY,
            labels=[self.concentration_label, self.resistivity_label])

    def plot_conductivity(self):
        self._canvas.plot(
            self.output_data.Ns / Units.CONCENTRATION,
            self.output_data.sigma / Units.CONDUCTIVITY,
            labels=[self.concentration_label, self.conductivity_label])

    def update_model(self):
        print(f'updating_model')

        if self.input_data.plot_resistivity:
            self.plot_resistivity()
        if self.input_data.plot_conductivity:
            self.plot_conductivity()
