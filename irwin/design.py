# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("main_window")
        MainWindow.resize(1040, 734)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MaterialcomboBox = QtWidgets.QComboBox(self.centralwidget)
        self.MaterialcomboBox.setGeometry(QtCore.QRect(600, 60, 73, 22))
        self.MaterialcomboBox.setObjectName("MaterialcomboBox")
        self.MaterialcomboBox.addItem("")
        self.MaterialcomboBox.setItemText(0, "")
        self.MaterialcomboBox.addItem("")
        self.MaterialcomboBox.addItem("")
        self.Materiallabel = QtWidgets.QLabel(self.centralwidget)
        self.Materiallabel.setGeometry(QtCore.QRect(530, 60, 55, 16))
        self.Materiallabel.setObjectName("Materiallabel")
        self.AcceptorConcentrationlabel = QtWidgets.QLabel(self.centralwidget)
        self.AcceptorConcentrationlabel.setGeometry(QtCore.QRect(440, 110, 141, 20))
        self.AcceptorConcentrationlabel.setObjectName("AcceptorConcentrationlabel")
        self.DonorEnergylabel = QtWidgets.QLabel(self.centralwidget)
        self.DonorEnergylabel.setGeometry(QtCore.QRect(440, 170, 141, 20))
        self.DonorEnergylabel.setObjectName("DonorEnergylabel")
        self.AcceptorEnergylabel = QtWidgets.QLabel(self.centralwidget)
        self.AcceptorEnergylabel.setGeometry(QtCore.QRect(440, 190, 141, 20))
        self.AcceptorEnergylabel.setObjectName("AcceptorEnergylabel")
        self.Temperaturelabel = QtWidgets.QLabel(self.centralwidget)
        self.Temperaturelabel.setGeometry(QtCore.QRect(440, 140, 141, 20))
        self.Temperaturelabel.setObjectName("Temperaturelabel")
        self.AcceptorConcentrationlineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.AcceptorConcentrationlineEdit.setGeometry(QtCore.QRect(860, 110, 71, 22))
        self.AcceptorConcentrationlineEdit.setObjectName("AcceptorConcentrationlineEdit")
        self.DonorEnergylineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.DonorEnergylineEdit.setGeometry(QtCore.QRect(860, 170, 71, 22))
        self.DonorEnergylineEdit.setObjectName("DonorEnergylineEdit")
        self.AcceptorEnergylineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.AcceptorEnergylineEdit.setGeometry(QtCore.QRect(860, 200, 71, 22))
        self.AcceptorEnergylineEdit.setObjectName("AcceptorEnergylineEdit")
        self.TemperaturelineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.TemperaturelineEdit.setGeometry(QtCore.QRect(860, 140, 71, 22))
        self.TemperaturelineEdit.setObjectName("TemperaturelineEdit")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(600, 100, 241, 121))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(10, 11, 11, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.AcceptorConcentrationhorizontalSlider = QtWidgets.QSlider(self.layoutWidget)
        self.AcceptorConcentrationhorizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.AcceptorConcentrationhorizontalSlider.setObjectName("AcceptorConcentrationhorizontalSlider")
        self.verticalLayout.addWidget(self.AcceptorConcentrationhorizontalSlider)
        self.TemperaturehorizontalSlider = QtWidgets.QSlider(self.layoutWidget)
        self.TemperaturehorizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.TemperaturehorizontalSlider.setObjectName("TemperaturehorizontalSlider")
        self.verticalLayout.addWidget(self.TemperaturehorizontalSlider)
        self.DonorEnergyhorizontalSlider = QtWidgets.QSlider(self.layoutWidget)
        self.DonorEnergyhorizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.DonorEnergyhorizontalSlider.setObjectName("DonorEnergyhorizontalSlider")
        self.verticalLayout.addWidget(self.DonorEnergyhorizontalSlider)
        self.AcceptorEnergyhorizontalSlider = QtWidgets.QSlider(self.layoutWidget)
        self.AcceptorEnergyhorizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.AcceptorEnergyhorizontalSlider.setObjectName("AcceptorEnergyhorizontalSlider")
        self.verticalLayout.addWidget(self.AcceptorEnergyhorizontalSlider)
        self.verticalLayout.setStretch(3, 100)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(610, 380, 241, 111))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalSlider_8 = QtWidgets.QSlider(self.layoutWidget1)
        self.horizontalSlider_8.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_8.setObjectName("horizontalSlider_8")
        self.verticalLayout_2.addWidget(self.horizontalSlider_8)
        self.horizontalSlider_7 = QtWidgets.QSlider(self.layoutWidget1)
        self.horizontalSlider_7.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_7.setObjectName("horizontalSlider_7")
        self.verticalLayout_2.addWidget(self.horizontalSlider_7)
        self.horizontalSlider_6 = QtWidgets.QSlider(self.layoutWidget1)
        self.horizontalSlider_6.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_6.setObjectName("horizontalSlider_6")
        self.verticalLayout_2.addWidget(self.horizontalSlider_6)
        self.horizontalSlider_5 = QtWidgets.QSlider(self.layoutWidget1)
        self.horizontalSlider_5.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_5.setObjectName("horizontalSlider_5")
        self.verticalLayout_2.addWidget(self.horizontalSlider_5)
        self.TestpushButton = QtWidgets.QPushButton(self.centralwidget)
        self.TestpushButton.setGeometry(QtCore.QRect(600, 250, 93, 28))
        self.TestpushButton.setObjectName("TestpushButton")
        self.CalculatepushButton = QtWidgets.QPushButton(self.centralwidget)
        self.CalculatepushButton.setGeometry(QtCore.QRect(710, 250, 93, 28))
        self.CalculatepushButton.setObjectName("CalculatepushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1040, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("main_window", "main_window"))
        self.MaterialcomboBox.setItemText(1, _translate("main_window", "Si"))
        self.MaterialcomboBox.setItemText(2, _translate("main_window", "GaAs"))
        self.Materiallabel.setText(_translate("main_window", "Material"))
        self.AcceptorConcentrationlabel.setText(_translate("main_window", "Acceptor Concentration"))
        self.DonorEnergylabel.setText(_translate("main_window", "Donor Energy"))
        self.AcceptorEnergylabel.setText(_translate("main_window", "Acceptor Energy"))
        self.Temperaturelabel.setText(_translate("main_window", "Temperature"))
        self.TestpushButton.setText(_translate("main_window", "Test"))
        self.CalculatepushButton.setText(_translate("main_window", "Calculate"))