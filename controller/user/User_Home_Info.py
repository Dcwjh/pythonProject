import sys
import time

from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication

from WindowInterface.User_Home_Info import Ui_MainWindow


class User_Home_Info(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(User_Home_Info, self).__init__()
        self.setupUi(self)

        self.pushButton_2.clicked.connect(self.returnHome)

    def info_getSlot_MySignal(self, id, username):
        self.id = id
        self.username = username
        print("查看信息：00000" + id)
        self.label_2.setText("ID:00000" + id)

    def returnHome(self):
        self.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('./logo.png'))
    myMainWindow = User_Home_Info()  # 自定义的类例化
    myMainWindow.show()
    sys.exit(app.exec_())