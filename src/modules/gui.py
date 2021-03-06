import numpy as np
import sys
from .error import Ui_Dialog
from .chart import Ui_Dialog2
from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QWidget
from matplotlib.figure import Figure
import time

from modules.perceptron import Preceptron

class ChartMPL(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.ax = fig.add_subplot(111)
        super(ChartMPL, self).__init__(fig)

class Ui_MainWindow(object):
    def __init__(self,system):
        self.system=system

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.mainWidget = QtWidgets.QWidget(MainWindow)
        self.mainWidget.setObjectName("mainWidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.mainWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.mainFrame = QtWidgets.QFrame(self.mainWidget)
        self.mainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainFrame.setObjectName("mainFrame")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.mainFrame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.leftMainFrame = QtWidgets.QFrame(self.mainFrame)
        self.leftMainFrame.setMinimumSize(QtCore.QSize(100, 0))
        self.leftMainFrame.setMaximumSize(QtCore.QSize(100, 16777215))
        self.leftMainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.leftMainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.leftMainFrame.setObjectName("leftMainFrame")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.leftMainFrame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.readButton = QtWidgets.QPushButton(self.leftMainFrame)
        self.readButton.setMinimumSize(QtCore.QSize(0, 30))
        self.readButton.setObjectName("readButton")
        self.readButton.clicked.connect(self.browsefiles)


        self.verticalLayout_2.addWidget(self.readButton)
        self.saveButton = QtWidgets.QPushButton(self.leftMainFrame)
        self.saveButton.setMinimumSize(QtCore.QSize(0, 30))
        self.saveButton.setObjectName("saveButton")
        self.saveButton.clicked.connect(self.saveToFile)

        self.verticalLayout_2.addWidget(self.saveButton)
        self.configurationLearingFrame = QtWidgets.QFrame(self.leftMainFrame)
        self.configurationLearingFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.configurationLearingFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.configurationLearingFrame.setObjectName("configurationLearingFrame")


        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.configurationLearingFrame)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem)

        self.learningButton = QtWidgets.QPushButton(self.configurationLearingFrame)
        self.learningButton.setMinimumSize(QtCore.QSize(0, 60))
        self.learningButton.setObjectName("learningButton")
        self.verticalLayout_6.addWidget(self.learningButton)
        self.learningButton.clicked.connect(self.actionOnClickLearning)

        self.configurationButton = QtWidgets.QPushButton(self.configurationLearingFrame)
        self.configurationButton.setMinimumSize(QtCore.QSize(0, 60))
        self.configurationButton.setObjectName("configurationButton")
        self.verticalLayout_6.addWidget(self.configurationButton)
        self.configurationButton.clicked.connect(self.actionOnClickConfiguration)

        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(spacerItem1)
        self.verticalLayout_2.addWidget(self.configurationLearingFrame)
        self.horizontalLayout.addWidget(self.leftMainFrame)

        self.rightMainFrame = QtWidgets.QFrame(self.mainFrame)
        self.rightMainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.rightMainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rightMainFrame.setObjectName("rightMainFrame")

        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.rightMainFrame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.stackedWidget = QtWidgets.QStackedWidget(self.rightMainFrame)
        self.stackedWidget.setObjectName("stackedWidget")

        self.learningFrame = QtWidgets.QWidget()
        self.learningFrame.setObjectName("learningFrame")

        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.learningFrame)
        self.verticalLayout_5.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_5.setSpacing(9)
        self.verticalLayout_5.setObjectName("verticalLayout_5")

        self.learningFrameUp = QtWidgets.QFrame(self.learningFrame)
        self.learningFrameUp.setMaximumSize(QtCore.QSize(16777215, 100))
        self.learningFrameUp.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.learningFrameUp.setFrameShadow(QtWidgets.QFrame.Raised)
        self.learningFrameUp.setObjectName("learningFrameUp")

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.learningFrameUp)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.restartButton = QtWidgets.QPushButton(self.learningFrameUp)
        self.restartButton.setMinimumSize(QtCore.QSize(0, 60))
        self.restartButton.setObjectName("restartButton")
        self.restartButton.clicked.connect(self.actionOnClickRestart)

        self.horizontalLayout_3.addWidget(self.restartButton)
        self.oneStepButton = QtWidgets.QPushButton(self.learningFrameUp)
        self.oneStepButton.setMinimumSize(QtCore.QSize(0, 60))
        self.oneStepButton.setObjectName("oneStepButton")
        self.oneStepButton.clicked.connect(self.actionOnClickOneStep)

        self.horizontalLayout_3.addWidget(self.oneStepButton)
        self.autoStepButton = QtWidgets.QPushButton(self.learningFrameUp)
        self.autoStepButton.setMinimumSize(QtCore.QSize(0, 60))
        self.autoStepButton.setObjectName("autoStepButton")
        self.autoStepButton.clicked.connect(self.actionOnClickAutoStep)


        self.horizontalLayout_3.addWidget(self.autoStepButton)
        self.errorChartButton = QtWidgets.QPushButton(self.learningFrameUp)
        self.errorChartButton.setMinimumSize(QtCore.QSize(0, 60))
        self.errorChartButton.setObjectName("errorChartButton")
        self.errorChartButton.clicked.connect(self.showChart)


        self.horizontalLayout_3.addWidget(self.errorChartButton)
        self.verticalLayout_5.addWidget(self.learningFrameUp)
        self.learningFrameDown = QtWidgets.QFrame(self.learningFrame)
        self.learningFrameDown.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.learningFrameDown.setFrameShadow(QtWidgets.QFrame.Raised)
        self.learningFrameDown.setObjectName("learningFrameDown")

        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.learningFrameDown)
        self.verticalLayout_7.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_7.setSpacing(9)
        self.verticalLayout_7.setObjectName("verticalLayout_7")

        self.learningFrameDownChart = QtWidgets.QFrame(self.learningFrameDown)
        self.learningFrameDownChart.setMinimumSize(QtCore.QSize(0, 300))
        self.learningFrameDownChart.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.learningFrameDownChart.setFrameShadow(QtWidgets.QFrame.Raised)
        self.learningFrameDownChart.setObjectName("learningFrameDownChart")

        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.learningFrameDownChart)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")

        """
        *           *
        * Wykres    *
        *           *
        """
        self.timer = None
        self.chart = ChartMPL(self)
        self.chart.show()
        self.chart.setObjectName("wykres")
        self.verticalLayout_8.addWidget(self.chart)

        self.verticalLayout_7.addWidget(self.learningFrameDownChart)
        self.learningFrameDownText = QtWidgets.QFrame(self.learningFrameDown)
        self.learningFrameDownText.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.learningFrameDownText.setFrameShadow(QtWidgets.QFrame.Raised)
        self.learningFrameDownText.setObjectName("learningFrameDownText")

        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.learningFrameDownText)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        self.resultText = QtWidgets.QPlainTextEdit(self.learningFrameDownText)
        self.resultText.setReadOnly(True)
        self.resultText.setObjectName("resultText")

        self.horizontalLayout_4.addWidget(self.resultText)
        self.verticalLayout_7.addWidget(self.learningFrameDownText)
        self.verticalLayout_5.addWidget(self.learningFrameDown)
        self.stackedWidget.addWidget(self.learningFrame)

        self.configurationFrame = QtWidgets.QWidget()
        self.configurationFrame.setObjectName("configurationFrame")

        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.configurationFrame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        self.configurationFrameUp = QtWidgets.QFrame(self.configurationFrame)
        self.configurationFrameUp.setMaximumSize(QtCore.QSize(16777215, 100))
        self.configurationFrameUp.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.configurationFrameUp.setFrameShadow(QtWidgets.QFrame.Raised)
        self.configurationFrameUp.setObjectName("configurationFrameUp")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.configurationFrameUp)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.stopConditionButton = QtWidgets.QPushButton(self.configurationFrameUp)
        self.stopConditionButton.setMinimumSize(QtCore.QSize(0, 60))
        self.stopConditionButton.setMaximumSize(QtCore.QSize(200, 16777215))
        self.stopConditionButton.setObjectName("stopConditionButton")
        self.stopConditionButton.clicked.connect(self.errorConfiguration)

        self.horizontalLayout_2.addWidget(self.stopConditionButton)
        self.verticalLayout_4.addWidget(self.configurationFrameUp)
        self.configurationFrameDown = QtWidgets.QFrame(self.configurationFrame)
        self.configurationFrameDown.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.configurationFrameDown.setFrameShadow(QtWidgets.QFrame.Raised)
        self.configurationFrameDown.setObjectName("configurationFrameDown")

        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.configurationFrameDown)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")

        self.codeEdition = QtWidgets.QPlainTextEdit(self.configurationFrameDown)
        self.codeEdition.setObjectName("codeEdition")
        self.horizontalLayout_5.addWidget(self.codeEdition)
        self.verticalLayout_4.addWidget(self.configurationFrameDown)
        self.stackedWidget.addWidget(self.configurationFrame)
        self.verticalLayout_3.addWidget(self.stackedWidget)
        self.horizontalLayout.addWidget(self.rightMainFrame)
        self.verticalLayout.addWidget(self.mainFrame)
        MainWindow.setCentralWidget(self.mainWidget)

        self.codeEdition.setPlainText(str(self.system.fileText))

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.readButton.setText(_translate("MainWindow", "Wczytaj"))
        self.saveButton.setText(_translate("MainWindow", "Zapisz"))
        self.learningButton.setText(_translate("MainWindow", "Uczenie"))
        self.configurationButton.setText(_translate("MainWindow", "Konfiguracja"))
        self.restartButton.setText(_translate("MainWindow", "Restart"))
        self.oneStepButton.setText(_translate("MainWindow", "One Step"))
        self.autoStepButton.setText(_translate("MainWindow", "Auto step"))
        self.errorChartButton.setText(_translate("MainWindow", "Wykres b????d??w"))
        self.resultText.setPlainText(_translate("MainWindow", "Wyniki.\n"""))
        self.stopConditionButton.setText(_translate("MainWindow", "Ustawienie warunku stopu"))


    def actionOnClickLearning(self):
        self.stackedWidget.setCurrentWidget(self.learningFrame)
        self.getPoints()
        self.chart.ax.cla()
        self.chart.ax.plot(self.F_x, self.F_y, 'r')
        self.chart.ax.scatter(self.A_x,self.A_y)
        self.chart.ax.scatter(self.B_x,self.B_y)
        self.chart.ax.grid()
        self.chart.draw()
        self.system.fileText = self.codeEdition.toPlainText()
        self.system.fileTextToCoordinates()
        self.updatePlot()


    def actionOnClickConfiguration(self):
        self.stackedWidget.setCurrentWidget(self.configurationFrame)

    def actionOnClickOneStep(self):
        self.updatePlot()

    def actionOnClickRestart(self):
        self.restart()
        self.chart.ax.cla()
        self.chart.ax.scatter(self.A_x,self.A_y)
        self.chart.ax.scatter(self.B_x,self.B_y)
        self.chart.ax.grid()
        self.chart.draw()


    def actionOnClickAutoStep(self):
        if self.timer == None:
            self.autoStepButton.setText("Stop")
            self.timer = QtCore.QTimer()
            self.timer.setInterval(1)
            self.timer.timeout.connect(self.updatePlot)
            self.timer.start()
        else:
            self.autoStepButton.setText("Auto step")
            self.timer.stop()
            self.timer = None

    def updatePlot(self):
        self.chart.ax.cla()
        try:
            self.system.oneStepLearning()
            self.getPoints()
        except:
            pass
        else:
            self.chart.ax.plot(self.F_x, self.F_y, 'r')
        self.chart.ax.scatter(self.A_x,self.A_y)
        self.chart.ax.scatter(self.B_x,self.B_y)
        self.chart.ax.grid()
        self.chart.draw()
        self.system.generateResaults()             
        self.resultText.setPlainText(self.system.resultText)

        if self.timer != None and self.system.stopCondition():
            self.autoStepButton.setText("Auto step")
            self.timer.stop()
            self.timer = None

    def getPoints(self):
        self.A_x = self.system.A_x
        self.A_y = self.system.A_y
        self.B_x = self.system.B_x
        self.B_y = self.system.B_y
        self.F_x = self.system.F_x
        self.F_y = self.system.F_y

    def restart(self):
        self.system.F_y = self.system.F_x
        self.system.p = Preceptron()
        self.system.resultText = ""
        self.resultText.setPlainText("")
        self.system.tab = []
        self.system.resultErrorText = ""
        self.system.currIteration = 0


    def actionOnClickErrorConfiguration(self):
        self.errorConfiguration()

    def errorConfiguration(self):
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog(self.system)
        ui.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()

    def browsefiles(self):
        fileName = QtWidgets.QFileDialog.getOpenFileName(None, 'Open File', 'C:\\', 'Text Files (*.txt)')
        self.system.defaultFileName = fileName[0]
        self.system.readFromFile()
        self.restart()
        self.system.fileTextToCoordinates()
        self.codeEdition.setPlainText(str(self.system.fileText))

    def showChart(self):
        Dialog2 = QtWidgets.QDialog()
        ui2 = Ui_Dialog2(self.system)
        ui2.setupUi(Dialog2)
        Dialog2.show()
        Dialog2.exec_()

    def saveToFile(self):
        self.system.fileText = self.codeEdition.toPlainText()
        file = open("zapis.txt","w")
        file.write(self.system.fileText)