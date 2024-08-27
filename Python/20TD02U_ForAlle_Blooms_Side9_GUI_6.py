python
   def test_label_text(qtbot):
       label = QLabel("Hei, verden!")
       qtbot.addWidget(label)
       assert label.text() == "Hei, verden!"