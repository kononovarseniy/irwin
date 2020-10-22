from irwin.ConcentrationCalculator import ConcentrationCalculator


class PConcentrationCalculator(ConcentrationCalculator):
    def __init__(self):
        super().__init__()
        self.temperature = None
        self.acceptor_energy = None
        self.donor_energy = None

    def __repr__(self):
        return f'T={self.temperature}, AcceptorE={self.acceptor_energy}, DonorE={self.donor_energy}'

    def calculate_concentration(self, *args, **kwargs):
        for key, val in kwargs.items():
            if key == 'temperature':
                self.temperature = val
            elif key == 'acceptor_energy':
                self.acceptor_energy = val
            elif key == 'donor_energy':
                self.donor_energy = val
            # elif key == 'material':
            #    self.material = val

        # Вот теперь приступаем к алгоритму
        print(f'Calculator begins calc with parameters {self.__repr__()}')
        return
