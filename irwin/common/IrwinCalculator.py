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
        self.model = OutputData()

    def calculate_concentration(self, params):
        print(f'Calculator begins calc with parameters {params}')

        if params.type == 'n':
            Na = params.acceptor_concentration
            Nd = Ns = params.donor_concentration_range.get_array()
        else:
            Na = Ns = params.acceptor_concentration_range.get_array()
            Nd = params.donor_concentration

        try:
            sigma = conductivity(params.material, params.type,
                                 Na, params.acceptor_energy,
                                 Nd, params.donor_energy,
                                 params.temperature)

            self.model.Ns = Ns
            self.model.rho = 1 / sigma
            self.model.sigma = sigma
            self.model.notify_visualizers()
        except:
            print(exc_info())

        return
