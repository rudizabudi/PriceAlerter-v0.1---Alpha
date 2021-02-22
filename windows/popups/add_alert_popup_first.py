# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_alert_popup_first.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(420, 210)
        Form.setStyleSheet("background-color: rgb(54, 54, 54);")
        self.label_Alertlist = QtWidgets.QLabel(Form)
        self.label_Alertlist.setGeometry(QtCore.QRect(20, 20, 90, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_Alertlist.setFont(font)
        self.label_Alertlist.setStyleSheet("color: rgb(234, 230, 228);")
        self.label_Alertlist.setTextFormat(QtCore.Qt.RichText)
        self.label_Alertlist.setScaledContents(False)
        self.label_Alertlist.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Alertlist.setObjectName("label_Alertlist")
        self.label_Alertlist_2 = QtWidgets.QLabel(Form)
        self.label_Alertlist_2.setGeometry(QtCore.QRect(20, 61, 90, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_Alertlist_2.setFont(font)
        self.label_Alertlist_2.setStyleSheet("color: rgb(234, 230, 228);")
        self.label_Alertlist_2.setTextFormat(QtCore.Qt.RichText)
        self.label_Alertlist_2.setScaledContents(False)
        self.label_Alertlist_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Alertlist_2.setObjectName("label_Alertlist_2")
        self.label_Alertlist_3 = QtWidgets.QLabel(Form)
        self.label_Alertlist_3.setGeometry(QtCore.QRect(20, 104, 90, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_Alertlist_3.setFont(font)
        self.label_Alertlist_3.setStyleSheet("color: rgb(234, 230, 228);")
        self.label_Alertlist_3.setTextFormat(QtCore.Qt.RichText)
        self.label_Alertlist_3.setScaledContents(False)
        self.label_Alertlist_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Alertlist_3.setObjectName("label_Alertlist_3")
        self.comboBox_alertlistSelect = QtWidgets.QComboBox(Form)
        self.comboBox_alertlistSelect.setGeometry(QtCore.QRect(140, 13, 250, 36))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(16)
        self.comboBox_alertlistSelect.setFont(font)
        self.comboBox_alertlistSelect.setStyleSheet("color: rgb(234, 230, 228);")
        self.comboBox_alertlistSelect.setCurrentText("")
        self.comboBox_alertlistSelect.setObjectName("comboBox_alertlistSelect")
        self.comboBox_alertlistSelect.addItem("")
        self.pushButton_Continue = QtWidgets.QPushButton(Form)
        self.pushButton_Continue.setGeometry(QtCore.QRect(160, 160, 100, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Continue.setFont(font)
        self.pushButton_Continue.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(234, 230, 228);")
        self.pushButton_Continue.setObjectName("pushButton_Continue")
        self.lineEdit_name = QtWidgets.QLineEdit(Form)
        self.lineEdit_name.setGeometry(QtCore.QRect(140, 54, 250, 36))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(16)
        self.lineEdit_name.setFont(font)
        self.lineEdit_name.setStyleSheet("background-color: rgb(222, 220, 216);")
        self.lineEdit_name.setText("")
        self.lineEdit_name.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.lineEdit_symbol = QtWidgets.QLineEdit(Form)
        self.lineEdit_symbol.setGeometry(QtCore.QRect(140, 97, 250, 36))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(16)
        self.lineEdit_symbol.setFont(font)
        self.lineEdit_symbol.setStyleSheet("background-color: rgb(222, 220, 216);")
        self.lineEdit_symbol.setText("")
        self.lineEdit_symbol.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.lineEdit_symbol.setObjectName("lineEdit_symbol")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.comboBox_alertlistSelect, self.lineEdit_name)
        Form.setTabOrder(self.lineEdit_name, self.lineEdit_symbol)
        Form.setTabOrder(self.lineEdit_symbol, self.pushButton_Continue)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Add Alert"))
        self.label_Alertlist.setText(_translate("Form", "Alert List:"))
        self.label_Alertlist_2.setText(_translate("Form", "Name:"))
        self.label_Alertlist_3.setText(_translate("Form", "Symbol:"))
        self.comboBox_alertlistSelect.setPlaceholderText(_translate("Form", "Source"))
        self.comboBox_alertlistSelect.setItemText(0, _translate("Form", "Price"))
        self.pushButton_Continue.setText(_translate("Form", "Continue"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
