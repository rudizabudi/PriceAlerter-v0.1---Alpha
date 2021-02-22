from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
import sys
from time import sleep

#custom imports
import windows.gui.qtgui as qtgui
import windows.popups.add_watchlist_popup as awp
import windows.popups.popup_handler as ph


class WindowHandler():
    reSize = QtCore.pyqtSignal(QtCore.QSize)
    def __init__(self):
        super().__init__()
        self.app_root = QtWidgets.QApplication(sys.argv)
        self.root = QtWidgets.QMainWindow()
        print(self)
        print(self.root)
        self.ui = qtgui.Ui_root()
        self.ui.setupUi(self.root)
        self.root.show()
        self.qtgui_triggers()
        sys.exit(self.app_root.exec_())

    def qtgui_triggers(self):
        self.ui.button_watchlistAdd.clicked.connect(lambda: self.add_watchlist_popup())

    def add_watchlist_popup(self):
        print(123)
        self.watchlist_popup = QtWidgets.QMainWindow()
        self.watchlist_ui = awp.Ui_Form()
        self.watchlist_ui.setupUi(self.watchlist_popup)
        self.watchlist_popup.show()
        ph.popup_triggers('addWatchlist', self.ui, self.watchlist_ui, self.watchlist_popup)


if __name__ == '__main__':
    wh = WindowHandler()
    wh.Ui_root()
