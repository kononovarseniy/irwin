from irwin.common.CalculateAndSaveOperator import CalculateAndSaveOperator
from irwin.p_semiconductor_module.PInputData import PInputData


class PCalculateAndSaveOperator(CalculateAndSaveOperator):
    def __init__(self):
        super().__init__(
            output_filename='P type irwin curve.csv',
            calculation_params=PInputData()
        )

    def connect_callback(self, window):
        window.p_calculate_and_save_button.clicked.connect(self.calculate_and_save)
