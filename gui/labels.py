from PyQt6.QtWidgets import QVBoxLayout, QWidget, QLabel
from PyQt6.QtCore import Qt
from util import *


class Labels(QWidget):
    def __init__(self):
        super().__init__()

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        self.setStyleSheet("""
            QWidget {
                background: %s;
                border-radius: 10px
            }
        """ % Color.back)

        self.setFixedHeight(150)
        self.setFixedWidth(250)

        self.yaw = QLabel('YAW:')
        self.pitch = QLabel('PITCH:')
        self.roll = QLabel('ROLL:')


        self.yaw.setStyleSheet("""
            QLabel {
                font: bold 20px;
                color: %s
            } #
        """ % Color.white)

        self.pitch.setStyleSheet("""
            QLabel {
                font: bold 20px;
                color: %s
            } #
        """ % Color.white)

        self.roll.setStyleSheet("""
            QLabel {
                font: bold 20px;
                color: %s
            } #
        """ % Color.white)
 
        self.layout = QVBoxLayout()        
        self.layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.layout.setSpacing(8)
        self.layout.addWidget(self.yaw)
        self.layout.addWidget(self.pitch)
        self.layout.addWidget(self.roll)

        self.setLayout(self.layout)