import sys

from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMessageBox

from MySQL import MySql
from WindowInterface.Register import Ui_MainWindow
from entity.User import User


class Register_window(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(Register_window, self).__init__()
        self.setupUi(self)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)

        self.pushButton.clicked.connect(self.register)

    def jumptoLogin(self):
        self.close()

    def register(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        confirm = self.lineEdit_3.text()
        if len(username) == 0:
            QMessageBox.warning(self, "警告", "请输入用户名", QMessageBox.Close)
        elif len(password) == 0:
            QMessageBox.warning(self, "警告", "请输入密码", QMessageBox.Close)
        elif len(confirm) == 0:
            QMessageBox.warning(self, "警告", "请输入确认密码", QMessageBox.Close)
        else:
            users = MySql.DBconnect().findUserByName(username)
            if users == username:
                QMessageBox.information(self, "提示", "用户已存在", QMessageBox.Close)
                self.lineEdit.clear()
            else:
                if password != confirm:
                    QMessageBox.information(self, "提示", "两次密码输入不一致，重新输入", QMessageBox.Close)
                    self.lineEdit_3.clear()
                else:
                    print("用户注册成功")
                    newUser = User(username, password, 0)
                    print(newUser)
                    MySql.DBconnect().insertUser(newUser)
                    self.close()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('./logo.png'))
    myMainWindow = Register_window()  # 自定义的类例化
    myMainWindow.show()
    sys.exit(app.exec_())
