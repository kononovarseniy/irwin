from irwin.CallbackOperator import CallbackOperator
from irwin.n_semiconductor_module.NInputData import NInputData
from irwin.materials import N_MATERIALS


class NMaterialCallbackOperator(CallbackOperator):

    def __init__(self):
        self.window = None
        self.parameters = NInputData()

    def connect_callback(self, window):
        self.window = window
        window.n_MaterialcomboBox.currentIndexChanged.connect(self.set_material)

    def set_material(self):
        arg = self.window.n_MaterialcomboBox.currentText()
        if len(arg):
            # TODO: Задать в GUIParameters Материал
            self.parameters.material = N_MATERIALS[arg]
            print(f'METHOD: set_material: {self.parameters.__repr__()}')
