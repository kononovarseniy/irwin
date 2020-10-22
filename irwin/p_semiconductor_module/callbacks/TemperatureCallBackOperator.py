import sys

from irwin.CalculationParameters import CalculationParameters
from irwin.CallbackOperator import CallbackOperator
from irwin.GUIParameters import GUIParameters


class TemperatureCallbackOperator(CallbackOperator):
    def __init__(self):
        self.window = None
        self.parameters = CalculationParameters()

    def connect_callback(self, window):
        self.window = window

        self.setup_callback_and_synchronize_slider(
            validator_min=GUIParameters.TemperatureSliderMin,
            validator_max=GUIParameters.TemperatureSliderMax,
            validator_accuracy=GUIParameters.TemperatureLineEditAccuracy,
            line_edit=self.window.TemperaturelineEdit,
            slider_min=GUIParameters.TemperatureSliderMin / 5,
            slider_max=GUIParameters.TemperatureSliderMax / 5,
            slider=self.window.TemperaturehorizontalSlider,
            update_slider_func=self.update_temperature_slider,
            update_line_edit_func=self.update_temperature_line_edit
        )

    def update_temperature_slider(self):
        # TODO: fix duplicated code
        line_edit_text = self.window.TemperaturelineEdit.text()

        if len(line_edit_text) == 0:
            line_edit_text = '0'
        line_edit_text = line_edit_text.replace(',', '.')
        value = float(line_edit_text)  # * 10.0
        self.window.TemperaturehorizontalSlider.setValue(
            value * (10 ** GUIParameters.TemperatureLineEditAccuracy))

    def update_temperature_line_edit(self):
        value_to_set = self.window.TemperaturehorizontalSlider.value()
        value_to_set /= 10 ** GUIParameters.TemperatureLineEditAccuracy  # These calculations
        # are for correct scaling on the slider
        text_to_set = str(value_to_set).replace('.', ',')
        self.window.TemperaturelineEdit.setText(str(text_to_set))
        self.update_temperature(value_to_set)

    def update_temperature(self, val):
        self.parameters.temperature = val
