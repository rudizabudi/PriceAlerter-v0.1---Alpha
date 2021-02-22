from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class RootWindow(QMainWindow):
    def __init__(self, **kwargs):
        super(RootWindow, self).__init__()

        xpos = 500
        ypos = 200
        width = 1000
        height = 800
        self.setGeometry(xpos, ypos, width, height)

        self.setWindowTitle('Price Alerter')

        self.initGUI()

    def initGUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText('My first label')
        self.label.move(50, 50)
        self.button1 = QtWidgets.QPushButton(self)
        self.button1.setText('Click me!')
        self.button1.clicked.connect(self.clicked)

    def clicked(self):
        self.button1.setText('clicked')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = RootWindow()
    win.show()
    sys.exit(app.exec_())
