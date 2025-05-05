from PyQt6.QtCore import QTimer
from ui.startup.view import StartupOverlayWiew
from ui.telemetry.controller import TelemetryOverlayController
import irsdk
from settings.constants import IRACING_CHECK_INTERVAL_MS


class StartupOverlayController:
    """
    Контроллер стартового меню, отвечающий за:
    - отображение стартового окна (меню),
    - отслеживание подключения к iRacing,
    - запуск контроллера телеметрии при обнаружении соединения.
    """

    def __init__(self):
        """
        Инициализирует контроллер:
        - запускает стартовое меню (view),
        - начинает отслеживание подключения к iRacing.
        """
        self.ir = irsdk.IRSDK()
        self.controller = None

        self.view = StartupOverlayWiew(self.hide_menu)
        self.view.show()

        self.start_iracing_watch()

    def hide_menu(self):
        """
        Обработчик скрытия меню.
        Вызывается из представления при клике на кнопку "Скрыть меню".
        """
        self.view.hide()

    def start_iracing_watch(self):
        """
        Запускает периодическую проверку состояния iRacing.
        Если iRacing запущен и соединение установлено — создаёт телеметрию.
        """
        self.timer = QTimer()
        self.timer.timeout.connect(self.check_iracing)
        self.timer.start(IRACING_CHECK_INTERVAL_MS)

    def check_iracing(self):
        """
        Проверка инициализации и соединения с iRacing.
        При успешном соединении запускает контроллер телеметрии.
        """
        self.ir.startup()
        if self.ir.is_initialized and self.ir.is_connected:
            if self.controller is None:
                self.controller = TelemetryOverlayController(self.ir)
                self.controller.view.show()
