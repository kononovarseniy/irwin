import csv

from irwin.config import Units


class DataWriter:
    def __init__(self):
        pass

    @staticmethod
    def save_results(filename, model):
        print(f'saving results')
        with open(filename, 'w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(('concentration', 'conductivity', 'resistivity'))
            rows = zip(
                model.Ns / Units.CONCENTRATION,
                model.sigma / Units.CONDUCTIVITY,
                model.rho / Units.RESISTIVITY)
            writer.writerows(rows)
