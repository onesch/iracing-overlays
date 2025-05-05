from PyQt6.QtWidgets import QProgressBar
from PyQt6.QtCore import Qt
from ui.styles import STYLE_THROTTLE_BAR, STYLE_BRAKE_BAR


class ThrottleBar(QProgressBar):
    def __init__(self, parent):
        super().__init__(parent)
        self.setGeometry(395, 40, 10, 80)
        self.setOrientation(Qt.Orientation.Vertical)
        self.setTextVisible(False)
        self.setStyleSheet(STYLE_THROTTLE_BAR)

class BrakeBar(QProgressBar):
    def __init__(self, parent):
        super().__init__(parent)
        self.setGeometry(405, 40, 10, 80)
        self.setOrientation(Qt.Orientation.Vertical)
        self.setTextVisible(False)
        self.setStyleSheet(STYLE_BRAKE_BAR)
