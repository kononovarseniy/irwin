from irwin.CallbackOperator import CallbackOperator
from irwin.common.IrwinCalculator import IrwinCalculator
from irwin.p_semiconductor_module.PDataVisualiser import PDataVisualiser
from irwin.p_semiconductor_module.PInputData import PInputData


class PCalculationCallbackOperator(CallbackOperator):
    def __init__(self):
        self.window = None
        self.parameters = PInputData()
        self.calculator = IrwinCalculator()

    def connect_callback(self, window):
        self.window = window
        PDataVisualiser(self.calculator.model, self.window.pTypePlot)  # Visualiser registers itself
        window.CalculatepushButton.clicked.connect(self.calculate_concentration)

    def calculate_concentration(self):
        print('Recalculating the p concentration')
        self.calculator.calculate_concentration(self.parameters)
