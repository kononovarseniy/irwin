from PyQt5 import QtWidgets

from irwin.design import Ui_MainWindow
from irwin.n_semiconductor_module.NPlotCanvas import NPlotCanvas
from irwin.p_semiconductor_module.PPlotCanvas import PPlotCanvas


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # TODO: Can we somehow automatically put it into design.py?
        self.pTypePlot = PPlotCanvas(parent=self)
        self.pTypePlot.move(0, 0)
        self.nTypePlot = NPlotCanvas(parent=self)
        self.nTypePlot.move(0, 350)
        self.setupUi(self)
