# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from p_semiconductor_module.PPlotCanvas import PPlotCanvas
from n_semiconductor_module.NPlotCanvas import NPlotCanvas


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1040, 734)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MaterialcomboBox = QtWidgets.QComboBox(self.centralwidget)
        self.MaterialcomboBox.setGeometry(QtCore.QRect(560, 90, 73, 22))
        self.pTypePlot = PPlotCanvas(parent=self)
        self.pTypePlot.move(0, 0)
        self.nTypePlot = NPlotCanvas(parent=self)
        self.nTypePlot.move(0, 350)
        self.MaterialcomboBox.setObjectName("MaterialcomboBox")
        self.MaterialcomboBox.addItem("")
        self.MaterialcomboBox.setItemText(0, "")
        self.MaterialcomboBox.addItem("")
        self.MaterialcomboBox.addItem("")
        self.Materiallabel = QtWidgets.QLabel(self.centralwidget)
        self.Materiallabel.setGeometry(QtCore.QRect(490, 90, 55, 16))
        self.Materiallabel.setObjectName("Materiallabel")
        self.AcceptorConcentrationlabel = QtWidgets.QLabel(self.centralwidget)
        self.AcceptorConcentrationlabel.setGeometry(
            QtCore.QRect(400, 140, 141, 20))
        self.AcceptorConcentrationlabel.setObjectName(
            "AcceptorConcentrationlabel")
        self.DonorEnergylabel = QtWidgets.QLabel(self.centralwidget)
        self.DonorEnergylabel.setGeometry(QtCore.QRect(400, 200, 141, 20))
        self.DonorEnergylabel.setObjectName("DonorEnergylabel")
        self.AcceptorEnergylabel = QtWidgets.QLabel(self.centralwidget)
        self.AcceptorEnergylabel.setGeometry(QtCore.QRect(400, 220, 141, 20))
        self.AcceptorEnergylabel.setObjectName("AcceptorEnergylabel")
        self.Temperaturelabel = QtWidgets.QLabel(self.centralwidget)
        self.Temperaturelabel.setGeometry(QtCore.QRect(400, 170, 141, 20))
        self.Temperaturelabel.setObjectName("Temperaturelabel")
        self.AcceptorConcentrationlineEdit = QtWidgets.QLineEdit(
            self.centralwidget)
        self.AcceptorConcentrationlineEdit.setGeometry(
            QtCore.QRect(870, 140, 71, 22))
        self.AcceptorConcentrationlineEdit.setReadOnly(True)
        self.AcceptorConcentrationlineEdit.setObjectName(
            "AcceptorConcentrationlineEdit")
        self.DonorEnergylineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.DonorEnergylineEdit.setGeometry(QtCore.QRect(870, 200, 71, 22))
        self.DonorEnergylineEdit.setObjectName("DonorEnergylineEdit")
        self.AcceptorEnergylineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.AcceptorEnergylineEdit.setGeometry(QtCore.QRect(870, 230, 71, 22))
        self.AcceptorEnergylineEdit.setObjectName("AcceptorEnergylineEdit")
        self.TemperaturelineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.TemperaturelineEdit.setGeometry(QtCore.QRect(870, 170, 71, 22))
        self.TemperaturelineEdit.setObjectName("TemperaturelineEdit")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(560, 130, 241, 121))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(10, 11, 11, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.AcceptorConcentrationhorizontalSlider = QtWidgets.QSlider(
            self.layoutWidget)
        self.AcceptorConcentrationhorizontalSlider.setOrientation(
            QtCore.Qt.Horizontal)
        self.AcceptorConcentrationhorizontalSlider.setObjectName(
            "AcceptorConcentrationhorizontalSlider")
        self.verticalLayout.addWidget(
            self.AcceptorConcentrationhorizontalSlider)
        self.TemperaturehorizontalSlider = QtWidgets.QSlider(self.layoutWidget)
        self.TemperaturehorizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.TemperaturehorizontalSlider.setObjectName(
            "TemperaturehorizontalSlider")
        self.verticalLayout.addWidget(self.TemperaturehorizontalSlider)
        self.DonorEnergyhorizontalSlider = QtWidgets.QSlider(self.layoutWidget)
        self.DonorEnergyhorizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.DonorEnergyhorizontalSlider.setObjectName(
            "DonorEnergyhorizontalSlider")
        self.verticalLayout.addWidget(self.DonorEnergyhorizontalSlider)
        self.AcceptorEnergyhorizontalSlider = QtWidgets.QSlider(
            self.layoutWidget)
        self.AcceptorEnergyhorizontalSlider.setOrientation(
            QtCore.Qt.Horizontal)
        self.AcceptorEnergyhorizontalSlider.setObjectName(
            "AcceptorEnergyhorizontalSlider")
        self.verticalLayout.addWidget(self.AcceptorEnergyhorizontalSlider)
        self.verticalLayout.setStretch(3, 100)
        self.CalculatepushButton = QtWidgets.QPushButton(self.centralwidget)
        self.CalculatepushButton.setGeometry(QtCore.QRect(560, 280, 93, 28))
        self.CalculatepushButton.setObjectName("CalculatepushButton")
        self.ConcentrationOrderspinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.ConcentrationOrderspinBox.setGeometry(
            QtCore.QRect(810, 140, 42, 22))
        self.ConcentrationOrderspinBox.setMinimum(1)
        self.ConcentrationOrderspinBox.setMaximum(12)
        self.ConcentrationOrderspinBox.setObjectName(
            "ConcentrationOrderspinBox")
        self.n_TemperaturelineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.n_TemperaturelineEdit.setGeometry(QtCore.QRect(870, 490, 71, 22))
        self.n_TemperaturelineEdit.setObjectName("n_TemperaturelineEdit")
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(560, 450, 241, 121))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_2.setContentsMargins(10, 11, 11, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.DonorConcentrationhorizontalSlider = QtWidgets.QSlider(
            self.layoutWidget_2)
        self.DonorConcentrationhorizontalSlider.setOrientation(
            QtCore.Qt.Horizontal)
        self.DonorConcentrationhorizontalSlider.setObjectName(
            "DonorConcentrationhorizontalSlider")
        self.verticalLayout_2.addWidget(
            self.DonorConcentrationhorizontalSlider)
        self.n_TemperaturehorizontalSlider = QtWidgets.QSlider(
            self.layoutWidget_2)
        self.n_TemperaturehorizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.n_TemperaturehorizontalSlider.setObjectName(
            "n_TemperaturehorizontalSlider")
        self.verticalLayout_2.addWidget(self.n_TemperaturehorizontalSlider)
        self.n_DonorEnergyhorizontalSlider = QtWidgets.QSlider(
            self.layoutWidget_2)
        self.n_DonorEnergyhorizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.n_DonorEnergyhorizontalSlider.setObjectName(
            "n_DonorEnergyhorizontalSlider")
        self.verticalLayout_2.addWidget(self.n_DonorEnergyhorizontalSlider)
        self.n_AcceptorEnergyhorizontalSlider = QtWidgets.QSlider(
            self.layoutWidget_2)
        self.n_AcceptorEnergyhorizontalSlider.setOrientation(
            QtCore.Qt.Horizontal)
        self.n_AcceptorEnergyhorizontalSlider.setObjectName(
            "n_AcceptorEnergyhorizontalSlider")
        self.verticalLayout_2.addWidget(self.n_AcceptorEnergyhorizontalSlider)
        self.verticalLayout_2.setStretch(3, 100)
        self.n_ConcentrationOrderspinBox = QtWidgets.QSpinBox(
            self.centralwidget)
        self.n_ConcentrationOrderspinBox.setGeometry(
            QtCore.QRect(810, 460, 42, 22))
        self.n_ConcentrationOrderspinBox.setMinimum(1)
        self.n_ConcentrationOrderspinBox.setMaximum(12)
        self.n_ConcentrationOrderspinBox.setObjectName(
            "n_ConcentrationOrderspinBox")
        self.DonorConcentrationlineEdit = QtWidgets.QLineEdit(
            self.centralwidget)
        self.DonorConcentrationlineEdit.setGeometry(
            QtCore.QRect(870, 460, 71, 22))
        self.DonorConcentrationlineEdit.setReadOnly(True)
        self.DonorConcentrationlineEdit.setObjectName(
            "DonorConcentrationlineEdit")
        self.n_AcceptorEnergylineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.n_AcceptorEnergylineEdit.setGeometry(
            QtCore.QRect(870, 550, 71, 22))
        self.n_AcceptorEnergylineEdit.setObjectName("n_AcceptorEnergylineEdit")
        self.Materiallabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.Materiallabel_2.setGeometry(QtCore.QRect(490, 410, 55, 16))
        self.Materiallabel_2.setObjectName("Materiallabel_2")
        self.DonorEnergylabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.DonorEnergylabel_2.setGeometry(QtCore.QRect(400, 520, 141, 20))
        self.DonorEnergylabel_2.setObjectName("DonorEnergylabel_2")
        self.Temperaturelabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.Temperaturelabel_2.setGeometry(QtCore.QRect(400, 490, 141, 20))
        self.Temperaturelabel_2.setObjectName("Temperaturelabel_2")
        self.n_CalculatepushButton = QtWidgets.QPushButton(self.centralwidget)
        self.n_CalculatepushButton.setGeometry(QtCore.QRect(560, 600, 93, 28))
        self.n_CalculatepushButton.setObjectName("n_CalculatepushButton")
        self.n_MaterialcomboBox = QtWidgets.QComboBox(self.centralwidget)
        self.n_MaterialcomboBox.setGeometry(QtCore.QRect(560, 410, 73, 22))
        self.n_MaterialcomboBox.setObjectName("n_MaterialcomboBox")
        self.n_MaterialcomboBox.addItem("")
        self.n_MaterialcomboBox.setItemText(0, "")
        self.n_MaterialcomboBox.addItem("")
        self.n_MaterialcomboBox.addItem("")
        self.AcceptorEnergylabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.AcceptorEnergylabel_2.setGeometry(QtCore.QRect(400, 540, 141, 20))
        self.AcceptorEnergylabel_2.setObjectName("AcceptorEnergylabel_2")
        self.n_DonorEnergylineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.n_DonorEnergylineEdit.setGeometry(QtCore.QRect(870, 520, 71, 22))
        self.n_DonorEnergylineEdit.setObjectName("n_DonorEnergylineEdit")
        self.AcceptorConcentrationlabel_2 = QtWidgets.QLabel(
            self.centralwidget)
        self.AcceptorConcentrationlabel_2.setGeometry(
            QtCore.QRect(400, 460, 141, 20))
        self.AcceptorConcentrationlabel_2.setObjectName(
            "AcceptorConcentrationlabel_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(650, 60, 241, 61))
        self.groupBox.setTitle("")
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName("groupBox")
        self.ResistivityradioButton = QtWidgets.QRadioButton(self.groupBox)
        self.ResistivityradioButton.setEnabled(True)
        self.ResistivityradioButton.setGeometry(QtCore.QRect(0, 30, 121, 20))
        self.ResistivityradioButton.setAutoFillBackground(False)
        self.ResistivityradioButton.setChecked(True)
        self.ResistivityradioButton.setObjectName("ResistivityradioButton")
        self.ConductivityradioButton = QtWidgets.QRadioButton(self.groupBox)
        self.ConductivityradioButton.setGeometry(
            QtCore.QRect(120, 30, 121, 20))
        self.ConductivityradioButton.setObjectName("ConductivityradioButton")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(660, 390, 271, 51))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setFlat(True)
        self.groupBox_2.setObjectName("groupBox_2")
        self.n_ResistivityradioButton = QtWidgets.QRadioButton(self.groupBox_2)
        self.n_ResistivityradioButton.setEnabled(True)
        self.n_ResistivityradioButton.setGeometry(
            QtCore.QRect(10, 20, 121, 20))
        self.n_ResistivityradioButton.setAutoFillBackground(False)
        self.n_ResistivityradioButton.setChecked(True)
        self.n_ResistivityradioButton.setObjectName("n_ResistivityradioButton")
        self.n_ConductivityradioButton = QtWidgets.QRadioButton(
            self.groupBox_2)
        self.n_ConductivityradioButton.setGeometry(
            QtCore.QRect(130, 20, 121, 20))
        self.n_ConductivityradioButton.setObjectName(
            "n_ConductivityradioButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(390, 30, 601, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(233, 233, 233))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 106, 106))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(141, 141, 141))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(233, 233, 233))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(233, 233, 233))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 106, 106))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(141, 141, 141))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(233, 233, 233))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 106, 106))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(233, 233, 233))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 106, 106))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(141, 141, 141))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 106, 106))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 106, 106))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.PlaceholderText, brush)
        self.lineEdit.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.lineEdit.setFont(font)
        self.lineEdit.setFrame(False)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(390, 350, 601, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(233, 233, 233))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 106, 106))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(141, 141, 141))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(233, 233, 233))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(233, 233, 233))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 106, 106))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(141, 141, 141))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(233, 233, 233))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 106, 106))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(233, 233, 233))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 106, 106))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(141, 141, 141))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 106, 106))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 106, 106))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 212, 212))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.PlaceholderText, brush)
        self.lineEdit_2.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setFrame(False)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.AcceptorConcentrationlabel_3 = QtWidgets.QLabel(
            self.centralwidget)
        self.AcceptorConcentrationlabel_3.setGeometry(
            QtCore.QRect(950, 140, 141, 20))
        self.AcceptorConcentrationlabel_3.setObjectName(
            "AcceptorConcentrationlabel_3")
        self.AcceptorConcentrationlabel_4 = QtWidgets.QLabel(
            self.centralwidget)
        self.AcceptorConcentrationlabel_4.setGeometry(
            QtCore.QRect(950, 170, 141, 20))
        self.AcceptorConcentrationlabel_4.setObjectName(
            "AcceptorConcentrationlabel_4")
        self.AcceptorConcentrationlabel_5 = QtWidgets.QLabel(
            self.centralwidget)
        self.AcceptorConcentrationlabel_5.setGeometry(
            QtCore.QRect(950, 200, 141, 20))
        self.AcceptorConcentrationlabel_5.setObjectName(
            "AcceptorConcentrationlabel_5")
        self.AcceptorConcentrationlabel_6 = QtWidgets.QLabel(
            self.centralwidget)
        self.AcceptorConcentrationlabel_6.setGeometry(
            QtCore.QRect(950, 230, 141, 20))
        self.AcceptorConcentrationlabel_6.setObjectName(
            "AcceptorConcentrationlabel_6")
        self.AcceptorConcentrationlabel_7 = QtWidgets.QLabel(
            self.centralwidget)
        self.AcceptorConcentrationlabel_7.setGeometry(
            QtCore.QRect(950, 490, 141, 20))
        self.AcceptorConcentrationlabel_7.setObjectName(
            "AcceptorConcentrationlabel_7")
        self.AcceptorConcentrationlabel_8 = QtWidgets.QLabel(
            self.centralwidget)
        self.AcceptorConcentrationlabel_8.setGeometry(
            QtCore.QRect(950, 520, 141, 20))
        self.AcceptorConcentrationlabel_8.setObjectName(
            "AcceptorConcentrationlabel_8")
        self.AcceptorConcentrationlabel_9 = QtWidgets.QLabel(
            self.centralwidget)
        self.AcceptorConcentrationlabel_9.setGeometry(
            QtCore.QRect(950, 460, 141, 20))
        self.AcceptorConcentrationlabel_9.setObjectName(
            "AcceptorConcentrationlabel_9")
        self.AcceptorConcentrationlabel_10 = QtWidgets.QLabel(
            self.centralwidget)
        self.AcceptorConcentrationlabel_10.setGeometry(
            QtCore.QRect(950, 550, 141, 20))
        self.AcceptorConcentrationlabel_10.setObjectName(
            "AcceptorConcentrationlabel_10")
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
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.MaterialcomboBox.setItemText(1, _translate("MainWindow", "Si"))
        self.MaterialcomboBox.setItemText(2, _translate("MainWindow", "GaAs"))
        self.Materiallabel.setText(_translate("MainWindow", "Material"))
        self.AcceptorConcentrationlabel.setText(
            _translate("MainWindow", "Acceptor Concentration"))
        self.DonorEnergylabel.setText(_translate("MainWindow", "Donor Energy"))
        self.AcceptorEnergylabel.setText(
            _translate("MainWindow", "Acceptor Energy"))
        self.Temperaturelabel.setText(_translate("MainWindow", "Temperature"))
        self.CalculatepushButton.setText(_translate("MainWindow", "Calculate"))
        self.Materiallabel_2.setText(_translate("MainWindow", "Material"))
        self.DonorEnergylabel_2.setText(
            _translate("MainWindow", "Donor Energy"))
        self.Temperaturelabel_2.setText(
            _translate("MainWindow", "Temperature"))
        self.n_CalculatepushButton.setText(
            _translate("MainWindow", "Calculate"))
        self.n_MaterialcomboBox.setItemText(1, _translate("MainWindow", "Si"))
        self.n_MaterialcomboBox.setItemText(
            2, _translate("MainWindow", "GaAs"))
        self.AcceptorEnergylabel_2.setText(
            _translate("MainWindow", "Acceptor Energy"))
        self.AcceptorConcentrationlabel_2.setText(
            _translate("MainWindow", "Donor Concentration"))
        self.ResistivityradioButton.setText(
            _translate("MainWindow", "Plot Resistivity"))
        self.ConductivityradioButton.setText(
            _translate("MainWindow", "Plot Conductivity"))
        self.n_ResistivityradioButton.setText(
            _translate("MainWindow", "Plot Resistivity"))
        self.n_ConductivityradioButton.setText(
            _translate("MainWindow", "Plot Conductivity"))
        self.lineEdit.setText(_translate("MainWindow", "P-type semiconductor"))
        self.lineEdit_2.setText(_translate(
            "MainWindow", "N-type semiconductor"))
        self.AcceptorConcentrationlabel_3.setText(
            _translate("MainWindow", "[cm^(-3)]"))
        self.AcceptorConcentrationlabel_4.setText(
            _translate("MainWindow", "K"))
        self.AcceptorConcentrationlabel_5.setText(
            _translate("MainWindow", "eV "))
        self.AcceptorConcentrationlabel_6.setText(
            _translate("MainWindow", "eV"))
        self.AcceptorConcentrationlabel_7.setText(
            _translate("MainWindow", "K"))
        self.AcceptorConcentrationlabel_8.setText(
            _translate("MainWindow", "eV "))
        self.AcceptorConcentrationlabel_9.setText(
            _translate("MainWindow", "[cm^(-3)]"))
        self.AcceptorConcentrationlabel_10.setText(
            _translate("MainWindow", "eV"))
