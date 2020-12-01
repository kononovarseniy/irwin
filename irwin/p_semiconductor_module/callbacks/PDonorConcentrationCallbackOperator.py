from irwin.common.ScientificValueInputOperator import ScientificValueInputOperator
from irwin.config import GUIParameters, p_defaults


class PDonorConcentrationCallbackOperator(ScientificValueInputOperator):
    def __init__(self, input_data):
        super().__init__(
            GUIParameters.second_concentration_accuracy,
            GUIParameters.second_concentration_min_order,
            GUIParameters.second_concentration_max_order,
            p_defaults.second_concentration
        )
        self.input_data = input_data

    def connect_callback(self, window):
        self.connect_callback_implementation(
            window.p_donor_concentration_slider,
            window.p_donor_concentration_line_edit,
            window.p_donor_concentration_spinbox
        )

    def value_changed(self, value):
        self.input_data.donor_concentration = value
