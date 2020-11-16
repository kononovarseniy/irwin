from irwin.CallbackOperator import CallbackOperator
from irwin.n_semiconductor_module.NCalculationParameters import NCalculationParameters


class NRadioButtonsCallbackOperator(CallbackOperator):
    def __init__(self):
        self.window = None
        self.parameters = NCalculationParameters()

    def connect_callback(self, window):
        self.window = window
        window.n_ResistivityradioButton.clicked.connect(
            self.set_plotting_parameter)  # What to plot along Y-axis - resistivity or Conductivity
        window.n_ConductivityradioButton.clicked.connect(self.set_plotting_parameter)

    def set_plotting_parameter(self):
        if self.window.n_ResistivityradioButton.isChecked():
            self.parameters.plot_resistivity = True
            self.parameters.plot_conductivity = False
        elif self.window.n_ConductivityradioButton.isChecked():
            self.parameters.plot_conductivity = True
            self.parameters.plot_resistivity = False
