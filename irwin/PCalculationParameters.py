from irwin.singleton import singleton
from irwin.CalculationParameters import CalculationParameters


@singleton
class PCalculationParameters(CalculationParameters):
    def __init__(self):
        super().__init__()

        self._acceptor_concentration_mantissa = 0.0  # значащая часть
        self._acceptor_concentration_order = 0  # порядок величины
        self._acceptor_concentration = 0.0

    def __repr__(self):
        return f'Material = {self.material}, T = {self.temperature},' \
               f'Donor E = {self.donor_energy}, Acceptor E = {self.acceptor_energy},' \
               f'Acceptor concentration = {self.acceptor_concentration}'

    @property
    def acceptor_concentration_order(self):
        return self._acceptor_concentration_order

    @acceptor_concentration_order.setter
    def acceptor_concentration_order(self, val):
        self._acceptor_concentration_order = val

    @property
    def acceptor_concentration(self):
        return self._acceptor_concentration_mantissa * (10 ** (self._acceptor_concentration_order))

    @property
    def acceptor_concentration_mantissa(self):
        return self._acceptor_concentration_mantissa

    @acceptor_concentration_mantissa.setter
    def acceptor_concentration_mantissa(self, val):
        self._acceptor_concentration_mantissa = val
