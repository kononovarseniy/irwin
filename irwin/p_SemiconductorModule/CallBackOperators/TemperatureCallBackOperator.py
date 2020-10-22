from irwin.CallBackOperator import CallBackOperator
from irwin.CalculationParameters import CalculationParameters
from irwin.GUIParameters import GUIParameters
import sys

class TemperatureCallBackOperator(CallBackOperator):
    def __init__(self):
        self.window = None
        self.DataToUpdate = CalculationParameters()



    def ConnectCallBack(self, window):
        self.window = window

        self.SetUpCallBackAndSynchroniseSlider(
            ValidatorMin = GUIParameters.TemperatureSliderMin,
            ValidatorMax = GUIParameters.TemperatureSliderMax,
            ValidatorAccuracy = GUIParameters.TemperatureLineEditAccuracy,
            LineEdit = self.window.TemperaturelineEdit,
            SliderMin = GUIParameters.TemperatureSliderMin / 5,
            SliderMax = GUIParameters.TemperatureSliderMax / 5,
            Slider = self.window.TemperaturehorizontalSlider,
            UpdateSliderFunc = self.UpdateTemperatureSlider,
            UpdateLineEditFunc = self.UpdateTemperatureLineEdit
        )


    def UpdateTemperatureSlider(self):
        lineEditText = self.window.TemperaturelineEdit.text()

        if (len(lineEditText) == 0):
            lineEditText = '0'
        try:
            lineEditText = lineEditText.replace(',', '.')
            value = float(lineEditText)  # * 10.0
            self.window.TemperaturehorizontalSlider.setValue(
                value * (10 ** GUIParameters.TemperatureLineEditAccuracy))
        except:
            print('SHIT')
            print(sys.exc_info())


    def UpdateTemperatureLineEdit(self):
        try:
            value_to_set = self.window.TemperaturehorizontalSlider.value()
            value_to_set /= 10 ** GUIParameters.TemperatureLineEditAccuracy  #  These calculations
                                                                    # are for correct scaling on the slider
            text_to_set = str(value_to_set).replace('.', ',')
            self.window.TemperaturelineEdit.setText(str(text_to_set))
            self.UpdateTemperature(value_to_set)

        except:
            print('caught!')
            print(sys.exc_info())

    def UpdateTemperature(self, val):
        self.DataToUpdate.Temperature = val
        # self.DataToUpdate.Temperature = val

