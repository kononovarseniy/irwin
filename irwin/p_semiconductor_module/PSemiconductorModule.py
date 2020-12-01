from irwin.ApplicationModule import ApplicationModule
from irwin.common.InputData import InputData
from irwin.config import P_TYPE_OUTPUT_FILE
from irwin.p_semiconductor_module.callbacks.PAcceptorEnergyCallbackOperator import PAcceptorEnergyCallbackOperator
from irwin.p_semiconductor_module.callbacks.PCalculationCallbackOperator import PCalculationCallbackOperator
from irwin.p_semiconductor_module.callbacks.PDonorConcentrationCallbackOperator import \
    PDonorConcentrationCallbackOperator
from irwin.p_semiconductor_module.callbacks.PDonorEnergyCallbackOperator import PDonorEnergyCallbackOperator
from irwin.p_semiconductor_module.callbacks.PMaterialCallbackOperator import \
    PMaterialCallbackOperator
from irwin.p_semiconductor_module.callbacks.PRadioButtonsCallbackOperator import PRadioButtonsCallbackOperator
from irwin.p_semiconductor_module.callbacks.PTemperatureCallbackOperator import PTemperatureCallbackOperator


class PSemiconductorModule(ApplicationModule):
    def create_operators(self):
        input_data = InputData('p')
        return [
            PTemperatureCallbackOperator(input_data),
            PDonorEnergyCallbackOperator(input_data),
            PMaterialCallbackOperator(input_data),
            PCalculationCallbackOperator(input_data, output_filename=P_TYPE_OUTPUT_FILE),
            PRadioButtonsCallbackOperator(input_data),
            PDonorConcentrationCallbackOperator(input_data),
            PAcceptorEnergyCallbackOperator(input_data)
        ]
