import csv


class DataWriter:
    def __init__(self):
        pass

    @staticmethod
    def save_results(filename, concentration, conductivity, resistivity):
        print(f'saving results')
        with open(filename, 'w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(('concentration', 'conductivity', 'resistivity'))
            rows = zip(concentration, conductivity, resistivity)
            writer.writerows(rows)
