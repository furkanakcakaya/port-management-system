from PyQt5.QtWidgets import*
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtWidgets

import psycopg2

import sys

# diger pencereleri import etme
from addShip import AddShip
from addOwner import AddOwner
from addPresidential import AddPresidential
from addType import AddType
from addHistory import AddHistory
from deleteElement import DeleteElement
from query import Query
from typeOrder import TypeOrder

# pgadmin baglantisi 
con = psycopg2.connect(
                host = "127.0.0.1",
                database = "limann",
                user = "postgres",
                password = "furkan")

class MainPage (QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        
        loadUi("mainMenu.ui",self)
        
        # butonlarin fonksiyon baglantilarini yapma (lambda fonksiyonlari arguman alan fonksiyonlar)
        self.btnInsertElement.clicked.connect(self.openInsertWindow)
        self.btnDeleteElement.clicked.connect(lambda: self.openDeleteWindow(con))
        self.btnUpdateElement.clicked.connect(self.openUpdateWindow)
        self.btnUpdateTable.clicked.connect(self.updateTable)
        self.btnQuery.clicked.connect(lambda: self.openQueryWindow(con))
        self.btnTypeOrder.clicked.connect(lambda: self.openTypeOrderWindow(con))
        self.commitSql.clicked.connect(lambda: self.saveAndClose(con))
        
        # baslangicta databasede bulunan verileri tablolara ekleme
        self.refreshShips(con)
        self.refreshOwners(con)
        self.refreshTypes(con)
        self.refreshPres(con)
        self.refreshHistory(con)
        
    def openInsertWindow(self):
        # Yeni eleman ekleme pencerelerinden hangisinin acilacagina secilen radio button'a gore karar verme
        if self.radShip.isChecked():
            self.addShip = AddShip("add",con)
            self.addShip.show()
        elif self.radOwner.isChecked():
            self.addOwner = AddOwner("add",con)
            self.addOwner.show()
        elif self.radPres.isChecked():
            self.addPresidential = AddPresidential("add",con)
            self.addPresidential.show()
        elif self.radType.isChecked():
            self.addType = AddType("add",con)
            self.addType.show()
        elif self.radHistory.isChecked():
            self.addHistory = AddHistory("add",con)
            self.addHistory.show()
        else:
            QMessageBox.about(self, "Hata", "Lütfen ekleme yapmak istediğiniz tabloyu seçiniz.")
    
    def openDeleteWindow(self, con):
        # Eleman silme penceresinin acilma fonksiyonunun alacagi argumana basilan radio button'a gore karar verme
        if self.radShip.isChecked():
            self.deleteElement = DeleteElement("ship",con)
            self.deleteElement.show()
        elif self.radOwner.isChecked():
            self.deleteElement = DeleteElement("owner",con)
            self.deleteElement.show()
        elif self.radPres.isChecked():
            self.deleteElement = DeleteElement("pres",con)
            self.deleteElement.show()
        elif self.radType.isChecked():
           self.deleteElement = DeleteElement("type",con)
           self.deleteElement.show()
        elif self.radHistory.isChecked():
            self.deleteElement = DeleteElement("history",con)
            self.deleteElement.show()
        else:
            QMessageBox.about(self, "Hata", "Lütfen silme yapmak istediğiniz tabloyu seçiniz.")
    
    
    def openUpdateWindow(self):

        if self.radShip.isChecked():
            self.addShip = AddShip("upd", con)
            self.addShip.show()
        elif self.radOwner.isChecked():
            self.addOwner = AddOwner("upd", con)
            self.addOwner.show()
        elif self.radPres.isChecked():
            self.addPresidential = AddPresidential("upd", con)
            self.addPresidential.show()
        elif self.radType.isChecked():
            self.addType = AddType("upd", con)
            self.addType.show()
        elif self.radHistory.isChecked():
            self.addHistory = AddHistory("upd", con)
            self.addHistory.show()
        else:
            QMessageBox.about(self, "Hata", "Lütfen güncelleme yapmak istediğiniz tabloyu seçiniz.")
          
    def openQueryWindow(self, con):
        # Gemi sorgu penceresini acma 
        self.query = Query(con)
        self.query.show()
        
    def openTypeOrderWindow(self, con):
        self.typeOrder = TypeOrder(con)
        self.typeOrder.show()
        
    def updateTable(self):
        # Butun tablolarin yenileme fonksiyonlarini sirasiyla calistirma
        self.refreshShips(con)
        self.refreshOwners(con)
        self.refreshTypes(con)
        self.refreshPres(con)
        self.refreshHistory(con)
        
    def refreshShips(self, con):
        # Gemi tablosunu yenileme
        
        cur = con.cursor()
        cur.execute("select * from ships")  # Butun gemiler sql fonksiyonuyla secilir
        data = cur.fetchall()               # Secilen tablo data adli degiskende tutulur
        cur.close()
        
        self.table1.clearContents()         # Gecerli tablo sifirlanir
        self.table1.setColumnCount(6)       # Tablonun sutun sayisi ayarlanir
        self.table1.setRowCount(0)          # Tablonun satir sayisi sifirlanir
        self.table1.setColumnWidth(0,50)    # Bazi sutunlarin uzunluklari ayarlanir.
        self.table1.setColumnWidth(2,50)
        self.table1.setColumnWidth(3,80)
        self.table1.setColumnWidth(4,70)
        self.table1.setColumnWidth(5,50)
        
        
        self.table1.setHorizontalHeaderLabels(['Gemi Id','Gemi Adi','Sahip Id','Kayıt Tarihi', 'Başkanlık Id','Tip Id'])
        
        
        
        
        
        # Tablonun el ile degistirilebilirligi kapatilir
        self.table1.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        # Tablonun satir numara gostergesi kapatilir
        self.table1.verticalHeader().hide()
        
        # Tablonun gecerli satir sayisi (0) row adli degiskene alinir
        row = self.table1.rowCount()
        
        # Data tablosundaki her eleman for dongusu ile donulur
        for x in data:
            # Her adimda tabloya yeni bir satir eklenip satirin sutunlari eklenir
            self.table1.setRowCount(row + 1)
            self.table1.setItem(row, 0, QtWidgets.QTableWidgetItem(str(x[0])))
            self.table1.setItem(row, 1, QtWidgets.QTableWidgetItem(x[1]))
            self.table1.setItem(row, 2, QtWidgets.QTableWidgetItem(str(x[2])))
            self.table1.setItem(row, 3, QtWidgets.QTableWidgetItem(str(x[3])))
            self.table1.setItem(row, 4, QtWidgets.QTableWidgetItem(str(x[4])))
            self.table1.setItem(row, 5, QtWidgets.QTableWidgetItem(str(x[5])))
            
            # Bir sonraki adim icin satir sayisi bir arttirilir
            row = row + 1
    
    
    def refreshOwners(self, con):
        
        cur = con.cursor()
        cur.execute("select * from owners")
        data = cur.fetchall()
        cur.close()
        
        self.table2.clearContents()
        self.table2.setColumnCount(3)
        self.table2.setRowCount(0)
        self.table2.setColumnWidth(0,50)
        
        self.table2.setHorizontalHeaderLabels(['Kişi Id','Ad','Soyad'])
        
        self.table2.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.table2.verticalHeader().hide()
        
        row = self.table2.rowCount()
        
        for x in data:
            self.table2.setRowCount(row + 1)
            self.table2.setItem(row, 0, QtWidgets.QTableWidgetItem(str(x[0])))
            self.table2.setItem(row, 1, QtWidgets.QTableWidgetItem(x[1]))
            self.table2.setItem(row, 2, QtWidgets.QTableWidgetItem(x[2]))
            
            row = row + 1
    
    
    def refreshTypes(self, con):
        
        cur = con.cursor()
        cur.execute("select * from typess")
        data = cur.fetchall()
        cur.close()
        
        self.table3.clearContents()
        self.table3.setColumnCount(4)
        self.table3.setRowCount(0)
        self.table3.setColumnWidth(0,50)
        self.table3.setColumnWidth(2,100)
        self.table3.setColumnWidth(3,75)
        
        self.table3.setHorizontalHeaderLabels(['Tip Id','Tip Adı','Gövde Uzunluğu','Tonaj'])
        
        self.table3.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.table3.verticalHeader().hide()
        
        row = self.table3.rowCount()
        
        for x in data:
            self.table3.setRowCount(row + 1)
            self.table3.setItem(row, 0, QtWidgets.QTableWidgetItem(str(x[0])))
            self.table3.setItem(row, 1, QtWidgets.QTableWidgetItem(x[1]))
            self.table3.setItem(row, 2, QtWidgets.QTableWidgetItem(str(x[2])))
            self.table3.setItem(row, 3, QtWidgets.QTableWidgetItem(str(x[3])))
            
            row = row + 1
    
    
    def refreshPres(self, con):
        
        cur = con.cursor()
        cur.execute("select * from presidentials")
        data = cur.fetchall()
        cur.close()
        
        self.table4.clearContents()
        self.table4.setColumnCount(4)
        self.table4.setRowCount(0)
        
        self.table4.setHorizontalHeaderLabels(['Başkanlık Id','Başkanlık Adı','Deniz','Şehir'])
        
        self.table4.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.table4.verticalHeader().hide()
        
        row = self.table4.rowCount()
        
        for x in data:
            self.table4.setRowCount(row + 1)
            self.table4.setItem(row, 0, QtWidgets.QTableWidgetItem(str(x[0])))
            self.table4.setItem(row, 1, QtWidgets.QTableWidgetItem(x[1]))
            self.table4.setItem(row, 2, QtWidgets.QTableWidgetItem(x[2]))
            self.table4.setItem(row, 3, QtWidgets.QTableWidgetItem(x[3]))
            
            row = row + 1
            
            
    def refreshHistory(self, con):
        
        cur = con.cursor()
        cur.execute("select * from history")
        data = cur.fetchall()
        cur.close()
        
        self.table5.clearContents()
        self.table5.setColumnCount(6)
        self.table5.setRowCount(0)
        self.table5.setColumnWidth(0,50)
        self.table5.setColumnWidth(1,50)
        self.table5.setColumnWidth(4,70)
        self.table5.setColumnWidth(5,70)
        
        self.table5.setHorizontalHeaderLabels(['Kayıt Id','Gemi Id','Geçerli Konum','Hedef Konum','Çıkış Tarihi','Varış Tarihi'])

        
        self.table5.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.table5.verticalHeader().hide()
        
        row = self.table5.rowCount()
        
        for x in data:
            self.table5.setRowCount(row + 1)
            self.table5.setItem(row, 0, QtWidgets.QTableWidgetItem(str(x[0])))
            self.table5.setItem(row, 1, QtWidgets.QTableWidgetItem(str(x[1])))
            self.table5.setItem(row, 2, QtWidgets.QTableWidgetItem(x[2]))
            self.table5.setItem(row, 3, QtWidgets.QTableWidgetItem(x[3]))
            self.table5.setItem(row, 4, QtWidgets.QTableWidgetItem(str(x[4])))
            self.table5.setItem(row, 5, QtWidgets.QTableWidgetItem(str(x[5])))
            
            row = row + 1
            
    def saveAndClose(self,con):
        con.commit()
        con.close()
        sys.exit(app.exec_())
        exit()
      
app = QApplication([])
window = MainPage()
window.show()
app.exec_()
