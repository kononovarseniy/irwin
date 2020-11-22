import pandas as pd
from irwin.CallbackOperator import CallbackOperator

from abc import ABC, abstractmethod


class AutoFillOperator(CallbackOperator):
    def __init__(self, configs_path):
        self.window = None
        self.configs_data = pd.read_excel(configs_path)

    def connect_callback(self, window):
        self.window = window
        self.auto_fill()


    @abstractmethod
    def auto_fill(self):
        pass


    def set_material(self, combo_box, material):
        combo_box.setCurrentText(material)

    def set_config_parameters(self, params_list):
        for param in params_list:
            value_to_set = param[0]
            slider = param[1]
            calc_constant = param[2]
            slider.setValue(value_to_set*calc_constant)