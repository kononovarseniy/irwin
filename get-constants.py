import csv
from functools import partial
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from fompy.materials import Si, DopedSemiconductor
from fompy.constants import *


class Line:
    def __init__(self, xs, ys):
        self.xs = np.array(list(xs))
        self.ys = np.array(list(ys))


def get_lines(filename):
    unit = 1 / volt

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
    return {l: Line((p[0] for p in ps), (p[1] * unit for p in ps)) for l, ps in lines.items()}


@np.vectorize
def _mobility(mat, temp, c0, c1):
    return 1 / ((temp / c0) ** (3 / 2) + (mat.p_donor_concentration(T=temp) + mat.n_acceptor_concentration(T=temp)) * (
            c1 / temp) ** (3 / 2))


def mobility(mat, temp, c0, c1):
    return _mobility(mat, temp, c0, c1)


def fit(line, mat, p0):
    mob = partial(mobility, mat)
    ps, cov = curve_fit(mob, line.xs, line.ys, p0, bounds=([0, 1e-20], [np.inf, 1]))
    print(cov)
    print(ps)
    return line.xs, mob(line.xs, *p0)  # WAARNING should be ps


lines = get_lines('data/Si_mobility.csv')

l1 = lines['1']
l2 = lines['2']
l3 = lines['3']
l4 = lines['4']

mat1 = DopedSemiconductor(Si, 0, 0, 0, 0)
mat3 = DopedSemiconductor(Si, 1.48e15, 0.045 * eV * 0, 1.75e16, Si.Eg - 0.045 * eV * 0)
mat4 = DopedSemiconductor(Si, 2.2e15, 0.045 * eV * 0, 1.3e17, Si.Eg - 0.045 * eV * 0)

print(mat4.p_donor_concentration(T=23.512) + mat4.n_acceptor_concentration(T=23.512))
print(mat4.p_donor_concentration(T=194.81) + mat4.n_acceptor_concentration(T=194.81))

plt.plot(l1.xs, l1.ys)
plt.plot(l2.xs, l2.ys)
plt.plot(l3.xs, l3.ys)
plt.plot(l4.xs, l4.ys)

# 4.764e5*300=(x/7.607)^(3/2)
plt.plot(*fit(l1, mat1, (2.07e6, 1e-14)), 'b:', label='1.1')
# 15854*300=1/((23.512/x)^(3/2)+2960277657111008*(y/23.512)^(3/2)), 2517.5*300=1/((194.81/x)^(3/2)+1.7606045716653234e+16*(y/194.81)^(3/2))
plt.plot(*fit(l3, mat3, (1.64e6, 3.31e-14)), 'g:', label='3.1')
# 3249.2*300=1/((23.986/x)^(3/2)+4400851187348220.5*(y/23.986)^(3/2)), 670.2*300=1/((346.91/x)^(3/2)+8.902938149675554e+16*(y/346.91)^(3/2))
plt.plot(*fit(l4, mat4, (1.24e6, 8.58e-14)), 'r:', label='4.1')

plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.show()
