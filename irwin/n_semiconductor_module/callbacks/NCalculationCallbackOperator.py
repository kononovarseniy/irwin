from irwin.common.CalculationOperator import CalculationOperator
from irwin.config import N_TYPE_OUTPUT_FILE
from irwin.n_semiconductor_module.NDataVisualiser import NDataVisualiser


class NCalculationCallbackOperator(CalculationOperator):
    def __init__(self, input_data):
        super().__init__(input_data, N_TYPE_OUTPUT_FILE, NDataVisualiser)

    def connect_callback(self, window):
        self.connect_callback_implementation(
            window.n_type_plot,
            window.n_calculate_button,
            window.n_calculate_and_save_button
        )
