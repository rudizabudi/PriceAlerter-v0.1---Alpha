from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QFileDialog
import sys
import os
from time import sleep
import threading

#custom imports
import windows.gui.qtgui as qtgui
import windows.popups.popup_handler as ph

import windows.popups.add_type_selection as ats
from config import command_ledger, data_ledger
import data_handler
import data_updater


from yahoofinancials import YahooFinancials

class RootWindowHandler(QtWidgets.QMainWindow, qtgui.Ui_root):
    def __init__(self, parent=None):
        super(RootWindowHandler, self).__init__(parent)
        self.setupUi(self)
        self.qtgui_triggers()

        dh = data_handler.DataHandler(self)
        dh_thread = threading.Thread(target=dh.logic_loop, name='Data Handler', args=(self,))
        dh_thread.start()

        self.tableWidget_listDisplay.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
        self.tableWidget_listDisplay.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.tableWidget_listDisplay.setGeometry(QtCore.QRect(190, 70, 621, 30))

        # for i in range(5):
        #     self.listWidget_alertlists.addItem(str(i))

    def resizeEvent(self, event):
        resize = True

    # Register all ptgui triggeres here
    def qtgui_triggers(self):
        # alertlist
        self.button_alertsAdd.clicked.connect(lambda: ph.popup_triggers('addAlertList'))
        self.button_alertsDelete.clicked.connect(lambda: command_ledger.append({'deleteList': ['Alert', [x.text() for x in self.listWidget_alertlists.selectedItems()]]}))
        #menubar
        self.actionNew.triggered.connect(lambda: command_ledger.append({'new': None}))
        self.actionOpen.triggered.connect(lambda: ph.popup_triggers('openfile', root_ui=self))
        self.actionSave.triggered.connect(lambda: command_ledger.append({'save': None}))
        self.actionSave_As.triggered.connect(lambda:  ph.popup_triggers('savetofile', root_ui=self))
        #topbar
        #TODO: send selected watchlist & autoselect in combobox
        self.toolButton_objectAdd.clicked.connect(lambda: self.add_type_selection())
        #list selection doubleclick
        self.listWidget_alertlists.itemDoubleClicked.connect(lambda x: command_ledger.append({'changeList': ['Alertlists', x]}))
        #self.toolButton_objectEdit.clicked.connect(lambda: print(123))


    def add_type_selection(self):
        # TODO Move to popup handler
        add_type_popup = QtWidgets.QMainWindow()
        add_type_ui = ats.Ui_Form()
        add_type_ui.setupUi(add_type_popup)
        add_type_popup.show()

        add_type_ui.toolButton_alertAdd.clicked.connect(lambda: ph.popup_triggers('addAlertOne', root_ui= self, popup=add_type_popup))
        #TODO Add watch-type here


if __name__ == '__main__':
    app = QApplication(sys.argv)
    rwh = RootWindowHandler()
    rwh.show()

    sys.exit(app.exec_())



