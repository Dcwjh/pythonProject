import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMessageBox

from WindowInterface.Model import Ui_MainWindow


class BuildModel(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(BuildModel, self).__init__()
        self.gui_home_user = None
        self.setupUi(self)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('../../logo.png'))
    myMainWindow = BuildModel()  # 自定义的类例化
    myMainWindow.show()
    sys.exit(app.exec_())