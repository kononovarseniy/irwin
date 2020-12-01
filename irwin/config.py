from fompy.units import unit

from irwin.common.LogSpace import LogSpace

P_TYPE_OUTPUT_FILE = 'P_type_irwin_curve.csv'
N_TYPE_OUTPUT_FILE = 'N_type_irwin_curve.csv'


class Units:
    RESISTIVITY = unit('Ohm cm')
    CONDUCTIVITY = unit('1 / Ohm cm')
    CONCENTRATION = unit('cm-3')
    RESISTIVITY_TEXT = r'$Ohm \cdot cm$'
    CONDUCTIVITY_TEXT = r'$\frac{1}{Ohm \cdot cm}$'


class Ranges:
    concentration_range = LogSpace(12, 20, 100)


class DefaultValues:
    def __init__(self, material, temperature, donor_energy, acceptor_energy, concentration_mantissa,
                 concentration_order):
        self.material = material
        self.temperature = temperature
        self.donor_energy = donor_energy
        self.acceptor_energy = acceptor_energy
        self.concentration_mantissa = concentration_mantissa
        self.concentration_order = concentration_order


n_defaults = DefaultValues(
    material='Si',
    temperature=250,
    donor_energy=0.75,
    acceptor_energy=0.4,
    concentration_mantissa=3.48,
    concentration_order=2
)

p_defaults = DefaultValues(
    material='Si',
    temperature=300,
    donor_energy=0.75,
    acceptor_energy=0.4,
    concentration_mantissa=3.48,
    concentration_order=2
)


class GUIParameters:
    TemperatureCalcConstant = 100
    TemperatureSliderMin = 0.0
    TemperatureSliderMax = 500.0  # Kelvin
    TemperatureLineEditAccuracy = 2
    TemperatureSliderMin = TemperatureSliderMin * TemperatureCalcConstant  # These calculations for correct
    TemperatureSliderMax = TemperatureSliderMax * TemperatureCalcConstant

    DonorEnergyCalcConstant = 10000
    DonorEnergySliderMin = 0.0
    DonorEnergySliderMax = 2.0  # electron-Volt
    DonorEnergyLineEditAccuracy = 2
    DonorEnergySliderMin = DonorEnergySliderMin * DonorEnergyCalcConstant
    DonorEnergySliderMax = DonorEnergySliderMax * DonorEnergyCalcConstant

    AcceptorEnergyCalcConstant = 10000
    AcceptorEnergySliderMin = 0.0
    AcceptorEnergySliderMax = 1.0  # electron-Volt
    AcceptorEnergyLineEditAccuracy = 2
    AcceptorEnergySliderMin = AcceptorEnergySliderMin * AcceptorEnergyCalcConstant
    AcceptorEnergySliderMax = AcceptorEnergySliderMax * AcceptorEnergyCalcConstant

    AcceptorConcentrationCalcConstant = 100
    AcceptorConcentrationSliderMin = 1.0 * AcceptorConcentrationCalcConstant
    AcceptorConcentrationSliderMax = 9.0 * AcceptorConcentrationCalcConstant  # ХЗ зачем нужна такая константа (10)
    AcceptorConcentrationLineEditAccuracy = 2

    DonorConcentrationCalcConstant = 100
    DonorConcentrationSliderMin = 1.0 * DonorConcentrationCalcConstant
    DonorConcentrationSliderMax = 9.0 * DonorConcentrationCalcConstant  # ХЗ зачем нужна такая константа (10)
    DonorConcentrationLineEditAccuracy = 2
