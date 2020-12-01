import math
from abc import ABC, abstractmethod

from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtWidgets import QSlider, QLineEdit, QSpinBox

from irwin.CallbackOperator import CallbackOperator
from irwin.common.ValueInputOperator import squeeze, stretch


def get_mantissa_and_order(value):
    o = int(math.floor(math.log(value, 10)))
    m = value / 10 ** o
    return m, o


class ScientificValueRange:
    def __init__(self, min_order, max_order, mantissa_decimals):
        self.min_order = min_order
        self.max_order = max_order
        self.decimals = mantissa_decimals


class ScientificValueInputOperator(CallbackOperator, ABC):
    line_edit: QLineEdit
    slider: QSlider
    spinbox: QSpinBox

    def __init__(self, value_range, default):
        self.value_range = value_range
        self.default = default
        self.default_mantissa, self.default_order = get_mantissa_and_order(default)

        self.changing_value = False

    def connect_callback_implementation(self, slider, line_edit, spinbox):
        self.slider = slider
        self.line_edit = line_edit
        self.spinbox = spinbox

        validator = QDoubleValidator()
        self.line_edit.setValidator(validator)

        self.spinbox.setMinimum(self.value_range.min_order)
        self.spinbox.setMaximum(self.value_range.max_order)

        self.set_slider_value(self.default_mantissa)
        self.set_spinbox_value(self.default_order)
        self.set_line_edit_value(self.default)
        self.value_changed(self.default)

        self.slider.valueChanged.connect(self.slider_value_changed)
        self.line_edit.textEdited.connect(self.text_changed)
        self.spinbox.valueChanged.connect(self.spinbox_value_changed)

    def slider_value_changed(self):
        if self.changing_value:
            return
        self.changing_value = True

        value = self.get_slider_value() * 10 ** self.get_spinbox_value()
        self.set_line_edit_value(value)
        self.value_changed(value)

        self.changing_value = False

    def spinbox_value_changed(self):
        if self.changing_value:
            return
        self.changing_value = True

        value = self.get_slider_value() * 10 ** self.get_spinbox_value()
        self.set_line_edit_value(value)
        self.value_changed(value)

        self.changing_value = False

    def text_changed(self):
        if self.changing_value:
            return
        self.changing_value = True

        value = self.get_line_edit_value()
        m, o = get_mantissa_and_order(value)
        self.set_slider_value(m)
        self.set_spinbox_value(o)
        self.value_changed(value)

        self.changing_value = False

    @abstractmethod
    def value_changed(self, value):
        pass

    def get_slider_value(self):
        tmp = squeeze(self.slider.value(), self.slider.minimum(), self.slider.maximum())
        return stretch(tmp, 1, 10)

    def set_slider_value(self, value):
        tmp = squeeze(value, 1, 10)
        self.slider.setValue(stretch(tmp, self.slider.minimum(), self.slider.maximum()))

    def get_spinbox_value(self):
        return self.spinbox.value()

    def set_spinbox_value(self, value):
        self.spinbox.setValue(value)

    def get_line_edit_value(self):
        return self.line_edit.locale().toDouble(self.line_edit.text())[0]

    def set_line_edit_value(self, value):
        self.line_edit.setText(self.line_edit.locale().toString(float(value), 'e', self.value_range.decimals))
