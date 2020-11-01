from irwin.p_semiconductor_module import Visualiser

class DataVisualiser(Visualiser):
    def __init__(self, controller, model):
        super().__init__(controller, model)


    #  overriden
    def update_model(self):
        pass
