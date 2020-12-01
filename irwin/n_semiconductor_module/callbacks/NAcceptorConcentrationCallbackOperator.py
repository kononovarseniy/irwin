from irwin.common.ScientificValueInputOperator import ScientificValueInputOperator
from irwin.config import GUIParameters, n_defaults


class NAcceptorConcentrationCallbackOperator(ScientificValueInputOperator):
    def __init__(self, input_data):
        super().__init__(
            GUIParameters.second_concentration_accuracy,
            GUIParameters.second_concentration_min_order,
            GUIParameters.second_concentration_max_order,
            n_defaults.second_concentration
        )
        self.input_data = input_data

    def connect_callback(self, window):
        self.connect_callback_implementation(
            window.n_acceptor_concentration_slider,
            window.n_acceptor_concentration_line_edit,
            window.n_acceptor_concentration_spinbox
        )

    def value_changed(self, value):
        self.input_data.secondary_concentration = value
