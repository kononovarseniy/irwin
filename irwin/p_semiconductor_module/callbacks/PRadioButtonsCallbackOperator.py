from irwin.common.PlotTypeInputOperator import PlotTypeInputOperator


class PRadioButtonsCallbackOperator(PlotTypeInputOperator):
    def connect_callback(self, window):
        self.connect_callback_implementation(
            window.p_resistivity_radio_button,
            window.p_conductivity_radio_button
        )
