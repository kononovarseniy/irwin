from irwin.ApplicationModule import ApplicationModule
from irwin.n_semiconductor_module.callbacks.n_TemperatureCallBackOperator import n_TemperatureCallbackOperator

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
            # DonorEnergyCallbackOperator(),
            # SemiconductorMaterialOperator(),
            # CalculationOperator(),
            # RadioButtonsCallBackOperator(),
            # AcceptorConcentrationCallbackOperator(),
            # AcceptorEnergyCallBackOperator()
        ]

    def __init__(self):
        self.window = None