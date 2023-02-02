from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget, QLabel
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt, QTimer
from util import *

from buttons import Button

# class StopwatchBar(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

#         self.setStyleSheet("""
#             QWidget {
#                 background: %s;
#                 border-radius: 10px
#             } #
#         """ % Color.lobster)

#         self.setFixedHeight(100)
#         self.setFixedWidth(70)

#         self.startstopButt = Button('gui/icons/start.png', 'Start')
#         self.startstopButt.clicked.connect(self.startstop)

#         self.resetButt = Button('gui/icons/reset.png', 'Reset')
#         self.resetButt.clicked.connect(self.reset)

#         self.layout = QVBoxLayout()
#         self.layout.setSpacing(10)

#         self.layout.addWidget(self.startstopButt)
#         self.layout.addWidget(self.resetButt)

#         self.setLayout(self.layout)


    # def startstop(self):
    #     if self.parent.stopwatch.stopwatch_on:
    #         self.parent.stopwatch.stopwatch_on = False

    #         self.startstop_button.setIcon(QIcon('gui/icons/play_icon.png'))
    #         self.startstop_button.setToolTip('Resume')

    #     else:
    #         if self.quickstart_button.isEnabled():
    #             self.quickstart_button.setDisabled(True)

    #         self.startstop_button.setIcon(QIcon('gui/icons/pause_icon.png'))
    #         self.startstop_button.setToolTip('Pause')

    #         self.parent.stopwatch.stopwatch_on = True


    # def reset(self):
    #     self.parent.stopwatch.stopwatch_on = False

    #     self.parent.stopwatch.centiseconds = 0
    #     self.parent.stopwatch.seconds = 0
    #     self.parent.stopwatch.minutes = 0

    #     self.parent.stopwatch.stopwatch_label.setText('00:00.00')

    #     self.startstop_button.setIcon(QIcon('gui/icons/play_icon.png'))
    #     self.startstop_button.setToolTip('Start')

    #     if not self.parent.capture_control.recording:
    #         self.parent.stopwatch_control.quickstart_button.setDisabled(False)


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


    def startstop(self):
        if self.parent.stopwatch.stopwatch_on:
            self.parent.stopwatch.stopwatch_on = False
            
            self.startstop_button.setToolTip('Resume')

        else:
            if self.quickstart_button.isEnabled():
                self.quickstart_button.setDisabled(True)

            self.startstop_button.setToolTip('Pause')

            self.parent.stopwatch.stopwatch_on = True


    def reset(self):
        # self.parent.stopwatch.sto = False

        self.centiseconds = 0
        self.seconds = 0
        self.minutes = 0

        self.stopwatch_label.setText('00:00:00')

        # self.startstop_button.setToolTip('Start')

        # if not self.parent.capture_control.recording:
        #     self.parent.stopwatch_control.quickstart_button.setDisabled(False)