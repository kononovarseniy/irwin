from irwin.common.MaterialInputOperator import MaterialInputOperator
from irwin.config import n_defaults
from irwin.materials import N_MATERIALS


class NMaterialCallbackOperator(MaterialInputOperator):
    def __init__(self, input_data):
        super().__init__(input_data, N_MATERIALS, n_defaults.material)

    def connect_callback(self, window):
        self.connect_callback_implementation(window.n_material_combobox)
