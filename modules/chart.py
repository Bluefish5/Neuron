

from time import sleep
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QWidget
from matplotlib.figure import Figure

class ChartMPL(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.ax = fig.add_subplot(111)
        super(ChartMPL, self).__init__(fig)

class Ui_Dialog2(object):
    def __init__(self,system):
        self.system=system

    def setupUi(self, Dialog):
        
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 600)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Wykres = QtWidgets.QLabel(Dialog)
        self.Wykres.setMaximumSize(QtCore.QSize(16777215, 30))
        self.Wykres.setObjectName("Wykres")
        self.verticalLayout.addWidget(self.Wykres)

        self.chart = ChartMPL(Dialog)
        self.system.tab = []
        self.chart.ax.cla()
        for i in self.system.resultErrorText.split("\n"):
            if i == "":
                break
            self.system.tab.append(float(i))
        self.chart.ax.plot(self.system.tab)
        self.chart.show()
        self.verticalLayout.addWidget(self.chart)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Wykres.setText(_translate("Dialog", "Wykres:"))

