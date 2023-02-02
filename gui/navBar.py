from PyQt6.QtWidgets import QVBoxLayout, QWidget, QLabel, QHBoxLayout
from PyQt6.QtCore import Qt
from util import *
from buttons import Button


class NavBar(QWidget):
    def __init__(self):
        super().__init__()

        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        self.setStyleSheet("""
            QWidget {
                background: %s;
                border-top-right-radius: 10px;
                border-bottom-right-radius: 10px;
            } #
        """ % Color.lobster)

        self.setFixedHeight(300)
        self.setFixedWidth(75)

        self.startstopButt = Button('gui/icons/start.png', 'Start')

        self.resetButt = Button('gui/icons/reset.png', 'Reset')

        self.capButt = Button('gui/icons/capture.png', 'Capture')

        self.bunn = Button('gui/icons/bunny.png', 'Bunny')

        self.lobButt = Button('gui/icons/lobster.png', 'Lobster')


        self.layout = QVBoxLayout()
        self.layout.setSpacing(10)
        self.layout.setAlignment(Qt.AlignmentFlag.AlignVCenter.AlignLeft)

        self.layout.addWidget(self.startstopButt)
        self.layout.addWidget(self.resetButt)
        self.layout.addWidget(self.capButt)
        self.layout.addWidget(self.bunn)
        self.layout.addWidget(self.lobButt)

        self.setLayout(self.layout)