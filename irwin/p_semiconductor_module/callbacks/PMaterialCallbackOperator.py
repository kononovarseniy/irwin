from irwin.CallbackOperator import CallbackOperator
from irwin.p_semiconductor_module.PCalculationParameters import PCalculationParameters
from irwin.materials import P_MATERIALS


class PMaterialCallbackOperator(CallbackOperator):

    def __init__(self):
        self.window = None
        self.parameters = PCalculationParameters()

    def connect_callback(self, window):
        self.window = window
        window.MaterialcomboBox.currentIndexChanged.connect(self.set_material)

    def set_material(self):
        arg = self.window.MaterialcomboBox.currentText()
        if len(arg):
            # TODO: Задать в GUIParameters Материал
            self.parameters.material = P_MATERIALS[arg]
            print(f'METHOD: set_material: {self.parameters.__repr__()}')
