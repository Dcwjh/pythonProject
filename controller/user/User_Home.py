import sys
import time

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication

from WindowInterface.User_Home import Ui_MainWindow
from controller.user.User_Home_Info import User_Home_Info


class User_Home(QtWidgets.QMainWindow, Ui_MainWindow):
    mySignalToInfo = pyqtSignal(str, str)
    def __init__(self):
        super(User_Home, self).__init__()

        # self.user = User("001","1234", 0)
        self.id = ""
        self.username = ""
        self.setupUi(self)
        self.frame.setStyleSheet('QFrame{background-color:rgb(203, 220, 255)},')  # 增加的代码
        self.label.setText("welcome!")
        self.label_2.setText("")
        self.label_3.setText(time.strftime("%Y/%m/%d ", time.localtime()))
        self.label_27.setText(time.strftime("%H:%M:%S", time.localtime()))
        # % H: % M: % S
        self.label_2.setText("ID:000001")

        self.infoWindow = User_Home_Info()

        self.pushButton_5.clicked.connect(self.jumptoInfo)

        # 绑定接受函数
        self.mySignalToInfo.connect(self.infoWindow.info_getSlot_MySignal)


    def getSlot_MySignal(self, id, username):
        self.id = id
        self.username = username
        print("主页：00000" + id)
        self.label_2.setText("ID:00000" + id)

    def jumptoInfo(self):
        try:
            print(type(self.id), self.id)
            print(type(self.username),self.username)
            self.mySignalToInfo.emit(self.id, self.username)
            self.infoWindow.show()
        except Exception as e:
            print(repr(e))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('C:/Users/Wang/PycharmProjects/pythonProject/logo.png'))
    myMainWindow = User_Home()  # 自定义的类例化
    myMainWindow.show()
    sys.exit(app.exec_())