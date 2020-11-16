class CalculationParameters:
    def __init__(self):
        self._material = None

        self._plot_resistivity = True
        self._plot_conductivity = False

        self._temperature = 0.0
        self._donor_energy = 0.0
        self._acceptor_energy = 0.0

    @property
    def plot_resistivity(self):
        return self._plot_resistivity

    @plot_resistivity.setter
    def plot_resistivity(self, val):
        self._plot_resistivity = val

    @property
    def plot_conductivity(self):
        return self._plot_conductivity

    @plot_conductivity.setter
    def plot_conductivity(self, val):
        self._plot_conductivity = val

    @property
    def material(self):
        return self._material

    @property
    def temperature(self):
        return self._temperature

    @property
    def donor_energy(self):
        return self._donor_energy

    @property
    def acceptor_energy(self):
        return self._acceptor_energy

    @material.setter
    def material(self, val):
        self._material = val

    @temperature.setter
    def temperature(self, val):
        self._temperature = val

    @donor_energy.setter
    def donor_energy(self, val):
        self._donor_energy = val

    @acceptor_energy.setter
    def acceptor_energy(self, val):
        self._acceptor_energy = val
