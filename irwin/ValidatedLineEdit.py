from PyQt5.QtWidgets import QLineEdit


class ValidatedLineEdit(QLineEdit):
    def __init__(self, parent):
        super().__init__(parent)

        self.textEdited.connect(self.text_changed)
        self.default_style = self.styleSheet()

    def text_changed(self):
        if self.hasAcceptableInput():
            self.setStyleSheet(self.default_style)
        else:
            self.setStyleSheet("color: red;")
