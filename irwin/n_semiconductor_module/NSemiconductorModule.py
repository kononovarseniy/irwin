from irwin.ApplicationModule import ApplicationModule
from irwin.common.InputData import InputData
from irwin.n_semiconductor_module.operators import NAcceptorConcentrationCallbackOperator, \
    NAcceptorEnergyCallbackOperator, NCalculationCallbackOperator, NDonorEnergyCallbackOperator, \
    NMaterialCallbackOperator, NRadioButtonsCallbackOperator, NTemperatureCallbackOperator


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
            NCalculationCallbackOperator(input_data)
        ]
