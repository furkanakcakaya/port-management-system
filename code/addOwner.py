from PyQt5.QtWidgets import*
from PyQt5.uic import loadUi
from PyQt5 import QtCore
import psycopg2

class AddOwner (QWidget):

    def __init__(self, type_,con):
        super().__init__()
        
        loadUi("addOwner.ui",self)

        if type_ == "add":
            self.txtOwnerId.setDisabled(True)

        self.btnSave.clicked.connect(lambda: self.AddOwner(con, type_))


    def AddOwner(self, con, type_):
        cur = con.cursor()
        if (type_ == "add"):
            cur.execute(
                "INSERT INTO Owners (OwnerID, OwnerNAME, OwnerLNAME) "
                "VALUES (nextval('ownerseq'), %s, %s)",
                (self.txtOwnerName.text(), self.txtOwnerLName.text()));
        elif (type_ == "upd"):
            cur.execute(
                "UPDATE Owners SET (OwnerNAME, OwnerLNAME) = (%s, %s)"
                " WHERE OwnerID = %s",
                (self.txtOwnerName.text(), self.txtOwnerLName.text(), self.txtOwnerId.text()));
        else:
            QMessageBox.about(self, "Hata", "Yanlış işlem")
        con.commit()
        cur.close()
        self.close()