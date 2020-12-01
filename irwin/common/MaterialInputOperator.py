from abc import ABC

from PyQt5.QtWidgets import QComboBox

from irwin.CallbackOperator import CallbackOperator


class MaterialInputOperator(CallbackOperator, ABC):
    combobox: QComboBox

    def __init__(self, input_data, materials, default):
        self.input_data = input_data
        self.materials = materials
        self.default = default

    def connect_callback_implementation(self, combobox):
        self.combobox = combobox
        for t, m in self.materials.items():
            self.combobox.addItem(t, m)
        self.combobox.setCurrentText(self.default)
        self.combobox.currentIndexChanged.connect(self.selection_changed)

    def selection_changed(self):
        print(f'METHOD: set_material: {self.input_data}')
        self.input_data.material = self.combobox.currentData()
