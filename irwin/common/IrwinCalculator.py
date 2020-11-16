from abc import ABC, abstractmethod


class IrwinCalculator(ABC):
    def __init__(self):
        self.model = None  # Модель данных для отображения на графике

        self.temperature = None
        self.acceptor_energy = None
        self.donor_energy = None
        self.material = None

        self.init_model()

    @abstractmethod
    def calculate_concentration(self, *args, **kwargs):
        pass

    @abstractmethod
    def init_model(self):
        pass
