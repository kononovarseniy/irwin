from irwin.config import GUIParameters
from irwin.common.AutoFillOperator import AutoFillOperator


class PAutoFillOperator(AutoFillOperator):
    # overridden
    def auto_fill(self):
        self.set_material(self.window.MaterialcomboBox, self.defaults.material)
        self.set_config_parameters(
            [
                [self.defaults.temperature, self.window.TemperaturehorizontalSlider,
                 GUIParameters.TemperatureCalcConstant],
                [self.defaults.donor_energy, self.window.DonorEnergyhorizontalSlider,
                 GUIParameters.DonorEnergyCalcConstant],
                [self.defaults.acceptor_energy, self.window.AcceptorEnergyhorizontalSlider,
                 GUIParameters.AcceptorEnergyCalcConstant],
                [self.defaults.concentration_mantissa, self.window.DonorConcentrationhorizontalSlider,
                 GUIParameters.DonorConcentrationCalcConstant],
                [self.defaults.concentration_order, self.window.ConcentrationOrderspinBox, 1]
            ]
        )
