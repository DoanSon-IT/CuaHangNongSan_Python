# export_to_excel.py

import pandas as pd
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QStandardItemModel, QStandardItem

def Print_File(tableView, txtTien, labels):
    # Lấy dữ liệu từ tableView
    model = tableView.model()
    rows = model.rowCount()
    columns = model.columnCount()
    
    data = []
    headers = []
    for column in range(columns):
        headers.append(model.headerData(column, QtCore.Qt.Orientation.Horizontal))

    for row in range(rows):
        rowData = []
        for column in range(columns):
            index = model.index(row, column)
            rowData.append(model.data(index))
        data.append(rowData)

    # Tạo DataFrame
    df = pd.DataFrame(data, columns=headers)

    # Tạo Workbook
    wb = Workbook()
    ws = wb.active

    # Ghi DataFrame vào Worksheet
    for r in dataframe_to_rows(df, index=False, header=True):
        ws.append(r)

    # Ghi thông tin bổ sung vào Worksheet
    ws.append([])
    ws.append(["Thành Tiền", txtTien.text(), "$"])
    for label in labels:
        ws.append(["", "", label])

    # Lưu Workbook
    file_path = QtWidgets.QFileDialog.getSaveFileName(None, "Save File", "", "Excel Files (*.xlsx);;All Files (*)")[0]
    if file_path:
        wb.save(file_path)
        QtWidgets.QMessageBox.information(None, "Success", "Lưu file thành công.")
