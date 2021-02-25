from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
import threading

#custom imports
import windows.gui.qtgui as qtgui
import windows.popups.popup_handler as ph
from config import command_ledger
import data_handler


class RootWindowHandler(QtWidgets.QMainWindow, qtgui.Ui_root):
    def __init__(self, parent=None):
        super(RootWindowHandler, self).__init__(parent)
        self.setupUi(self)
        self.qtgui_triggers()

        dh = data_handler.DataHandler(self)
        dh_thread = threading.Thread(target=dh.logic_loop, name='Data Handler', args=(self,))
        dh_thread.start()

        #self.tableWidget_listDisplay.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
        self.tableWidget_listDisplay.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableWidget_listDisplay.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.tableWidget_listDisplay.setGeometry(QtCore.QRect(190, 70, 621, 30))

    def resizeEvent(self, event):
        resize = True

    # Register all ptgui triggeres here
    def qtgui_triggers(self):
        #alertlist
        self.button_alertsAdd.clicked.connect(lambda: ph.popup_triggers('addAlertList'))
        self.button_alertsDelete.clicked.connect(lambda: command_ledger.append({'deleteList': ['Alert', [x.text() for x in self.listWidget_alertlists.selectedItems()]]}))

        #watchlist
        self.button_watchAdd.clicked.connect(lambda: ph.popup_triggers('addWatchList'))
        self.button_watchDelete.clicked.connect(lambda: command_ledger.append({'deleteList': ['Watch', [x.text() for x in self.listWidget_watchlists.selectedItems()]]}))

        #menubar
        self.actionNew.triggered.connect(lambda: command_ledger.append({'new': None}))
        self.actionOpen.triggered.connect(lambda: ph.popup_triggers('openfile', root_ui=self))
        self.actionSave.triggered.connect(lambda: command_ledger.append({'save': None}))
        self.actionSave_As.triggered.connect(lambda:  ph.popup_triggers('savetofile', root_ui=self))

        #topbar
        #TODO: send selected watchlist & autoselect in combobox
        self.toolButton_objectAdd.clicked.connect(lambda: ph.popup_triggers('addTypeSelection', root_ui=self))
        self.toolButton_objectSettings.clicked.connect(lambda: ph.popup_triggers('settings', root_ui=self))

        #list selection doubleclick
        self.listWidget_alertlists.itemDoubleClicked.connect(lambda x: command_ledger.append({'changeList': ['Alertlists', x]}))
        self.listWidget_watchlists.itemDoubleClicked.connect(lambda x: command_ledger.append({'changeList': ['Watchlists', x]}))

        self.toolButton_objectEdit.clicked.connect(lambda: print(len(self.tableWidget_listDisplay.selectionModel().selectedRows())))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    rwh = RootWindowHandler()
    rwh.show()

    sys.exit(app.exec_())



