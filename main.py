from PyQt6.QtWidgets import QApplication
from gui.gui import MainWindow
from comms import Comms

import sys
import os

from serial.tools import list_ports

if __name__ == '__main__':
    try:
        os.mkdir("gui/captures")
    except FileExistsError:
        pass

    arduino = None
    
    for v in list_ports.comports():
        if "USB" in v.description:
            arduino = v

    if arduino:
        print(f"Successfully connected - {arduino.description} detected!")
        comms = Comms(arduino.device, 9600)
    else:
        print("Failed to connect - arduino not detected!")
        comms = None

    app = QApplication(sys.argv)

    window = MainWindow(comms)
    window.show()

    app.exec()
