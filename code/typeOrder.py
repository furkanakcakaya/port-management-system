from PyQt5.QtWidgets import*
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtWidgets

class TypeOrder (QWidget):

    def __init__(self, con):
        super().__init__()
        
        loadUi("typeOrder.ui",self)
        
        self.slider.setMaximum(0)
        self.slider.valueChanged[int].connect(self.changeValue)
        
        self.radTonnage.toggled.connect(lambda:self.slider.setMaximum(30000))
        self.radHull.toggled.connect(lambda:self.slider.setMaximum(300))     
        
        self.btnOrder.clicked.connect(lambda:self.viewTable(con))
            
        avgTonnageStr = "Ortalama tonaj: "
        avgHullStr = "Ortalama Govde Boyu: "
        
        cur = con.cursor()
        
        cur.execute("select avg(tonnage) from typess")
        data = cur.fetchone()
        
        self.labelTonnage.setText(avgTonnageStr + str(data[0]))
        
        cur.execute("select avg(hulllen) from typess")
        data = cur.fetchone()
        
        self.labelHull.setText(avgHullStr + str(data[0]))
        
        cur.close()
        
       
    def changeValue(self, value):
        #print(value)
        self.label.setText(str(value))
        
        
    def viewTable(self,con):
        
        cur = con.cursor()
        
        if self.radHull.isChecked():
            sql = "select typename, hulllen from typess group by hulllen, typename having hulllen > %s order by hulllen"
        elif self.radTonnage.isChecked:
            #sql = "select typename, tonnage from typess group by tonnage, typename having tonnage > %s order by tonnage"
            sql = "select typename, tonnage from typess except select typename, tonnage from typess where tonnage <= %s order by tonnage"
            
            
        number = self.slider.value()
        cur.execute(sql, [str(number)])
        data = cur.fetchall()
        cur.close()
        
        self.table.clearContents()
        self.table.setColumnCount(2)
        self.table.setRowCount(0)
        #self.table.setColumnWidth(0,50)
        
        self.table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.table.verticalHeader().hide()
        
        row = self.table.rowCount()
        
        for x in data:
            self.table.setRowCount(row + 1)
            self.table.setItem(row, 0, QtWidgets.QTableWidgetItem(x[0]))
            self.table.setItem(row, 1, QtWidgets.QTableWidgetItem(str(x[1])))
            
            row = row + 1
        
        