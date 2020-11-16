from irwin.PlotCanvas import PlotCanvas


class NPlotCanvas(PlotCanvas):
    _state = {}

    def __new__(self, parent=None):
        instance = super().__new__(self)
        instance.__dict__ = self._state
        return instance
