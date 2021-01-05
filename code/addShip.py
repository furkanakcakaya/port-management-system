from PyQt5.QtWidgets import*
from PyQt5.uic import loadUi
from PyQt5 import QtCore

class AddShip (QWidget):

    def __init__(self, type_,con):
        super().__init__()
        
        loadUi("addShip.ui",self)
        
        if type_ == "add":
            self.txtShipId.setDisabled(True)
        
        
        
        self.btnSave.clicked.connect(lambda: self.AddHistory(con, type_))
        
        

    def AddHistory(self, con, type_):
        cur = con.cursor()
        recDate = self.clRecordDate.selectedDate().toString(QtCore.Qt.ISODate)


        if(type_ == "add"):
            cur.execute(
                "INSERT INTO Ships (ShipID, ShipName, OwnerId, RecordDATE, RecordedPId, TypeID) "
                "VALUES (nextval('shipseq'), %s, %s, %s, %s, %s)",
                (self.txtShipName.text(), self.txtShipOwnerId.text(), recDate, self.txtShipPreId.text(), self.txtShipType.text()));
            QMessageBox.about(self, "Bilgi", (str(con.notices[0][8:] + str(con.notices[1][8:]) + str(con.notices[2][8:]) + str(con.notices[3][8:]))))
        elif(type_ == "upd"):
            cur.execute(
                "UPDATE Ships SET (ShipName, OwnerId, RecordDATE, RecordedPId, TypeID) = (%s, %s, %s, %s, %s)"
                " WHERE ShipID = %s",
                (self.txtShipName.text(), self.txtShipOwnerId.text(), recDate, self.txtShipPreId.text(), self.txtShipType.text(), self.txtShipId.text()));
            QMessageBox.about(self, "Bilgi", (str(con.notices[0][8:] + str(con.notices[1][8:]) + str(con.notices[2][8:]) + str(con.notices[3][8:]))))
        else:
            QMessageBox.about(self, "Hata", "Yanlış işlem")
        con.commit()
        cur.close()
        self.close()