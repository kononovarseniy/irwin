class ConcentrationData:
    def __init__(self):
        self.visualizers = []
        self.rho = []  # Resistivity
        self.sigma = []  # Conductivity

    def add_visualiser(self, visualizer):
        self.visualizers.append(visualizer)

    def notify_visualizers(self):
        for vis in self.visualizers:
            vis.update_model()
