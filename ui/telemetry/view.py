from PyQt6.QtWidgets import QWidget, QLabel
from PyQt6.QtGui import QFont, QPainter, QColor, QPen
from PyQt6.QtCore import Qt
from ui.telemetry.widgets.bars import ThrottleBar, BrakeBar
from ui.styles import (
    COLOR_THROTTLE,
    COLOR_BRAKE,
    COLOR_BACKGROUND,
    GRAPH_WIDTH,
    GRAPH_HEIGHT,
    GRAPH_LEFT,
    GRAPH_TOP,
    GRAPH_LINE_WIDTH,
    STYLE_LABEL,
)

class TelemetryOverlayView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setGeometry(100, 100, 500, 200)
        self.visible_overlay = True

        self.speed_label = QLabel(self)
        self.speed_label.setGeometry(345, 10, 40, 30)
        self.speed_label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        self.speed_label.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        self.speed_label.setStyleSheet(STYLE_LABEL)

        self.throttle_bar = ThrottleBar(self)
        self.brake_bar = BrakeBar(self)

        self.throttle_label = QLabel(self)
        self.throttle_label.setGeometry(385, 10, 20, 30)
        self.throttle_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.throttle_label.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        self.throttle_label.setStyleSheet(STYLE_LABEL)

        self.brake_label = QLabel(self)
        self.brake_label.setGeometry(405, 10, 20, 30)
        self.brake_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.brake_label.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        self.brake_label.setStyleSheet(STYLE_LABEL)

    def set_interface_visible(self, visible: bool):
        """Метод для изменения видимости интерфейса"""
        self.visible_overlay = visible
        self.speed_label.setVisible(visible)
        self.throttle_label.setVisible(visible)
        self.brake_label.setVisible(visible)
        self.throttle_bar.setVisible(visible)
        self.brake_bar.setVisible(visible)
        self.repaint()

    def paint_history(self, event, history):
        """Рисование истории на графиках"""
        if len(history) < 2:
            return

        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setBrush(QColor(*COLOR_BACKGROUND))
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawRect(GRAPH_LEFT, GRAPH_TOP, GRAPH_WIDTH, GRAPH_HEIGHT)

        pen = QPen(QColor(*COLOR_THROTTLE))
        pen.setWidth(GRAPH_LINE_WIDTH)
        painter.setPen(pen)
        self.draw_history(painter, history, GRAPH_LEFT, GRAPH_TOP, 0)

        pen.setColor(QColor(*COLOR_BRAKE))
        painter.setPen(pen)
        self.draw_history(painter, history, GRAPH_LEFT, GRAPH_TOP, 1)

    def draw_history(self, painter, history, x_offset, y_offset, index):
        """Отображение истории на графиках"""
        width = 300
        height = 80
        step = width / len(history)
        scale = height / 100

        for i in range(1, len(history)):
            y1 = y_offset + (100 - history[i - 1][index]) * scale
            y2 = y_offset + (100 - history[i][index]) * scale
            x1 = x_offset + (i - 1) * step
            x2 = x_offset + i * step
            painter.drawLine(int(x1), int(y1), int(x2), int(y2))
