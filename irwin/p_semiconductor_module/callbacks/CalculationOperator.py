from irwin.PCalculationParameters import PCalculationParameters
from irwin.CallbackOperator import CallbackOperator
from irwin.p_semiconductor_module.PDataVisualiser import PDataVisualiser
from irwin.p_semiconductor_module.PIrwinCalculator import PIrwinCalculator


class CalculationOperator(CallbackOperator):
    def __init__(self):
        self.window = None
        self.parameters = PCalculationParameters()
        # PCalculationParameters - постоянно обновляемая Entity, по коллбэкам от пользователя на GUI.
        # Эти Данные и будем использовать для рассчёта
        self.calculator = PIrwinCalculator()  # Это будет контроллер в MVC паттерне, уже передаём на MVC

    def connect_callback(self, window):
        self.window = window
        PDataVisualiser(self.calculator.Model, self.window.pTypePlot)  # Visualizer registers itself
        window.CalculatepushButton.clicked.connect(self.calculate_concentration)

    def calculate_concentration(self):
        print('Recalculating the p concentration')
        self.calculator.calculate_concentration(
            temperature=self.parameters.temperature,
            acceptor_energy=self.parameters.acceptor_energy,
            acceptor_concentration=self.parameters.acceptor_concentration,
            donor_energy=self.parameters.donor_energy,
            material=self.parameters.material)
