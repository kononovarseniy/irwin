from sys import exc_info

import numpy as np

from irwin.common.IrwinCalculator import IrwinCalculator
from irwin.common.calculations import conductivity
from irwin.p_semiconductor_module.PConcentrationData import PConcentrationData


class PIrwinCalculator(IrwinCalculator):
    def __init__(self):
        super().__init__()
        self.acceptor_concentration = None

    def __repr__(self):
        return f'T={self.temperature}, AcceptorE={self.acceptor_energy}, DonorE={self.donor_energy},' \
               f'material={self.material}, acceptor concentration={self.acceptor_concentration}'

    def calculate_concentration(self, params):
        # Вот теперь приступаем к алгоритму
        # Расчёт для случая Na >> Nd
        # Nd физиксировано и меняется в пределах между 10^12 и 10^20
        print(f'Calculator begins calc with parameters {self.__repr__()}')

        try:
            # Prepare x array
            Nds = np.logspace(self.model.Nd_min_order,
                              self.model.Nd_max_order, self.model.points_number)

            sigma = conductivity(params.material, 'p',
                                 Nds, params.acceptor_energy,
                                 params.acceptor_concentration, params.donor_energy,
                                 params.temperature)

            self.model.Nds = Nds
            self.model.rho = 1 / sigma
            self.model.sigma = sigma
            self.model.notify_visualizers()
        except:
            print(exc_info())

        return

    def init_model(self):
        self.model = PConcentrationData()
