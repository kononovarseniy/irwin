from irwin.ApplicationModule import ApplicationModule
from irwin.common.InputData import InputData
from irwin.config import N_TYPE_OUTPUT_FILE
from irwin.n_semiconductor_module.callbacks.NAcceptorConcentrationCallbackOperator import \
    NAcceptorConcentrationCallbackOperator
from irwin.n_semiconductor_module.callbacks.NAcceptorEnergyCallbackOperator import NAcceptorEnergyCallbackOperator
from irwin.n_semiconductor_module.callbacks.NCalculationCallbackOperator import NCalculationCallbackOperator
from irwin.n_semiconductor_module.callbacks.NDonorEnergyCallbackOperator import NDonorEnergyCallbackOperator
from irwin.n_semiconductor_module.callbacks.NMaterialCallbackOperator import NMaterialCallbackOperator
from irwin.n_semiconductor_module.callbacks.NRadioButtonsCallbackOperator import NRadioButtonsCallbackOperator
from irwin.n_semiconductor_module.callbacks.NTemperatureCallbackOperator import NTemperatureCallbackOperator


class NSemiconductorModule(ApplicationModule):
    def create_operators(self):
        input_data = InputData('n')
        return [
            NTemperatureCallbackOperator(input_data),
            NDonorEnergyCallbackOperator(input_data),
            NAcceptorEnergyCallbackOperator(input_data),
            NMaterialCallbackOperator(input_data),
            NAcceptorConcentrationCallbackOperator(input_data),
            NRadioButtonsCallbackOperator(input_data),
            NCalculationCallbackOperator(input_data, output_filename=N_TYPE_OUTPUT_FILE)
        ]
