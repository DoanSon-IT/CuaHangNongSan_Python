import Dataconnection
from PyQt6 import QtCore, QtGui, QtWidgets
import mysql.connector
import xlsxwriter

class NhapThemHangDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(782, 457)  # Increased the height to accommodate new elements
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(210, 50, 71, 16))
        self.label.setObjectName("label")
        self.txtTimKiemMa = QtWidgets.QLineEdit(parent=Dialog)
        self.txtTimKiemMa.setGeometry(QtCore.QRect(330, 50, 151, 20))
        self.txtTimKiemMa.setObjectName("txtTimKiemMa")
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setGeometry(QtCore.QRect(210, 90, 71, 16))
        self.label_2.setObjectName("label_2")
        self.txtTenSP = QtWidgets.QLineEdit(parent=Dialog)
        self.txtTenSP.setGeometry(QtCore.QRect(330, 90, 151, 20))
        self.txtTenSP.setText("")
        self.txtTenSP.setObjectName("txtTenSP")
        self.txtSoLuongTonKho = QtWidgets.QLineEdit(parent=Dialog)
        self.txtSoLuongTonKho.setGeometry(QtCore.QRect(330, 130, 151, 20))
        self.txtSoLuongTonKho.setObjectName("txtSoLuongTonKho")
        self.label_3 = QtWidgets.QLabel(parent=Dialog)
        self.label_3.setGeometry(QtCore.QRect(210, 130, 111, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=Dialog)
        self.label_4.setGeometry(QtCore.QRect(210, 210, 111, 16))
        self.label_4.setObjectName("label_4")
        self.txtSoLuongNhapThem = QtWidgets.QLineEdit(parent=Dialog)
        self.txtSoLuongNhapThem.setGeometry(QtCore.QRect(330, 210, 151, 20))
        self.txtSoLuongNhapThem.setObjectName("txtSoLuongNhapThem")
        self.txtDonGia = QtWidgets.QLineEdit(parent=Dialog)
        self.txtDonGia.setGeometry(QtCore.QRect(330, 170, 151, 20))
        self.txtDonGia.setObjectName("txtDonGia")
        self.label_5 = QtWidgets.QLabel(parent=Dialog)
        self.label_5.setGeometry(QtCore.QRect(210, 170, 71, 16))
        self.label_5.setObjectName("label_5")
        self.txtMoTa = QtWidgets.QLineEdit(parent=Dialog)
        self.txtMoTa.setGeometry(QtCore.QRect(590, 90, 151, 20))
        self.txtMoTa.setObjectName("txtMoTa")
        self.label_6 = QtWidgets.QLabel(parent=Dialog)
        self.label_6.setGeometry(QtCore.QRect(530, 90, 51, 16))
        self.label_6.setObjectName("label_6")
        self.btnTim = QtWidgets.QPushButton(parent=Dialog)
        self.btnTim.setGeometry(QtCore.QRect(520, 50, 121, 23))
        self.btnTim.setStyleSheet("background-color: rgb(85, 85, 127);\n"
                                  "color: rgb(255, 255, 255);")
        self.btnTim.setObjectName("btnTim")
        self.btnXacNhanNhap = QtWidgets.QPushButton(parent=Dialog)
        self.btnXacNhanNhap.setGeometry(QtCore.QRect(210, 370, 271, 51))
        self.btnXacNhanNhap.setStyleSheet("background-color: rgb(85, 85, 127);\n"
                                          "color: rgb(255, 255, 255);")
        self.btnXacNhanNhap.setObjectName("btnXacNhanNhap")
        self.label_7 = QtWidgets.QLabel(parent=Dialog)
        self.label_7.setGeometry(QtCore.QRect(530, 120, 71, 16))
        self.label_7.setObjectName("label_7")
        self.txtNCC = QtWidgets.QLineEdit(parent=Dialog)
        self.txtNCC.setGeometry(QtCore.QRect(590, 120, 151, 20))
        self.txtNCC.setObjectName("txtNCC")

        self.label_tongtien = QtWidgets.QLabel(parent=Dialog)
        self.label_tongtien.setGeometry(QtCore.QRect(210, 300, 71, 16))
        self.label_tongtien.setObjectName("label_tongtien")
        self.txtTongTien = QtWidgets.QLineEdit(parent=Dialog)
        self.txtTongTien.setGeometry(QtCore.QRect(330, 300, 151, 20))
        self.txtTongTien.setObjectName("txtTongTien")
        self.txtTongTien.setReadOnly(True)

        self.label_giamgia = QtWidgets.QLabel(parent=Dialog)
        self.label_giamgia.setGeometry(QtCore.QRect(210, 330, 71, 16))
        self.label_giamgia.setObjectName("label_giamgia")
        self.txtGiamGia = QtWidgets.QLineEdit(parent=Dialog)
        self.txtGiamGia.setGeometry(QtCore.QRect(330, 330, 151, 20))
        self.txtGiamGia.setObjectName("txtGiamGia")

        self.btnTinh = QtWidgets.QPushButton(parent=Dialog)
        self.btnTinh.setGeometry(QtCore.QRect(520, 300, 121, 23))
        self.btnTinh.setStyleSheet("background-color: rgb(85, 85, 127);\n"
                                   "color: rgb(255, 255, 255);")
        self.btnTinh.setObjectName("btnTinh")

        self.btnInRaExcel = QtWidgets.QPushButton(parent=Dialog)
        self.btnInRaExcel.setGeometry(QtCore.QRect(520, 330, 121, 23))
        self.btnInRaExcel.setStyleSheet("background-color: rgb(85, 85, 127);\n"
                                        "color: rgb(255, 255, 255);")
        self.btnInRaExcel.setObjectName("btnInRaExcel")
        
        self.btnLamMoi = QtWidgets.QPushButton(parent=Dialog)
        self.btnLamMoi.setGeometry(QtCore.QRect(520, 360, 121, 23))
        self.btnLamMoi.setStyleSheet("background-color: rgb(85, 85, 127);\n"
                                        "color: rgb(255, 255, 255);")
        self.btnLamMoi.setObjectName("btnLamMoi")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.btnTim.clicked.connect(self.search_product)
        self.btnXacNhanNhap.clicked.connect(self.add_quantity)
        self.btnTinh.clicked.connect(self.calculate_total)
        self.btnInRaExcel.clicked.connect(self.print_to_excel)
        self.btnLamMoi.clicked.connect(self.reset_fields)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Nhap Them So Luong "))
        self.label.setText(_translate("Dialog", "Nhập Mã"))
        self.label_2.setText(_translate("Dialog", "Tên Sản Phẩm"))
        self.label_3.setText(_translate("Dialog", "Số Lượng Tồn Kho"))
        self.label_4.setText(_translate("Dialog",  "Thêm Số Lượng"))
        self.label_5.setText(_translate("Dialog", "Đơn Giá"))
        self.label_6.setText(_translate("Dialog", "Mô Tả"))
        self.btnTim.setText(_translate("Dialog", "Tìm "))
        self.btnXacNhanNhap.setText(_translate("Dialog", "Xác Nhận Nhập Thêm Hàng"))
        self.label_7.setText(_translate("Dialog", "NCC"))
        self.label_tongtien.setText(_translate("Dialog", "Tổng Tiền"))
        self.label_giamgia.setText(_translate("Dialog", "Giảm Giá"))
        self.btnTinh.setText(_translate("Dialog", "Tính Tổng"))
        self.btnInRaExcel.setText(_translate("Dialog", "In Ra Excel"))
        self.btnLamMoi.setText(_translate("Dialog", "LamMoi"))

    def search_product(self):
        product_id = self.txtTimKiemMa.text()
        if not product_id:
            QtWidgets.QMessageBox.warning(self, "Lỗi", "Vui lòng nhập mã sản phẩm để tìm kiếm.")
            return

        try:
            conn = Dataconnection.connectdatabase()
            cursor = conn.cursor()
            query = "SELECT TenSP, MoTa, Gia, SoLuong, MaNCC FROM SanPham WHERE MaSP = %s"
            cursor.execute(query, (product_id,))
            result = cursor.fetchone()
            conn.close()

            if result:
                self.txtTenSP.setText(result[0])
                self.txtMoTa.setText(result[1])
                self.txtDonGia.setText(str(result[2]))
                self.txtSoLuongTonKho.setText(str(result[3]))
                self.txtNCC.setText(str(result[4]))
            else:
                QtWidgets.QMessageBox.information(self, "Thông báo", "Không tìm thấy sản phẩm với mã đã nhập.")
        except mysql.connector.Error as err:
            QtWidgets.QMessageBox.critical(self, "Lỗi", f"Đã xảy ra lỗi: {err}")

    def add_quantity(self):
        product_id = self.txtTimKiemMa.text()
        additional_quantity = self.txtSoLuongNhapThem.text()

        if not product_id or not additional_quantity:
            QtWidgets.QMessageBox.warning(self, "Lỗi", "Vui lòng nhập mã sản phẩm và số lượng nhập thêm.")
            return

        try:
            additional_quantity = int(additional_quantity)
            conn = Dataconnection.connectdatabase()
            cursor = conn.cursor()
            query = "UPDATE SanPham SET SoLuong = SoLuong + %s WHERE MaSP = %s"
            cursor.execute(query, (additional_quantity, product_id))
            conn.commit()
            conn.close()
            QtWidgets.QMessageBox.information(self, "Thành công", "Đã cập nhật số lượng sản phẩm.")
            
        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Lỗi", "Số lượng nhập thêm phải là một số.")
        except mysql.connector.Error as err:
            QtWidgets.QMessageBox.critical(self, "Lỗi", f"Đã xảy ra lỗi: {err}")

    def calculate_total(self):
        try:
            don_gia = float(self.txtDonGia.text())
            so_luong = int(self.txtSoLuongNhapThem.text())
            giam_gia = float(self.txtGiamGia.text()) if self.txtGiamGia.text() else 0.0

            tong_tien = don_gia * so_luong
            tong_tien_sau_giam_gia = tong_tien - (tong_tien * giam_gia / 100)

            self.txtTongTien.setText(str(tong_tien_sau_giam_gia))
        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đúng định dạng số cho đơn giá, số lượng và giảm giá.")

    def print_to_excel(self):
        try:
            product_id = self.txtTimKiemMa.text()
            ten_sp = self.txtTenSP.text()
            so_luong = self.txtSoLuongNhapThem.text()
            don_gia = self.txtDonGia.text()
            giam_gia = self.txtGiamGia.text()
            tong_tien = self.txtTongTien.text()

            if not all([product_id, ten_sp, so_luong, don_gia, tong_tien]):
                QtWidgets.QMessageBox.warning(self, "Lỗi", "Vui lòng đảm bảo tất cả các thông tin cần thiết đã được nhập.")
                return
            
            workbook = xlsxwriter.Workbook('ThongTinNhapHang.xlsx')
            worksheet = workbook.add_worksheet()

            worksheet.write('A1', 'Mã Sản Phẩm')
            worksheet.write('B1', 'Tên Sản Phẩm')
            worksheet.write('C1', 'Số Lượng Nhập')
            worksheet.write('D1', 'Đơn Giá')
            worksheet.write('E1', 'Giảm Giá (%)')
            worksheet.write('F1', 'Tổng Tiền Sau Giảm Giá')

            worksheet.write('A2', product_id)
            worksheet.write('B2', ten_sp)
            worksheet.write('C2', so_luong)
            worksheet.write('D2', don_gia)
            worksheet.write('E2', giam_gia)
            worksheet.write('F2', tong_tien)

            workbook.close()
            QtWidgets.QMessageBox.information(self, "Thành công", "Thông tin đã được in ra file Excel.")
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Lỗi", f"Đã xảy ra lỗi: {e}")

    def reset_fields(self):
        self.txtTimKiemMa.clear()
        self.txtTenSP.clear()
        self.txtMoTa.clear()
        self.txtDonGia.clear()
        self.txtSoLuongTonKho.clear()
        self.txtSoLuongNhapThem.clear()
        self.txtNCC.clear()
        self.txtTongTien.clear()
        self.txtGiamGia.clear()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog = NhapThemHangDialog()
    dialog.show()
    sys.exit(app.exec())
