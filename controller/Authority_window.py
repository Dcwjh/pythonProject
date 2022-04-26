import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMessageBox, QTableWidgetItem, QPushButton

import MySQL.MySql
from WindowInterface.Authority import Ui_MainWindow


class Authority_window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Authority_window, self).__init__()
        self.setupUi(self)
        self.users_list = MySQL.MySql.DBconnect().findAllUser()
        self.display()

    def display(self):
        row = len(self.users_list)
        for i in range(row):
            print(str(self.users_list[i].ID))
            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(self.users_list[i].ID)))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(self.users_list[i].username))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(self.users_list[i].password))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(str(self.users_list[i].level)))
            updateBtn = QPushButton('UPDATE')
            updateBtn.setStyleSheet(
                ''' text-align : center;background-color : #ffffcc; font : 13px;''')
            # ''' text-align : center; background-color : NavajoWhite;height : 30px;border-style: outset;font : 13px  '''  DarkSeaGreen
            # updateBtn.clicked.connect(lambda: self.updateTable(self.users_list[i]))
            self.tableWidget.setCellWidget(i, 4, updateBtn)

            updateBtn = QPushButton('DELETE')
            updateBtn.setStyleSheet(
                ''' text-align : center;background-color : #ccffcc; font : 13px;''')
            # ''' text-align : center; background-color : NavajoWhite;height : 30px;border-style: outset;font : 13px  '''  DarkSeaGreen
            # updateBtn.clicked.connect(lambda: self.updateTable(self.users_list[i]))
            self.tableWidget.setCellWidget(i, 5, updateBtn)

            updateBtn = QPushButton('DETAIL')
            updateBtn.setStyleSheet(
                ''' text-align : center;background-color : #00ffff;font : 13px;''')
            self.tableWidget.setCellWidget(i, 6, updateBtn)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('../logo.png'))
    myMainWindow = Authority_window()  # 自定义的类例化
    myMainWindow.show()
    sys.exit(app.exec_())