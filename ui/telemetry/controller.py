from PyQt6.QtCore import QTimer, Qt
from services.telemetry_updater import TelemetryUpdater
from ui.telemetry.view import TelemetryOverlayView


class TelemetryOverlayController:
    def __init__(self, ir):
        """
        Initializes the telemetry overlay controller.

        Parameters:
        ir: An object providing access to telemetry data (likely an iRacing SDK wrapper).

        Creates the view and telemetry updater, sets up a timer to periodically update
        telemetry data, and connects custom event handlers for user interaction.
        """
        self.view = TelemetryOverlayView()

        self.old_pos = None

        self.ir = ir
        self.telemetry_updater = TelemetryUpdater(ir, self.view, self)
        self.telemetry_updater.load_window_position()

        self.timer = QTimer(self.view)
        self.timer.timeout.connect(self.telemetry_updater.update_telemetry)
        self.timer.start(100)

        self._connect_events()


    def update_interface_visibility(self, is_on_track: bool):
        """
        Updates the visibility of the telemetry overlay based on whether the car is on track.

        Parameters:
        is_on_track (bool): If True, the overlay is shown; otherwise, it is hidden.
        """
        self.view.set_interface_visible(is_on_track)


    def save_window_position(self):
        """
        Saves the current position of the telemetry overlay window.

        This is typically called when the user finishes moving the window.
        """
        self.telemetry_updater.save_window_position()


    def _connect_events(self):
        """
        Connects mouse and paint events from the view to controller methods.

        Overrides default QWidget event handlers with custom logic for:
        - mouse press (start dragging)
        - mouse move (dragging)
        - mouse release (stop dragging and save position)
        - paint event (drawing throttle/brake history)
        """
        self.view.mousePressEvent = self.mousePressEvent
        self.view.mouseMoveEvent = self.mouseMoveEvent
        self.view.mouseReleaseEvent = self.mouseReleaseEvent
        self.view.paintEvent = self.paintEvent


    def paintEvent(self, event):
        """
        Paints the telemetry graphs onto the overlay.

        Parameters:
        event (QPaintEvent): The paint event triggered by the view.
        """
        if not self.view.visible_overlay:
            return
        self.view.render_graphs(event, self.telemetry_updater.get_history())


    def mousePressEvent(self, event):
        """
        Handles the beginning of a window drag.

        Parameters:
        event (QMouseEvent): The mouse press event.
        """
        if event.button() == Qt.MouseButton.LeftButton:
            self.old_pos = event.globalPosition().toPoint()


    def mouseMoveEvent(self, event):
        """
        Handles the dragging of the telemetry window.

        Parameters:
        event (QMouseEvent): The mouse move event.
        """
        if self.old_pos and event.buttons() == Qt.MouseButton.LeftButton:
            delta = event.globalPosition().toPoint() - self.old_pos
            self.view.move(self.view.pos() + delta)
            self.old_pos = event.globalPosition().toPoint()


    def mouseReleaseEvent(self, event):
        """
        Handles the end of a window drag and saves the window's new position.

        Parameters:
        event (QMouseEvent): The mouse release event.
        """
        self.old_pos = None
        self.telemetry_updater.save_window_position()
