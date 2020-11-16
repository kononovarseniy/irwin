from sys import exc_info

from irwin.common.IrwinCalculator import IrwinCalculator
from irwin.common.calculations import conductivity


class NIrwinCalculator(IrwinCalculator):
    def __init__(self):
        super().__init__()

    def calculate_concentration(self, params):
        print(f'Calculator begins calc with parameters {params}')

        try:
            Nds = params.donor_concentration_range.get_array()

            sigma = conductivity(params.material, 'n',
                                 params.acceptor_concentration, params.acceptor_energy,
                                 Nds, params.donor_energy,
                                 params.temperature)

            self.model.Ns = Nds
            self.model.rho = 1 / sigma
            self.model.sigma = sigma
            self.model.notify_visualizers()
        except:
            print(exc_info())

        return
