from irwin.common.ValueInputOperator import ValueInputOperator
from irwin.config import Ranges, n_defaults


class NTemperatureCallbackOperator(ValueInputOperator):
    def __init__(self, input_data):
        super().__init__(
            Ranges.temperature_range,
            n_defaults.temperature
        )
        self.input_data = input_data

    def connect_callback(self, window):
        self.connect_callback_implementation(
            window.n_temperature_slider,
            window.n_temperature_line_edit)

    def value_changed(self, value):
        self.input_data.temperature = value
