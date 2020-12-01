import sys

from PyQt5 import QtWidgets

from irwin.ApplicationManager import ApplicationManager

if __name__ == "__main__":
    qt_app = QtWidgets.QApplication(sys.argv)
    app = ApplicationManager()
    app.show_gui()
    sys.exit(qt_app.exec_())
