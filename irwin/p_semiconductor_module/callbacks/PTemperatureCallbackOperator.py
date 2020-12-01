from irwin.common.ValueInputOperator import ValueInputOperator
from irwin.config import GUIParameters, p_defaults


class PTemperatureCallbackOperator(ValueInputOperator):
    def __init__(self, input_data):
        super().__init__(
            GUIParameters.temperature_min,
            GUIParameters.temperature_max,
            GUIParameters.temperature_accuracy,
            p_defaults.temperature
        )
        self.input_data = input_data

    def connect_callback(self, window):
        self.connect_callback_implementation(
            window.p_temperature_slider,
            window.p_temperature_line_edit)

    def value_changed(self, value):
        self.input_data.temperature = value
