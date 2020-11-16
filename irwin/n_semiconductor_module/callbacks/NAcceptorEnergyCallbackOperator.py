from fompy.constants import eV

from irwin.CallbackOperator import CallbackOperator
from irwin.config import GUIParameters
from irwin.n_semiconductor_module.NInputData import NInputData


class NAcceptorEnergyCallbackOperator(CallbackOperator):
    def __init__(self):
        self.window = None
        self.parameters = NInputData()

    def connect_callback(self, window):
        self.window = window

        self.setup_callback_and_synchronize_slider(
            validator_min=GUIParameters.AcceptorEnergySliderMin,
            validator_max=GUIParameters.AcceptorEnergySliderMax,
            validator_accuracy=GUIParameters.AcceptorEnergyLineEditAccuracy,
            line_edit=self.window.n_AcceptorEnergylineEdit,
            slider_min=GUIParameters.AcceptorEnergySliderMin,
            slider_max=GUIParameters.AcceptorEnergySliderMax,
            slider=self.window.n_AcceptorEnergyhorizontalSlider,
            update_slider_func=self.update_energy_slider,
            update_line_edit_func=self.update_energy_line_edit
        )

    def update_energy_slider(self):
        self.update_slider(
            line_edit=self.window.n_AcceptorEnergylineEdit,
            slider=self.window.n_AcceptorEnergyhorizontalSlider,
            calc_constant=GUIParameters.AcceptorEnergyCalcConstant
        )

    def update_energy_line_edit(self):
        self.update_line_edit(
            line_edit=self.window.n_AcceptorEnergylineEdit,
            slider=self.window.n_AcceptorEnergyhorizontalSlider,
            calc_constant=GUIParameters.AcceptorEnergyCalcConstant,
            update_model_func=self.update_acceptor_energy
        )

    def update_acceptor_energy(self, val):
        self.parameters.acceptor_energy = val * eV
