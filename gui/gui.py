from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout

from widgets import camera



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.cameras = camera.CameraTab()

        self.frame = QWidget()
        self.frame.layout = QHBoxLayout()
        self.frame.layout.addWidget(self.cameras)
        self.frame.layout.addStretch()
        self.frame.setLayout(self.frame.layout)

        self.setCentralWidget(self.frame)

if __name__ == '__main__':
    app = QApplication([])

    window = MainWindow()
    window.show()

    app.exec()
