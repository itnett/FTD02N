python
   from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

   app = QApplication([])

   vindu = QWidget()
   vindu.setWindowTitle('Enkel PyQt Applikasjon')

   layout = QVBoxLayout()
   layout.addWidget(QLabel('Hei, verden!'))
   vindu.setLayout(layout)

   vindu.show()
   app.exec_()