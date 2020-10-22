from irwin.CallBackOperator import CallBackOperator
from irwin.GUIParameters import GUIParameters
from irwin.CalculationParameters import CalculationParameters
import sys


class DonorEnergyCallBackOperator(CallBackOperator):
    def __init__(self):
        self.window = None


    def ConnectCallBack(self, window):
        self.window = window
        self.DataToUpdate = CalculationParameters()

        self.SetUpCallBackAndSynchroniseSlider(
            ValidatorMin = GUIParameters.DonorEnergySliderMin,
            ValidatorMax = GUIParameters.DonorEnergySliderMax,
            ValidatorAccuracy = GUIParameters.DonorEnergyLineEditAccuracy,
            LineEdit = self.window.DonorEnergylineEdit,
            SliderMin = GUIParameters.DonorEnergySliderMin,
            SliderMax = GUIParameters.DonorEnergySliderMax,
            Slider = self.window.DonorEnergyhorizontalSlider,
            UpdateSliderFunc = self.UpdateEnergySlider,
            UpdateLineEditFunc = self.UpdateEnergyLineEdit
        )


    def UpdateEnergySlider(self):
        lineEditText = self.window.DonorEnergylineEdit.text()

        if (len(lineEditText) == 0):
            lineEditText = '0'
        try:
            lineEditText = lineEditText.replace(',', '.')
            value = float(lineEditText)  # * 10.0
            self.window.DonorEnergyhorizontalSlider.setValue(
                value * (10 ** GUIParameters.DonorEnergyLineEditAccuracy))
        except:
            print('SHIT')
            print(sys.exc_info())


    def UpdateEnergyLineEdit(self):
        try:
            value_to_set = self.window.DonorEnergyhorizontalSlider.value()
            value_to_set /= 10 ** GUIParameters.DonorEnergyLineEditAccuracy  #  These calculations
                                                                    # are for correct scaling on the slider
            text_to_set = str(value_to_set).replace('.', ',')
            self.window.DonorEnergylineEdit.setText(str(text_to_set))
            self.UpdateDonorEnergy(value_to_set)

        except:
            print('caught!')
            print(sys.exc_info())

    def UpdateDonorEnergy(self, val):
        self.DataToUpdate.SetDonorEnergy(val)
        #self.DataToUpdate.DonorEnergy = val