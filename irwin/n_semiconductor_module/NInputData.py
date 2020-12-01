from irwin.common.InputData import InputData
from irwin.config import Ranges


class NInputData(InputData):
    def __init__(self):
        super().__init__('n')
        self.donor_concentration_range = Ranges.concentration_range
        self.acceptor_concentration = 0

    def __str__(self):
        return f'<n-type, material = {self.material}, T = {self.temperature}, ' \
               f'Ea = {self.acceptor_energy}, Ed = {self.donor_energy}, ' \
               f'Na = {self.acceptor_concentration:e}, Nd = {self.donor_concentration_range}'
