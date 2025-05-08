from typing import List
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
        """
        Initializes the telemetry overlay.

        Creates a frameless, transparent window and places the following control elements on it:
        - speed label,
        - throttle and brake indicators (progress bars),
        - labels for throttle and brake.
        Sets the basic geometry and styles.
        """
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
        """
        Controls the visibility of the overlay interface elements.

        Parameters:
        visible (bool): If True — all elements are visible, otherwise they are hidden.
        """
        self.visible_overlay = visible
        self.speed_label.setVisible(visible)
        self.throttle_label.setVisible(visible)
        self.brake_label.setVisible(visible)
        self.throttle_bar.setVisible(visible)
        self.brake_bar.setVisible(visible)
        self.repaint()


    def render_graphs(self, event, history: List[List[int]]):
        """
        Renders the graphs for throttle and brake history.

        Parameters:
        event (QPaintEvent): The repaint event (not used directly).
        history (List[List[int]]): A list of history containing throttle and brake values.
                                   Each element is expected to be a list of two numbers [throttle, brake].
        """
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
        self.draw_graph_line(painter, history, GRAPH_LEFT, GRAPH_TOP, 0)

        pen.setColor(QColor(*COLOR_BRAKE))
        painter.setPen(pen)
        self.draw_graph_line(painter, history, GRAPH_LEFT, GRAPH_TOP, 1)


    def draw_graph_line(self, painter, history: List[List[int]], x_offset: int, y_offset: int, index: int):
        """
        Draws a graph line for the given data index (throttle or brake).

        Parameters:
        painter (QPainter): The object used for painting.
        history (List[List[int]]): A list of history containing throttle and brake values.
        x_offset (int): The x-axis offset where the drawing should start.
        y_offset (int): The y-axis offset where the drawing should start.
        index (int): The index of the data to draw (0 for throttle, 1 for brake).
        """
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
