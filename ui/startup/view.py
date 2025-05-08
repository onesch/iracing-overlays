from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout
from PyQt6.QtCore import Qt


class StartupOverlayView(QWidget):
    """
    View for the startup overlay containing a 'Hide Menu' button.

    When the button is clicked, it calls the provided callback (on_close_menu_callback).
    """

    def __init__(self, on_close_menu_callback):
        """
        :param on_close_menu_callback: Function to call when the menu is hidden.
        """
        super().__init__()
        self.on_close_menu_callback = on_close_menu_callback

        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setStyleSheet("background-color: rgba(0, 0, 0, 180); color: white;")
        self.setGeometry(300, 300, 300, 100)

        layout = QVBoxLayout()

        self.button = QPushButton("Скрыть меню")
        self.button.clicked.connect(self.hide_menu)

        layout.addWidget(self.button)
        self.setLayout(layout)

    def hide_menu(self):
        """
        Hides the menu and calls the provided callback in the controller.
        """
        self.hide()
        self.on_close_menu_callback()
