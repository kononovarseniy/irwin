from irwin.PCalculationParameters import PCalculationParameters
from irwin.CallbackOperator import CallbackOperator
from irwin.GUIParameters import GUIParameters


class AcceptorConcentrationCallbackOperator(CallbackOperator):
    def __init__(self):
        self.window = None
        self.parameters = PCalculationParameters()

    def connect_callback(self, window):
        self.window = window

        self.setup_callback_and_synchronize_slider(
            validator_min=GUIParameters.AcceptorConcentrationSliderMin,
            validator_max=GUIParameters.AcceptorConcentrationSliderMax,
            validator_accuracy=GUIParameters.AcceptorConcentrationLineEditAccuracy,
            line_edit=self.window.AcceptorConcentrationlineEdit,
            slider_min=GUIParameters.AcceptorConcentrationSliderMin,
            slider_max=GUIParameters.AcceptorConcentrationSliderMax,
            slider=self.window.AcceptorConcentrationhorizontalSlider,
            update_slider_func=self.update_acc_concentration_slider,
            update_line_edit_func=self.update_acc_concentration_line_edit
        )

        window.ConcentrationOrderspinBox.valueChanged.connect(self.update_order)

    def update_order(self):
        self.parameters.acceptor_concentration_order = self.window.ConcentrationOrderspinBox.value()
        self.update_acc_concentration_line_edit()

    def update_acc_concentration_slider(self):
        # TODO: fix duplicated code

        line_edit_text = self.window.AcceptorConcentrationlineEdit.text()

        if len(line_edit_text) == 0:
            line_edit_text = '0'
        line_edit_text = line_edit_text.replace(',', '.')
        value = float(line_edit_text)
        self.window.TemperaturehorizontalSlider.setValue(
            value * (10 ** GUIParameters.AcceptorConcentrationLineEditAccuracy))


    def update_acc_concentration_line_edit(self):
        value_to_set = self.window.AcceptorConcentrationhorizontalSlider.value()
        value_to_set /= GUIParameters.AcceptorConcentrationCalcConstant
        self.update_acc_concentration_mantissa(value_to_set)

        acceptor_concentration = self.parameters.acceptor_concentration
        scientific_notation = "{:.2e}".format(acceptor_concentration)
        text_to_set = str(scientific_notation)
        self.window.AcceptorConcentrationlineEdit.setText(text_to_set)


    def update_acc_concentration_mantissa(self, val):
        self.parameters.acceptor_concentration_mantissa = val
