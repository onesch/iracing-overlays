import sys
from PyQt6.QtWidgets import QApplication
from ui.startup.controller import StartupOverlayController

if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = StartupOverlayController()
    controller.view.show()
    sys.exit(app.exec())
