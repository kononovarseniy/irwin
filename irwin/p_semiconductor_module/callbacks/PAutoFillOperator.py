from irwin.config import GUIParameters
from irwin.common.AutoFillOperator import AutoFillOperator


class PAutoFillOperator(AutoFillOperator):
    # overridden
    def auto_fill(self):
        self.set_material(self.window.MaterialcomboBox, self.defaults.material)
        self.set_config_parameters(
            [
                [self.defaults.concentration_mantissa, self.window.DonorConcentrationhorizontalSlider,
                 GUIParameters.DonorConcentrationCalcConstant],
                [self.defaults.concentration_order, self.window.ConcentrationOrderspinBox, 1]
            ]
        )
