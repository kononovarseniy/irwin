import csv
from dataclasses import dataclass
from typing import Dict, Iterable, List

import matplotlib.pyplot as plt
import numpy as np
from fompy.materials import Si, Ge, GaAs
from fompy.models import DopedSemiconductor
from fompy.units import unit
from scipy.optimize import curve_fit

MOBILITY_UNIT = unit('cm^2 / V s')
A_UNIT = unit('cm^2 K^3/2 / V s')
B_UNIT = unit('K^3')


@dataclass
class LineDescription:
    material: DopedSemiconductor
    style: str
    label: str


@dataclass
class Line:
    xs: np.array
    ys: np.array
    description: LineDescription


@dataclass
class FileDescription:
    title: str
    best_lines: List[str]
    lines: Dict[str, LineDescription]


def load_lines(filename: str, description: Dict[str, LineDescription]) -> Dict[str, Line]:
    line = None
    lines = dict()
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) == 0:
                continue
            if row[0] == 'x':  # Line header
                line = row[1]
                lines[line] = ([], [])
                continue
            x, y = map(float, row)
            lines[line][0].append(x)
            lines[line][1].append(y * MOBILITY_UNIT)

    res = {}
    for key, d in description.items():
        xs, ys = lines[key]
        res[key] = Line(np.array(xs), np.array(ys), d)

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


def make_mobility_func(mat):
    return np.vectorize(lambda t, a, b: mobility(mat, t, a, b))


def print_params(ps, title):
    print(title)
    print(f'    A = {ps[0]:e} CGS = {ps[0] / A_UNIT:e} cm^2 K^3/2 / V s')
    print(f'    B = {ps[1]:e} K^3')


def fit_mobility_curve(line: Line, p0: (float, float)) -> (float, float):
    mob = make_mobility_func(line.description.material)
    ps, _cov = curve_fit(mob, line.xs, line.ys, p0)
    return ps


def fit_then_average(lines: Iterable[Line], p0: (float, float)) -> (float, float):
    sum_a = 0
    sum_b = 0
    num = 0
    for line in lines:
        a, b = fit_mobility_curve(line, p0)
        sum_a += a
        sum_b += b
        num += 1
    return sum_a / num, sum_b / num


def draw_theoretical_line(line: Line, ps: (float, float)):
    xs = line.xs
    ys = make_mobility_func(line.description.material)(xs, *ps)
    plt.plot(xs, ys, line.description.style + '--', label=line.description.label)


def start_plot(lines: Iterable[Line], title: str):
    plt.title(title)
    for line in lines:
        plt.plot(line.xs, line.ys, line.description.style)


def complete_plot():
    plt.legend()
    plt.xscale('log')
    plt.yscale('log')
    plt.show()


descriptions = {
    'Si_n': FileDescription('Si electrons (Si_n)', ['3', '4'], {
        '1': LineDescription(DopedSemiconductor(Si, 0, 0, 1e12, Si.Eg), 'k', '1'),
        '2': LineDescription(DopedSemiconductor(Si, 0, 0, 1e13, Si.Eg), 'r', '2'),
        '3': LineDescription(DopedSemiconductor(Si, 1.48e15, 0, 1.75e16, Si.Eg), 'g', '3'),
        '4': LineDescription(DopedSemiconductor(Si, 2.2e15, 0, 1.3e17, Si.Eg), 'b', '4'),
    }),
    'Si_p': FileDescription('Si holes (Si_p)', ['3', '4'], {
        '1': LineDescription(DopedSemiconductor(Si, 1e12, 0, 0, Si.Eg), 'k', '1'),
        '2': LineDescription(DopedSemiconductor(Si, 1e14, 0, 0, Si.Eg), 'r', '2'),
        '3': LineDescription(DopedSemiconductor(Si, 2.4e16, 0, 2.3e15, Si.Eg), 'g', '3'),
        '4': LineDescription(DopedSemiconductor(Si, 2.0e17, 0, 4.9e15, Si.Eg), 'b', '4'),
    }),
    'Ge_n': FileDescription('Ge electrons (Ge_n)', ['2', '3', '4', '5', '6', '7'], {
        '1': LineDescription(DopedSemiconductor(Ge, 0, 0, 1.0e10, Ge.Eg), 'k', '1'),
        '2': LineDescription(DopedSemiconductor(Ge, 0, 0, 1.0e13, Ge.Eg), 'r', '2'),
        '3': LineDescription(DopedSemiconductor(Ge, 0, 0, 1.4e14, Ge.Eg), 'g', '3'),
        '4': LineDescription(DopedSemiconductor(Ge, 0, 0, 1.7e15, Ge.Eg), 'b', '4'),
        '5': LineDescription(DopedSemiconductor(Ge, 0, 0, 7.5e15, Ge.Eg), 'y', '5'),
        '6': LineDescription(DopedSemiconductor(Ge, 0, 0, 5.5e16, Ge.Eg), 'r', '6'),
        '7': LineDescription(DopedSemiconductor(Ge, 0, 0, 1.2e19, Ge.Eg), 'g', '7'),
    }),
    'Ge_p': FileDescription('Ge holes (Ge_p)', ['4', '5', '6', '7'], {
        '1': LineDescription(DopedSemiconductor(Ge, 1.0e10, 0, 0, Ge.Eg), 'k', '1'),
        '2': LineDescription(DopedSemiconductor(Ge, 4.9e13, 0, 0, Ge.Eg), 'r', '2'),
        '3': LineDescription(DopedSemiconductor(Ge, 3.2e15, 0, 0, Ge.Eg), 'g', '3'),
        '4': LineDescription(DopedSemiconductor(Ge, 2.7e16, 0, 0, Ge.Eg), 'b', '4'),
        '5': LineDescription(DopedSemiconductor(Ge, 1.2e17, 0, 0, Ge.Eg), 'y', '5'),
        '6': LineDescription(DopedSemiconductor(Ge, 4.9e18, 0, 0, Ge.Eg), 'r', '6'),
        '7': LineDescription(DopedSemiconductor(Ge, 2.0e20, 0, 0, Ge.Eg), 'g', '7'),
    }),
    'GaAs_n': FileDescription('GaAs electrons (GaAs_n)', ['bottom', 'middle'], {
        'bottom': LineDescription(DopedSemiconductor(GaAs, 0, 0, 5e15, GaAs.Eg), 'k', 'bottom'),
        'middle': LineDescription(DopedSemiconductor(GaAs, 0, 0, 1e15, GaAs.Eg), 'r', 'middle'),
        'top': LineDescription(DopedSemiconductor(GaAs, 0, 0, 5e15, GaAs.Eg), 'g', 'top'),  # Typo in description?
    }),
}


def main():
    for f_name, f_desc in descriptions.items():
        print('==========')
        print(f'Handling file {f_name}: {f_desc.title}')
        print('==========')
        filename = f'../data/{f_name}/mobility.csv'
        lines = load_lines(filename, f_desc.lines)
        start_plot(lines.values(), 'Независимые константы для каждой кривой')
        best_keys = set(key for key in f_desc.best_lines if key in lines)
        sum_a = sum_b = 0
        best_labels = []
        for key, line in lines.items():
            ps = fit_mobility_curve(line, (2e9, 2e-12))
            print_params(ps, f'{f_desc.title}: {line.description.label}')
            draw_theoretical_line(line, ps)
            if key in best_keys:
                sum_a += ps[0]
                sum_b += ps[1]
                best_labels.append(line.description.label)
        complete_plot()
        start_plot(lines.values(), f'Константы для кривых {", ".join(best_labels)}')
        avg_ps = sum_a / len(best_keys), sum_b / len(best_keys)
        print_params(avg_ps, f'{f_desc.title}: average constants')
        for key, line in lines.items():
            if key not in best_keys:
                continue
            draw_theoretical_line(line, avg_ps)
        complete_plot()
        print()


if __name__ == '__main__':
    main()
