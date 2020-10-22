from fompy.materials import Si, Ge, GaAs


class Material:
    def __init__(self, semiconductor, mobility_const_a, mobility_const_b):
        self.semiconductor = semiconductor
        self.mobility_const_a = mobility_const_a
        self.mobility_const_b = mobility_const_b


# TODO: insert calculated constants
MATERIALS = {
    'Si': Material(Si, 1, 1),
    'Ge': Material(Ge, 1, 1),
    'GaAs': Material(GaAs, 1, 1)
}
