import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMessageBox

from MySQL import MySql

from WindowInterface.Login import Ui_MainWindow
from controller.Register import Register_window

from controller.user.Clerk_Home import Clerk_Home
from controller.user.User_Home import User_Home


class Login_window(QtWidgets.QMainWindow, Ui_MainWindow):
    mySignal = pyqtSignal(str, str)
    mySignal2 = pyqtSignal(str,str)

    def __init__(self):
        super(Login_window, self).__init__()
        self.gui_home_user = None
        self.setupUi(self)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pushButton.clicked.connect(self.btn_login)
        self.pushButton_2.clicked.connect(self.jumptoRegister)

        self.gui_home_clerk = Clerk_Home()
        self.gui_home_user = User_Home()
        self.gui_register = Register_window()


        self.mySignal.connect(self.gui_home_user.getSlot_MySignal)
        self.mySignal2.connect(self.gui_home_clerk.getSlot_MySignal)


    def jumptoRegister(self):
        self.gui_register.show()

    def btn_login(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        flag = False
        if username == "":
            QMessageBox.warning(self, "警告", "请输入用户名", QMessageBox.Close)
            return
        elif password == "":
            QMessageBox.warning(self, "警告", "请输入密码", QMessageBox.Close)
            return

        users = MySql.DBconnect().findUserByName(username)
        if len(users) == 0:
            QMessageBox.warning(self, "警告", "用户不存在", QMessageBox.Close)
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            return
        else:
            for u in users:
                if u.password == password:
                    flag = True
                    self.user = u
                    if self.user.level == 0:  # 普通用户
                        self.mySignal.emit(str(u.ID), u.username)
                        self.gui_home_user.show()
                        self.close()
                    elif self.user.level == 1:  # 业务人员
                        self.mySignal2.emit(str(u.ID), u.username)
                        self.gui_home_clerk.show()
                        self.close()
                    # elif self.user.level == 3:  # 系统管理员
                    #     self.mySignal.emit(str(u.ID), u.username)

            if not flag:
                QMessageBox.warning(self, "警告", "账号密码错误重新输入", QMessageBox.Close)
                self.lineEdit_2.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('./logo.png'))
    myMainWindow = Login_window()  # 自定义的类例化
    myMainWindow.show()
    sys.exit(app.exec_())
