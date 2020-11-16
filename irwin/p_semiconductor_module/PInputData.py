from irwin.common.InputData import InputData
from irwin.config import Ranges
from irwin.singleton import singleton


@singleton
class PInputData(InputData):
    def __init__(self):
        super().__init__()

        self.acceptor_concentration_range = Ranges.concentration_range
        self.donor_concentration_mantissa = 0.0  # значащая часть
        self.donor_concentration_order = 0  # порядок величины

    def __str__(self):
        return f'<p-type, material = {self.material}, T = {self.temperature}, ' \
               f'Ea = {self.acceptor_energy}, Ed = {self.donor_energy}, ' \
               f'Na = {self.acceptor_concentration_range}, Nd = {self.donor_concentration:e}'

    @property
    def donor_concentration(self):
        return self.donor_concentration_mantissa * (10 ** self.donor_concentration_order)
