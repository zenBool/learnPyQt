# Form implementation generated from reading ui file 'DbConDemo.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import mysql.connector as mc


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_createdb = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_createdb.setFont(font)
        self.pushButton_createdb.setObjectName("pushButton_createdb")

        #connect signal
        self.pushButton_createdb.clicked.connect(self.create_database)
        self.horizontalLayout_2.addWidget(self.pushButton_createdb)
        self.pushButton_dbcon = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_dbcon.setFont(font)
        self.pushButton_dbcon.setObjectName("pushButton_dbcon")

        #connect signal
        self.pushButton_dbcon.clicked.connect(self.db_connect)
        self.horizontalLayout_2.addWidget(self.pushButton_dbcon)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_result = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_result.setFont(font)
        self.label_result.setText("")
        self.label_result.setObjectName("label_result")
        self.verticalLayout.addWidget(self.label_result)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def create_database(self):
        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password=""
            )

            cursor = mydb.cursor()
            dbname = self.lineEdit.text()

            cursor.execute("CREATE DATABASE {} ".format(dbname))
            self.label_result.setText("Database {} Created ".format(dbname))

        except mc.Error as e:
            self.label_result.setText("Database creation failed")

    def db_connect(self):
        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="pyqtdb"
            )

            self.label_result.setText("There is a connection")

        except mc.Error as e:
            self.label_result.setText("Error in connection")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Database Name:"))
        self.pushButton_createdb.setText(_translate("Form", "Create Database"))
        self.pushButton_dbcon.setText(_translate("Form", "Database Connection"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())