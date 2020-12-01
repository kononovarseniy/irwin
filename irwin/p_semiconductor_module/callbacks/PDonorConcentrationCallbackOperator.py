from irwin.common.ScientificValueInputOperator import ScientificValueInputOperator
from irwin.config import Ranges, p_defaults


class PDonorConcentrationCallbackOperator(ScientificValueInputOperator):
    def __init__(self, input_data):
        super().__init__(
            Ranges.second_concentration_range,
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
        self.input_data.secondary_concentration = value
