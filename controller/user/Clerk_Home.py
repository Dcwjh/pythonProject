import sys
import time

from PyQt5 import QtWidgets, QtCore, QtGui, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QPushButton

import MySQL.MySql
from WindowInterface.Clerk_Home import Ui_MainWindow


class Clerk_Home(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(Clerk_Home, self).__init__()
        self.username = None
        self.id = None
        self.setupUi(self)
        # self.frame.setStyleSheet('QFrame{background-color:rgb(203, 220, 255)},')  # 增加的代码
        self.label.setStyleSheet("QLabel{background-color:rgb(194, 231, 255)}")
        self.users_list = MySQL.MySql.DBconnect().findAllScoring()
        self.display()
        # 默认值
        self.label_3.setText("操作员:000003")
        self.label_4.setText(time.strftime("%Y-%m-%d  %H:%M:%S", time.localtime()))


    def getSlot_MySignal(self, id, username):
        self.id = id
        print(type(id))
        self.username = username
        print("主页：" + id)

        self.label_3.setText("操作员:00000%s" % id)
        self.label_4.setText(time.strftime("%Y-%m-%d  %H:%M:%S", time.localtime()))



    def display(self):
        row = len(self.users_list)
        for i in range(row):
            print(str(self.users_list[i].ID))
            self.tableWidget.setItem( i, 0, QTableWidgetItem(str(self.users_list[i].ID)))
            self.tableWidget.setItem( i, 1, QTableWidgetItem( self.users_list[i].username))
            self.tableWidget.setItem( i, 2, QTableWidgetItem( self.users_list[i].applytime))
            self.tableWidget.setItem( i, 3, QTableWidgetItem(self.users_list[i].isscored))
            self.tableWidget.setItem( i, 4, QTableWidgetItem(self.users_list[i].scoringtime))
            self.tableWidget.setItem( i, 5, QTableWidgetItem(self.users_list[i].result))
            self.tableWidget.setItem( i, 6, QTableWidgetItem(str(self.users_list[i].score)))
            self.tableWidget.setItem(i, 7, QTableWidgetItem(str(self.users_list[i].judge)))
            self.tableWidget.setItem(i, 8, QTableWidgetItem(self.users_list[i].ispublish))


            updateBtn = QPushButton('DELETE')
            updateBtn.setStyleSheet(
                ''' text-align : center; font : 13px;color:blue''')
            # ''' text-align : center; background-color : NavajoWhite;height : 30px;border-style: outset;font : 13px  '''  DarkSeaGreen
            # updateBtn.clicked.connect(lambda: self.updateTable(self.users_list[i]))
            self.tableWidget.setCellWidget(i, 9, updateBtn)


            updateBtn = QPushButton('UPDATE')
            updateBtn.setStyleSheet(''' text-align : center;font : 13px; color: blue  ''')
            # ''' text-align : center; background-color : NavajoWhite;height : 30px;border-style: outset;font : 13px  '''  DarkSeaGreen
            # updateBtn.clicked.connect(lambda: self.updateTable(self.users_list[i]))
            self.tableWidget.setCellWidget(i, 10, updateBtn)
            # print(i)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('C:/Users/Wang/PycharmProjects/pythonProject/logo.png'))
    myMainWindow = Clerk_Home()  # 自定义的类例化
    myMainWindow.show()
    sys.exit(app.exec_())