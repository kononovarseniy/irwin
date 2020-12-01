from irwin.CallbackOperator import CallbackOperator


class NRadioButtonsCallbackOperator(CallbackOperator):
    def __init__(self, input_data):
        self.window = None
        self.input_data = input_data

    def connect_callback(self, window):
        self.window = window
        window.n_ResistivityradioButton.clicked.connect(
            self.set_plotting_parameter)  # What to plot along Y-axis - resistivity or Conductivity
        window.n_ConductivityradioButton.clicked.connect(self.set_plotting_parameter)

    def set_plotting_parameter(self):
        if self.window.n_ResistivityradioButton.isChecked():
            self.input_data.plot_resistivity = True
            self.input_data.plot_conductivity = False
        elif self.window.n_ConductivityradioButton.isChecked():
            self.input_data.plot_conductivity = True
            self.input_data.plot_resistivity = False
