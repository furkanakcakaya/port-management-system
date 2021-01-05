from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import psycopg2

class AddType(QWidget):

    def __init__(self, type_, con):
        super().__init__()

        loadUi("addType.ui", self)

        if type_ == "add":
            self.txtTypeId.setDisabled(True)

        self.btnSave.clicked.connect(lambda: self.AddHistory(con, type_))

    def AddHistory(self, con, type_):
        cur = con.cursor()
        if (type_ == "add"):
            cur.execute(
                "INSERT INTO Typess (TypeID, TypeName, HullLEN, Tonnage) "
                "VALUES (nextval('seqtypess'), %s, %s, %s)",
                (self.txtTypeName.text(), self.dsbHull.value(), self.dsbTonnage.value()));
        elif (type_ == "upd"):
            cur.execute(
                "UPDATE Typess SET (TypeName, HullLEN, Tonnage) = (%s, %s, %s)"
                " WHERE TypeID = %s",
                (self.txtTypeName.text(), self.dsbHull.value(), self.dsbTonnage.value(), self.txtTypeId.text()));
        else:
            QMessageBox.about(self, "Hata", "Yanlış işlem")
        con.commit()
        cur.close()
        self.close()