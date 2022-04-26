from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication

import sys
import time
from PyQt5.QtGui import QPixmap, QIcon


# class MainWindow(QMainWindow):
#     def __init__(self):
#         super(MainWindow, self).__init__()  # 调用父类的init
#
#
#
#     def closeEvent(self, event):
#         reply = QMessageBox.question(self, '提醒', "确定退出?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
#
#         if reply == QMessageBox.Yes:
#             event.accept()
#         else:
#             event.ignore()
#
#
#
#
# if __name__ == '__main__':
#     app = 0
#     app = QApplication(sys.argv)
#     app.setWindowIcon(QIcon('./logo.png'))
#     myMainWindow = MainWindow()  # 自定义的类例化
#     myMainWindow.show()
#     sys.exit(app.exec_())
