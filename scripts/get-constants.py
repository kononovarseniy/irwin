import csv

import matplotlib.pyplot as plt
import numpy as np
from fompy.materials import Si
from fompy.models import DopedSemiconductor
from fompy.units import unit
from scipy.optimize import curve_fit

MOBILITY_UNIT = unit('cm^2 / V s')
A_UNIT = unit('cm^2 K^3/2 / V s')
B_UNIT = unit('K^3')


class Line:
    def __init__(self, xs, ys, mat, color, label):
        self.xs = np.array(list(xs))
        self.ys = np.array(list(ys))
        self.mat = mat
        self.color = color
        self.label = label


def get_lines(filename, desc):
    line = None
    lines = dict()
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for r in reader:
            if len(r) == 0:
                continue
            if r[0] == 'x':
                line = r[1]
                lines[line] = ([], [])
                continue
            x, y = map(float, r)
            lines[line][0].append(x)
            lines[line][1].append(y * MOBILITY_UNIT)

    res = []
    for name, mat, color, label in desc:
        xs, ys = lines[name]
        res.append(Line(xs, ys, mat, color, label))

    return res


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


def print_params(ps, name):
    print(f'Results for {name}:')
    print(f'    A = {ps[0]:e} CGS = {ps[0] / A_UNIT:e} cm^2 K^3/2 / V s')
    print(f'    B = {ps[1]:e} K^3')


def make_mobility_func(mat):
    return np.vectorize(lambda t, a, b: mobility(mat, t, a, b))


def fit_mobility_curve(line, p0):
    mob = make_mobility_func(line.mat)
    ps, _cov = curve_fit(mob, line.xs, line.ys, p0)
    return ps


def fit_two_curves(l1, l2, p0=(2e9, 2e-12)):
    p1 = fit_mobility_curve(l1, p0)
    p2 = fit_mobility_curve(l2, p0)
    return tuple((a + b) / 2 for a, b in zip(p1, p2))


def handle_line(line, ps=None, p0=(2e9, 2e-12)):
    if ps is None:
        ps = fit_mobility_curve(line, p0)
        print_params(ps, line.label)
    xs = line.xs
    ys = make_mobility_func(line.mat)(xs, *ps)
    plt.plot(xs, ys, line.color + '--', label=line.label)
    return xs, ys


def start_plot(lines, title):
    plt.title(title)
    for l in lines:
        plt.plot(l.xs, l.ys, l.color)


def complete_plot():
    plt.legend()
    plt.xscale('log')
    plt.yscale('log')
    plt.show()


def handle_independent(lines, title):
    start_plot(lines, title)
    for line in lines:
        handle_line(line)
    complete_plot()


def handle_two(l1, l2, title):
    start_plot(lines, title)
    mean_ps = fit_two_curves(l1, l2)
    print_params(mean_ps, title)

    handle_line(l1, mean_ps)
    handle_line(l2, mean_ps)
    complete_plot()


if __name__ == '__main__':
    print('=== electrons ===')
    desc = [
        ('1', DopedSemiconductor(Si, 0, 0, 1e12, Si.Eg), 'k', '1'),
        ('2', DopedSemiconductor(Si, 0, 0, 1e13, Si.Eg), 'r', '2'),
        ('3', DopedSemiconductor(Si, 1.48e15, 0, 1.75e16, Si.Eg), 'g', '3'),
        ('4', DopedSemiconductor(Si, 2.2e15, 0, 1.3e17, Si.Eg), 'b', '4'),
    ]

    lines = get_lines('../data/Si_n/mobility.csv', desc)
    handle_independent(lines, 'Константы вчсиляются для каждой кривой')
    print('==========')
    handle_two(lines[2], lines[3], 'Константы усреднены для кривых 3 и 4')

    print('=== holes ===')
    desc = [
        ('1', DopedSemiconductor(Si, 1e12, 0, 0, Si.Eg), 'k', '1'),
        ('2', DopedSemiconductor(Si, 1e14, 0, 0, Si.Eg), 'r', '2'),
        ('3', DopedSemiconductor(Si, 2.4e16, 0, 2.3e15, Si.Eg), 'g', '3'),
        ('4', DopedSemiconductor(Si, 2.0e17, 0, 4.9e15, Si.Eg), 'b', '4'),
    ]

    lines = get_lines('../data/Si_p/mobility.csv', desc)
    handle_independent(lines, 'Константы вчсиляются для каждой кривой')
    print('==========')
    handle_two(lines[2], lines[3], 'Константы усреднены для кривых 3 и 4')
