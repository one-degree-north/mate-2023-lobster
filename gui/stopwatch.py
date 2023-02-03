from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget, QLabel
from PyQt6.QtCore import Qt, QTimer
from .util import *

class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        self.setStyleSheet("""
            QWidget {
                background: %s;
                border-radius: 10px
            } #
        """ % Color.lobster)
        
        self.setFixedHeight(50)
        self.setFixedWidth(170)

        self.stopwatch_label = QLabel('00:00:00')
        self.stopwatch_label.setStyleSheet("""
            QLabel {
                font: bold 30px;
                color: %s
            } #
        """ % Color.white)

        self.centiseconds = 0
        self.seconds = 0
        self.minutes = 0

        self.stopwatch_on = False

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_stopwatch)
        self.timer.start(10)

        self.layout = QHBoxLayout()
        self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.setSpacing(10)

        self.layout.addWidget(self.stopwatch_label)

        self.setLayout(self.layout)


    def update_stopwatch(self):
        if not self.stopwatch_on:
            return

        self.total_centiseconds = self.centiseconds + (self.seconds * 100) + (self.minutes * 6000) + 1

        self.seconds, self.centiseconds = divmod(self.total_centiseconds, 100)
        self.minutes, self.seconds = divmod(self.seconds, 60)

        self.stopwatch_label.setText(f'{self.minutes:02d}:{self.seconds:02d}:{self.centiseconds:02d}')