from irwin.CallbackOperator import CallbackOperator
from irwin.p_semiconductor_module.PCalculationParameters import PCalculationParameters


class PRadioButtonsCallbackOperator(CallbackOperator):
    def __init__(self):
        self.window = None
        self.parameters = PCalculationParameters()

    def connect_callback(self, window):
        self.window = window
        window.ResistivityradioButton.clicked.connect(
            self.set_plotting_parameter)  # What to plot along Y-axis - resistivity or Conductivity
        window.ConductivityradioButton.clicked.connect(self.set_plotting_parameter)

    def set_plotting_parameter(self):
        if self.window.ResistivityradioButton.isChecked():
            self.parameters.plot_resistivity = True
            self.parameters.plot_conductivity = False
        elif self.window.ConductivityradioButton.isChecked():
            self.parameters.plot_conductivity = True
            self.parameters.plot_resistivity = False
