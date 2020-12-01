from irwin.common.DataVisualiser import DataVisualiser
from irwin.n_semiconductor_module.NInputData import NInputData


class NDataVisualiser(DataVisualiser):
    def __init__(self, output_data, plot_canvas):
        super().__init__(output_data, plot_canvas, NInputData(), 'Donor concentration')
