from irwin.CallbackOperator import CallbackOperator
from irwin.common.IrwinCalculator import IrwinCalculator
from irwin.n_semiconductor_module.NDataVisualiser import NDataVisualiser
from irwin.n_semiconductor_module.NInputData import NInputData
from irwin.common.DataWriter import DataWriter


class NCalculationCallbackOperator(CallbackOperator):
    def __init__(self, output_filename):
        self.window = None
        self.parameters = NInputData()
        self.calculator = IrwinCalculator()
        self.output_filename = output_filename

    def connect_callback(self, window):
        self.window = window
        NDataVisualiser(self.calculator.model, self.window.n_type_plot)
        window.n_calculate_button.clicked.connect(self.calc_irwin_curve)
        window.n_calculate_and_save_button.clicked.connect(self.calc_irwin_and_save)

    def calc_irwin_curve(self):
        self.calculator.calculate_concentration(self.parameters)

    def calc_irwin_and_save(self):
        self.calculator.calculate_concentration(self.parameters)
        DataWriter.save_results(filename=self.output_filename,
                                concentration=self.calculator.model.Ns,
                                conductivity=self.calculator.model.sigma,
                                resistivity=self.calculator.model.rho)

