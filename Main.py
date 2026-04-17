import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QPainter, QColor, QPen
from PyQt6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Круги на форме")
        self.setGeometry(100, 100, 800, 600)

        self.storage = MyStorage()

        def paintEvent(self, event):
            painter = QPainter(self)
            self.storage.draw_all(painter)
        
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            modifiers = QApplication.keyboardModifiers()
            ctrl_pressed = bool(modifiers & Qt.KeyboardModifier.ControlModifier)

            self.storage.handle_click(
                int(event.position().x()),
                int(event.position().y()),
                ctrl_pressed
            )
            self.update()

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
    
    def draw_all(self, painter: QPainter):
        self.first()
        while not self.eol():
            obj = self.get_object()
            obj.draw(painter)
            self.next()

    def handle_click(self, x, y, ctrl_pressed):
        clicked = []

        self.first()
        while not self.eol():
            obj = self.get_object()
            if obj.contains(x, y):
                clicked.append(obj)
            self.next()

        if not ctrl_pressed:
            self.clear_selection()

        if clicked:
            for obj in clicked:
                if ctrl_pressed:
                    obj.set_selected(not obj.is_selected())
                else:
                    obj.set_selected(True)
        else:
            self.add(CCircle(x, y))
        
    def clear_selection(self):
        self.first()
        while not self.eol():
            self.get_object().set_selected(False)
            self.next()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())