from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt
import sys
import random

class CircleDrawer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Случайные окружности")
        self.setGeometry(100, 100, 400, 400)
        self.circles = []  # список для хранения окружностей

        self.button = QPushButton("Нарисовать окружность", self)
        self.button.setGeometry(150, 350, 150, 30)
        self.button.clicked.connect(self.draw_circle)

    def draw_circle(self):
        diameter = random.randint(10, 100)
        x = random.randint(0, self.width() - diameter)
        y = random.randint(0, self.height() - diameter)
        color = self.random_color()
        self.circles.append((x, y, diameter, color))  # добавляем информацию о новой окружности в список
        self.repaint()

    def paintEvent(self, event):
        painter = QPainter(self)
        for circle in self.circles:
            x, y, diameter, color = circle
            painter.setBrush(color)
            painter.drawEllipse(x, y, diameter, diameter)

    def random_color(self):
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        return QColor(red, green, blue)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CircleDrawer()
    window.show()
    sys.exit(app.exec_())
