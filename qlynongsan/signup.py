import Dataconnection
from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_Signup(object):
    def setupUi(self, Dialog):
        self.Dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(1920, 1080)
        
        # Background
        self.bgwidget = QtWidgets.QWidget(parent=Dialog)
        self.bgwidget.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
       
        self.bgwidget.setStyleSheet("background-color: rgb(255,255,255);")
        self.bgwidget.setObjectName("bgwidget")
        
        # Signup Panel
        self.signup_panel = QtWidgets.QWidget(parent=self.bgwidget)
        self.signup_panel.setGeometry(QtCore.QRect(800, 100, 400, 350))
        self.signup_panel.setStyleSheet("background-color: rgb(1,1,1); padding-left: 7px;")
        self.signup_panel.setObjectName("signup_panel")
        
        # Signup Label
        self.label = QtWidgets.QLabel(parent=self.signup_panel)
        self.label.setGeometry(QtCore.QRect(150, 30, 100, 30))
        self.label.setStyleSheet("font: 20pt 'MS Shell Dlg 2'; color: white;")
        self.label.setObjectName("label")
        
        # Username Field
        self.usernamefield = QtWidgets.QLineEdit(parent=self.signup_panel)
        self.usernamefield.setGeometry(QtCore.QRect(50, 80, 300, 40))
        self.usernamefield.setStyleSheet("background-color: white; font: 12pt 'MS Shell Dlg 2'; padding: 5px;")
        self.usernamefield.setObjectName("usernamefield")
        
        # Password Field
        self.passwordfield = QtWidgets.QLineEdit(parent=self.signup_panel)
        self.passwordfield.setGeometry(QtCore.QRect(50, 140, 300, 40))
        self.passwordfield.setStyleSheet("background-color: white; font: 12pt 'MS Shell Dlg 2'; padding: 5px;")
        self.passwordfield.setObjectName("passwordfield")
        self.passwordfield.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)  # Hide password input
        
        # Confirm Password Field
        self.confirmpasswordfield = QtWidgets.QLineEdit(parent=self.signup_panel)
        self.confirmpasswordfield.setGeometry(QtCore.QRect(50, 200, 300, 40))
        self.confirmpasswordfield.setStyleSheet("background-color: white; font: 12pt 'MS Shell Dlg 2'; padding: 5px;")
        self.confirmpasswordfield.setObjectName("confirmpasswordfield")
        self.confirmpasswordfield.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)  # Hide password input
        
        # Signup Button
        self.btnsignup = QtWidgets.QPushButton(parent=self.signup_panel)
        self.btnsignup.setGeometry(QtCore.QRect(50, 260, 300, 40))
        self.btnsignup.setStyleSheet("background-color: #4CAF50; color: white; font: 14pt 'MS Shell Dlg 2';")
        self.btnsignup.setObjectName("btnsignup")
        
        # Error Label
        self.error = QtWidgets.QLabel(parent=self.signup_panel)
        self.error.setGeometry(QtCore.QRect(50, 320, 300, 20))
        self.error.setStyleSheet("font: 12pt 'MS Shell Dlg 2'; color: red;")
        self.error.setText("")
        self.error.setObjectName("error")
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        # Connect signals and slots
        self.btnsignup.clicked.connect(self.handle_signup)
    
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Signup"))
        self.label.setText(_translate("Dialog", "Signup"))
        self.usernamefield.setPlaceholderText(_translate("Dialog", "Username"))
        self.passwordfield.setPlaceholderText(_translate("Dialog", "Password"))
        self.confirmpasswordfield.setPlaceholderText(_translate("Dialog", "Confirm Password"))
        self.btnsignup.setText(_translate("Dialog", "Sign up"))
    
    def handle_signup(self):
        username = self.usernamefield.text().strip()
        password = self.passwordfield.text().strip()
        confirm_password = self.confirmpasswordfield.text().strip()

        if not username or not password or not confirm_password:
            self.error.setText("Please fill in all fields.")
            return

        if password != confirm_password:
            self.error.setText("Passwords do not match.")
            return

        connection = Dataconnection.connectdatabase()
        if connection:
            cursor = connection.cursor()
            try:
                query = "INSERT INTO NguoiDung (TaiKhoan, MatKhau) VALUES (%s, %s)"
                cursor.execute(query, (username, password))
                connection.commit()
                cursor.close()
                connection.close()
                self.error.setStyleSheet("color: green;font-size:17px;")
                self.error.setText("Signup successful.")
                # If signup is successful, open the login window after a short delay
                QtCore.QTimer.singleShot(2000, self.open_login)
            except Exception as e:
                self.error.setStyleSheet("color: red; font-size: 16px;")
                self.error.setText(f"Error: {str(e)}")
        else:
            self.error.setText("Database connection failed.")
    
    def open_login(self):
        from Login import Ui_Login
        self.Dialog.close()  # Close the signup dialog
        # Open the login dialog
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Login()
        self.ui.setupUi(self.window)
        self.window.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Signup()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
