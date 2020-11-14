

class ConcentrationData:
    def __init__(self):
        self.Visualisers = []




    def add_visualiser(self, Visualiser):
        self.Visualisers.append(Visualiser)

    def notify_observers(self):
        for vis in self.Visualisers:
            vis.update_model()