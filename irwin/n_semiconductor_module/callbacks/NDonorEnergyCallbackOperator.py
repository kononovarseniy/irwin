from fompy.constants import eV

from irwin.CallbackOperator import CallbackOperator
from irwin.config import GUIParameters
from irwin.n_semiconductor_module.NCalculationParameters import NCalculationParameters


class NDonorEnergyCallbackOperator(CallbackOperator):
    def __init__(self):
        self.window = None
        self.parameters = NCalculationParameters()

    def connect_callback(self, window):
        self.window = window

        self.setup_callback_and_synchronize_slider(
            validator_min=GUIParameters.DonorEnergySliderMin,
            validator_max=GUIParameters.DonorEnergySliderMax,
            validator_accuracy=GUIParameters.DonorEnergyLineEditAccuracy,
            line_edit=self.window.n_DonorEnergylineEdit,
            slider_min=GUIParameters.DonorEnergySliderMin,
            slider_max=GUIParameters.DonorEnergySliderMax,
            slider=self.window.n_DonorEnergyhorizontalSlider,
            update_slider_func=self.update_energy_slider,
            update_line_edit_func=self.update_energy_line_edit
        )

    def update_energy_slider(self):
        self.update_slider(
            line_edit=self.window.DonorEnergylineEdit,
            slider=self.window.n_DonorEnergyhorizontalSlider,
            calc_constant=GUIParameters.DonorEnergyCalcConstant
        )

    def update_energy_line_edit(self):
        self.update_line_edit(
            line_edit=self.window.n_DonorEnergylineEdit,
            slider=self.window.n_DonorEnergyhorizontalSlider,
            calc_constant=GUIParameters.DonorEnergyCalcConstant,
            update_model_func=self.update_donor_energy
        )

    def update_donor_energy(self, val):
        self.parameters.donor_energy = val * eV
