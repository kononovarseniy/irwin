import numpy as np
from fompy import models
from fompy.models import DopedSemiconductor


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
