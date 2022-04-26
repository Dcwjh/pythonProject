from PyQt5 import QtWidgets

from Ui_Register_Window import Ui_Register_MainWindow


class Register_window(QtWidgets.QMainWindow, Ui_Register_MainWindow):
    def __init__(self):
        super(Register_window, self).__init__()
        self.setupUi(self)





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Register_window()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
