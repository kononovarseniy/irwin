from irwin.ApplicationManager import ApplicationManager
from PyQt5 import QtWidgets

if __name__ == "__main__":
    import sys

    qt_app = QtWidgets.QApplication(sys.argv)
    app = ApplicationManager()
    app.show_gui()
    sys.exit(qt_app.exec_())
