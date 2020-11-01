from irwin.p_semiconductor_module.Visualiser import Visualiser

class PDataVisualiser(Visualiser):
    def __init__(self, controller, model):
        super().__init__(controller, model)


    #  overriden
    def update_model(self):
        print(f'updating_model')
