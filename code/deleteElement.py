from PyQt5.QtWidgets import*
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMessageBox
import psycopg2

class DeleteElement (QWidget):

    def __init__(self, type_,con):
        super().__init__()
        
        loadUi("deleteElement.ui",self)
        
        # arguman olarak gonderilen tip degeri butonun baglandigi fonksiyona gonderilir
        self.type = type_
        self.btnDelete.clicked.connect(lambda: self.deleteSelectedId(con,type_))
        self.btnCancel.clicked.connect(self.close)              # Iptal butonu
        
        
    def deleteSelectedId(self,con,type_):
        
        if type_ == "ship":
            
            # sql fonksiyonu ile gonderilen id degerine sahip gemi database'den silinir
            cur = con.cursor()
            cur.execute("delete from ships where ShipID = %s", [self.txtId.text()])
            cur.close()
            
        elif type_ == "owner":
            
            cur = con.cursor()
            # Gonderilen sahip id once herhangi bir geminin foreign key'i olup olmadigi kontrol edilir foreign key ise kullaniciya uyari verilir, degil ise database'den silinir
            cur.execute("select * from ships where OwnerID = %s", [self.txtId.text()])
            data = cur.fetchall()
            if len(data) == 0:
                cur.execute("delete from owners where OwnerID = %s", [self.txtId.text()])
            else:
                QMessageBox.about(self, "Hata", "Silmeye Çalıştığınız OwnerID başka bir eleman tarafından Foreign Key olarak tutulmaktadır.")
            cur.close()
            
        elif type_ == "pres":
            
            cur = con.cursor()
            cur.execute("select * from ships where RecordedPId = %s", [self.txtId.text()])
            data = cur.fetchall()
            if len(data) == 0:
                cur.execute("delete from presidentials where PID = %s", [self.txtId.text()])
            else:
                QMessageBox.about(self, "Hata", "Silmeye Çalıştığınız PID başka bir eleman tarafından Foreign Key olarak tutulmaktadır.")
            cur.close()
            
        elif type_ == "type":
            
            cur = con.cursor()
            cur.execute("select * from ships where TypeID = %s", [self.txtId.text()])
            data = cur.fetchall()
            if len(data) == 0:
                cur.execute("delete from typess where TypeID = %s", [self.txtId.text()])
            else:
                QMessageBox.about(self, "Hata", "Silmeye Çalıştığınız TypeID başka bir eleman tarafından Foreign Key olarak tutulmaktadır.")
            cur.close()
            
        elif type_ == "history":
            
            cur = con.cursor()
            cur.execute("delete from history where ShipID = %s", [self.txtId.text()])
            cur.close()
        
        self.close()