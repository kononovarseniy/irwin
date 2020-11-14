from irwin.ApplicationModule import ApplicationModule
from irwin.n_semiconductor_module.callbacks.n_TemperatureCallBackOperator import n_TemperatureCallbackOperator
from irwin.n_semiconductor_module.callbacks.n_DonorEnergyCallBackOperator import n_DonorEnergyCallbackOperator
from irwin.n_semiconductor_module.callbacks.n_AcceptorEnergyCallBackOperator import n_AcceptorEnergyCallBackOperator
from irwin.n_semiconductor_module.callbacks.n_MaterialCallBackOperator import n_MaterialCallBackOperator
from irwin.n_semiconductor_module.callbacks.DonorConcentrationCallBackOperator import DonorConcentrationCallBackOperator
from irwin.n_semiconductor_module.callbacks.n_RadioButtonsCallBackOperator import n_RadioButtonsCallBackOperator
from irwin.n_semiconductor_module.callbacks.n_CalculationCallBackOperator import n_CalculationCallBackOperator


class NSemiconductorModule(ApplicationModule):
    callback_operators = \
        [
            n_TemperatureCallbackOperator(),
            n_DonorEnergyCallbackOperator(),
            n_AcceptorEnergyCallBackOperator(),
            n_MaterialCallBackOperator(),
            DonorConcentrationCallBackOperator(),
            n_RadioButtonsCallBackOperator(),
            # n_CalculationCallBackOperator()
        ]

    def __init__(self):
        self.window = None