from PyQt6.QtCore import QTimer, Qt
from services.telemetry_updater import TelemetryUpdater
from ui.telemetry.view import TelemetryOverlayView


class TelemetryOverlayController:
    def __init__(self, ir):
        self.view = TelemetryOverlayView()

        self.old_pos = None

        self.ir = ir
        self.telemetry_updater = TelemetryUpdater(ir, self.view, self)

        self.timer = QTimer(self.view)
        self.timer.timeout.connect(self.telemetry_updater.update_telemetry)
        self.timer.start(100)

        self._connect_events()

    def update_interface_visibility(self, is_on_track):
        """Обновление видимости интерфейса в зависимости от состояния"""
        self.view.set_interface_visible(is_on_track)

    def save_window_position(self):
        """Сохраняем позицию окна"""
        self.telemetry_updater.save_window_position()

    def _connect_events(self):
        """
        Подключает пользовательские обработчики событий мыши и перерисовки к виджету.

        Этот метод переназначает стандартные события `mousePressEvent`, 
        `mouseMoveEvent`, `mouseReleaseEvent` и `paintEvent` у объекта `view` 
        на методы текущего класса, чтобы обеспечить пользовательское поведение 
        при взаимодействии с интерфейсом.
        """
        self.view.mousePressEvent = self.mousePressEvent
        self.view.mouseMoveEvent = self.mouseMoveEvent
        self.view.mouseReleaseEvent = self.mouseReleaseEvent
        self.view.paintEvent = self.paintEvent

    def paintEvent(self, event):
        """Отрисовка истории на графиках"""
        if not self.view.visible_overlay:
            return
        self.view.paint_history(event, self.telemetry_updater.get_history())

    def mousePressEvent(self, event):
        """Начало перетаскивания окна"""
        if event.button() == Qt.MouseButton.LeftButton:
            self.old_pos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        """Перетаскивание окна"""
        if self.old_pos and event.buttons() == Qt.MouseButton.LeftButton:
            delta = event.globalPosition().toPoint() - self.old_pos
            self.view.move(self.view.pos() + delta)
            self.old_pos = event.globalPosition().toPoint()

    def mouseReleaseEvent(self, event):
        """Окончание перетаскивания и сохранение позиции окна"""
        self.old_pos = None
        self.telemetry_updater.save_window_position()
