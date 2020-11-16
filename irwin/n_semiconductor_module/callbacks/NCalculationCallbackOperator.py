from irwin.CallbackOperator import CallbackOperator
from irwin.common.IrwinCalculator import IrwinCalculator
from irwin.n_semiconductor_module.NDataVisualiser import NDataVisualiser
from irwin.n_semiconductor_module.NInputData import NInputData


class NCalculationCallbackOperator(CallbackOperator):
    def __init__(self):
        self.window = None
        self.parameters = NInputData()
        self.calculator = IrwinCalculator()

    def connect_callback(self, window):
        self.window = window
        NDataVisualiser(self.calculator.model, self.window.nTypePlot)
        window.n_CalculatepushButton.clicked.connect(self.calc_irwin_curve)

    def calc_irwin_curve(self):
        print('Recalculating the n concentration')
        self.calculator.calculate_concentration(self.parameters)
