from PyQt6.QtWidgets import QPushButton
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt, QSize

class Button(QPushButton):
    def __init__(self, icon, tip):
        super().__init__()

        self.setStyleSheet("""
            QPushButton {
                background: rgb(229,195,209);
                border-radius: 5px
            }
            QPushButton:hover {
                background: rgb(157,67,103)
            }
        """)

        self.setIcon(QIcon(icon))
        self.setIconSize(QSize(45,45))

        self.setToolTip(tip)