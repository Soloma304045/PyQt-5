import sys
from PyQt6.QtWidgets import QApplication, QDialog
from PyQt6.QtGui import QPainter, QColor, QPen, QBrush, QFont, QIcon
from PyQt6.QtCore import Qt, QRect

class PaintWindow(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setWindowIcon(QIcon("Images/Pepe.jpg"))
        self.setWindowTitle("Картина")
        self.setGeometry(100, 100, 1200, 600)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setBrush(QBrush(QColor(255, 255, 255), Qt.BrushStyle.SolidPattern))
        painter.drawRect(self.rect())
        painter.setPen(QPen(QColor(0, 0, 0), 8))
        painter.drawLine(200, 0, 200, 600)
        painter.drawLine(400, 0, 400, 600)
        painter.drawLine(0, 200, 600, 200)
        painter.drawLine(0, 400, 600, 400)
        painter.setBrush(QBrush(QColor(255, 0, 0), Qt.BrushStyle.SolidPattern))
        painter.drawRect(QRect(200, 0, 400, 400))
        painter.setBrush(QBrush(QColor(0, 0, 255), Qt.BrushStyle.SolidPattern))
        painter.drawRect(QRect(0, 400, 200, 200))
        painter.setBrush(QBrush(QColor(255, 255, 0), Qt.BrushStyle.SolidPattern))
        painter.drawRect(QRect(525, 525, 75, 75))
        painter.setFont(QFont("Arial", 14))
        painter.setPen(QPen(QColor(0, 0, 0), 1))
        painter.drawText(700, 100, '"Композиция с красным, синим и желтым"')
        painter.drawText(800, 150, 'Пит Мордриан')
        painter.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PaintWindow()
    window.show()
    sys.exit(app.exec())
