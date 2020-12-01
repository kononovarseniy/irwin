from abc import ABC

from irwin.CallbackOperator import CallbackOperator
from irwin.common.DataWriter import DataWriter
from irwin.common.IrwinCalculator import IrwinCalculator


class CalculationOperator(CallbackOperator, ABC):
    def __init__(self, input_data, output_filename, visualiser_class):
        self.input_data = input_data
        self.calculator = IrwinCalculator()
        self.output_filename = output_filename
        self.visualiser_class = visualiser_class

    def connect_callback_implementation(self, plot, calc_button, save_button):
        # DataVisualiser registers itself
        self.visualiser_class(self.input_data, self.calculator.output_data, plot)
        calc_button.clicked.connect(self.calculate_concentration)
        save_button.clicked.connect(self.calculate_and_save)

    def calculate_concentration(self):
        self.calculator.calculate_concentration(self.input_data)

    def calculate_and_save(self):
        self.calculator.calculate_concentration(self.input_data)
        DataWriter.save_results(self.output_filename, self.calculator.output_data)
