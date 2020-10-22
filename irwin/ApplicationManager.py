from PyQt5 import QtWidgets
from irwin.Graphics import Ui_MainWindow
from irwin.p_SemiconductorModule.p_SemiconductorModule import p_SemiconductorModule

class ApplicationManager():

    def __init__(self):

        self.ApplicationModules = \
            [
                p_SemiconductorModule(),
                # n_SemiconductorModule()
            ]

        self.GUI = QtWidgets.QMainWindow()
        self.UI = Ui_MainWindow()
        self.UI.setupUi(self.GUI)
        self.RunAllModules()

    def RunAllModules(self):
        for module in self.ApplicationModules:
            module.Run(self.UI)

    def ShowGUI(self):
        self.GUI.show()
