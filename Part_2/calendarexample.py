from PyQt6.QtWidgets import QApplication, QWidget, QCalendarWidget, QVBoxLayout, QLabel
from PyQt6.QtGui import QIcon, QFont
import sys



class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 700, 400)
        self.setWindowTitle("PyQt6 QCalendarWidget")
        self.setWindowIcon(QIcon('images/python.png'))

        vbox = QVBoxLayout()

        self.calendar = QCalendarWidget()
        self.calendar.setGridVisible(True)
        self.calendar.selectionChanged.connect(self.calendar_date)

        self.label = QLabel("Hello")
        self.label.setFont(QFont("Times", 15))
        self.setStyleSheet('color:green')


        vbox.addWidget(self.calendar)
        vbox.addWidget(self.label)


        self.setLayout(vbox)

    def calendar_date(self):
        dateSelected = self.calendar.selectedDate()
        date_string = str(dateSelected.toPyDate())

        self.label.setText("Date Is {} : ".format(date_string))


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())