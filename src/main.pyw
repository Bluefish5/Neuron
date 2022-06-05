from modules import *

system = System()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(system)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())