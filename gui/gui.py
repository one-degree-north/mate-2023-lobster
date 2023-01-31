from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel
from widgets import camera
from PyQt6.QtCore import Qt
from util import *
from stopwatch import Stopwatch
from lables import Lables
from navBar import NavBar


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setStyleSheet("""
            QMainWindow {
                background: %s
            } #
        """ % Color.back)
 
        self.setWindowTitle("Lobster")
        self.frame = QWidget()
        self.frame.layout = QVBoxLayout()
        self.frame.layout.addStretch()
        self.frame.setLayout(self.frame.layout)
        self.frame.layout.setContentsMargins(0,0,0,0)
        self.frame.layout.setSpacing(0)

        self.setCentralWidget(self.frame) 

        self.watch = Stopwatch()
        self.watchFrame = QWidget()
        self.watchFrame.layout = QVBoxLayout()
        self.watchFrame.layout.setSpacing(0)
        
        self.watchFrame.layout.addWidget(self.watch)
        self.watchFrame.layout.addStretch(1)

        self.watchFrame.layout.setContentsMargins(0,80,0,0)
        self.watchFrame.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.watchFrame.setLayout(self.watchFrame.layout)
        self.frame.layout.addWidget(self.watchFrame)

        self.cameras = camera.CameraTab()
        self.cameras.layout = QHBoxLayout()
        
        self.bar = NavBar()
        self.barFrame = QWidget()
        self.barFrame.layout = QHBoxLayout()
        self.barFrame.layout.setContentsMargins(0,0,0,0)
        # self.barFrame.layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.barFrame.setLayout(self.barFrame.layout)
        self.barFrame.layout.addWidget(self.bar)

        self.mid = QWidget()
        self.mid.layout = QHBoxLayout()
        self.mid.layout.addWidget(self.barFrame)
        self.mid.layout.addWidget(self.cameras)
        self.mid.layout.setContentsMargins(0,0,0,0)
        self.mid.setLayout(self.mid.layout)
        self.frame.layout.addWidget(self.mid)
        
        # self.cameras = camera.CameraTab()
        # self.cameras.layout = QHBoxLayout()
        # self.frame.layout.addWidget(self.cameras)

        # self.bar = NavBar()
        # self.barFrame = QWidget()
        # self.barFrame.layout = QHBoxLayout()
        # self.barFrame.layout.setContentsMargins(0,0,0,0)
        # self.barFrame.layout.setAlignment(Qt.AlignmentFlag.AlignLeft.AlignVCenter)
        # self.barFrame.layout.addWidget(self.bar)
        # # self.bar.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # #self.barFrame.layout.setAlignment(Qt.AlignmentFlag.AlignVCenter.AlignLeft)
        # self.barFrame.setLayout(self.barFrame.layout)
        # # self.cameras.layout.addWidget(self.barFrame)
        # self.frame.layout.addWidget(self.barFrame, 500)
        # # self.bar.layout.addStretch(1)
        # # self.barFrame.layout.addStretch(1)
        # # self.cameras = camera.CameraTab()
        # # self.barFrame.setLayout(self.barFrame.layout)
        # # self.cameras.layout.addWidget(self.barFrame)
        # # self.frame.layout.addWidget(self.cameras)


        self.xyz = Lables()
        self.xFrame = QWidget()
        self.xFrame.layout = QVBoxLayout()
        self.xFrame.layout.setContentsMargins(105,10,50,50)
        # self.xFrame.layout.setAlignment(Qt.AlignmentFlag.AlignTrailing)
        self.xFrame.layout.addWidget(self.xyz)
        self.xFrame.setLayout(self.xFrame.layout)
        self.frame.layout.addWidget(self.xFrame)




if __name__ == '__main__':
    app = QApplication([])

    window = MainWindow()
    window.show()

    app.exec()
