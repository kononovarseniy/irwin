from irwin.ApplicationModule import ApplicationModule
from irwin.n_semiconductor_module.callbacks.n_TemperatureCallBackOperator import n_TemperatureCallbackOperator
from irwin.n_semiconductor_module.callbacks.n_DonorEnergyCallBackOperator import n_DonorEnergyCallbackOperator
from irwin.n_semiconductor_module.callbacks.n_AcceptorEnergyCallBackOperator import n_AcceptorEnergyCallBackOperator
from irwin.n_semiconductor_module.callbacks.n_MaterialCallBackOperator import n_MaterialCallBackOperator
from irwin.n_semiconductor_module.callbacks.DonorConcentrationCallBackOperator import DonorConcentrationCallBackOperator

# from irwin.p_semiconductor_module.callbacks.CalculationOperator import n_CalculationOperator
# from irwin.p_semiconductor_module.callbacks.DonorEnergyCallBackOperator import n_DonorEnergyCallbackOperator
# from irwin.p_semiconductor_module.callbacks.SemiconductorMaterialOperator import SemiconductorMaterialOperator

# from irwin.p_semiconductor_module.callbacks.RadioButtonsCallBackOperator import RadioButtonsCallBackOperator
# from irwin.p_semiconductor_module.callbacks.AcceptorConcentrationCallBackOperator import AcceptorConcentrationCallbackOperator
# from irwin.p_semiconductor_module.callbacks.AcceptorEnergyCallBackOperator import AcceptorEnergyCallBackOperator

class NSemiconductorModule(ApplicationModule):
    callback_operators = \
        [
            n_TemperatureCallbackOperator(),
            n_DonorEnergyCallbackOperator(),
            n_AcceptorEnergyCallBackOperator(),
            n_MaterialCallBackOperator(),
            DonorConcentrationCallBackOperator()

            # CalculationOperator(),
            # RadioButtonsCallBackOperator(),
        ]

    def __init__(self):
        self.window = None