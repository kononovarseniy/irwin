from irwin.ApplicationModule import ApplicationModule
from irwin.p_semiconductor_module.callbacks.PDonorEnergyCallbackOperator import PDonorEnergyCallbackOperator
from irwin.n_semiconductor_module.callbacks.NAcceptorConcentrationCallbackOperator import \
    NAcceptorConcentrationCallbackOperator
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
            PDonorEnergyCallbackOperator(),
            PMaterialCallbackOperator(),
            PCalculationCallbackOperator(),
            PRadioButtonsCallbackOperator(),
            NAcceptorConcentrationCallbackOperator(),
            PAcceptorEnergyCallbackOperator()
        ]

    def __init__(self):
        self.window = None
