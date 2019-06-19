from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import os
import sys


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Flight Finder")
        self.setFixedHeight(720)
        self.setFixedWidth(1080)

        logo = QIcon()
        logo.addPixmap(QPixmap(os.path.join('resources', 'ico-noB-512.png')))
        self.setWindowIcon(logo)

        label = QLabel("Flight Finder")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)


app = QApplication(sys.argv)


window = MainWindow()
window.show()

app.exec()
