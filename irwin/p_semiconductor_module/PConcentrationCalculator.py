from irwin.ConcentrationCalculator import ConcentrationCalculator


class PConcentrationCalculator(ConcentrationCalculator):
    def __init__(self):
        super().__init__()
        self.temperature = None
        self.acceptor_energy = None
        self.donor_energy = None
        self.material = None

    def __repr__(self):
        return f'T={self.temperature}, AcceptorE={self.acceptor_energy}, DonorE={self.donor_energy}'

    def calculate_concentration(self, *args, **kwargs):
        self.temperature = kwargs['temperature']
        self.acceptor_energy = kwargs['acceptor_energy']
        self.donor_energy = kwargs['donor_energy']
        self.material = kwargs['material']

        # Вот теперь приступаем к алгоритму
        print(f'Calculator begins calc with parameters {self.__repr__()}')


        return
