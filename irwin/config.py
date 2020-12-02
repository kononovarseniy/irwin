from fompy.units import unit

from irwin.common.LogSpace import LogSpace
from irwin.common.operators.ScientificValueInputOperator import ScientificValueRange
from irwin.common.operators.ValueInputOperator import ValueRange

P_TYPE_OUTPUT_FILE = 'P_type_irwin_curve.csv'
N_TYPE_OUTPUT_FILE = 'N_type_irwin_curve.csv'


class Units:
    RESISTIVITY = unit('Ohm cm')
    CONDUCTIVITY = unit('1 / Ohm cm')
    CONCENTRATION = unit('cm-3')
    RESISTIVITY_TEXT = r'$Ohm \cdot cm$'
    CONDUCTIVITY_TEXT = r'$\frac{1}{Ohm \cdot cm}$'


class DefaultValues:
    def __init__(self, material, temperature, donor_energy, acceptor_energy, second_concentration):
        self.material = material
        self.temperature = temperature
        self.donor_energy = donor_energy
        self.acceptor_energy = acceptor_energy
        self.second_concentration = second_concentration


n_defaults = DefaultValues(
    material='Si',
    temperature=300,
    donor_energy=0.75,
    acceptor_energy=0.04,
    second_concentration=1e10
)

p_defaults = DefaultValues(
    material='Si',
    temperature=300,
    donor_energy=0.75,
    acceptor_energy=0.04,
    second_concentration=1e10
)


class Ranges:
    concentration_range = LogSpace(12, 20, 100)

    temperature_range = ValueRange(min_value=0, max_value=500, decimals=1)  # Kelvin
    donor_energy_range = ValueRange(min_value=0, max_value=2, decimals=2)  # electron-Volt
    acceptor_energy_range = ValueRange(min_value=0, max_value=2, decimals=2)  # electron-Volt

    second_concentration_range = ScientificValueRange(min_order=0, max_order=15, mantissa_decimals=2)
