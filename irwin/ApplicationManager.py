from irwin.MainWindow import MainWindow
from irwin.p_semiconductor_module.PSemiconductorModule import PSemiconductorModule


class ApplicationManager:

    def __init__(self):
        self.application_modules = [
            PSemiconductorModule(),
            # NSemiconductorModule()
        ]

        self.gui = MainWindow()
        self.run_all_modules()

    def run_all_modules(self):
        for module in self.application_modules:
            module.run(self.gui)

    def show_gui(self):
        self.gui.show()
