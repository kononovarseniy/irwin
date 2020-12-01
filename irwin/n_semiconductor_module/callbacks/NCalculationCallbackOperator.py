from irwin.CallbackOperator import CallbackOperator
from irwin.common.DataWriter import DataWriter
from irwin.common.IrwinCalculator import IrwinCalculator
from irwin.n_semiconductor_module.NDataVisualiser import NDataVisualiser


class NCalculationCallbackOperator(CallbackOperator):
    def __init__(self, input_data, output_filename):
        self.window = None
        self.input_data = input_data
        self.calculator = IrwinCalculator()
        self.output_filename = output_filename

    def connect_callback(self, window):
        self.window = window
        # DataVisualiser registers itself
        NDataVisualiser(self.input_data, self.calculator.output_data, self.window.n_type_plot)
        window.n_calculate_button.clicked.connect(self.calc_irwin_curve)
        window.n_calculate_and_save_button.clicked.connect(self.calc_irwin_and_save)

    def calc_irwin_curve(self):
        self.calculator.calculate_concentration(self.input_data)

    def calc_irwin_and_save(self):
        self.calculator.calculate_concentration(self.input_data)
        DataWriter.save_results(self.output_filename, self.calculator.output_data)
