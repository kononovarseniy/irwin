from fompy.materials import Si, Ge, GaAs
from fompy.units import unit


MOBILITY_UNIT = unit('cm^2 / V s')
RESISTIVITY_UNIT = unit('Ohm cm')
CONCENTRATION_UNIT = unit('cm-3')
A_UNIT = unit('cm^2 K^3/2 / V s')
B_UNIT = unit('K^3')


class Material:
    def __init__(self, semiconductor, mobility_const_a, mobility_const_b):
        self.semiconductor = semiconductor
        self.mobility_const_a = mobility_const_a
        self.mobility_const_b = mobility_const_b


# TODO: insert calculated constants
MATERIALS = {
    'Si': Material(Si, 2.413845e+06 * A_UNIT, 1.223030e-12 * B_UNIT),
    'Ge': Material(Ge, 2.413845e+06 * A_UNIT, 1.223030e-12 * B_UNIT),
    'GaAs': Material(GaAs, 2.413845e+06 * A_UNIT, 1.223030e-12 * B_UNIT)
}
