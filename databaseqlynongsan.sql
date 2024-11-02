CREATE DATABASE nongsan;

USE nongsan;

CREATE TABLE NguoiDung(
    TaiKhoan NVARCHAR(255) PRIMARY KEY NOT NULL,
	MatKhau NVARCHAR(255) NOT NULL
);

CREATE TABLE  NhanVien (
    MaNV INT PRIMARY KEY NOT NULL,
    TenNV NVARCHAR(255) NOT NULL,
    DiaChi NVARCHAR(255) NOT NULL,
    Luong FLOAT NOT NULL,
    Email NVARCHAR(255) NOT NULL,
    NgaySinh DATE NULL,
    GioiTinh NVARCHAR(10) NOT NULL,
    ChucVu NVARCHAR(50) NOT NULL
);


CREATE TABLE  NhaCungCap (
    MaNCC INT PRIMARY KEY NOT NULL,
    TenNCC NVARCHAR(255) NOT NULL,
    DiaChi NVARCHAR(255) NOT NULL,
    DienThoai NVARCHAR(15) NOT NULL,
    Email NVARCHAR(255) NOT NULL
);

CREATE TABLE  SanPham(
    MaSP INT PRIMARY KEY NOT NULL,
    TenSP NVARCHAR(255) NOT NULL,
    MoTa NVARCHAR(255) NOT NULL,
    Gia FLOAT NOT NULL,  
	SoLuong INT NOT NULL,
    MaNCC INT NOT NULL,
    FOREIGN KEY (MaNCC) REFERENCES NhaCungCap (MaNCC)
);



CREATE TABLE HoaDon (
    MaHD INT PRIMARY KEY NOT NULL,
    MaNV INT NOT NULL,
    NgayLap DATE NULL,
    TongTien FLOAT NOT NULL,
    FOREIGN KEY (MaNV) REFERENCES NhanVien (MaNV)
);


CREATE TABLE  ChiTietHoaDon (
	id_cthd INT AUTO_INCREMENT PRIMARY KEY,
	MaHD INT NOT NULL,
    MaSP INT NOT NULL,
    TenSP NVARCHAR(255) NOT NULL,
    SoLuong INT NOT NULL,
    GiaBan FLOAT NOT NULL
	
);
-- FOREIGN KEY (MaSP) REFERENCES SanPham (MaSP)
-- FOREIGN KEY (MaHD) REFERENCES HoaDon (MaHD),
   
INSERT INTO NguoiDung (TaiKhoan,MatKhau)
VALUES
    ('admin', 'admin12345');
INSERT INTO NhanVien (MaNV, TenNV, DiaChi, Luong, Email, NgaySinh, GioiTinh, ChucVu)
VALUES
	(1, 'LVChung', 'TP. Hà Nội', 2000, 'c@gmail.com', '2003-01-15', 'Nam', 'Quản lý'),
    (2, 'DVSon', 'TP. Hà Nội', 1000, 's@gmail.com', '2003-03-20', 'Nam', 'Nhân Viên'),
    (3, 'NTTan', 'TP. Hà Nội', 1000, 't@gmail.com', '2003-11-10', 'Nam', 'Nhân Viên'),
    (4, 'Trang', 'TP. Hai Phong', 500, 'tr@gmail.com', '2004-07-25', 'Nữ', 'Nhân Viên'),
    (5, 'Linh', 'TP. HCM', 500, 'l@gmail.com', '2005-04-12', 'Nữ', 'Nhân Viên');


INSERT INTO NhaCungCap (MaNCC, TenNCC, DiaChi, DienThoai, Email)
VALUES
    (1, 'Công ty Thực Phẩm Xanh', 'Số 1', '0123456789', 'info@thucphamxanh.vn'),
	(2, 'Công ty  Nông Sản Sạch','Số 2', '0987654321', 'contact@nongsansach.vn'),
	(3, 'Công ty  Rau Quả Việt', 'Số 3,', '0912345678', 'sales@rauquaviet.vn'),
	(4, 'Công ty Thực Phẩm An Toàn', 'Số 4', '0945678901', 'info@thucphaman.vn'),
	(5, 'Công ty  Nông Nghiệp Hữu Cơ', 'Số 5', '0934567890', 'organic@nongnghiephuuco.vn'),
	(6, 'Công ty  Sản Xuất Nông Sản', 'Số 6', '0923456789', 'production@nongsan.vn'),
	(7, 'Công ty  Phân Phối Nông Sản', 'Số 7', '0915678901', 'distribution@nongsan.vn'),
	(8, 'Công ty  Thực Phẩm Tươi Sống','Số 8', '0931234567', 'freshfood@thucphamtuisong.vn'),
	(9, 'Công ty  Nông Sản Việt', 'Số 9,', '0956781234', 'info@nongsanviet.vn'),
	(10, 'Công ty Nông Nghiệp Việt Nam', 'Số 10', '0941234567', 'contact@nongnghiepvn.vn');


INSERT INTO SanPham (MaSP, TenSP, MoTa, Gia, SoLuong, MaNCC)
VALUES
    (1, 'Gạo', 'Gạo thơm hảo hạng', 15.5, 100, 1),
	(2, 'Ngô', 'Ngô ngọt tươi ngon', 10.0, 200, 2),
	(3, 'Khoai tây', 'Khoai tây Đà Lạt', 12.0, 150, 3),
	(4, 'Cà chua', 'Cà chua sạch', 8.0, 250, 4),
	(5, 'Rau muống', 'Rau muống tươi', 5.0, 300, 5),
	(6, 'Bí đỏ', 'Bí đỏ dẻo ngọt', 6.5, 180, 6),
	(7, 'Hành tây', 'Hành tây Đà Lạt', 7.0, 200, 7),
	(8, 'Ớt', 'Ớt cay tươi', 4.0, 250, 8),
	(9, 'Chanh', 'Chanh tươi không hạt', 3.5, 300, 9),
	(10, 'Bắp cải', 'Bắp cải xanh', 5.5, 220, 10);
    
INSERT INTO SanPham (MaSP, TenSP, MoTa, Gia, SoLuong, MaNCC)
VALUES
    (11, 'Dưa hấu', 'Dưa hấu đỏ', 12.5, 150, 1),
    (12, 'Dưa leo', 'Dưa leo tươi', 6.0, 180, 2),
    (13, 'Nho', 'Nho Mỹ', 20.0, 100, 3),
    (14, 'Táo', 'Táo Fuji', 18.0, 120, 4),
    (15, 'Chuối', 'Chuối tiêu', 8.0, 200, 5),
    (16, 'Dâu tây', 'Dâu tây Đà Lạt', 25.0, 80, 6),
    (17, 'Mít', 'Mít Thái', 15.0, 90, 7),
    (18, 'Sầu riêng', 'Sầu riêng hạt lép', 30.0, 70, 8),
    (19, 'Cam', 'Cam sành', 12.0, 150, 9),
    (20, 'Quýt', 'Quýt đường', 10.0, 160, 10),
    (21, 'Bơ', 'Bơ sáp', 22.0, 60, 1),
    (22, 'Xoài', 'Xoài cát Hòa Lộc', 18.0, 100, 2),
    (23, 'Na', 'Na dai', 20.0, 90, 3),
    (24, 'Lê', 'Lê xanh', 14.0, 110, 4),
    (25, 'Mận', 'Mận hậu', 12.0, 140, 5),
    (26, 'Đào', 'Đào Mỹ', 25.0, 70, 6),
    (27, 'Dừa', 'Dừa xiêm', 8.0, 200, 7),
    (28, 'Đu đủ', 'Đu đủ chín', 10.0, 150, 8),
    (29, 'Mãng cầu', 'Mãng cầu xiêm', 18.0, 80, 9),
    (30, 'Chôm chôm', 'Chôm chôm Thái', 15.0, 100, 10),
    (31, 'Vải', 'Vải thiều', 20.0, 90, 1),
    (32, 'Sơ ri', 'Sơ ri đỏ', 12.0, 130, 2),
    (33, 'Cà phê', 'Cà phê Robusta', 40.0, 70, 3),
    (34, 'Cacao', 'Cacao nguyên chất', 45.0, 60, 4),
    (35, 'Chè', 'Chè Thái Nguyên', 25.0, 80, 5),
    (36, 'Nấm', 'Nấm rơm', 10.0, 150, 6),
    (37, 'Rau mầm', 'Rau mầm sạch', 5.0, 200, 7),
    (38, 'Rau cải', 'Rau cải ngọt', 6.0, 180, 8),
    (39, 'Bí ngòi', 'Bí ngòi xanh', 7.0, 160, 9),
    (40, 'Khoai lang', 'Khoai lang tím', 9.0, 170, 10),
    (41, 'Rau dền', 'Rau dền đỏ', 5.5, 200, 1),
    (42, 'Cải bắp', 'Cải bắp trắng', 6.5, 190, 2),
    (43, 'Đậu xanh', 'Đậu xanh tươi', 8.0, 150, 3),
    (44, 'Đậu đen', 'Đậu đen xanh lòng', 9.0, 140, 4),
    (45, 'Đậu đỏ', 'Đậu đỏ hạt nhỏ', 10.0, 130, 5),
    (46, 'Hạt sen', 'Hạt sen tươi', 12.0, 120, 6),
    (47, 'Cà pháo', 'Cà pháo muối', 6.0, 200, 7),
    (48, 'Cà chua bi', 'Cà chua bi đỏ', 7.0, 180, 8),
    (49, 'Hành lá', 'Hành lá tươi', 4.0, 250, 9),
    (50, 'Rau cải xoong', 'Rau cải xoong sạch', 5.5, 210, 10);

DELIMITER //

CREATE TRIGGER trg_UpdateSoLuongSanPham
AFTER INSERT ON ChiTietHoaDon
FOR EACH ROW
BEGIN
    UPDATE SanPham
    SET SoLuong = SoLuong - NEW.SoLuong
    WHERE MaSP = NEW.MaSP;
END;

//

DELIMITER ;

-- DELIMITER //

-- CREATE TRIGGER trg_UpdateSoLuongSanPham_AfterDelete
-- AFTER DELETE ON ChiTietHoaDon
-- FOR EACH ROW
-- BEGIN
--     DECLARE soLuongHuy INT;
--     SELECT SoLuong INTO soLuongHuy FROM ChiTietHoaDon WHERE MaSP = OLD.MaSP;
--     UPDATE SanPham
--     SET SoLuong = SoLuong + soLuongHuy
--     WHERE MaSP = OLD.MaSP;
-- END;

-- //

-- DELIMITER ;

