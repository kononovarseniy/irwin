from irwin.ConcentrationData import ConcentrationData


class NConcentrationData(ConcentrationData):
    def __init__(self):
        super().__init__()
        self._Na_min_order = 12
        self._Na_max_order = 20
        self._points_number = 100

        self._Nas = []  # X array - acceptor concentrations

    @property
    def points_number(self):
        return self._points_number

    @property
    def Na_min_order(self):
        return self._Na_min_order

    @property
    def Na_max_order(self):
        return self._Na_max_order

    @property
    def Nas(self):
        return self._Nas

    @Nas.setter
    def Nas(self, val):
        self._Nas = val
