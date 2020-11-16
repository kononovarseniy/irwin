import numpy as np


class LogSpace:
    def __init__(self, exp_min, exp_max, points):
        self.exp_min = exp_min
        self.exp_max = exp_max
        self.points = points

    def get_array(self):
        return np.logspace(self.exp_min, self.exp_max, self.points)

    def __str__(self):
        return f'1e{self.exp_min}..1e{self.exp_max}'
