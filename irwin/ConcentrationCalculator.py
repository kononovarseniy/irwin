from abc import ABC, abstractmethod


class ConcentrationCalculator(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def calculate_concentration(self, *args, **kwargs):
        pass
