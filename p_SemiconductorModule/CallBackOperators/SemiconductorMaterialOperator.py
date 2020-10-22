from CallBackOperator import CallBackOperator
from CalculationParameters import CalculationParameters

class SemiconductorMaterialOperator(CallBackOperator):


    def __init__(self):
        self.ParamsToUpdate = CalculationParameters()

    def ConnectCallBack(self, window):
        window.MaterialcomboBox.currentIndexChanged.connect(self.SetMaterial)
        self.window = window



    def SetMaterial(self):
        arg = self.window.MaterialcomboBox.currentText()
        if len(arg):
            # TODO: Задать в GUIParameters Материал
            self.ParamsToUpdate.SetMaterial(arg)
            print(f'METHOD: SetMaterial: {self.ParamsToUpdate.__repr__()}')
