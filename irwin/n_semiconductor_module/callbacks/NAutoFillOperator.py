from irwin.config import GUIParameters
from irwin.common.AutoFillOperator import AutoFillOperator


class NAutoFillOperator(AutoFillOperator):
    # overridden
    def auto_fill(self):
        self.set_material(self.window.n_MaterialcomboBox, self.defaults.material)
        self.set_config_parameters(
            [
                [self.defaults.temperature, self.window.n_TemperaturehorizontalSlider,
                 GUIParameters.TemperatureCalcConstant],
                [self.defaults.donor_energy, self.window.n_DonorEnergyhorizontalSlider,
                 GUIParameters.DonorEnergyCalcConstant],
                [self.defaults.acceptor_energy, self.window.n_AcceptorEnergyhorizontalSlider,
                 GUIParameters.AcceptorEnergyCalcConstant],
                [self.defaults.concentration_mantissa, self.window.AcceptorConcentrationhorizontalSlider,
                 GUIParameters.AcceptorConcentrationCalcConstant],
                [self.defaults.concentration_order, self.window.n_ConcentrationOrderspinBox, 1]
            ]
        )
