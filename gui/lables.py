from PyQt6.QtWidgets import QVBoxLayout, QWidget, QLabel
from PyQt6.QtCore import Qt
from util import *


class Lables(QWidget):
    def __init__(self):
        super().__init__()

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        self.setStyleSheet("""
            QWidget {
                background: %s;
                border-radius: 10px
            } #
        """ % Color.back)

        self.setFixedHeight(150)
        self.setFixedWidth(250)

        self.rickL = QLabel('YAW:')
        self.rawL = QLabel('PITCH:')
        self.yollL = QLabel('ROLL:')


        self.rickL.setStyleSheet("""
            QLabel {
                font: bold 20px;
                color: %s
            } #
        """ % Color.white)

        self.rawL.setStyleSheet("""
            QLabel {
                font: bold 20px;
                color: %s
            } #
        """ % Color.white)

        self.yollL.setStyleSheet("""
            QLabel {
                font: bold 20px;
                color: %s
            } #
        """ % Color.white)
 
        self.layout = QVBoxLayout()        
        self.layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.layout.setSpacing(8)
        self.layout.addWidget(self.rickL)
        self.layout.addWidget(self.rawL)
        self.layout.addWidget(self.yollL)

        self.setLayout(self.layout)