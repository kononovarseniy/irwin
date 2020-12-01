from irwin.singleton import singleton

@singleton
class OutputData:
    def __init__(self):
        self.visualizers = []
        self.Ns = []  # Concentrations
        self.rho = []  # Resistivity
        self.sigma = []  # Conductivity

    def add_visualiser(self, visualizer):
        self.visualizers.append(visualizer)

    def notify_visualizers(self):
        for vis in self.visualizers:
            vis.update_model()
