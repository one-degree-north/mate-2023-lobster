from PyQt6.QtWidgets import QApplication
from gui.gui import MainWindow
from comms import Comms

import sys
import os

if __name__ == '__main__':
    try:
        os.mkdir("gui/captures")
    except FileExistsError:
        pass

    comms = None

    if input("Comms? ") == "y":
        comms = Comms("/dev/cu.usbmodem112301", 9600)

    app = QApplication(sys.argv)

    window = MainWindow(comms=comms)
    window.show()

    app.exec()
