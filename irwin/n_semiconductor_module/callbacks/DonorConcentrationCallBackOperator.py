from irwin.NCalculationParameters import NCalculationParameters
from irwin.CallbackOperator import CallbackOperator
from irwin.GUIParameters import GUIParameters


class DonorConcentrationCallBackOperator(CallbackOperator):
    def __init__(self):
        self.window = None
        self.parameters = NCalculationParameters()

    def connect_callback(self, window):
        self.window = window

        self.setup_callback_and_synchronize_slider(
            validator_min=GUIParameters.DonorConcentrationSliderMin,
            validator_max=GUIParameters.DonorConcentrationSliderMax,
            validator_accuracy=GUIParameters.DonorConcentrationLineEditAccuracy,
            line_edit=self.window.DonorConcentrationlineEdit,
            slider_min=GUIParameters.DonorConcentrationSliderMin,
            slider_max=GUIParameters.DonorConcentrationSliderMax,
            slider=self.window.DonorConcentrationhorizontalSlider,
            update_slider_func=self.update_donor_concentration_slider,
            update_line_edit_func=self.update_donor_concentration_line_edit
        )

        window.n_ConcentrationOrderspinBox.valueChanged.connect(self.update_order)

    def update_order(self):
        self.parameters.donor_concentration_order = self.window.n_ConcentrationOrderspinBox.value()
        self.update_donor_concentration_line_edit()

    def update_donor_concentration_slider(self):
        self.update_slider(
            line_edit=self.window.DonorConcentrationlineEdit,
            slider=self.window.DonorConcentrationhorizontalSlider,
            calc_constant=GUIParameters.DonorConcentrationCalcConstant
        )


    def update_donor_concentration_line_edit(self):
        value_to_set = self.window.DonorConcentrationhorizontalSlider.value()
        value_to_set /= GUIParameters.DonorConcentrationCalcConstant
        self.update_donor_concentration_mantissa(value_to_set)

        donor_concentration = self.parameters.donor_concentration
        scientific_notation = "{:.2e}".format(donor_concentration)
        text_to_set = str(scientific_notation)
        self.window.DonorConcentrationlineEdit.setText(text_to_set)


    def update_donor_concentration_mantissa(self, val):
        self.parameters.donor_concentration_mantissa = val