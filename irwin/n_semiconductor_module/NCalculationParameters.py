from irwin.singleton import singleton
from irwin.common.CalculationParameters import CalculationParameters


@singleton
class NCalculationParameters(CalculationParameters):
    def __init__(self):
        super().__init__()

        self._donor_concentration_mantissa = 0.0  # значащая часть
        self._donor_concentration_order = 0  # порядок величины
        self._donor_concentration = 0.0

    def __repr__(self):
        return f'Material = {self.material}, T = {self.temperature},' \
               f'Donor E = {self.donor_energy}, donor E = {self.donor_energy},' \
               f'donor concentration = {self.donor_concentration}'

    @property
    def donor_concentration_order(self):
        return self._donor_concentration_order

    @donor_concentration_order.setter
    def donor_concentration_order(self, val):
        self._donor_concentration_order = val

    @property
    def donor_concentration(self):
        return self._donor_concentration_mantissa * (10 ** (self._donor_concentration_order))

    @property
    def donor_concentration_mantissa(self):
        return self._donor_concentration_mantissa

    @donor_concentration_mantissa.setter
    def donor_concentration_mantissa(self, val):
        self._donor_concentration_mantissa = val