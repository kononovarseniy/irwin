from irwin.common.CalculationOperator import CalculationOperator
from irwin.config import P_TYPE_OUTPUT_FILE
from irwin.p_semiconductor_module.PDataVisualiser import PDataVisualiser


class PCalculationCallbackOperator(CalculationOperator):
    def __init__(self, input_data):
        super().__init__(input_data, P_TYPE_OUTPUT_FILE, PDataVisualiser)

    def connect_callback(self, window):
        self.connect_callback_implementation(
            window.p_type_plot,
            window.p_calculate_button,
            window.p_calculate_and_save_button
        )
