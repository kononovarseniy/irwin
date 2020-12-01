from irwin.config import GUIParameters
from irwin.common.AutoFillOperator import AutoFillOperator


class PAutoFillOperator(AutoFillOperator):
    # overridden
    def auto_fill(self):
        self.set_material(self.window.MaterialcomboBox, self.defaults.material)
