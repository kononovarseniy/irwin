from irwin.config import GUIParameters
from irwin.AutoFillOperator import AutoFillOperator


class PAutoFillOperator(AutoFillOperator):
    def __init__(self, configs_path):
        super().__init__(configs_path)

    # overridden
    def auto_fill(self):
        config_params = self.configs_data.loc[0:1, :]
        self.set_material(self.window.MaterialcomboBox, config_params['Material'][0])
        self.set_config_parameters(
            [
                [config_params['Temperature'][0],       self.window.TemperaturehorizontalSlider,        GUIParameters.TemperatureCalcConstant],
                [config_params['Donor Energy'][0],      self.window.DonorEnergyhorizontalSlider,        GUIParameters.DonorEnergyCalcConstant],
                [config_params['Acceptor Energy'][0],   self.window.AcceptorEnergyhorizontalSlider,     GUIParameters.AcceptorEnergyCalcConstant],
                [config_params['Donors Mantissa'][0],   self.window.DonorConcentrationhorizontalSlider, GUIParameters.DonorConcentrationCalcConstant],
                [config_params['Donors Order'][0],      self.window.ConcentrationOrderspinBox,          1]
            ]
        )

