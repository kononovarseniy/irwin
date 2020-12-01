from PyQt5 import QtWidgets

from irwin.design import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.p_show_all.toggled.emit(False)
        self.n_show_all.toggled.emit(False)
