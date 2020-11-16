from irwin.PlotCanvas import PlotCanvas


class PPlotCanvas(PlotCanvas):
    _state = {}

    def __new__(self, parent=None):
        instance = super().__new__(self)
        instance.__dict__ = self._state
        return instance
