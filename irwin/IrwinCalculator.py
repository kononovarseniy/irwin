from abc import ABC, abstractmethod


class IrwinCalculator(ABC):
    def __init__(self):
        self.Model = None  # Модель данных для отображения на графике
        self.View = None

        self.temperature = None
        self.acceptor_energy = None
        self.donor_energy = None
        self.material = None

        self.init_model()
        self.init_view()

    @abstractmethod
    def calculate_concentration(self, *args, **kwargs):
        pass

    @abstractmethod
    def init_model(self):
        pass

    @abstractmethod
    def init_view(self):
        pass
