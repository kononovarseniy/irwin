from abc import ABC, abstractmethod
from PyQt5.QtGui import QDoubleValidator


class CallBackOperator(ABC):

    @abstractmethod
    def ConnectCallBack(self, window):
        pass

    def SetUpCallBackAndSynchroniseSlider(
            self,
            ValidatorMin,
            ValidatorMax,
            ValidatorAccuracy,
            LineEdit,
            SliderMin,
            SliderMax,
            Slider,
            UpdateSliderFunc,
            UpdateLineEditFunc
    ):
        Validator = QDoubleValidator()
        Validator.setRange(
            ValidatorMin,
            ValidatorMax,
            ValidatorAccuracy
        )
        LineEdit.setValidator(Validator)
        Slider.setMaximum(SliderMax)
        Slider.setMinimum(SliderMin)
        LineEdit.textEdited.connect(UpdateSliderFunc)
        Slider.valueChanged.connect(UpdateLineEditFunc)
