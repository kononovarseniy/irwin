from irwin.common.PlotTypeInputOperator import PlotTypeInputOperator


class NRadioButtonsCallbackOperator(PlotTypeInputOperator):
    def connect_callback(self, window):
        self.connect_callback_implementation(
            window.n_resistivity_radio_button,
            window.n_conductivity_radio_button
        )
