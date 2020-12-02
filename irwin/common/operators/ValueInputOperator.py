from abc import ABC, abstractmethod

from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtWidgets import QSlider, QLineEdit

from irwin.CallbackOperator import CallbackOperator


class ValueRange:
    def __init__(self, min_value, max_value, decimals):
        self.min = min_value
        self.max = max_value
        self.decimals = decimals


class ValueInputOperator(CallbackOperator, ABC):
    line_edit: QLineEdit
    slider: QSlider

    def __init__(self, value_range, default):
        self.value_range = value_range
        self.default = default
        self.changing_value = False

    def connect_callback_implementation(self, slider, line_edit):
        self.slider = slider
        self.line_edit = line_edit

        validator = QDoubleValidator()
        validator.setRange(self.value_range.min, self.value_range.max, self.value_range.decimals)
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
        if value is not None:
            self.set_slider_value(value)
            self.value_changed(value)

        self.changing_value = False

    @abstractmethod
    def value_changed(self, value):
        pass

    def get_slider_value(self):
        tmp = squeeze(self.slider.value(), self.slider.minimum(), self.slider.maximum())
        return stretch(tmp, self.value_range.min, self.value_range.max)

    def set_slider_value(self, value):
        tmp = squeeze(value, self.value_range.min, self.value_range.max)
        self.slider.setValue(stretch(tmp, self.slider.minimum(), self.slider.maximum()))

    def get_line_edit_value(self):
        if not self.line_edit.hasAcceptableInput():
            return None
        return self.line_edit.locale().toDouble(self.line_edit.text())[0]

    def set_line_edit_value(self, value):
        self.line_edit.setText(self.line_edit.locale().toString(float(value), 'f', self.value_range.decimals))


def squeeze(value, minimum, maximum):
    return (value - minimum) / (maximum - minimum)


def stretch(value, minimum, maximum):
    return minimum + (maximum - minimum) * value


def value_input_operator(prop_name, allowed_range, default, slider, line_edit, unit=1):
    class Operator(ValueInputOperator):
        def __init__(self, input_data):
            super().__init__(allowed_range, default)
            self.input_data = input_data

        def connect_callback(self, window):
            self.connect_callback_implementation(
                getattr(window, slider),
                getattr(window, line_edit))

        def value_changed(self, value):
            setattr(self.input_data, prop_name, value * unit)

    return Operator
