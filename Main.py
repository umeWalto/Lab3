import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QPainter, QColor, QPen
from PyQt6.QtCore import Qt

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

def draw(self, painter: QPainter):
    if self._selected:
        painter.setBrush(QColor(255, 100, 100))
    else:
        painter.setBrush(QColor(100, 200, 255))

    painter.setPen(QPen(Qt.GlobalColor.black, 2))
    painter.drawEllipse(
        self._x - self._radius,
        self._y - self._radius,
        self._radius * 2,
        self._radius * 2
    )

class MyStorage:
    def __init__(self):
        self._data = []
        self._index = 0

    def add(self, obj):
        self._data.append(obj)

    def first(self):
        self._index = 0

    def next(self):
        self._index += 1

    def eol(self):
        return self._index >= len(self._data)

    def get_object(self):
        return self._data[self._index]

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())