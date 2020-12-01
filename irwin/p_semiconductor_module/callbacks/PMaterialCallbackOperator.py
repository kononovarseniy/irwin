from irwin.common.MaterialInputOperator import MaterialInputOperator
from irwin.config import p_defaults
from irwin.materials import P_MATERIALS


class PMaterialCallbackOperator(MaterialInputOperator):
    def __init__(self, input_data):
        super().__init__(input_data, P_MATERIALS, p_defaults.material)

    def connect_callback(self, window):
        self.connect_callback_implementation(window.p_material_combobox)
