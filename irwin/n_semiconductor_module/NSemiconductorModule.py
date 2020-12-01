from irwin.ApplicationModule import ApplicationModule
from irwin.config import n_defaults
from irwin.n_semiconductor_module.callbacks.NAcceptorConcentrationCallbackOperator import \
    NAcceptorConcentrationCallbackOperator
from irwin.n_semiconductor_module.callbacks.NAcceptorEnergyCallbackOperator import NAcceptorEnergyCallbackOperator
from irwin.n_semiconductor_module.callbacks.NCalculationCallbackOperator import NCalculationCallbackOperator
from irwin.n_semiconductor_module.callbacks.NDonorEnergyCallbackOperator import NDonorEnergyCallbackOperator
from irwin.n_semiconductor_module.callbacks.NMaterialCallbackOperator import NMaterialCallbackOperator
from irwin.n_semiconductor_module.callbacks.NRadioButtonsCallbackOperator import NRadioButtonsCallbackOperator
from irwin.n_semiconductor_module.callbacks.NTemperatureCallbackOperator import NTemperatureCallbackOperator
from irwin.n_semiconductor_module.callbacks.NAutoFillOperator import NAutoFillOperator


class NSemiconductorModule(ApplicationModule):
    callback_operators = \
        [
            NTemperatureCallbackOperator(),
            NDonorEnergyCallbackOperator(),
            NAcceptorEnergyCallbackOperator(),
            NMaterialCallbackOperator(),
            NAcceptorConcentrationCallbackOperator(),
            NRadioButtonsCallbackOperator(),
            NCalculationCallbackOperator(output_filename='N type irwin curve.csv'),
            NAutoFillOperator(n_defaults),
        ]

    def __init__(self):
        super().__init__()
        self.window = None
