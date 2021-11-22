from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QDoubleSpinBox
from PyQt6 import uic



class UI(QWidget):
    def __init__(self):
        super().__init__()

        uic.loadUi("DoubleSpinDemo.ui", self)

        self.linePrice = self.findChild(QLineEdit, "lineEdit_price")
        self.doublespin = self.findChild(QDoubleSpinBox, "doubleSpinBox")
        self.lineResult = self.findChild(QLineEdit, "lineEdit_total")

        self.doublespin.valueChanged.connect(self.spin_selected)


    def spin_selected(self):
        if self.linePrice.text() != 0:
            price = int(self.linePrice.text())
            totalPrice = self.doublespin.value() * price

            self.lineResult.setText(str(totalPrice))



app = QApplication([])
window = UI()
window.show()
app.exec()