from PyQt5 import QtWidgets

from irwin.PlotCanvas import PlotCanvas
from irwin.design import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # TODO: Can we somehow automatically put it into design.py?
        self.pTypePlot = PlotCanvas(parent=self)
        self.pTypePlot.move(0, 0)
        self.nTypePlot = PlotCanvas(parent=self)
        self.nTypePlot.move(0, 350)
        self.setupUi(self)
