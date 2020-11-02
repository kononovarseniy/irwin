from irwin.p_semiconductor_module.Visualiser import Visualiser
import matplotlib.pyplot as plt


class PDataVisualiser(Visualiser):
    def __init__(self, controller, model):
        super().__init__(controller, model)
        self._figure = plt.figure()
        self._graph = self._figure.add_subplot(111)

    #  overriden
    def update_model(self):
        print(f'updating_model')
        self._graph.clear()
        self._graph.plot(
            x=self.Model.Nds, y=self.Model.rho
        )
        plt.title('Irwin Curve')
        plt.ylabel('Resistivity')
        plt.xlabel('Donor concentrations')
