from irwin.ApplicationModule import ApplicationModule
from irwin.p_semiconductor_module.callbacks.DonorEnergyCallbackOperator import DonorEnergyCallbackOperator
from irwin.p_semiconductor_module.callbacks.PAcceptorConcentrationCallbackOperator import \
    PAcceptorConcentrationCallbackOperator
from irwin.p_semiconductor_module.callbacks.PAcceptorEnergyCallbackOperator import PAcceptorEnergyCallbackOperator
from irwin.p_semiconductor_module.callbacks.PCalculationCallbackOperator import PCalculationCallbackOperator
from irwin.p_semiconductor_module.callbacks.PRadioButtonsCallbackOperator import PRadioButtonsCallbackOperator
from irwin.p_semiconductor_module.callbacks.PMaterialCallbackOperator import \
    PMaterialCallbackOperator
from irwin.p_semiconductor_module.callbacks.PTemperatureCallbackOperator import PTemperatureCallbackOperator


class PSemiconductorModule(ApplicationModule):
    callback_operators = \
        [
            PTemperatureCallbackOperator(),
            DonorEnergyCallbackOperator(),
            PMaterialCallbackOperator(),
            PCalculationCallbackOperator(),
            PRadioButtonsCallbackOperator(),
            PAcceptorConcentrationCallbackOperator(),
            PAcceptorEnergyCallbackOperator()
        ]

    def __init__(self):
        self.window = None
