from irwin.common.CalculateAndSaveOperator import CalculateAndSaveOperator
from irwin.n_semiconductor_module.NInputData import NInputData


class NCalculateAndSaveOperator(CalculateAndSaveOperator):
    def __init__(self):
        super().__init__(
            output_filename='N type irwin curve.csv',
            calculation_params=NInputData()
        )

    def connect_callback(self, window):
        window.n_calculate_and_save_button.clicked.connect(self.calculate_and_save)