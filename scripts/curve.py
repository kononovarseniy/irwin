import matplotlib.pyplot as plt
import numpy as np
from fompy.constants import eV
from fompy.materials import Si
from fompy.models import DopedSemiconductor, conductivity
from fompy.units import unit

from irwin.materials import Material

MOBILITY_UNIT = unit('cm^2 / V s')
RESISTIVITY_UNIT = unit('Ohm cm')
CONCENTRATION_UNIT = unit('cm-3')
A_UNIT = unit('cm^2 K^3/2 / V s')
B_UNIT = unit('K^3')


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
    return 1 / conductivity(0, 0, sem.p_concentration(T=T), mobility(sem, T, A, B))


def irwin(mat, Ea, Nd, Ed, T, Nas):
    """
    То же что и выше но бес постоянного создания объектов (хотя это совсем не критично)
    Мне даже больше нравится первый вариант
    """
    A = mat.mobility_const_a
    B = mat.mobility_const_b
    sem = DopedSemiconductor(mat.semiconductor, -1, Ea, Nd, Ed)
    res = []
    for na in Nas:
        sem.Na = na
        cond = conductivity(0, 0, sem.p_concentration(T=T), mobility(sem, T, A, B))
        res.append(1 / cond)
    return np.array(res)


if __name__ == '__main__':
    # Константы расчитаны скриптом get-constants.py
    material = Material(Si, 2.413845e+06 * A_UNIT, 1.223030e-12 * B_UNIT)

    # Первым способом, через resistivity
    f = np.vectorize(resistivity)
    xs = np.logspace(13, 19, 100)
    ys = f(material, xs, 0.045 * eV, 0, Si.Eg, 300)
    # Вторым способом, через функцию irwin
    # (чуть быстрее но основные тормоза при вычислении уровня ферми)
    ys2 = irwin(material, 0.045 * eV, 0, Si.Eg, 300, xs)

    plt.title('Кривая Ирвина для Si p типа')
    plt.ylabel(r'$\rho$, $Ом \cdot см$')
    plt.xlabel(r'$N_a$, $см^{-3}$')
    plt.plot(xs / CONCENTRATION_UNIT, ys / RESISTIVITY_UNIT)
    plt.grid(True, which='both', axis='both')
    plt.xscale('log')
    plt.yscale('log')
    plt.show()
