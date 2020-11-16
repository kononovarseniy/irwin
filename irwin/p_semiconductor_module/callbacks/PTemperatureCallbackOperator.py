from irwin.CallbackOperator import CallbackOperator
from irwin.config import GUIParameters
from irwin.p_semiconductor_module.PInputData import PInputData


class PTemperatureCallbackOperator(CallbackOperator):
    def __init__(self):
        self.window = None
        self.parameters = PInputData()

    def connect_callback(self, window):
        self.window = window

        self.setup_callback_and_synchronize_slider(
            validator_min=GUIParameters.TemperatureSliderMin,
            validator_max=GUIParameters.TemperatureSliderMax,
            validator_accuracy=GUIParameters.TemperatureLineEditAccuracy,
            line_edit=self.window.TemperaturelineEdit,
            slider_min=GUIParameters.TemperatureSliderMin,
            slider_max=GUIParameters.TemperatureSliderMax,
            slider=self.window.TemperaturehorizontalSlider,
            update_slider_func=self.update_temperature_slider,
            update_line_edit_func=self.update_temperature_line_edit
        )

    def update_temperature_slider(self):
        self.update_slider(
            line_edit=self.window.TemperaturelineEdit,
            slider=self.window.TemperaturehorizontalSlider,
            calc_constant=GUIParameters.TemperatureCalcConstant
        )

    def update_temperature_line_edit(self):
        self.update_line_edit(
            line_edit=self.window.TemperaturelineEdit,
            slider=self.window.TemperaturehorizontalSlider,
            calc_constant=GUIParameters.TemperatureCalcConstant,
            update_model_func=self.update_temperature
        )

    def update_temperature(self, val):
        self.parameters.temperature = val
