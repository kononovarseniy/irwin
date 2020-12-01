from irwin.common.DataVisualiser import DataVisualiser


class NDataVisualiser(DataVisualiser):
    def __init__(self, input_data, output_data, plot_canvas):
        super().__init__(output_data, plot_canvas, input_data, 'Donor concentration')
