from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout
from gui.camera import CameraTab
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from .util import *
from .stopwatch import Stopwatch
from .labels import Labels
from .navbar import NavBar
from datetime import datetime
import cv2
import os
# import logging

class MainWindow(QMainWindow):
    def __init__(self, comms):
        super().__init__()

        self.setStyleSheet("""
            QMainWindow {\
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

        self.cameras = CameraTab()
        self.cameras.layout = QHBoxLayout()
        
        self.bar = NavBar()
        self.barFrame = QWidget()
        self.barFrame.layout = QHBoxLayout()
        self.barFrame.layout.setContentsMargins(0,0,0,0)
        self.barFrame.setLayout(self.barFrame.layout)
        self.barFrame.layout.addWidget(self.bar)

        self.mid = QWidget()
        self.mid.layout = QHBoxLayout()
        self.mid.layout.addWidget(self.barFrame)
        self.mid.layout.addWidget(self.cameras)
        self.mid.layout.setContentsMargins(0,0,0,0)
        self.mid.setLayout(self.mid.layout)
        self.frame.layout.addWidget(self.mid)


        self.bar.startstopButt.clicked.connect(self.stopwatch_toggle)
        self.bar.resetButt.clicked.connect(self.stopwatch_reset)
        self.bar.capButt.clicked.connect(self.capture_image)


        self.xyz = Labels()
        self.xFrame = QWidget()
        self.xFrame.layout = QVBoxLayout()
        self.xFrame.layout.setContentsMargins(105,10,50,50)
        self.xFrame.layout.addWidget(self.xyz)
        self.xFrame.setLayout(self.xFrame.layout)
        self.frame.layout.addWidget(self.xFrame)


    def stopwatch_toggle(self):
        self.watch.stopwatch_on = not self.watch.stopwatch_on
        if self.watch.stopwatch_on:
            self.bar.startstopButt.setIcon(QIcon('gui/icons/pause.png'))
            self.bar.startstopButt.setToolTip("Pause")
        else:
            self.bar.startstopButt.setIcon(QIcon('gui/icons/start.png'))
            self.bar.startstopButt.setToolTip("Start")

    def stopwatch_reset(self):
        self.watch.centiseconds = 0
        self.watch.seconds = 0
        self.watch.minutes = 0

        self.watch.stopwatch_label.setText('00:00:00')

        self.watch.stopwatch_on = False
        self.bar.startstopButt.setIcon(QIcon('gui/icons/start.png'))

    def capture_image(self):
        time = datetime.now().strftime(f"%d-%m-%y_%H:%M:%S.%f")[:-4]

        cv2.imwrite("gui/captures/cam1s"+time+".png", self.cameras.cam_1.thread.image)
        cv2.imwrite("gui/captures/cam2s"+time+".png", self.cameras.cam_2.thread.image)

    def keyPressEvent(self, e):
        if not e.isAutoRepeat():
            if e.key() == Qt.Key.Key_W:
                print("fowrad")
            elif e.key() == Qt.Key.Key_A:
                print("left")
            elif e.key() == Qt.Key.Key_S:
                print("back")
            elif e.key() == Qt.Key.Key_D:
                print("right")
            elif e.key() == Qt.Key.Key_Q:
                print("roll left")
            elif e.key() == Qt.Key.Key_E:
                print("roll right")
            elif e.key() == Qt.Key.Key_Control:
                print("down")
            elif e.key() == Qt.Key.Key_Space:
                print("up")
            elif e.key() == Qt.Key.Key_H:
                print("hover")
            elif e.key() == Qt.Key.Key_F:
                print("pitch up")
            elif e.key() == Qt.Key.Key_C:
                print("pitch up")
            elif e.key() == Qt.Key.Key_1:
                print("speed 10%")
            elif e.key() == Qt.Key.Key_2:
                print("speed 20%")
            elif e.key() == Qt.Key.Key_3:
                print("speed 30%")
            elif e.key() == Qt.Key.Key_4:
                print("speed 40%")
            elif e.key() == Qt.Key.Key_5:
                print("speed 50%")
            elif e.key() == Qt.Key.Key_6:
                print("speed 60%")
            elif e.key() == Qt.Key.Key_7:
                print("speed 70%")
            elif e.key() == Qt.Key.Key_8:
                print("speed 80%")
            elif e.key() == Qt.Key.Key_9:
                print("speed 90%")
            elif e.key() == Qt.Key.Key_0:
                print("speed 100%")

    def keyReleaseEvent(self, e):
        if not e.isAutoRepeat():
            if e.key() == Qt.Key.Key_W:
                print("release fowrad")
            elif e.key() == Qt.Key.Key_A:
                print("release left")
            elif e.key() == Qt.Key.Key_S:
                print("release back")
            elif e.key() == Qt.Key.Key_D:
                print("release right")
            elif e.key() == Qt.Key.Key_Q:
                print("release roll left")
            elif e.key() == Qt.Key.Key_E:
                print("release roll right")
            elif e.key() == Qt.Key.Key_Control:
                print("release down")
            elif e.key() == Qt.Key.Key_Space:
                print("release up")
            elif e.key() == Qt.Key.Key_F:
                print("release pitch up")
            elif e.key() == Qt.Key.Key_C:
                print("release pitch up")

            

if __name__ == '__main__':
    try:
        os.mkdir("gui/captures")
    except FileExistsError:
        pass

    app = QApplication([])

    window = MainWindow()
    window.show()

    app.exec()
