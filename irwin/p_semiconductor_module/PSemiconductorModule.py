from irwin.ApplicationModule import ApplicationModule
from irwin.config import p_defaults, P_TYPE_OUTPUT_FILE
from irwin.p_semiconductor_module.PInputData import PInputData
from irwin.p_semiconductor_module.callbacks.PAcceptorEnergyCallbackOperator import PAcceptorEnergyCallbackOperator
from irwin.p_semiconductor_module.callbacks.PAutoFillOperator import PAutoFillOperator
from irwin.p_semiconductor_module.callbacks.PCalculationCallbackOperator import PCalculationCallbackOperator
from irwin.p_semiconductor_module.callbacks.PDonorConcentrationCallbackOperator import \
    PDonorConcentrationCallbackOperator
from irwin.p_semiconductor_module.callbacks.PDonorEnergyCallbackOperator import PDonorEnergyCallbackOperator
from irwin.p_semiconductor_module.callbacks.PMaterialCallbackOperator import \
    PMaterialCallbackOperator
from irwin.p_semiconductor_module.callbacks.PRadioButtonsCallbackOperator import PRadioButtonsCallbackOperator
from irwin.p_semiconductor_module.callbacks.PTemperatureCallbackOperator import PTemperatureCallbackOperator


class PSemiconductorModule(ApplicationModule):
    callback_operators = \
        [
            PTemperatureCallbackOperator(PInputData()),
            PDonorEnergyCallbackOperator(PInputData()),
            PMaterialCallbackOperator(),
            PCalculationCallbackOperator(output_filename=P_TYPE_OUTPUT_FILE),
            PRadioButtonsCallbackOperator(),
            PDonorConcentrationCallbackOperator(PInputData()),
            PAcceptorEnergyCallbackOperator(PInputData()),
            PAutoFillOperator(p_defaults),
        ]

    def __init__(self):
        super().__init__()
        self.window = None
