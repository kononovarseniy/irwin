from irwin.CallBackOperator import CallBackOperator
from irwin.CalculationParameters import CalculationParameters
from irwin.p_SemiconductorModule.p_ConcentrationCalculator import p_ConcentrationCalculator



class CalculationOperator(CallBackOperator):
    def __init__(self):
        self.window = None
        self.RawData = CalculationParameters()  # CalculationParameters - постоянно обновляемая Entity, по коллбэкам от пользователя на GUI, Эти Данные и будем использовать для рассчёта
        self.Calculator = p_ConcentrationCalculator()  # Это будет контроллер в MVC паттерне, уже передаём на MVC


    def ConnectCallBack(self, window):
        self.window = window
        window.CalculatepushButton.clicked.connect(self.CalculateConcentration)


    def CalculateConcentration(self):
        print('Recalculating the p concentration')
        self.Calculator.CalcConcentration(
            Temperature=self.RawData.GetTemperature(),
            AcceptorEnergy=self.RawData.GetAcceptorEnergy(),
            DonorEnergy=self.RawData.GetDonorEnergy(),
            Material=self.RawData.GetMaterial())

