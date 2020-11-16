from irwin.CallbackOperator import CallbackOperator
from irwin.p_semiconductor_module.PInputData import PInputData
from irwin.p_semiconductor_module.PDataVisualiser import PDataVisualiser
from irwin.p_semiconductor_module.PIrwinCalculator import PIrwinCalculator


class PCalculationCallbackOperator(CallbackOperator):
    def __init__(self):
        self.window = None
        self.parameters = PInputData()
        # PInputData - постоянно обновляемая Entity, по коллбэкам от пользователя на GUI.
        # Эти Данные и будем использовать для рассчёта
        self.calculator = PIrwinCalculator()  # Это будет контроллер в MVC паттерне, уже передаём на MVC

    def connect_callback(self, window):
        self.window = window
        PDataVisualiser(self.calculator.model, self.window.pTypePlot)  # Visualiser registers itself
        window.CalculatepushButton.clicked.connect(self.calculate_concentration)

    def calculate_concentration(self):
        print('Recalculating the p concentration')
        self.calculator.calculate_concentration(self.parameters)
