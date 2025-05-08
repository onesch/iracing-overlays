from PyQt6.QtCore import QTimer
from ui.startup.view import StartupOverlayView
from ui.telemetry.controller import TelemetryOverlayController
import irsdk
from settings.constants import IRACING_CHECK_INTERVAL_MS


class StartupOverlayController:
    """
    Controller for the startup overlay. Responsible for:
    - displaying the startup menu,
    - monitoring the iRacing connection,
    - launching the telemetry overlay when iRacing is active.
    """

    def __init__(self):
        """
        Initializes the controller:
        - creates and displays the startup overlay,
        - starts watching for an iRacing connection.
        """
        self.ir = irsdk.IRSDK()
        self.controller = None

        self.setup_view()
        self.start_iracing_watch()


    def setup_view(self):
        """
        Initializes and shows the startup overlay view.
        """
        self.view = StartupOverlayView(self.hide_menu)
        self.view.show()


    def hide_menu(self):
        """
        Handles the 'hide menu' action.
        Called when the user clicks the 'Hide Menu' button in the view.
        """
        self.view.hide()


    def start_iracing_watch(self):
        """
        Starts a timer that periodically checks for an active iRacing session.
        If iRacing is running and connected, the telemetry overlay is launched.
        """
        self.timer = QTimer()
        self.timer.timeout.connect(self.check_iracing)
        self.timer.start(IRACING_CHECK_INTERVAL_MS)


    def check_iracing(self):
        """
        Periodically checks if iRacing is initialized and connected.
        If so, creates the telemetry controller and displays its view.
        """
        if not self.ir.is_initialized:
            self.ir.startup()

        if self.ir.is_initialized and self.ir.is_connected:
            if self.controller is None:
                self.controller = TelemetryOverlayController(self.ir)
                self.controller.view.show()
                self.timer.stop()
