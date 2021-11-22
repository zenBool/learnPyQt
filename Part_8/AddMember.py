# Form implementation generated from reading ui file 'AddMember.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import mysql.connector as mc


class Member_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(450, 450)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_mid = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_mid.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_mid.setFont(font)
        self.lineEdit_mid.setObjectName("lineEdit_mid")
        self.verticalLayout.addWidget(self.lineEdit_mid)
        self.lineEdit_mname = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_mname.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_mname.setFont(font)
        self.lineEdit_mname.setObjectName("lineEdit_mname")
        self.verticalLayout.addWidget(self.lineEdit_mname)
        self.lineEdit_mmobile = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_mmobile.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_mmobile.setFont(font)
        self.lineEdit_mmobile.setObjectName("lineEdit_mmobile")
        self.verticalLayout.addWidget(self.lineEdit_mmobile)
        self.lineEdit_memail = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_memail.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_memail.setFont(font)
        self.lineEdit_memail.setObjectName("lineEdit_memail")
        self.verticalLayout.addWidget(self.lineEdit_memail)
        self.pushButton_save = QtWidgets.QPushButton(Dialog)

        #connect signal
        self.pushButton_save.clicked.connect(self.insert_member)

        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_save.setFont(font)
        self.pushButton_save.setStyleSheet("QPushButton {\n"
"\n"
"background-color:gray;\n"
"color:white\n"
"\n"
"\n"
"}")
        self.pushButton_save.setObjectName("pushButton_save")
        self.verticalLayout.addWidget(self.pushButton_save)
        self.label_result = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_result.setFont(font)
        self.label_result.setText("")
        self.label_result.setObjectName("label_result")
        self.verticalLayout.addWidget(self.label_result)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def insert_member(self):
        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="library"
            )

            id = self.lineEdit_mid.text()
            name= self.lineEdit_mname.text()
            mobile = self.lineEdit_mmobile.text()
            email = self.lineEdit_memail.text()

            if name == "" or id == "" or mobile == "" or email == "":
                self.label_result.setText("Please add all fields")
                self.label_result.setStyleSheet('color:red')
                return
            mycursor = mydb.cursor()
            query = "INSERT INTO tbl_addmember (id, name,mobile,email) VALUES (%s,%s,%s,%s)"
            value = (id, name, mobile, email)
            mycursor.execute(query, value)

            mydb.commit()
            self.label_result.setText("Member Added Successfully")
            self.label_result.setStyleSheet('color:green')

            self.lineEdit_mid.setText("")
            self.lineEdit_mname.setText("")
            self.lineEdit_memail.setText("")
            self.lineEdit_mmobile.setText("")


        except mc.Error as e:
            self.label_result.setText("Failed to add member")
            self.label_result.setStyleSheet('color:red')

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Insert Member"))
        self.lineEdit_mid.setPlaceholderText(_translate("Dialog", "Please Enter Member ID"))
        self.lineEdit_mname.setPlaceholderText(_translate("Dialog", "Please Enter Member Name"))
        self.lineEdit_mmobile.setPlaceholderText(_translate("Dialog", "Please Enter Member Mobile"))
        self.lineEdit_memail.setPlaceholderText(_translate("Dialog", "Please Enter Member Email"))
        self.pushButton_save.setText(_translate("Dialog", "Insert Member"))

