from Singleton import Singleton
from Materials.SiliconMaterial import SiliconMaterial

@Singleton
class CalculationParameters:
    def __init__(self):
        self.Material = None
        self.Temperature = 0.0
        self.DonorEnergy = 0.0
        self.AcceptorEnergy = 0.0


    def __repr__(self):
        return f'Material = {self.Material}, T = {self.Temperature},' \
            f'Donor E = {self.DonorEnergy}, Acceptor E = {self.AcceptorEnergy}'


    def SetMaterial(self, val):
        if val == 'Si':
            self.Material = SiliconMaterial()
        elif val == 'GaAs':
            # TODO: Прописать материалы остальные
            # self.Material = GaAsMaterial()
            pass

    def SetTemperature(self, val):
        self.Temperature = val

    def SetDonorEnergy(self, val):
        self.DonorEnergy = val

    def SetAcceptorEnergy(self, val):
        self.AcceptorEnergy = val


    def GetMaterial(self):
        return self.Material

    def GetTemperature(self):
        return self.Temperature

    def GetDonorEnergy(self):
        return self.DonorEnergy

    def GetAcceptorEnergy(self):
        return self.AcceptorEnergy


