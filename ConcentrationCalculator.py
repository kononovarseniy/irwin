from abc import ABC, abstractmethod

class ConcentrationCalculator:
    def __init__(self):
        pass

    @abstractmethod
    def CalcConcentration(self, *args, **kwargs):
        pass