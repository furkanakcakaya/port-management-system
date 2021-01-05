from PyQt5.QtWidgets import QApplication
from mainMenu import MainPage

import sys

# Programin calistigi main fonksiyonu

app=QApplication([])
window = MainPage()
window.show()


sys.exit(app.exec_())
#app.exec_()

