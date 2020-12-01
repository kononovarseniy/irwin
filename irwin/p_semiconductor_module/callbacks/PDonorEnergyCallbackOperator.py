from fompy.constants import eV

from irwin.common.ValueInputOperator import ValueInputOperator
from irwin.config import Ranges
from irwin.config import p_defaults


class PDonorEnergyCallbackOperator(ValueInputOperator):
    def __init__(self, input_data):
        super().__init__(
            Ranges.donor_energy_range,
            p_defaults.donor_energy
        )
        self.input_data = input_data

    def connect_callback(self, window):
        self.connect_callback_implementation(
            window.p_donor_energy_slider,
            window.p_donor_energy_line_edit)

    def value_changed(self, value):
        self.input_data.donor_energy = value * eV
