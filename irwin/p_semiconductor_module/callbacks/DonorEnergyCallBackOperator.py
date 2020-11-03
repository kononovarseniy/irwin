from irwin.CalculationParameters import CalculationParameters
from irwin.CallbackOperator import CallbackOperator
from irwin.GUIParameters import GUIParameters


class DonorEnergyCallbackOperator(CallbackOperator):
    def __init__(self):
        self.window = None
        self.parameters = CalculationParameters()

    def connect_callback(self, window):
        self.window = window

        self.setup_callback_and_synchronize_slider(
            validator_min=GUIParameters.DonorEnergySliderMin,
            validator_max=GUIParameters.DonorEnergySliderMax,
            validator_accuracy=GUIParameters.DonorEnergyLineEditAccuracy,
            line_edit=self.window.DonorEnergylineEdit,
            slider_min=GUIParameters.DonorEnergySliderMin,
            slider_max=GUIParameters.DonorEnergySliderMax,
            slider=self.window.DonorEnergyhorizontalSlider,
            update_slider_func=self.update_energy_slider,
            update_line_edit_func=self.update_energy_line_edit
        )

    def update_energy_slider(self):
        # TODO: fix duplicated code
        line_edit_text = self.window.DonorEnergylineEdit.text()

        if len(line_edit_text) == 0:
            line_edit_text = '0'

        line_edit_text = line_edit_text.replace(',', '.')
        value = float(line_edit_text)
        self.window.DonorEnergyhorizontalSlider.setValue(
            value * GUIParameters.DonorEnergyCalcConstant)

    def update_energy_line_edit(self):
        value_to_set = self.window.DonorEnergyhorizontalSlider.value()
        value_to_set /= GUIParameters.DonorEnergyCalcConstant
        text_to_set = str(value_to_set).replace('.', ',')
        self.window.DonorEnergylineEdit.setText(str(text_to_set))
        self.update_donor_energy(value_to_set)

    def update_donor_energy(self, val):
        self.parameters.donor_energy = val
