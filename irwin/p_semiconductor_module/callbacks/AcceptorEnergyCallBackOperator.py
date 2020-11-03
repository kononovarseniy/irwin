from irwin.CalculationParameters import CalculationParameters
from irwin.CallbackOperator import CallbackOperator
from irwin.GUIParameters import GUIParameters


class AcceptorEnergyCallBackOperator(CallbackOperator):
    def __init__(self):
        self.window = None
        self.parameters = CalculationParameters()

    def connect_callback(self, window):
        self.window = window

        self.setup_callback_and_synchronize_slider(
            validator_min=GUIParameters.AcceptorEnergySliderMin,
            validator_max=GUIParameters.AcceptorEnergySliderMax,
            validator_accuracy=GUIParameters.AcceptorEnergyLineEditAccuracy,
            line_edit=self.window.AcceptorEnergylineEdit,
            slider_min=GUIParameters.AcceptorEnergySliderMin,
            slider_max=GUIParameters.AcceptorEnergySliderMax,
            slider=self.window.AcceptorEnergyhorizontalSlider,
            update_slider_func=self.update_energy_slider,
            update_line_edit_func=self.update_energy_line_edit
        )

    def update_energy_slider(self):
        # TODO: fix duplicated code
        line_edit_text = self.window.AcceptorEnergylineEdit.text()

        if len(line_edit_text) == 0:
            line_edit_text = '0'
        line_edit_text = line_edit_text.replace(',', '.')
        value = float(line_edit_text)  # * 10.0
        self.window.AcceptorEnergyhorizontalSlider.setValue(
            value * GUIParameters.AcceptorEnergyCalcConstant)

    def update_energy_line_edit(self):
        value_to_set = self.window.AcceptorEnergyhorizontalSlider.value()
        value_to_set /= GUIParameters.AcceptorEnergyCalcConstant
        text_to_set = str(value_to_set).replace('.', ',')

        self.window.AcceptorEnergylineEdit.setText(str(text_to_set))
        self.update_acceptor_energy(value_to_set)


    def update_acceptor_energy(self, val):
        self.parameters.acceptor_energy = val
