from irwin.ApplicationManager import ApplicationManager
from PyQt5 import QtWidgets

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    App = ApplicationManager()
    App.ShowGUI()
    sys.exit(app.exec_())
