from PyQt6.QtWidgets import QApplication, QWidget, QListWidget, QLabel, QVBoxLayout
from PyQt6.QtGui import QIcon, QFont
import sys



class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 700, 400)
        self.setWindowTitle("PyQt6 QListWidget")
        self.setWindowIcon(QIcon('images/python.png'))

        vbox = QVBoxLayout()

        self.list_widget = QListWidget()


        self.list_widget.insertItem(0, "Python")
        self.list_widget.insertItem(1, "Java")
        self.list_widget.insertItem(2, "C++")
        self.list_widget.insertItem(3, "C#")
        self.list_widget.insertItem(1, "Kotlin")
        self.list_widget.setFont(QFont("Times", 15))
        self.list_widget.setStyleSheet('background-color:gray')

        self.list_widget.clicked.connect(self.item_clicked)



        self.label = QLabel("")
        self.label.setFont(QFont("Times", 15))




        vbox.addWidget(self.list_widget)
        vbox.addWidget(self.label)


        self.setLayout(vbox)

    def item_clicked(self):
        item = self.list_widget.currentItem()
        self.label.setText("You have selected : " + str(item.text()))



app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())