from sys import exc_info

import numpy as np
from fompy import models
from fompy.models import DopedSemiconductor

from irwin.common.OutputData import OutputData


def mobility(mat, T, A, B):
    """
                                            A
    mobility(T; Nd, Na; A, B) = --------------------------
                                 3/2                   3/2
                                T  +  B * (Nd + Na) / T
    """
    Nd = mat.p_donor_concentration(T=T)
    Na = mat.n_acceptor_concentration(T=T)
    T32 = T ** (3 / 2)
    return A / (T32 + B * (Nd + Na) / T32)


@np.vectorize
def conductivity(mat, type, Na, Ea, Nd, Ed, T):
    """Вычисляет проводимость по концентрациям в функции"""
    a = mat.mobility_const_a
    b = mat.mobility_const_b
    sem = DopedSemiconductor(mat.semiconductor, Na, Ea, Nd, Ed)
    n = sem.p_concentration(T=T) if type == 'p' else sem.n_concentration(T=T)
    mob = mobility(sem, T, a, b)
    return models.conductivity(n, mob)


class IrwinCalculator:
    def __init__(self):
        self.output_data = OutputData()

    def calculate_concentration(self, input_data):
        print(f'Calculator begins calc with parameters {input_data}')

        if input_data.type == 'n':
            Na = input_data.secondary_concentration
            Nd = Ns = input_data.primary_concentration_range.get_array()
        else:
            Na = Ns = input_data.primary_concentration_range.get_array()
            Nd = input_data.secondary_concentration

        try:
            sigma = conductivity(input_data.material, input_data.type,
                                 Na, input_data.acceptor_energy,
                                 Nd, input_data.donor_energy,
                                 input_data.temperature)

            self.output_data.Ns = Ns
            self.output_data.rho = 1 / sigma
            self.output_data.sigma = sigma
            self.output_data.notify_visualizers()
        except:
            print(exc_info())

        return
