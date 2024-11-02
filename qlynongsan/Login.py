import Dataconnection
from Banhang import Ui_BanHang
from signup import Ui_Signup
from PyQt6.QtWidgets import QMessageBox, QDialog, QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QCheckBox, QCommandLinkButton, QWidget
from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_Login(object):
    def setupUi(self, Dialog):
        self.Dialog = Dialog  # Save reference to the Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(1920, 1080)
        
        # Background
        self.bgwidget = QtWidgets.QWidget(Dialog)
        self.bgwidget.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        # //self.bgwidget.setStyleSheet("background-image: url('./qlynongsan/img/login.jpg'); background-repeat: no-repeat; background-size: cover;")
        self.bgwidget.setStyleSheet("background-color: rgb(255,255,255);")
        self.bgwidget.setObjectName("bgwidget")
        
        # Login Panel
        self.login_panel = QtWidgets.QWidget(self.bgwidget)
        self.login_panel.setGeometry(QtCore.QRect(800, 150, 400, 350))
        self.login_panel.setStyleSheet("background-color: rgb(1,1,1);padding-left: 5px;")
        self.login_panel.setObjectName("login_panel")
        
        # Login Label
        self.label = QtWidgets.QLabel(self.login_panel)
        self.label.setGeometry(QtCore.QRect(150, 30, 100, 30))
        self.label.setStyleSheet("font: 20pt 'MS Shell Dlg 2'; color: white;")
        self.label.setObjectName("label")
        
        # Email Field
        self.emailfield = QtWidgets.QLineEdit(self.login_panel)
        self.emailfield.setGeometry(QtCore.QRect(50, 80, 300, 40))
        self.emailfield.setStyleSheet("background-color: white; font: 12pt 'MS Shell Dlg 2'; padding-left: 5px;")
        self.emailfield.setObjectName("emailfield")
        
        # Password Field
        self.passwordfield = QtWidgets.QLineEdit(self.login_panel)
        self.passwordfield.setGeometry(QtCore.QRect(50, 140, 300, 40))
        self.passwordfield.setStyleSheet("background-color: white; font: 12pt 'MS Shell Dlg 2'; padding-left: 5px;")
        self.passwordfield.setObjectName("passwordfield")
        self.passwordfield.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)  # Hide password input
        
        # Remember Me Checkbox
        self.remember_me = QtWidgets.QCheckBox(self.login_panel)
        self.remember_me.setGeometry(QtCore.QRect(50, 190, 150, 20))
        self.remember_me.setStyleSheet("color: white;")
        self.remember_me.setObjectName("remember_me")
        
        # Forgot Password Link
        self.forgot_password = QtWidgets.QLabel(self.login_panel)
        self.forgot_password.setGeometry(QtCore.QRect(250, 190, 100, 20))
        self.forgot_password.setStyleSheet("color: white; text-decoration: underline;")
        self.forgot_password.setObjectName("forgot_password")
        
        # Login Button
        self.btnlogin = QtWidgets.QPushButton(self.login_panel)
        self.btnlogin.setGeometry(QtCore.QRect(50, 220, 300, 40))
        self.btnlogin.setStyleSheet("background-color: #4CAF50; color: white; font: 14pt 'MS Shell Dlg 2';")
        self.btnlogin.setObjectName("btnlogin")
        
        # Register Link
        self.label_5 = QtWidgets.QLabel(self.login_panel)
        self.label_5.setGeometry(QtCore.QRect(80, 270, 150, 20))
        self.label_5.setStyleSheet("color: white;")
        self.label_5.setObjectName("label_5")
        
        self.LinkButtoDangKy = QtWidgets.QCommandLinkButton(self.login_panel)
        self.LinkButtoDangKy.setGeometry(QtCore.QRect(255, 260, 100, 40))
        self.LinkButtoDangKy.setStyleSheet("color: white;")
        self.LinkButtoDangKy.setObjectName("LinkButtoDangKy")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        # Connect signals and slots
        self.btnlogin.clicked.connect(self.handle_login)
        self.LinkButtoDangKy.clicked.connect(lambda: self.openWindow(Ui_Signup))

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Login"))
        self.label.setText(_translate("Dialog", "Login"))
        self.emailfield.setPlaceholderText(_translate("Dialog", "Username"))
        self.passwordfield.setPlaceholderText(_translate("Dialog", "Password"))
        self.remember_me.setText(_translate("Dialog", "Remember me"))
        self.forgot_password.setText(_translate("Dialog", "Forgot password?"))
        self.btnlogin.setText(_translate("Dialog", "Login"))
        self.label_5.setText(_translate("Dialog", "Don't have an account?"))
        self.LinkButtoDangKy.setText(_translate("Dialog", "Register"))

    def handle_login(self):
        username = self.emailfield.text()
        password = self.passwordfield.text()

        if self.KiemTraTaiKhoan(username, password):
            self.openBanHang()
        else:
            self.show_error("Invalid credentials or account does not exist.")

    def KiemTraTaiKhoan(self, username, password):
        connection = Dataconnection.connectdatabase()
        if connection:
            cursor = connection.cursor()
            try:
                cursor.execute("SELECT * FROM NguoiDung WHERE TaiKhoan = %s AND MatKhau = %s", (username, password))
                record = cursor.fetchone()
                cursor.close()
                connection.close()
                return record is not None
            except Exception as e:
                self.show_error("Database connection error: " + str(e))
        return False

    def show_error(self, message):
        error = QMessageBox()
        error.setText(message)
        error.setStyleSheet("color: red;")
        error.exec()

    def openBanHang(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_BanHang()
        self.ui.setupUi(self.window)
        self.window.show()
        self.Dialog.close()

    def openWindow(self, UiClass):
        self.window = QtWidgets.QMainWindow()
        self.ui = UiClass()
        self.ui.setupUi(self.window)
        self.window.show()
        self.window.closeEvent = self.reopenMainWindow
        self.Dialog.hide()
        
    def reopenMainWindow(self, event):
        self.Dialog.show()
        event.accept()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Login()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
