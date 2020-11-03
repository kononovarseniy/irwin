from irwin.ConcentrationCalculator import ConcentrationCalculator
from irwin.p_semiconductor_module.PConcentrationData import PConcentrationData
from irwin.p_semiconductor_module.PDataVisualiser import PDataVisualiser
from scripts.curve import *
from sys import exc_info

class PConcentrationCalculator(ConcentrationCalculator):
    def __init__(self):
        super().__init__()
        self.acceptor_concentration = None
        self.temperature = None
        self.acceptor_energy = None
        self.donor_energy = None
        self.material = None

    def __repr__(self):
        return f'T={self.temperature}, AcceptorE={self.acceptor_energy}, DonorE={self.donor_energy},' \
               f'material={self.material}, acceptor concentration={self.acceptor_concentration}'

    def calculate_concentration(self, *args, **kwargs):
        self.temperature = kwargs['temperature']
        self.acceptor_energy = kwargs['acceptor_energy']
        self.donor_energy = kwargs['donor_energy']
        self.material = kwargs['material']
        self.acceptor_concentration = kwargs['acceptor_concentration']

        # Вот теперь приступаем к алгоритму
        # Расчёт для случая Na >> Nd
        # Nd физиксировано и меняется в пределах между 10^12 и 10^20
        print(f'Calculator begins calc with parameters {self.__repr__()}')

        try:
            f = np.vectorize(resistivity)

            # Prepare x array
            Nds = np.logspace(self.Model.Nd_min_order, self.Model.Nd_max_order, self.Model.points_number)
            ys = f(self.material, self.acceptor_concentration, self.acceptor_energy, Nds, self.donor_energy, self.temperature)


            self.Model.sigma = [(1 / val) for val in ys]
            self.Model.rho = ys
            self.Model.Nds = Nds
        except:
            print(exc_info())

        return

    def init_model(self):
        self.Model = PConcentrationData()

    def init_view(self):
        self.View = PDataVisualiser(self, self.Model)
