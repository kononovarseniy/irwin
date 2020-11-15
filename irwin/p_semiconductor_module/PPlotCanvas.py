from irwin.PlotCanvas import PlotCanvas
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class PPlotCanvas(PlotCanvas, FigureCanvas):
    _state = {}

    def __new__(self, parent=None):
        instance = super().__new__(self)
        instance.__dict__ = self._state
        return instance
