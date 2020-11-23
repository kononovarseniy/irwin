import pandas as pd
from irwin.CallbackOperator import CallbackOperator

from abc import ABC, abstractmethod


class AutoFillOperator(CallbackOperator):
    def __init__(self, defaults):
        self.window = None
        self.defaults = defaults

    def connect_callback(self, window):
        self.window = window
        self.auto_fill()

    @abstractmethod
    def auto_fill(self):
        pass

    def set_material(self, combo_box, material):
        combo_box.setCurrentText(material)

    def set_config_parameters(self, params_list):
        for val, slider, const in params_list:
            slider.setValue(val * const)
