from PyQt5.QtWidgets import*
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtWidgets

class Query (QWidget):

    def __init__(self, con):
        super().__init__()
        
        loadUi("query.ui",self)
        
        self.btnEnter.clicked.connect(lambda:self.querySelected(con))
          
    def querySelected(self, con):
        
        if self.radHistory.isChecked():
            # history id sine gore gemi sorgula
            cur = con.cursor()
            sql = "select recId, shipName from historyAndShip where recId = %s"
            id_ = self.txtId.text()
            cur.execute(sql, id_)
            data = cur.fetchall()
            cur.close()
            
            self.table.clearContents()         # Gecerli tablo sifirlanir
            self.table.setColumnCount(2)       # Tablonun sutun sayisi ayarlanir
            self.table.setRowCount(0)          # Tablonun satir sayisi sifirlanir
            
            self.table.setHorizontalHeaderLabels(['Kayıt Id','Gemi Adı'])
            
            # Tablonun el ile degistirilebilirligi kapatilir
            self.table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
            # Tablonun satir numara gostergesi kapatilir
            self.table.verticalHeader().hide()
            
            # Tablonun gecerli satir sayisi (0) row adli degiskene alinir
            row = self.table.rowCount()
            
            # Data tablosundaki her eleman for dongusu ile donulur
            for x in data:
                # Her adimda tabloya yeni bir satir eklenip satirin sutunlari eklenir
                self.table.setRowCount(row + 1)
                self.table.setItem(row, 0, QtWidgets.QTableWidgetItem(str(x[0])))
                self.table.setItem(row, 1, QtWidgets.QTableWidgetItem(x[1]))
               
                # Bir sonraki adim icin satir sayisi bir arttirilir
                row = row + 1
            
            
        elif self.radType.isChecked():
            # tip id sine gore gemi sorgula
            cur = con.cursor()
            sql = "select typeId, typeName, shipName from typeAndShips where typeId = %s"
            id_ = self.txtId.text()
            cur.execute(sql, id_)
            data = cur.fetchall()
            cur.close()
            
            self.table.clearContents()         # Gecerli tablo sifirlanir
            self.table.setColumnCount(3)       # Tablonun sutun sayisi ayarlanir
            self.table.setRowCount(0)          # Tablonun satir sayisi sifirlanir
            
            self.table.setHorizontalHeaderLabels(['Tip Id','Tip Adı', 'Gemi Adı'])
            
            # Tablonun el ile degistirilebilirligi kapatilir
            self.table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
            # Tablonun satir numara gostergesi kapatilir
            self.table.verticalHeader().hide()
            
            # Tablonun gecerli satir sayisi (0) row adli degiskene alinir
            row = self.table.rowCount()
            
            # Data tablosundaki her eleman for dongusu ile donulur
            for x in data:
                # Her adimda tabloya yeni bir satir eklenip satirin sutunlari eklenir
                self.table.setRowCount(row + 1)
                self.table.setItem(row, 0, QtWidgets.QTableWidgetItem(str(x[0])))
                self.table.setItem(row, 1, QtWidgets.QTableWidgetItem(x[1]))
                self.table.setItem(row, 2, QtWidgets.QTableWidgetItem(x[2]))
               
                # Bir sonraki adim icin satir sayisi bir arttirilir
                row = row + 1
            
            
            
            
        elif self.radOwner.isChecked():
            #sahip id sine gore gemi sorgula
            cur = con.cursor()
            sql = "select  ownerId, ownerName, ownerLName ,shipName from ownerAndShips where ownerId = %s"
            id_ = self.txtId.text()
            cur.execute(sql, id_)
            data = cur.fetchall()
            cur.close()
            
            self.table.clearContents()         # Gecerli tablo sifirlanir
            self.table.setColumnCount(4)       # Tablonun sutun sayisi ayarlanir
            self.table.setRowCount(0)          # Tablonun satir sayisi sifirlanir
            
            self.table.setHorizontalHeaderLabels(['Sahip Id','Sahip Adı', 'Sahip Soyadı','Gemi Adı'])
            
            # Tablonun el ile degistirilebilirligi kapatilir
            self.table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
            # Tablonun satir numara gostergesi kapatilir
            self.table.verticalHeader().hide()
            
            # Tablonun gecerli satir sayisi (0) row adli degiskene alinir
            row = self.table.rowCount()
            
            # Data tablosundaki her eleman for dongusu ile donulur
            for x in data:
                # Her adimda tabloya yeni bir satir eklenip satirin sutunlari eklenir
                self.table.setRowCount(row + 1)
                self.table.setItem(row, 0, QtWidgets.QTableWidgetItem(str(x[0])))
                self.table.setItem(row, 1, QtWidgets.QTableWidgetItem(x[1]))
                self.table.setItem(row, 2, QtWidgets.QTableWidgetItem(x[2]))
                self.table.setItem(row, 3, QtWidgets.QTableWidgetItem(x[3]))
               
                # Bir sonraki adim icin satir sayisi bir arttirilir
                row = row + 1
            
            
        else:
            QMessageBox.about(self, "Hata", "Lütfen sorgu seçeneklerinden birini seçiniz.")
            