from sys import exc_info

from irwin.common.IrwinCalculator import IrwinCalculator
from irwin.common.calculations import conductivity


class PIrwinCalculator(IrwinCalculator):
    def __init__(self):
        super().__init__()

    def calculate_concentration(self, params):
        print(f'Calculator begins calc with parameters {params}')

        try:
            Nas = params.acceptor_concentration_range.get_array()

            sigma = conductivity(params.material, 'p',
                                 Nas, params.acceptor_energy,
                                 params.donor_concentration, params.donor_energy,
                                 params.temperature)

            self.model.Ns = Nas
            self.model.rho = 1 / sigma
            self.model.sigma = sigma
            self.model.notify_visualizers()
        except:
            print(exc_info())

        return
