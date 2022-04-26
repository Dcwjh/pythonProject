import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from MySQL import MySql
import Register_Window
from Ui_Login_Window import Ui_Login_Window


class Login_window1111111(QtWidgets.QMainWindow, Ui_Login_Window):
    def __init__(self):
        super(Login_window, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.btn_login)
        self.pushButton_2.clicked.connect(self.btn_register)
        self.gui = Register_Window.Register_window()

    def jumptoMain(self):
        self.gui.show()
        self.close()

    def btn_login(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        if username == "":
            QMessageBox.warning(self, "警告", "请输入用户名", QMessageBox.Close)
            return
        elif password == "":
            QMessageBox.warning(self, "警告", "请输入密码", QMessageBox.Close)
            return

        users = MySql.DBconnect().findUserByName(username)
        if len(users) == 0:
            QMessageBox.warning(self, "警告", "用户不存在", QMessageBox.Close)
            return
        else:
            for u in users:
                if u.password.__eq__(password):
                    self.jumptoMain()

            QMessageBox.warning(self, "警告", "账号密码错误重新输入", QMessageBox.Close)
            self.lineEdit_2.clear()

    def btn_register(self):
        self.gui = Register_Window.Register_window()
        self.gui.show()

if __name__ == '__main__': #如果这个文件是主程序。
    app = QtWidgets.QApplication(sys.argv) #QApplication相当于main函数，也就是整个程序（很多文件）的主入口函数。对于GUI程序必须至少有一个这样的实例来让程序运行。
    window = Login_window() #生成一个实例（对象）
    window.show() #有了实例，就得让它显示。这里的show()是QWidget的方法，用来显示窗口。
    sys.exit(app.exec_()) # 调用sys库的exit退出方法，条件是app.exec_()也就是整个窗口关闭。