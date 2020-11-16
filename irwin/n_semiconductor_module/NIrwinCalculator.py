from sys import exc_info

import numpy as np
from fompy.constants import eV

from irwin.IrwinCalculator import IrwinCalculator
from irwin.calculations import *
from irwin.n_semiconductor_module.NConcentrationData import NConcentrationData


class NIrwinCalculator(IrwinCalculator):
    def __init__(self):
        super().__init__()
        self.donor_concentration = None

    def __repr__(self):
        return f'T={self.temperature}, AcceptorE={self.acceptor_energy}, DonorE={self.donor_energy},' \
               f'material={self.material}, donor concentration={self.donor_concentration}'

    def calculate_concentration(self, params):
        print(f'Calculator begins calc with parameters {self.__repr__()}')

        try:
            # Prepare x array
            Nas = np.logspace(self.model.Na_min_order,
                              self.model.Na_max_order, self.model.points_number)

            sigma = conductivity(params.material, 'n',
                                 params.donor_concentration, params.acceptor_energy * eV,
                                 Nas, params.donor_energy * eV,
                                 params.temperature)

            self.model.Nas = Nas / CONCENTRATION_UNIT
            self.model.rho = 1 / sigma / RESISTIVITY_UNIT
            self.model.sigma = sigma / CONDUCTIVITY_UNIT
            self.model.notify_visualizers()
        except:
            print(exc_info())

        return

    def init_model(self):
        self.model = NConcentrationData()
