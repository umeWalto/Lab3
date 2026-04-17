import sys
from PyQt6.QtWidgets import QApplication, QWidget

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Круги на форме")
        self.setGeometry(100, 100, 800, 600)

class CCircle:
    def __init__(self, x, y, radius=30):
        self._x = x
        self._y = y
        self._radius = radius
        self._selected = False

    def contains(self, x, y):
        dx = x - self._x
        dy = y - self._y
        return dx * dx + dy * dy <= self._radius * self._radius

    def set_selected(self, value: bool):
        self._selected = value

    def is_selected(self):
        return self._selected

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())