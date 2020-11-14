from irwin.ApplicationModule import ApplicationModule
from irwin.p_semiconductor_module.callbacks.CalculationOperator import CalculationOperator
from irwin.p_semiconductor_module.callbacks.DonorEnergyCallBackOperator import DonorEnergyCallbackOperator
from irwin.p_semiconductor_module.callbacks.SemiconductorMaterialOperator import SemiconductorMaterialOperator
from irwin.p_semiconductor_module.callbacks.TemperatureCallBackOperator import TemperatureCallbackOperator
from irwin.p_semiconductor_module.callbacks.RadioButtonsCallBackOperator import RadioButtonsCallBackOperator
from irwin.p_semiconductor_module.callbacks.AcceptorConcentrationCallBackOperator import AcceptorConcentrationCallbackOperator
from irwin.p_semiconductor_module.callbacks.AcceptorEnergyCallBackOperator import AcceptorEnergyCallBackOperator

class PSemiconductorModule(ApplicationModule):
    callback_operators = \
        [
            TemperatureCallbackOperator(),
            DonorEnergyCallbackOperator(),
            SemiconductorMaterialOperator(),
            CalculationOperator(),
            RadioButtonsCallBackOperator(),
            AcceptorConcentrationCallbackOperator(),
            AcceptorEnergyCallBackOperator()
        ]

    def __init__(self):
        self.window = None

