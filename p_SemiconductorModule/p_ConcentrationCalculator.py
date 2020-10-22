
from ConcentrationCalculator import ConcentrationCalculator

class p_ConcentrationCalculator(ConcentrationCalculator):
    def __init__(self):
        super().__init__()
        self.Temperature = None
        self.AcceptorEnergy = None
        self.DonorEnergy = None

    def __repr__(self):
        return(f'T={self.Temperature}, AcceptorE={self.AcceptorEnergy}, DonorE={self.DonorEnergy}')

    def CalcConcentration(self, *args, **kwargs):
        for key, val in kwargs.items():
            if key == 'Temperature':
                self.Temperature = val
            elif key == 'AcceptorEnergy':
                self.AcceptorEnergy = val
            elif key == 'DonorEnergy':
                self.DonorEnergy = val
            #elif key == 'Material':
            #    self.Material = val

        # Вот теперь приступаем к алгоритму
        #print(f'Calculator begins calc with parameters {self.__repr__()}')
        return
