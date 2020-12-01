from irwin.CallbackOperator import CallbackOperator
from irwin.common.IrwinCalculator import IrwinCalculator
from irwin.p_semiconductor_module.PDataVisualiser import PDataVisualiser
from irwin.p_semiconductor_module.PInputData import PInputData
from irwin.common.DataWriter import DataWriter


class PCalculationCallbackOperator(CallbackOperator):
    def __init__(self, output_filename):
        self.window = None
        self.parameters = PInputData()
        self.calculator = IrwinCalculator()
        self.output_filename = output_filename

    def connect_callback(self, window):
        self.window = window
        PDataVisualiser(self.calculator.model, self.window.p_type_plot)  # Visualiser registers itself
        window.p_calculate_button.clicked.connect(self.calculate_concentration)
        window.p_calculate_and_save_button.clicked.connect(self.calc_irwin_and_save)

    def calculate_concentration(self):
        print('Recalculating the p concentration')
        self.calculator.calculate_concentration(self.parameters)

    def calc_irwin_and_save(self):
        self.calculator.calculate_concentration(self.parameters)
        DataWriter.save_results(filename=self.output_filename,
                                concentration=self.calculator.model.Ns,
                                conductivity=self.calculator.model.sigma,
                                resistivity=self.calculator.model.rho)