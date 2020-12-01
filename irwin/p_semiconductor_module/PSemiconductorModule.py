from irwin.ApplicationModule import ApplicationModule
from irwin.config import p_defaults
from irwin.p_semiconductor_module.callbacks.PAcceptorEnergyCallbackOperator import PAcceptorEnergyCallbackOperator
from irwin.p_semiconductor_module.callbacks.PCalculationCallbackOperator import PCalculationCallbackOperator
from irwin.p_semiconductor_module.callbacks.PDonorConcentrationCallbackOperator import \
    PDonorConcentrationCallbackOperator
from irwin.p_semiconductor_module.callbacks.PDonorEnergyCallbackOperator import PDonorEnergyCallbackOperator
from irwin.p_semiconductor_module.callbacks.PMaterialCallbackOperator import \
    PMaterialCallbackOperator
from irwin.p_semiconductor_module.callbacks.PRadioButtonsCallbackOperator import PRadioButtonsCallbackOperator
from irwin.p_semiconductor_module.callbacks.PTemperatureCallbackOperator import PTemperatureCallbackOperator
from irwin.p_semiconductor_module.callbacks.PAutoFillOperator import PAutoFillOperator
from irwin.p_semiconductor_module.callbacks.PCalculateAndSaveOperator import PCalculateAndSaveOperator


class PSemiconductorModule(ApplicationModule):
    callback_operators = \
        [
            PTemperatureCallbackOperator(),
            PDonorEnergyCallbackOperator(),
            PMaterialCallbackOperator(),
            PCalculationCallbackOperator(),
            PRadioButtonsCallbackOperator(),
            PDonorConcentrationCallbackOperator(),
            PAcceptorEnergyCallbackOperator(),
            PAutoFillOperator(p_defaults),
            PCalculateAndSaveOperator()
        ]

    def __init__(self):
        super().__init__()
        self.window = None
