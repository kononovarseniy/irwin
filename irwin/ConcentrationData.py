

class ConcentrationData:
    def __init__(self):
        self.Visualisers = []
        self._rho = []  # Resistivity
        self._sigma = []  # Conductivity



    def add_visualiser(self, Visualiser):
        self.Visualisers.append(Visualiser)

    def notify_observers(self):
        for vis in self.Visualisers:
            vis.update_model()

    @property
    def rho(self):
        return self._rho

    @rho.setter
    def rho(self, val):
        self._rho = val

    @property
    def sigma(self):
        return self._sigma

    @sigma.setter
    def sigma(self, val):
        self._sigma = val