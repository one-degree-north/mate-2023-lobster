from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon

import os
import cv2
from datetime import datetime

from gui.camera import CameraTab
from gui.util import *
from gui.stopwatch import Stopwatch
from gui.labels import Labels
from gui.navbar import Navbar
from comms import Comms


class MainWindow(QMainWindow):
    def __init__(self, comms: Comms):
        super().__init__()

        self.comms = comms

        self.setStyleSheet("""
            QMainWindow {
                background: %s;
            }
        """ % Color.mardi_gras)
 
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
        
        self.bar = Navbar()
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
        if not self.comms or e.isAutoRepeat():
            return
        
        match e.key():
            case Qt.Key.Key_W:
                self.comms.forward()
            case Qt.Key.Key_A:
                self.comms.yaw_left()
            case Qt.Key.Key_S:
                self.comms.backward()
            case Qt.Key.Key_D:
                self.comms.yaw_right()
            case Qt.Key.Key_Q:
                self.comms.roll_left()
            case Qt.Key.Key_E:
                self.comms.roll_right()
            case Qt.Key.Key_Control:
                self.comms.down()
            case Qt.Key.Key_Space:
                self.comms.up()
            case Qt.Key.Key_F:
                self.comms.pitch_up()
            case Qt.Key.Key_C:
                self.comms.pitch_down()
            case Qt.Key.Key_H:
                print("hover")
            case Qt.Key.Key_1:
                self.comms.set_speed(1)
            case Qt.Key.Key_2:
                self.comms.set_speed(2)
            case Qt.Key.Key_3:
                self.comms.set_speed(3)
            case Qt.Key.Key_4:
                self.comms.set_speed(4)
            case Qt.Key.Key_5:
                self.comms.set_speed(5)
            case Qt.Key.Key_0:
                self.comms.stop_thrusters()

    def keyReleaseEvent(self, e):
        if not self.comms or e.isAutoRepeat():
            return
        
        match e.key():
            case Qt.Key.Key_W:
                self.comms.stop_thrusters(side=True)
            case Qt.Key.Key_A:
                self.comms.stop_thrusters(side=True)
            case Qt.Key.Key_S:
                self.comms.stop_thrusters(side=True)
            case Qt.Key.Key_D:
                self.comms.stop_thrusters(side=True)
            case Qt.Key.Key_Q:
                self.comms.stop_thrusters(vertical=True)
            case Qt.Key.Key_E:
                self.comms.stop_thrusters(vertical=True)
            case Qt.Key.Key_Control:
                self.comms.stop_thrusters(vertical=True)
            case Qt.Key.Key_Space:
                self.comms.stop_thrusters(vertical=True)
            case Qt.Key.Key_F:
                self.comms.stop_thrusters(vertical=True)
            case Qt.Key.Key_C:
                self.comms.stop_thrusters(vertical=True)

            

if __name__ == '__main__':
    try:
        os.mkdir("gui/captures")
    except FileExistsError:
        pass

    app = QApplication([])

    window = MainWindow()
    window.show()

    app.exec()
