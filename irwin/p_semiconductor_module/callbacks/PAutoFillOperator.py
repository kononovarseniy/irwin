from irwin.CallbackOperator import CallbackOperator
import pandas as pd
from irwin.config import GUIParameters


class PAutoFillOperator(CallbackOperator):
    def __init__(self):
        self.window = None
        self.config_path = "..\\AutoFillConfigs\\PTypeConfigs\\PTypeConfigs.xlsx"
        self.configs_data = pd.read_excel(self.config_path)
        print(self.configs_data)

    def connect_callback(self, window):
        self.window = window
        self.auto_fill()

    def auto_fill(self):
        config_params = self.configs_data.loc[0:1, :]
        print(f'config params = \n{config_params}')
        self.set_material(config_params['Material'][0])
        self.set_config_parameters(
            [
                [config_params['Temperature'][0],       self.window.TemperaturehorizontalSlider,        GUIParameters.TemperatureCalcConstant],
                [config_params['Donor Energy'][0],      self.window.DonorEnergyhorizontalSlider,        GUIParameters.DonorEnergyCalcConstant],
                [config_params['Acceptor Energy'][0],   self.window.AcceptorEnergyhorizontalSlider,     GUIParameters.AcceptorEnergyCalcConstant],
                [config_params['Donors Mantissa'][0],   self.window.DonorConcentrationhorizontalSlider, GUIParameters.DonorConcentrationCalcConstant],
                [config_params['Donors Order'][0],      self.window.ConcentrationOrderspinBox,          1]
            ]
        )

    def set_material(self, material):
        self.window.MaterialcomboBox.setCurrentText(material)

    def set_config_parameters(self, params_list):
        for param in params_list:
            value_to_set = param[0]
            slider = param[1]
            calc_constant = param[2]
            slider.setValue(value_to_set*calc_constant)

