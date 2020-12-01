from irwin.MainWindow import MainWindow
from irwin.p_semiconductor_module.PSemiconductorModule import PSemiconductorModule
from irwin.n_semiconductor_module.NSemiconductorModule import NSemiconductorModule


class ApplicationManager:
    def __init__(self):
        self.gui = MainWindow()
        self.application_modules = [
            PSemiconductorModule(self.gui),
            NSemiconductorModule(self.gui)
        ]

    def show_gui(self):
        self.gui.show()
