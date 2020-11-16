from fompy.materials import Si, Ge
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


# For n-type
N_MATERIALS = {
    'Si': Material(Si, 4.476183e+06 * A_UNIT, 1.592302e-12 * B_UNIT),
    'Ge': Material(Ge, 1.018281e+07 * A_UNIT, 1.071256e-11 * B_UNIT),
    'GaAs': Material(Ge, 4.833961e+07 * A_UNIT, 1.069558e-10 * B_UNIT)
}

# For p-type
P_MATERIALS = {
    'Si': Material(Si, 2.413845e+06 * A_UNIT, 1.223030e-12 * B_UNIT),
    'Ge': Material(Ge, 4.402371e+06 * A_UNIT, 9.567049e-12 * B_UNIT)
}
