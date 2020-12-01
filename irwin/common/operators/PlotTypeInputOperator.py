from abc import ABC

from PyQt5.QtWidgets import QRadioButton

from irwin.CallbackOperator import CallbackOperator


class PlotTypeInputOperator(CallbackOperator, ABC):
    resistivity: QRadioButton
    conductivity: QRadioButton

    def __init__(self, input_data):
        self.input_data = input_data

    def connect_callback_implementation(self, resistivity, conductivity):
        self.resistivity = resistivity
        self.conductivity = conductivity
        self.resistivity.clicked.connect(self.plot_type_changed)
        self.conductivity.clicked.connect(self.plot_type_changed)

    def plot_type_changed(self):
        if self.resistivity.isChecked():
            self.input_data.plot_resistivity = True
            self.input_data.plot_conductivity = False
        elif self.conductivity.isChecked():
            self.input_data.plot_conductivity = True
            self.input_data.plot_resistivity = False
