import json
from settings.constants import SETTINGS_FILE


class TelemetryUpdater:
    def __init__(self, ir, view, controller):
        self.ir = ir
        self.view = view
        self.controller = controller
        self.history = []
        self.max_history = 100


    def update_telemetry(self):
        if self.ir.is_initialized and self.ir.is_connected:
            is_on_track = self.ir['IsOnTrack']
            self.controller.update_interface_visibility(is_on_track)

            if not is_on_track:
                return

            speed_kmh = self.ir['Speed'] * 3.6
            throttle = self.ir['Throttle'] * 100
            brake = self.ir['Brake'] * 100

            self.view.speed_label.setText(f"{int(speed_kmh)}")
            self.view.throttle_label.setText(f"{int(throttle)}")
            self.view.brake_label.setText(f"{int(brake)}")

            self.history.append((throttle, brake))
            if len(self.history) > self.max_history:
                self.history.pop(0)

            self.view.throttle_bar.setValue(int(throttle))
            self.view.brake_bar.setValue(int(brake))
            self.view.update()


    def save_window_position(self):
        pos = self.controller.view.pos()
        data = {"x": pos.x(), "y": pos.y()}
        with open(SETTINGS_FILE, "w") as f:
            json.dump(data, f)


    def load_window_position(self):
        try:
            with open(SETTINGS_FILE, "r") as f:
                data = json.load(f)
                x, y = data.get("x", 100), data.get("y", 100)
                self.view.move(x, y)
        except (FileNotFoundError, json.JSONDecodeError):
            pass


    def get_history(self):
        return self.history
