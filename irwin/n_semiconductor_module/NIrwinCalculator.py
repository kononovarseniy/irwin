from irwin.IrwinCalculator import IrwinCalculator
from irwin.n_semiconductor_module.NConcentrationData import NConcentrationData


class NIrwinCalculator(IrwinCalculator):
    def __init__(self):
        super().__init__()
        self.donor_concentration = None

    def __repr__(self):
        return f'T={self.temperature}, AcceptorE={self.acceptor_energy}, DonorE={self.donor_energy},' \
               f'material={self.material}, donor concentration={self.donor_concentration}'

    def calculate_concentration(self, *args, **kwargs):
        self.temperature = kwargs['temperature']
        self.acceptor_energy = kwargs['acceptor_energy']
        self.donor_energy = kwargs['donor_energy']
        self.material = kwargs['material']
        self.donor_concentration = kwargs['acceptor_concentration']

        # TODO: Катя, здесь вот надо разобраться как считать Ирвина для N типа
        # TODO: (Должно быть та же самая процедура абсолютно, по логике --> если сработает, можешь
        #  вывести эту процедуру в родительский класс, чтоб не дублировать код)
        #  РАСЧЁТ ДЛЯ Nd >> Na

    def init_model(self):
        self.Model = NConcentrationData()

    def init_view(self):
        pass