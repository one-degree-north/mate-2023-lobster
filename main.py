from PyQt6.QtWidgets import QApplication
from gui.gui import MainWindow
# from comms import Comms
import os

if __name__ == '__main__':
    try:
        os.mkdir("gui/captures")
    except FileExistsError:
        pass

    app = QApplication([])

    # comms = Comms("/dev/w0e0", 9600)

    window = MainWindow(None)
    window.show()

    app.exec()
