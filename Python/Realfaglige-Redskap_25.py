python
# Eksempel med PyQt
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton

def klikk():
    label.setText("Knappen ble trykket!")

app = QApplication([])
label = QLabel("Hei, PyQt!")
knapp = QPushButton("Trykk her")
knapp.clicked.connect(klikk)
label.show()
knapp.show()
app.exec_()