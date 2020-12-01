from irwin.config import GUIParameters
from irwin.common.AutoFillOperator import AutoFillOperator


class NAutoFillOperator(AutoFillOperator):
    # overridden
    def auto_fill(self):
        self.set_material(self.window.n_MaterialcomboBox, self.defaults.material)
