from irwin.config import GUIParameters
from irwin.AutoFillOperator import AutoFillOperator


class NAutoFillOperator(AutoFillOperator):
    def __init__(self, configs_path):
        super().__init__(configs_path)

    # overridden
    def auto_fill(self):
        config_params = self.configs_data.loc[0:1, :]
        self.set_material(self.window.n_MaterialcomboBox, config_params['Material'][0])
        self.set_config_parameters(
            [
                [config_params['Temperature'][0], self.window.n_TemperaturehorizontalSlider,
                 GUIParameters.TemperatureCalcConstant],
                [config_params['Donor Energy'][0], self.window.n_DonorEnergyhorizontalSlider,
                 GUIParameters.DonorEnergyCalcConstant],
                [config_params['Acceptor Energy'][0], self.window.n_AcceptorEnergyhorizontalSlider,
                 GUIParameters.AcceptorEnergyCalcConstant],
                [config_params['Acceptors Mantissa'][0], self.window.AcceptorConcentrationhorizontalSlider,
                 GUIParameters.AcceptorConcentrationCalcConstant],
                [config_params['Acceptors Order'][0], self.window.n_ConcentrationOrderspinBox, 1]
            ]
        )
