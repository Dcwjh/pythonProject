import sys
import time

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication

from WindowInterface.User_Home_result import Ui_MainWindow


class User_Home_Result(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(User_Home_Result, self).__init__()

        # self.user = User("001","1234", 0)
        self.id = ""
        self.username = ""
        self.setupUi(self)
        self.frame.setStyleSheet('QFrame{background-color:rgb(203, 220, 255)},')  # 增加的代码
        self.label.setText("welcome!")
        self.label_2.setText("ID:000001")
        self.label_3.setText(time.strftime("%Y/%m/%d ", time.localtime()))
        self.label_27.setText(time.strftime("%H:%M:%S", time.localtime()))
        # % H: % M: % S

    # def getVaules(self,id, username):
    #     login = Login.Login_window()
    #     login.mySignal.connect(self.getSlot_MySignal)
    #
    # #
    def getSlot_MySignal(self, id, username):
        self.id = id
        self.username = username
        print("主页：00000" + id)
        self.label_2.setText("ID:00000" + id)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('C:/Users/Wang/PycharmProjects/pythonProject/logo.png'))
    myMainWindow = User_Home_Result()  # 自定义的类例化
    myMainWindow.show()
    sys.exit(app.exec_())