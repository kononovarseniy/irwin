from sys import exc_info

import numpy as np

from irwin.IrwinCalculator import IrwinCalculator
from irwin.p_semiconductor_module.PConcentrationData import PConcentrationData
from irwin.resistivityCalculation import *


class PIrwinCalculator(IrwinCalculator):
    def __init__(self):
        super().__init__()
        self.acceptor_concentration = None

    def __repr__(self):
        return f'T={self.temperature}, AcceptorE={self.acceptor_energy}, DonorE={self.donor_energy},' \
               f'material={self.material}, acceptor concentration={self.acceptor_concentration}'

    def calculate_concentration(self, *args, **kwargs):
        self.temperature = kwargs['temperature']
        self.acceptor_energy = kwargs['acceptor_energy']
        self.donor_energy = kwargs['donor_energy']
        self.material = kwargs['material']
        self.acceptor_concentration = kwargs['acceptor_concentration']

        # Вот теперь приступаем к алгоритму
        # Расчёт для случая Na >> Nd
        # Nd физиксировано и меняется в пределах между 10^12 и 10^20
        print(f'Calculator begins calc with parameters {self.__repr__()}')

        try:
            # Prepare x array
            Nds = np.logspace(self.model.Nd_min_order,
                              self.model.Nd_max_order, self.model.points_number)
            f = np.vectorize(resistivity)
            ys = f(self.material, Nds,
                   self.acceptor_energy * eV, self.acceptor_concentration, self.donor_energy * eV, self.temperature)

            self.model.Nds = Nds / CONCENTRATION_UNIT
            self.model.rho = ys / RESISTIVITY_UNIT
            self.model.sigma = 1 / ys / CONDUCTIVITY_UNIT
            self.model.notify_visualizers()
        except:
            print(exc_info())

        return

    def init_model(self):
        self.model = PConcentrationData()
