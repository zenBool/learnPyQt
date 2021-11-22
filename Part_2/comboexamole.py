from PyQt6.QtWidgets import QApplication, QWidget, QComboBox, QLabel, QHBoxLayout, QVBoxLayout
from PyQt6.QtGui import QIcon, QFont
import sys



class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 500, 200)
        self.setWindowTitle("PyQt6 QComboBox")
        self.setWindowIcon(QIcon('images/python.png'))

        self.create_combo()


    def create_combo(self):
        hbox = QHBoxLayout()

        label = QLabel("Select Account Type: ")
        label.setFont(QFont("Times", 15))

        self.combo = QComboBox()
        self.combo.addItem("Current Account")
        self.combo.addItem("Deposte Account")
        self.combo.addItem("Saving Account")

        self.combo.currentTextChanged.connect(self.combo_changed)

        vbox = QVBoxLayout()
        self.label_result = QLabel("")
        self.label_result.setFont(QFont("Times", 15))
        vbox.addWidget(self.label_result)
        vbox.addLayout(hbox)




        hbox.addWidget(label)
        hbox.addWidget(self.combo)

        self.setLayout(vbox)

    def combo_changed(self):
        item = self.combo.currentText()
        self.label_result.setText("Your Account Type Is : " + item)

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())