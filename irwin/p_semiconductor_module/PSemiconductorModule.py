from irwin.ApplicationModule import ApplicationModule
from irwin.common.InputData import InputData
from irwin.p_semiconductor_module.operators import *


class PSemiconductorModule(ApplicationModule):
    def create_operators(self):
        input_data = InputData('p')
        return [
            PTemperatureCallbackOperator(input_data),
            PDonorEnergyCallbackOperator(input_data),
            PMaterialCallbackOperator(input_data),
            PCalculationCallbackOperator(input_data),
            PRadioButtonsCallbackOperator(input_data),
            PDonorConcentrationCallbackOperator(input_data),
            PAcceptorEnergyCallbackOperator(input_data)
        ]
