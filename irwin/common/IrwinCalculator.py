from abc import ABC, abstractmethod

from irwin.common.OutputData import OutputData


class IrwinCalculator(ABC):
    def __init__(self):
        self.model = OutputData()

    @abstractmethod
    def calculate_concentration(self, *args, **kwargs):
        pass
