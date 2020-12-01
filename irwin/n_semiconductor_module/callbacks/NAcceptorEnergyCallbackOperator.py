from fompy.constants import eV

from irwin.common.ValueInputOperator import ValueInputOperator
from irwin.config import GUIParameters
from irwin.config import n_defaults


class NAcceptorEnergyCallbackOperator(ValueInputOperator):
    def __init__(self, input_data):
        super().__init__(
            GUIParameters.acceptor_energy_min,
            GUIParameters.acceptor_energy_max,
            GUIParameters.acceptor_energy_accuracy,
            n_defaults.acceptor_energy
        )
        self.input_data = input_data

    def connect_callback(self, window):
        self.connect_callback_implementation(
            window.n_acceptor_energy_slider,
            window.n_acceptor_energy_line_edit)

    def value_changed(self, value):
        self.input_data.acceptor_energy = value * eV
