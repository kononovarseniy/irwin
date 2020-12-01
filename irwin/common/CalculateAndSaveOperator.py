from abc import abstractmethod
from irwin.common.OutputData import OutputData
from irwin.common.IrwinCalculator import IrwinCalculator
from irwin.CallbackOperator import CallbackOperator
import pandas as pd


class CalculateAndSaveOperator(CallbackOperator):
    def __init__(self, output_filename, calculation_params):
        super().__init__()
        self.output_filename = output_filename
        self.calculation_params = calculation_params
        self.calculator = IrwinCalculator()
        self.data_to_save = OutputData()

    @abstractmethod
    def connect_callback(self, window):
        pass

    def calculate_and_save(self):
        self.calculator.calculate_concentration(self.calculation_params)
        data = {
            'conductivity': self.data_to_save.sigma,
            'resistivity': self.data_to_save.rho,
            'concentration': self.data_to_save.Ns
        }
        df = pd.DataFrame(data)
        df.to_csv(self.output_filename)