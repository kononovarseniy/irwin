import csv

import matplotlib.pyplot as plt
import numpy as np
from fompy.constants import *
from fompy.materials import Si, DopedSemiconductor
from scipy.optimize import curve_fit

MOBILITY_UNIT = 1 / volt


class Line:
    def __init__(self, xs, ys):
        self.xs = np.array(list(xs))
        self.ys = np.array(list(ys))


def get_lines(filename):
    line = None
    lines = dict()
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for r in reader:
            if len(r) == 0:
                continue
            if r[0] == 'x':
                line = r[1]
                lines[line] = []
                continue
            lines[line].append(tuple(map(float, r)))
    return {l: Line((p[0] for p in ps), (p[1] * MOBILITY_UNIT for p in ps)) for l, ps in lines.items()}


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


def make_mobility_func(mat):
    return np.vectorize(lambda t, a, b: mobility(mat, t, a, b))


def fit_mobility_curve(mat, data, p0=(2e9, 2e-12)):
    mob = make_mobility_func(mat)
    ps, _cov = curve_fit(mob, data.xs, data.ys, p0)
    return ps


def fit_two_curves(m1, d1, m2, d2):
    p1 = fit_mobility_curve(m1, d1)
    p2 = fit_mobility_curve(m2, d2)
    return tuple((a + b) / 2 for a, b in zip(p1, p2))


def print_params(ps, name):
    print(f'Results for {name}:')
    print(f'    A = {ps[0]:e} CGS = {ps[0] / MOBILITY_UNIT:e} cm^2 / V s K^3')
    print(f'    B = {ps[1]:e} K^3')


def display_curve(mat, data, line, name, ps=None):
    if ps is None:
        ps = fit_mobility_curve(mat, data)
        print_params(ps, name)
    xs = data.xs
    ys = make_mobility_func(mat)(xs, *ps)
    plt.plot(xs, ys, line, label=name)
    return xs, ys


if __name__ == '__main__':
    lines = get_lines('data/Si_mobility.csv')

    l1 = lines['1']
    l2 = lines['2']
    l3 = lines['3']
    l4 = lines['4']

    mat1 = DopedSemiconductor(Si, 0, 0, 0, 0)
    mat3 = DopedSemiconductor(Si, 1.48e15, 0, 1.75e16, Si.Eg)
    mat4 = DopedSemiconductor(Si, 2.2e15, 0, 1.3e17, Si.Eg)

    plt.title('Константы вчсиляются для каждой кривой')
    plt.plot(l1.xs, l1.ys)
    plt.plot(l2.xs, l2.ys)
    plt.plot(l3.xs, l3.ys)
    plt.plot(l4.xs, l4.ys)

    display_curve(mat1, l1, 'b--', 'Pure Si')
    display_curve(mat3, l3, 'g--', '3')
    display_curve(mat4, l4, 'r--', '4')

    plt.xscale('log')
    plt.yscale('log')
    plt.legend()
    plt.show()

    print('==========')

    plt.title('Константы усреднены для кривых 3 и 4')
    plt.plot(l1.xs, l1.ys)
    plt.plot(l2.xs, l2.ys)
    plt.plot(l3.xs, l3.ys)
    plt.plot(l4.xs, l4.ys)

    mean = fit_two_curves(mat3, l3, mat4, l4)
    print_params(mean, 'curves 3 and 4')

    display_curve(mat1, l1, 'b--', 'Pure Si', mean)
    display_curve(mat3, l3, 'g--', '3', mean)
    display_curve(mat4, l4, 'r--', '4', mean)

    plt.xscale('log')
    plt.yscale('log')
    plt.legend()
    plt.show()
