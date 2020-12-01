from fompy.constants import eV

from irwin.common.operators.CalculationOperator import CalculationOperator
from irwin.common.operators.MaterialInputOperator import MaterialInputOperator
from irwin.common.operators.PlotTypeInputOperator import PlotTypeInputOperator
from irwin.common.operators.ScientificValueInputOperator import ScientificValueInputOperator
from irwin.common.operators.ValueInputOperator import ValueInputOperator
from irwin.config import Ranges, n_defaults, N_TYPE_OUTPUT_FILE
from irwin.materials import N_MATERIALS
from irwin.n_semiconductor_module.NDataVisualiser import NDataVisualiser


class NMaterialCallbackOperator(MaterialInputOperator):
    def __init__(self, input_data):
        super().__init__(input_data, N_MATERIALS, n_defaults.material)

    def connect_callback(self, window):
        self.connect_callback_implementation(window.n_material_combobox)


class NRadioButtonsCallbackOperator(PlotTypeInputOperator):
    def connect_callback(self, window):
        self.connect_callback_implementation(
            window.n_resistivity_radio_button,
            window.n_conductivity_radio_button
        )


class NTemperatureCallbackOperator(ValueInputOperator):
    def __init__(self, input_data):
        super().__init__(
            Ranges.temperature_range,
            n_defaults.temperature
        )
        self.input_data = input_data

    def connect_callback(self, window):
        self.connect_callback_implementation(
            window.n_temperature_slider,
            window.n_temperature_line_edit)

    def value_changed(self, value):
        self.input_data.temperature = value


class NDonorEnergyCallbackOperator(ValueInputOperator):
    def __init__(self, input_data):
        super().__init__(
            Ranges.donor_energy_range,
            n_defaults.donor_energy
        )
        self.input_data = input_data

    def connect_callback(self, window):
        self.connect_callback_implementation(
            window.n_donor_energy_slider,
            window.n_donor_energy_line_edit)

    def value_changed(self, value):
        self.input_data.donor_energy = value * eV


class NAcceptorEnergyCallbackOperator(ValueInputOperator):
    def __init__(self, input_data):
        super().__init__(
            Ranges.acceptor_energy_range,
            n_defaults.acceptor_energy
        )
        self.input_data = input_data

    def connect_callback(self, window):
        self.connect_callback_implementation(
            window.n_acceptor_energy_slider,
            window.n_acceptor_energy_line_edit)

    def value_changed(self, value):
        self.input_data.acceptor_energy = value * eV


class NAcceptorConcentrationCallbackOperator(ScientificValueInputOperator):
    def __init__(self, input_data):
        super().__init__(
            Ranges.second_concentration_range,
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


class NCalculationCallbackOperator(CalculationOperator):
    def __init__(self, input_data):
        super().__init__(input_data, N_TYPE_OUTPUT_FILE, NDataVisualiser)

    def connect_callback(self, window):
        self.connect_callback_implementation(
            window.n_type_plot,
            window.n_calculate_button,
            window.n_calculate_and_save_button
        )
