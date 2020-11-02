from irwin.ConcentrationData import ConcentrationData


class PConcentrationData(ConcentrationData):
    def __init__(self):
        super().__init__()
        self._Nd_min_order = 12
        self._Nd_max_order = 20
        self._points_number = 100

        self._rho = []  # Resistivity
        self._sigma = []  # Conductivity
        self._Nds = []  # X array - donor concentrations

    @property
    def points_number(self):
        return self._points_number

    @property
    def Nd_min_order(self):
        return self._Nd_min_order

    @property
    def Nd_max_order(self):
        return self._Nd_max_order

    @property
    def Nds(self):
        return self._Nds

    @Nds.setter
    def Nds(self, val):
        self._Nds = val
        self.notify_observers()

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
