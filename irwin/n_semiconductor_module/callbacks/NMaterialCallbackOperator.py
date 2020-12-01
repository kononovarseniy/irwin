from irwin.CallbackOperator import CallbackOperator
from irwin.materials import N_MATERIALS


class NMaterialCallbackOperator(CallbackOperator):

    def __init__(self, input_data):
        self.window = None
        self.input_data = input_data

    def connect_callback(self, window):
        self.window = window
        window.n_MaterialcomboBox.currentIndexChanged.connect(
            self.set_material)

    def set_material(self):
        arg = self.window.n_MaterialcomboBox.currentText()
        if len(arg):
            # TODO: Задать в GUIParameters Материал
            self.input_data.material = N_MATERIALS[arg]
            print(f'METHOD: set_material: {self.input_data.__repr__()}')
