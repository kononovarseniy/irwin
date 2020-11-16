from irwin.CallbackOperator import CallbackOperator
from irwin.NCalculationParameters import NCalculationParameters
from irwin.n_semiconductor_module.NDataVisualiser import NDataVisualiser
from irwin.n_semiconductor_module.NIrwinCalculator import NIrwinCalculator


class n_CalculationCallBackOperator(CallbackOperator):
    def __init__(self):
        self.window = None
        self.parameters = NCalculationParameters()
        self.calculator = NIrwinCalculator()

    def connect_callback(self, window):
        self.window = window
        NDataVisualiser(self.calculator.Model, self.window.nTypePlot)
        window.n_CalculatepushButton.clicked.connect(self.calc_irwin_curve)

    def calc_irwin_curve(self):
        print('Recalculating the n concentration')
        self.calculator.calculate_concentration(
            temperature=self.parameters.temperature,
            acceptor_energy=self.parameters.acceptor_energy,
            acceptor_concentration=self.parameters.acceptor_concentration,
            donor_energy=self.parameters.donor_energy,
            material=self.parameters.material)
