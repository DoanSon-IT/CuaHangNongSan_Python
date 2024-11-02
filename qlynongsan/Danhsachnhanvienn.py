
import Dataconnection
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox
import re
from datetime import datetime
class Ui_NhanVien(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1515, 854)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 20, 1471, 371))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.tableView_NhanVien = QtWidgets.QTableView(parent=self.frame)
        self.tableView_NhanVien.setGeometry(QtCore.QRect(0, 0, 1471, 371))
        self.tableView_NhanVien.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableView_NhanVien.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.tableView_NhanVien.setObjectName("tableView_NhanVien")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 430, 1471, 361))
        self.groupBox_2.setObjectName("groupBox_2")
        self.frame_4 = QtWidgets.QFrame(parent=self.groupBox_2)
        self.frame_4.setGeometry(QtCore.QRect(780, 20, 671, 321))
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.btnThem = QtWidgets.QPushButton(parent=self.frame_4)
        self.btnThem.setGeometry(QtCore.QRect(70, 30, 191, 71))
        self.btnThem.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);")
        self.btnThem.setObjectName("btnThem")
        self.btnSua = QtWidgets.QPushButton(parent=self.frame_4)
        self.btnSua.setGeometry(QtCore.QRect(70, 130, 191, 71))
        self.btnSua.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);")
        self.btnSua.setObjectName("btnSua")
        self.btnXoa = QtWidgets.QPushButton(parent=self.frame_4)
        self.btnXoa.setGeometry(QtCore.QRect(400, 30, 191, 71))
        self.btnXoa.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);")
        self.btnXoa.setObjectName("btnXoa")
        self.btnLamMoi = QtWidgets.QPushButton(parent=self.frame_4)
        self.btnLamMoi.setGeometry(QtCore.QRect(400, 130, 191, 71))
        self.btnLamMoi.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);")
        self.btnLamMoi.setObjectName("btnLamMoi")
        self.frame_6 = QtWidgets.QFrame(parent=self.groupBox_2)
        self.frame_6.setGeometry(QtCore.QRect(20, 100, 731, 241))
        self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_6.setObjectName("frame_6")
        self.txtMaNhanVien = QtWidgets.QLineEdit(parent=self.frame_6)
        self.txtMaNhanVien.setGeometry(QtCore.QRect(140, 20, 171, 22))
        self.txtMaNhanVien.setObjectName("txtMaNhanVien")
        self.txtTenNhanVien = QtWidgets.QLineEdit(parent=self.frame_6)
        self.txtTenNhanVien.setGeometry(QtCore.QRect(140, 70, 171, 22))
        self.txtTenNhanVien.setObjectName("txtTenNhanVien")
        self.txtDiaChi = QtWidgets.QLineEdit(parent=self.frame_6)
        self.txtDiaChi.setGeometry(QtCore.QRect(140, 130, 171, 22))
        self.txtDiaChi.setObjectName("txtDiaChi")
        self.txtEmail = QtWidgets.QLineEdit(parent=self.frame_6)
        self.txtEmail.setGeometry(QtCore.QRect(520, 190, 151, 22))
        self.txtEmail.setObjectName("txtEmail")
        self.txtLuong = QtWidgets.QLineEdit(parent=self.frame_6)
        self.txtLuong.setGeometry(QtCore.QRect(140, 190, 171, 22))
        self.txtLuong.setObjectName("txtLuong")
        self.label_22 = QtWidgets.QLabel(parent=self.frame_6)
        self.label_22.setGeometry(QtCore.QRect(20, 20, 101, 16))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(parent=self.frame_6)
        self.label_23.setGeometry(QtCore.QRect(20, 70, 101, 16))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(parent=self.frame_6)
        self.label_24.setGeometry(QtCore.QRect(20, 130, 55, 16))
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(parent=self.frame_6)
        self.label_25.setGeometry(QtCore.QRect(20, 190, 55, 16))
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(parent=self.frame_6)
        self.label_26.setGeometry(QtCore.QRect(390, 20, 55, 16))
        self.label_26.setStyleSheet("font: 75 9pt \"MS Shell Dlg 2\";")
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(parent=self.frame_6)
        self.label_27.setGeometry(QtCore.QRect(390, 70, 61, 16))
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(parent=self.frame_6)
        self.label_28.setGeometry(QtCore.QRect(390, 130, 55, 16))
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(parent=self.frame_6)
        self.label_29.setGeometry(QtCore.QRect(390, 190, 55, 16))
        self.label_29.setObjectName("label_29")
        self.radioButton_Nam = QtWidgets.QRadioButton(parent=self.frame_6)
        self.radioButton_Nam.setGeometry(QtCore.QRect(520, 20, 61, 20))
        self.radioButton_Nam.setObjectName("radioButton_Nam")
        self.radioButton_Nu = QtWidgets.QRadioButton(parent=self.frame_6)
        self.radioButton_Nu.setGeometry(QtCore.QRect(590, 20, 61, 20))
        self.radioButton_Nu.setObjectName("radioButton_Nu")
        self.comboBox_ChucVu = QtWidgets.QComboBox(parent=self.frame_6)
        self.comboBox_ChucVu.setGeometry(QtCore.QRect(520, 130, 151, 22))
        self.comboBox_ChucVu.setObjectName("comboBox_ChucVu")
        self.comboBox_ChucVu.addItem("")
        self.comboBox_ChucVu.addItem("")
        
        self.dateEdit_NgaySinh = QtWidgets.QDateEdit(parent=self.frame_6)
        self.dateEdit_NgaySinh.setGeometry(QtCore.QRect(520, 60, 151, 22))
        self.dateEdit_NgaySinh.setObjectName("dateEdit_NgaySinh")
        self.label_30 = QtWidgets.QLabel(parent=self.frame_6)
        self.label_30.setGeometry(QtCore.QRect(320, 190, 21, 16))
        self.label_30.setObjectName("label_30")
        self.frame_2 = QtWidgets.QFrame(parent=self.groupBox_2)
        self.frame_2.setGeometry(QtCore.QRect(20, 20, 731, 71))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.txtTimKiem = QtWidgets.QLineEdit(parent=self.frame_2)
        self.txtTimKiem.setGeometry(QtCore.QRect(140, 30, 171, 22))
        self.txtTimKiem.setObjectName("txtTimKiem")
        self.label_21 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_21.setGeometry(QtCore.QRect(10, 30, 131, 16))
        self.label_21.setObjectName("label_21")
        self.btnTimKiem = QtWidgets.QPushButton(parent=self.frame_2)
        self.btnTimKiem.setGeometry(QtCore.QRect(390, 30, 93, 28))
        self.btnTimKiem.setStyleSheet("background-color: rgb(85, 85, 127);\n"
"color: rgb(255, 255, 255);")
        self.btnTimKiem.setObjectName("btnTimKiem")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 400, 451, 21))
        self.label.setStyleSheet("color: rgb(255, 85, 0);\n"
"border-bottom-color: rgb(255, 85, 0);\n"
"font: 75 9pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1515, 26))
        self.menubar.setObjectName("menubar")
        self.menuManager = QtWidgets.QMenu(parent=self.menubar)
        self.menuManager.setObjectName("menuManager")
        self.menusetting = QtWidgets.QMenu(parent=self.menubar)
        self.menusetting.setObjectName("menusetting")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionHome = QtGui.QAction(parent=MainWindow)
        self.actionHome.setObjectName("actionHome")
        self.actionSanPham = QtGui.QAction(parent=MainWindow)
        self.actionSanPham.setObjectName("actionSanPham")
        self.actionBanHang = QtGui.QAction(parent=MainWindow)
        self.actionBanHang.setObjectName("actionBanHang")
        self.actionNhanVien = QtGui.QAction(parent=MainWindow)
        self.actionNhanVien.setObjectName("actionNhanVien")
        self.actionNhaCungCap = QtGui.QAction(parent=MainWindow)
        self.actionNhaCungCap.setObjectName("actionNhaCungCap")
        self.actionThongKe = QtGui.QAction(parent=MainWindow)
        self.actionThongKe.setObjectName("actionThongKe")
        self.actionExit = QtGui.QAction(parent=MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionLogout = QtGui.QAction(parent=MainWindow)
        self.actionLogout.setObjectName("actionLogout")
        self.actionHoTro = QtGui.QAction(parent=MainWindow)
        self.actionHoTro.setObjectName("actionHoTro")
        self.menuManager.addAction(self.actionHome)
        self.menuManager.addAction(self.actionSanPham)
        self.menuManager.addAction(self.actionBanHang)
        self.menuManager.addAction(self.actionNhanVien)
        self.menuManager.addAction(self.actionNhaCungCap)
        self.menuManager.addAction(self.actionThongKe)
        self.menusetting.addAction(self.actionExit)
        self.menusetting.addAction(self.actionLogout)
        self.menusetting.addAction(self.actionHoTro)
        self.menubar.addAction(self.menuManager.menuAction())
        self.menubar.addAction(self.menusetting.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
         # Connect buttons to their respective functions
        self.btnThem.clicked.connect(self.themNhanVien)
        self.btnSua.clicked.connect(self.suaNhanVien)
        self.btnXoa.clicked.connect(self.xoaNhanVien)
        self.btnLamMoi.clicked.connect(self.lamMoi)
        self.btnTimKiem.clicked.connect(self.timKiemNhanVien)
        self.tableView_NhanVien.clicked.connect(self.fillFormFromTable)

        # Initialize the table view
        self.model = QtGui.QStandardItemModel()
        self.tableView_NhanVien.setModel(self.model)
        self.loadTableData()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "QUẢN LÝ NHÂN VIÊN"))
        self.btnThem.setText(_translate("MainWindow", "Thêm Nhân Viên"))
        self.btnSua.setText(_translate("MainWindow", "Sửa Thông Tin"))
        self.btnXoa.setText(_translate("MainWindow", "Xóa Nhân Viên"))
        self.btnLamMoi.setText(_translate("MainWindow", "Làm Mới"))
        self.label_22.setText(_translate("MainWindow", "Mã Nhân Viên"))
        self.label_23.setText(_translate("MainWindow", "Tên Nhân Viên"))
        self.label_24.setText(_translate("MainWindow", "Địa Chỉ "))
        self.label_25.setText(_translate("MainWindow", "Lương"))
        self.label_26.setText(_translate("MainWindow", "Giới Tính"))
        self.label_27.setText(_translate("MainWindow", "Ngày Sinh"))
        self.label_28.setText(_translate("MainWindow", "Chức Vụ"))
        self.label_29.setText(_translate("MainWindow", "Email"))
        self.radioButton_Nam.setText(_translate("MainWindow", "Nam"))
        self.radioButton_Nu.setText(_translate("MainWindow", "Nữ"))
        self.comboBox_ChucVu.setItemText(0, _translate("MainWindow", "Quản Lý"))
        self.comboBox_ChucVu.setItemText(1, _translate("MainWindow", "Nhân Viên"))
        self.label_30.setText(_translate("MainWindow", "$"))
        self.label_21.setText(_translate("MainWindow", "Nhập Tên Nhân Viên"))
        self.btnTimKiem.setText(_translate("MainWindow", "Tìm Kiếm"))
        self.label.setText(_translate("MainWindow", "* Lưu ý thao tác cẩn thận !"))
        self.menuManager.setTitle(_translate("MainWindow", "Manager"))
        self.menusetting.setTitle(_translate("MainWindow", "Setting"))
        self.actionHome.setText(_translate("MainWindow", "Home"))
        self.actionSanPham.setText(_translate("MainWindow", "SanPham"))
        self.actionBanHang.setText(_translate("MainWindow", "BanHang"))
        self.actionNhanVien.setText(_translate("MainWindow", "NhanVien"))
        self.actionNhaCungCap.setText(_translate("MainWindow", "NhaCungCap"))
        self.actionThongKe.setText(_translate("MainWindow", "ThongKe"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionLogout.setText(_translate("MainWindow", "Logout"))
        self.actionHoTro.setText(_translate("MainWindow", "HoTro"))
        
        
        
    def loadTableData(self):
        # Implement this function to load data from your database into the table view
        try:
            conn = Dataconnection.connectdatabase()  # Get your database connection
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM NhanVien")
            rows = cursor.fetchall()

            self.model.clear()
            self.model.setColumnCount(8)
            self.model.setHorizontalHeaderLabels(["Mã Nhân viên", "Tên Nhân viên", "Địa Chỉ", "Lương Tháng", "Email", "Ngày Sinh", "Giới Tính", "Chức Vụ"])
            

            for row_number, row_data in enumerate(rows):
                for column_number, data in enumerate(row_data):
                    item = QtGui.QStandardItem(str(data))
                    self.model.setItem(row_number, column_number, item)

            self.tableView_NhanVien.setModel(self.model)
            header = self.tableView_NhanVien.horizontalHeader()
            header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
            self.tableView_NhanVien.verticalHeader().setDefaultSectionSize(60)
            conn.close()
        except Exception as e:
            print(f"Error loading data: {e}")

    def kiemTraTuoi(self, ngay_sinh):
        # Kiểm tra tuổi của nhân viên (phải từ 18 tuổi trở lên)
        ngay_hien_tai = datetime.now()
        ngay_sinh_dt = datetime.strptime(ngay_sinh, '%Y-%m-%d')
        tuoi = ngay_hien_tai.year - ngay_sinh_dt.year - ((ngay_hien_tai.month, ngay_hien_tai.day) < (ngay_sinh_dt.month, ngay_sinh_dt.day))
        return tuoi >= 18

    def kiemTraEmail(self, email):
        # Kiểm tra định dạng email
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email)

    def kiemTraLuong(self, luong):
    # Kiểm tra lương là số (chỉ chấp nhận dấu chấm hay phẩy)
        try:
            # Xóa đi các dấu phân cách ngàn nếu có
            luong_cleaned = luong.replace('.', '').replace(',', '.')

            float(luong_cleaned)
            return True
        except ValueError:
            return False

    def themNhanVien(self):
        # Thêm nhân viên vào cơ sở dữ liệu
        try:
            maNV = int(self.txtMaNhanVien.text())
            tenNV = self.txtTenNhanVien.text()
            diaChi = self.txtDiaChi.text()
            luong = self.txtLuong.text()
            email = self.txtEmail.text()
            ngaySinh = self.dateEdit_NgaySinh.date().toString(QtCore.Qt.DateFormat.ISODate)
            gioiTinh = "Nam" if self.radioButton_Nam.isChecked() else "Nữ"
            chucVu = self.comboBox_ChucVu.currentText()

            # Kiểm tra các điều kiện
            if not self.kiemTraTuoi(ngaySinh):
                QMessageBox.warning(None, "Lỗi", "Nhân viên phải từ 18 tuổi trở lên!")
                return

            if not self.kiemTraEmail(email):
                QMessageBox.warning(None, "Lỗi", "Email không hợp lệ phải có @ !")
                return

            if not self.kiemTraLuong(luong):
                QMessageBox.warning(None, "Lỗi", "Tiền lương không đúng định dạng!")
                return
            
            if maNV == '' or tenNV == '' or diaChi == '' or luong == '' or email == '':
               QMessageBox.warning(None, "Lỗi", "Vui lòng điền đầy đủ thông tin nhân viên!")
               return 

            luong = float(luong.replace(',', '.'))  # Chuyển đổi lương thành số
            

            # Thực hiện thêm vào cơ sở dữ liệu
            conn = Dataconnection.connectdatabase()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO NhanVien (MaNV, TenNV, DiaChi, Luong, Email, NgaySinh, GioiTinh, ChucVu) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                        (maNV, tenNV, diaChi, luong, email, ngaySinh, gioiTinh, chucVu))
            conn.commit()
            conn.close()

            self.loadTableData()
            self.lamMoi()
            QMessageBox.information(None, "Thông báo", "Thêm nhân viên thành công!")
        except Exception as e:
            QMessageBox.warning(None, "Lỗi", f"Lỗi: {e}")

    def suaNhanVien(self):
        # Sửa thông tin nhân viên trong cơ sở dữ liệu
        try:
            maNV = int(self.txtMaNhanVien.text())
            tenNV = self.txtTenNhanVien.text()
            diaChi = self.txtDiaChi.text()
            luong = self.txtLuong.text()
            email = self.txtEmail.text()
            ngaySinh = self.dateEdit_NgaySinh.date().toString(QtCore.Qt.DateFormat.ISODate)
            gioiTinh = "Nam" if self.radioButton_Nam.isChecked() else "Nữ"
            chucVu = self.comboBox_ChucVu.currentText()

            # Kiểm tra các điều kiện
            if not self.kiemTraTuoi(ngaySinh):
                QMessageBox.warning(None, "Lỗi", "Nhân viên phải từ 18 tuổi trở lên!")
                return

            if not self.kiemTraEmail(email):
                QMessageBox.warning(None, "Lỗi", "Email không hợp lệ!")
                return

            if not self.kiemTraLuong(luong):
                QMessageBox.warning(None, "Lỗi", "Lương phải là số!")
                return
            if maNV == '' or tenNV == '' or diaChi == '' or luong == '' or email == '':
               QMessageBox.warning(None, "Lỗi", "Vui lòng điền đầy đủ thông tin nhân viên!")
               return 

            luong = float(luong.replace(',', '.'))  # Chuyển đổi lương thành số

            # Thực hiện cập nhật vào cơ sở dữ liệu
            conn = Dataconnection.connectdatabase()
            cursor = conn.cursor()
            cursor.execute("UPDATE NhanVien SET TenNV=%s, DiaChi=%s, Luong=%s, Email=%s, NgaySinh=%s, GioiTinh=%s, ChucVu=%s WHERE MaNV=%s",
                        (tenNV, diaChi, luong, email, ngaySinh, gioiTinh, chucVu, maNV))
            conn.commit()
            conn.close()

            self.loadTableData()
            self.lamMoi()
            QMessageBox.information(None, "Thông báo", "Sửa thông tin nhân viên thành công!")
        except Exception as e:
            QMessageBox.warning(None, "Lỗi", f"Lỗi: {e}")
   
            
    def xoaNhanVien(self):
        # Implement deleting employee functionality
        maNV = int(self.txtMaNhanVien.text())
        conn = Dataconnection.connectdatabase()
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM NhanVien WHERE MaNV=%s", (maNV,))
            conn.commit()
            conn.close()

            self.loadTableData()
            self.lamMoi()
            QMessageBox.information(None, "Thông báo", "Xóa nhân viên thành công!")
        except Exception as e:
            QMessageBox.warning(None, "Lỗi", f"Lỗi: {e}")

    def lamMoi(self):
        # Implement clearing input fields
        self.txtMaNhanVien.clear()
        self.txtTenNhanVien.clear()
        self.txtDiaChi.clear()
        self.txtLuong.clear()
        self.txtEmail.clear()
        self.radioButton_Nam.setChecked(True)
        self.comboBox_ChucVu.setCurrentIndex(0)
        self.dateEdit_NgaySinh.setDate(QtCore.QDate.currentDate())
        self.loadTableData()

    def timKiemNhanVien(self):
        # Implement employee search functionality
        try:
            tenNV = self.txtTimKiem.text()

            conn = Dataconnection.connectdatabase()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM NhanVien WHERE TenNV LIKE %s", ('%' + tenNV + '%',))
            rows = cursor.fetchall()

            self.model.clear()
            self.model.setColumnCount(8)
            self.model.setHorizontalHeaderLabels(["Mã NV", "Tên NV", "Địa Chỉ", "Lương", "Email", "Ngày Sinh", "Giới Tính", "Chức Vụ"])

            for row_number, row_data in enumerate(rows):
                for column_number, data in enumerate(row_data):
                    item = QtGui.QStandardItem(str(data))
                    self.model.setItem(row_number, column_number, item)

            self.tableView_NhanVien.setModel(self.model)
            conn.close()
        except Exception as e:
            QMessageBox.warning(None, "Lỗi", f"Lỗi: {e}")
    
    def fillFormFromTable(self, index):
        # Fill form fields when a row in the table view is clicked
        row = index.row()
        maNV = self.model.index(row, 0).data()
        tenNV = self.model.index(row, 1).data()
        diaChi = self.model.index(row, 2).data()
        luong = self.model.index(row, 3).data()
        email = self.model.index(row, 4).data()
        ngaySinh = self.model.index(row, 5).data()
        gioiTinh = self.model.index(row, 6).data()
        chucVu = self.model.index(row, 7).data()

        self.txtMaNhanVien.setText(str(maNV))
        self.txtTenNhanVien.setText(tenNV)
        self.txtDiaChi.setText(diaChi)
        self.txtLuong.setText(str(luong))
        self.txtEmail.setText(email)
        self.dateEdit_NgaySinh.setDate(QtCore.QDate.fromString(ngaySinh, QtCore.Qt.DateFormat.ISODate))
        if gioiTinh == "Nam":
            self.radioButton_Nam.setChecked(True)
        else:
            self.radioButton_Nu.setChecked(True)
        self.comboBox_ChucVu.setCurrentText(chucVu)
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_NhanVien()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())