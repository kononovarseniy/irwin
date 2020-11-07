from fompy.units import unit
from fompy.constants import eV
from fompy.models import DopedSemiconductor, conductivity

RESISTIVITY_UNIT = unit('Ohm cm')
CONCENTRATION_UNIT = unit('cm-3')


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


def resistivity(mat, Na, Ea, Nd, Ed, T):
    """Вычисляет сопротивление по концентрациям в функции irwin написано тоже самое но *немного* оптимальнее"""
    A = mat.mobility_const_a
    B = mat.mobility_const_b
    sem = DopedSemiconductor(mat.semiconductor, Na, Ea, Nd, Ed)
    mob = mobility(sem, T, A, B)
    return 1 / conductivity(0, 0, sem.p_concentration(T=T), mobility(sem, T, A, B))
    # return 1 / conductivity(sem.n_concentration(T=T), mob, sem.p_concentration(T=T), mob)
