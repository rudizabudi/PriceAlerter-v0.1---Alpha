# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_alertlist_popup.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(292, 144)
        Form.setStyleSheet("background-color: rgb(54, 54, 54);")
        self.pushButton_Cancel = QtWidgets.QPushButton(Form)
        self.pushButton_Cancel.setGeometry(QtCore.QRect(195, 110, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Cancel.setFont(font)
        self.pushButton_Cancel.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(234, 230, 228);")
        self.pushButton_Cancel.setObjectName("pushButton_Cancel")
        self.label_Watchlist = QtWidgets.QLabel(Form)
        self.label_Watchlist.setEnabled(True)
        self.label_Watchlist.setGeometry(QtCore.QRect(10, 20, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_Watchlist.setFont(font)
        self.label_Watchlist.setStyleSheet("color: rgb(234, 230, 228);")
        self.label_Watchlist.setTextFormat(QtCore.Qt.RichText)
        self.label_Watchlist.setScaledContents(False)
        self.label_Watchlist.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Watchlist.setObjectName("label_Watchlist")
        self.lineEdit_NewAlertName = QtWidgets.QLineEdit(Form)
        self.lineEdit_NewAlertName.setGeometry(QtCore.QRect(20, 50, 250, 31))
        self.lineEdit_NewAlertName.setStyleSheet("background-color: rgb(222, 220, 216);")
        self.lineEdit_NewAlertName.setText("")
        self.lineEdit_NewAlertName.setCursorPosition(0)
        self.lineEdit_NewAlertName.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.lineEdit_NewAlertName.setObjectName("lineEdit_NewAlertName")
        self.pushButton_Add = QtWidgets.QPushButton(Form)
        self.pushButton_Add.setGeometry(QtCore.QRect(120, 110, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Add.setFont(font)
        self.pushButton_Add.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(234, 230, 228);")
        self.pushButton_Add.setObjectName("pushButton_Add")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.lineEdit_NewAlertName, self.pushButton_Add)
        Form.setTabOrder(self.pushButton_Add, self.pushButton_Cancel)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Add Alertlist"))
        self.pushButton_Cancel.setText(_translate("Form", "Cancel"))
        self.label_Watchlist.setText(_translate("Form", "Name of the alertlist:"))
        self.lineEdit_NewAlertName.setPlaceholderText(_translate("Form", "New Alertlist"))
        self.pushButton_Add.setText(_translate("Form", "Add"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
