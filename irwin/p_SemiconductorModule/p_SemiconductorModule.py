from irwin.ApplicationModule import ApplicationModule
from irwin.p_SemiconductorModule.CallBackOperators.TemperatureCallBackOperator import TemperatureCallBackOperator
from irwin.p_SemiconductorModule.CallBackOperators.DonorEnergyCallBackOperator import DonorEnergyCallBackOperator
from irwin.p_SemiconductorModule.CallBackOperators.SemiconductorMaterialOperator import SemiconductorMaterialOperator
from irwin.p_SemiconductorModule.CallBackOperators.CalculationOperator import CalculationOperator

class p_SemiconductorModule(ApplicationModule):

    callback_operators = \
        [
            TemperatureCallBackOperator(),
            DonorEnergyCallBackOperator(),
            SemiconductorMaterialOperator(),
            CalculationOperator()
            # AcceptorEnergyCallBackOperator -- TODO: Сделать всё аналогично + поправить баг, на  значения не те, что в GUIParameters указаны
            #
        ]

    def __init__(self):
        self.window = None


    def Run(self, UserInterface):
        self.UserInterface = UserInterface
        self.ConnectAllCallBacks()


