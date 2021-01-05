from PyQt5.QtWidgets import*
from PyQt5.uic import loadUi
from PyQt5 import QtCore
import psycopg2
import datetime

class AddHistory (QWidget):

    def __init__(self, type_,con):
        super().__init__()
        
        loadUi("addHistory.ui",self)
        
        if type_ == "add":
            self.txtHistId.setDisabled(True)
            
        self.btnSave.clicked.connect(lambda: self.AddHistory(con, type_))


    def AddHistory(self, con, type_):
        cur = con.cursor()
        depDate = self.clDepartDate.selectedDate().toString(QtCore.Qt.ISODate)
        arrDate = self.clArriveDate.selectedDate().toString(QtCore.Qt.ISODate)

        if(type_ == "add"):
            cur.execute(
                "INSERT INTO History (RecID, ShipID, CurrentLoc,Destination,DepartDATE,ArriveDATE) "
                "VALUES (nextval('hisrecseq'), %s, %s, %s, %s, %s)",
                (self.txtShipId.text(), self.txtCLoc.text(), self.txtDest.text(), depDate, arrDate));
        elif(type_ == "upd"):
            cur.execute(
                "UPDATE History SET (ShipID, CurrentLoc, Destination, DepartDATE, ArriveDATE) = (%s, %s, %s, %s, %s)"
                " WHERE RecID = %s",
                (self.txtShipId.text(), self.txtCLoc.text(), self.txtDest.text(), depDate, arrDate, self.txtHistId.text()));
        else:
            QMessageBox.about(self, "Hata", "Yanlış işlem")
        con.commit()
        cur.close()
        self.close()