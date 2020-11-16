class InputData:
    def __init__(self, conductivity_type):
        self.type = conductivity_type
        self.material = None
        self.plot_resistivity = True
        self.plot_conductivity = False

        self.temperature = 0.0
        self.donor_energy = 0.0
        self.acceptor_energy = 0.0
