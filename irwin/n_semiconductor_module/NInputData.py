from irwin.common.InputData import InputData
from irwin.config import Ranges
from irwin.singleton import singleton


@singleton
class NInputData(InputData):
    def __init__(self):
        super().__init__()

        self.donor_concentration_range = Ranges.concentration_range
        self.acceptor_concentration_mantissa = 0.0  # значащая часть
        self.acceptor_concentration_order = 0  # порядок величины

    def __str__(self):
        return f'<n-type, material = {self.material}, T = {self.temperature}, ' \
               f'Ea = {self.acceptor_energy}, Ed = {self.donor_energy}, ' \
               f'Na = {self.acceptor_concentration:e}, Nd = {self.donor_concentration_range}'

    @property
    def acceptor_concentration(self):
        return self.acceptor_concentration_mantissa * (10 ** self.acceptor_concentration_order)
