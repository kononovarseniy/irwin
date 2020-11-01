from irwin.ConcentrationData import ConcentrationData


class PConcentrationData(ConcentrationData):
    def __init__(self):
        super().__init__()
        self._Nd_min = 10**12
        self._Nd_max = 10**20
        self._PointsNumber = 100

        self._rho = []  # Resistivity
        self._sigma = []  # Conductivity


    @property
    def rho(self):
        return self._rho

    @rho.setter
    def rho(self, val):
        self._rho = val
        self.notify_observers()

    @property
    def sigma(self):
        return self._sigma


    @sigma.setter
    def sigma(self, val):
        self._sigma = val
        self.notify_observers()
