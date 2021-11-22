from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QComboBox
from PyQt6 import uic



class UI(QWidget):
    def __init__(self):
        super().__init__()

        uic.loadUi("ComboDemo.ui", self)

        self.label_result = self.findChild(QLabel, "label_result")

        self.combo = self.findChild(QComboBox, "comboBox")

        self.combo.currentTextChanged.connect(self.combo_changed)


    def combo_changed(self):
        item = self.combo.currentText()
        self.label_result.setText("Your Favorite Language : " + item)



app = QApplication([])
window = UI()
window.show()
app.exec()