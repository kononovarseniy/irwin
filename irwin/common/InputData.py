from irwin.config import Ranges


class InputData:
    def __init__(self, conductivity_type):
        self.type = conductivity_type
        self.material = None
        self.plot_resistivity = True
        self.plot_conductivity = False

        self.temperature = 0.0
        self.donor_energy = 0.0
        self.acceptor_energy = 0.0

        self.primary_concentration_range = Ranges.concentration_range
        self.secondary_concentration = 0.0

    def __str__(self):
        if self.type == 'n':
            return f'<n-type, material = {self.material}, T = {self.temperature}, ' \
                   f'Ea = {self.acceptor_energy}, Ed = {self.donor_energy}, ' \
                   f'Na = {self.secondary_concentration:e}, Nd = {self.primary_concentration_range}'
        else:
            return f'<p-type, material = {self.material}, T = {self.temperature}, ' \
                   f'Ea = {self.acceptor_energy}, Ed = {self.donor_energy}, ' \
                   f'Na = {self.primary_concentration_range}, Nd = {self.secondary_concentration:e}'
