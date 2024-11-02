# Form implementation generated from reading ui file 'welcome.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.
import Dataconnection
from mysql.connector import Error
from PyQt6.QtWidgets import QMessageBox,QDialog,QApplication, QMainWindow
from PyQt6.QtCore import QDate
from PyQt6.QtGui import QStandardItemModel, QStandardItem

from PyQt6 import QtCore, QtGui, QtWidgets
from Login import Ui_Login
from signup import Ui_Signup
class Ui_Home(object):

    def setupUi(self, Dialog):
        self.Dialog = Dialog  # Save reference to the Dialog
        
        Dialog.setObjectName("Dialog")
        Dialog.resize(1920, 1080)
        self.bgwidget = QtWidgets.QWidget(parent=Dialog)
        self.bgwidget.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.bgwidget.setStyleSheet("background-color: rgb(115, 202, 255);")
        self.bgwidget.setObjectName("bgwidget")
        self.label = QtWidgets.QLabel(parent=self.bgwidget)
        self.label.setGeometry(QtCore.QRect(700, 110, 251, 61))
        self.label.setStyleSheet("font: 36pt \"MS Shell Dlg 2\"; color:rgb(255, 255, 255)\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.bgwidget)
        self.label_2.setGeometry(QtCore.QRect(660, 200, 391, 41))
        self.label_2.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";color:rgb(255, 255, 255)")
        self.label_2.setObjectName("label_2")
        self.login = QtWidgets.QPushButton(parent=self.bgwidget)
        self.login.setGeometry(QtCore.QRect(630, 300, 341, 51))
        self.login.setStyleSheet("border-radius:20px;\n"
"background-color: rgb(170, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.login.setObjectName("login")
        self.create = QtWidgets.QPushButton(parent=self.bgwidget)
        self.create.setGeometry(QtCore.QRect(630, 400, 341, 51))
        self.create.setStyleSheet("border-radius:20px;\n"
"background-color: rgb(170, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.create.setObjectName("create")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        # 
        self.login.clicked.connect(
            lambda: self.openWindow(Ui_Login) 
        )
        self.create.clicked.connect(
            lambda: self.openWindow(Ui_Signup) 
        )

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "HOME"))
        self.label.setText(_translate("Dialog", "Welcome"))
        self.label_2.setText(_translate("Dialog", "Quản Lý Cửa Hàng Nông Sản"))
        self.login.setText(_translate("Dialog", "Log in"))
        self.create.setText(_translate("Dialog", "Sign up"))

# 

    def openWindow(self, UiClass):
        self.window = QtWidgets.QMainWindow()
        self.ui = UiClass()
        self.ui.setupUi(self.window)
        self.window.show()
        self.window.destroyed.connect(self.reopenMainWindow)
        self.Dialog.close()  # Đóng cửa sổ ban đầu

    def reopenMainWindow(self):
        self.Dialog = QtWidgets.QDialog()
        self.ui = Ui_Home()
        self.ui.setupUi(self.Dialog)
        self.Dialog.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Home()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())