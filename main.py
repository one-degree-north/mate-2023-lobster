from PyQt6.QtWidgets import QApplication
from gui.gui import MainWindow

import os

if __name__ == '__main__':
    try:
        os.mkdir("gui/captures")
    except FileExistsError:
        pass

    app = QApplication([])

    window = MainWindow()
    window.show()

    app.exec()
