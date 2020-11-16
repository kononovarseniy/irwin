from irwin.CallbackOperator import CallbackOperator
from irwin.config import GUIParameters
from irwin.n_semiconductor_module.NCalculationParameters import NCalculationParameters


class NTemperatureCallbackOperator(CallbackOperator):
    def __init__(self):
        self.window = None
        self.parameters = NCalculationParameters()

    def connect_callback(self, window):
        self.window = window

        self.setup_callback_and_synchronize_slider(
            validator_min=GUIParameters.TemperatureSliderMin,
            validator_max=GUIParameters.TemperatureSliderMax,
            validator_accuracy=GUIParameters.TemperatureLineEditAccuracy,
            line_edit=self.window.n_TemperaturelineEdit,
            slider_min=GUIParameters.TemperatureSliderMin,
            slider_max=GUIParameters.TemperatureSliderMax,
            slider=self.window.n_TemperaturehorizontalSlider,
            update_slider_func=self.update_temperature_slider,
            update_line_edit_func=self.update_temperature_line_edit
        )

    def update_temperature_slider(self):
        self.update_slider(
            line_edit=self.window.n_TemperaturelineEdit,
            slider=self.window.n_TemperaturehorizontalSlider,
            calc_constant=GUIParameters.TemperatureCalcConstant
        )

    def update_temperature_line_edit(self):
        self.update_line_edit(
            line_edit=self.window.n_TemperaturelineEdit,
            slider=self.window.n_TemperaturehorizontalSlider,
            calc_constant=GUIParameters.TemperatureCalcConstant,
            update_model_func=self.update_temperature
        )

    def update_temperature(self, val):
        self.parameters.temperature = val
