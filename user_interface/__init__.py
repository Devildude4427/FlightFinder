from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic

import os
import sys


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Flight Finder")

        logo = QIcon()
        logo.addPixmap(QPixmap(os.path.join('resources', 'ico-noB-512.png')))
        self.setWindowIcon(logo)

        label = QLabel("Flight Finder")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

        uic.loadUi((os.path.join('user_interface', 'mainwindow2.ui')), self)


app = QApplication(sys.argv)


window = MainWindow()
window.show()

app.exec()
