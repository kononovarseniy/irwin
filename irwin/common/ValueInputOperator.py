from abc import ABC, abstractmethod

from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtWidgets import QSlider, QLineEdit

from irwin.CallbackOperator import CallbackOperator


class ValueInputOperator(CallbackOperator, ABC):
    line_edit: QLineEdit
    slider: QSlider

    def __init__(self, min_value, max_value, decimals, default):
        self.min_value = min_value
        self.max_value = max_value
        self.decimals = decimals
        self.default = default
        self.changing_value = False

    def connect_callback_implementation(self, slider, line_edit):
        self.slider = slider
        self.line_edit = line_edit

        validator = QDoubleValidator()
        validator.setRange(self.min_value, self.max_value, self.decimals)
        self.line_edit.setValidator(validator)

        self.set_slider_value(self.default)
        self.set_line_edit_value(self.default)
        self.value_changed(self.default)

        self.slider.valueChanged.connect(self.slider_value_changed)
        self.line_edit.textEdited.connect(self.text_changed)

    def slider_value_changed(self):
        if self.changing_value:
            return
        self.changing_value = True

        value = self.get_slider_value()
        self.set_line_edit_value(value)
        self.value_changed(value)

        self.changing_value = False

    def text_changed(self):
        if self.changing_value:
            return
        self.changing_value = True

        value = self.get_line_edit_value()
        self.set_slider_value(value)
        self.value_changed(value)

        self.changing_value = False

    @abstractmethod
    def value_changed(self, value):
        pass

    def get_slider_value(self):
        tmp = squeeze(self.slider.value(), self.slider.minimum(), self.slider.maximum())
        return stretch(tmp, self.min_value, self.max_value)

    def set_slider_value(self, value):
        tmp = squeeze(value, self.min_value, self.max_value)
        self.slider.setValue(stretch(tmp, self.slider.minimum(), self.slider.maximum()))

    def get_line_edit_value(self):
        return self.line_edit.locale().toDouble(self.line_edit.text())[0]

    def set_line_edit_value(self, value):
        self.line_edit.setText(self.line_edit.locale().toString(float(value), 'f', self.decimals))


def squeeze(value, minimum, maximum):
    return (value - minimum) / (maximum - minimum)


def stretch(value, minimum, maximum):
    return minimum + (maximum - minimum) * value
