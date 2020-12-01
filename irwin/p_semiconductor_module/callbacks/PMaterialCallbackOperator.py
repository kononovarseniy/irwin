from irwin.CallbackOperator import CallbackOperator
from irwin.materials import P_MATERIALS


class PMaterialCallbackOperator(CallbackOperator):

    def __init__(self, input_data):
        self.window = None
        self.input_data = input_data

    def connect_callback(self, window):
        self.window = window
        window.MaterialcomboBox.currentIndexChanged.connect(self.set_material)

    def set_material(self):
        arg = self.window.MaterialcomboBox.currentText()
        if len(arg):
            # TODO: Задать в GUIParameters Материал
            self.input_data.material = P_MATERIALS[arg]
            print(f'METHOD: set_material: {self.input_data.__repr__()}')
