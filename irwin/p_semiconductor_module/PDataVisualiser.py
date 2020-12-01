from irwin.common.DataVisualiser import DataVisualiser
from irwin.p_semiconductor_module.PInputData import PInputData


class PDataVisualiser(DataVisualiser):
    def __init__(self, output_data, plot_canvas):
        super().__init__(output_data, plot_canvas, PInputData(), 'Acceptor concentrations')
