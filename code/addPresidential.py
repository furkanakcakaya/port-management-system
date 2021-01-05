from PyQt5.QtWidgets import*
from PyQt5.uic import loadUi

class AddPresidential (QWidget):

    def __init__(self, type_,con):
        super().__init__()
        
        loadUi("addPresidential.ui",self)

        if type_ == "add":
            self.txtPId.setDisabled(True)

        self.btnSave.clicked.connect(lambda: self.AddHistory(con, type_))


    def AddHistory(self, con, type_):
        cur = con.cursor()
        if(type_ == "add"):
            cur.execute(
                "INSERT INTO Presidentials (PID, PNAME, SEAOCEANLAKE, City) "
                "VALUES (nextval('presseq'), %s, %s, %s)",
                (self.txtPName.text(), self.txtSeaName.text(), self.txtCity.text()));
        elif(type_ == "upd"):
            cur.execute(
                "UPDATE Presidentials SET (PNAME, SEAOCEANLAKE, City) = (%s, %s, %s)"
                " WHERE PID = %s",
                (self.txtPName.text(), self.txtSeaName.text(), self.txtCity.text(), self.txtPId.text()));
        else:
            QMessageBox.about(self, "Hata", "Yanlış işlem")
        con.commit()
        cur.close()
        self.close()