from fompy.constants import eV

from irwin.common.operators.CalculationOperator import CalculationOperator
from irwin.common.operators.MaterialInputOperator import MaterialInputOperator
from irwin.common.operators.PlotTypeInputOperator import PlotTypeInputOperator
from irwin.common.operators.ScientificValueInputOperator import ScientificValueInputOperator
from irwin.common.operators.ValueInputOperator import value_input_operator
from irwin.config import Ranges, p_defaults, P_TYPE_OUTPUT_FILE
from irwin.materials import P_MATERIALS
from irwin.p_semiconductor_module.PDataVisualiser import PDataVisualiser

PTemperatureCallbackOperator = value_input_operator(prop_name='temperature',
                                                    allowed_range=Ranges.temperature_range,
                                                    default=p_defaults.temperature,
                                                    slider='p_temperature_slider',
                                                    line_edit='p_temperature_line_edit')

PAcceptorEnergyCallbackOperator = value_input_operator(prop_name='acceptor_energy',
                                                       allowed_range=Ranges.acceptor_energy_range,
                                                       default=p_defaults.acceptor_energy,
                                                       slider='p_acceptor_energy_slider',
                                                       line_edit='p_acceptor_energy_line_edit',
                                                       unit=eV)

PDonorEnergyCallbackOperator = value_input_operator(prop_name='donor_energy',
                                                    allowed_range=Ranges.donor_energy_range,
                                                    default=p_defaults.donor_energy,
                                                    slider='p_donor_energy_slider',
                                                    line_edit='p_donor_energy_line_edit',
                                                    unit=eV)


class PMaterialCallbackOperator(MaterialInputOperator):
    def __init__(self, input_data):
        super().__init__(input_data, P_MATERIALS, p_defaults.material)

    def connect_callback(self, window):
        self.connect_callback_implementation(window.p_material_combobox)


class PRadioButtonsCallbackOperator(PlotTypeInputOperator):
    def connect_callback(self, window):
        self.connect_callback_implementation(
            window.p_resistivity_radio_button,
            window.p_conductivity_radio_button
        )


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


class PCalculationCallbackOperator(CalculationOperator):
    def __init__(self, input_data):
        super().__init__(input_data, P_TYPE_OUTPUT_FILE, PDataVisualiser)

    def connect_callback(self, window):
        self.connect_callback_implementation(
            window.p_type_plot,
            window.p_calculate_button,
            window.p_calculate_and_save_button
        )
