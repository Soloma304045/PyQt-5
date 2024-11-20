import sys
from PyQt6.QtWidgets import QApplication, QDialog
from PyQt6.QtGui import QPainter, QFont, QColor, QPixmap, QIcon
from PyQt6.QtCore import Qt, QRect


class NewspaperWindow(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setWindowTitle("Газета: Использование математики в покере")
        self.setGeometry(100, 100, 800, 540)
        self.setWindowIcon(QIcon("Images/Pepe.jpg"))

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setBrush(QColor(200, 200, 180))
        painter.drawRect(self.rect())

        painter.setPen(Qt.GlobalColor.black)
        painter.setBrush(Qt.GlobalColor.white)
        painter.drawRect(20, 20, 760, 60)
        painter.setFont(QFont("Times New Roman", 28, QFont.Weight.Bold))
        painter.drawText(20, 20, 760, 60, Qt.AlignmentFlag.AlignCenter, "Использование математики в покере")

        columnWidth = 240
        padding = 20
        for i in range(3):
            x = padding + i * (columnWidth + padding)
            painter.drawRect(x, 100, columnWidth, 400)

        painter.setFont(QFont("Arial", 12))
        text1 = (
            "Математика — это важный инструмент, который помогает профессиональным "
            "игрокам в покере принимать решения. Шансы банка и вероятность выигрыша "
            "используются для вычисления выгодности хода."
        )
        rect1 = QRect(30, 110, columnWidth - 20, 150)
        painter.drawText(rect1, Qt.AlignmentFlag.AlignLeft | Qt.TextFlag.TextWordWrap, text1)
        pixmap1 = QPixmap("Images/Cards.jpg")
        painter.drawPixmap(30, 280, 200, 120, pixmap1)

        text2 = (
            "Шансы банка определяются соотношением текущего размера банка к стоимости "
            "следующего хода. Эти данные помогают игрокам лучше управлять своими ставками."
        )
        rect2 = QRect(290, 110, columnWidth - 20, 150)
        painter.drawText(rect2, Qt.AlignmentFlag.AlignLeft | Qt.TextFlag.TextWordWrap, text2)
        pixmap2 = QPixmap("Images/Chips.jpg")
        painter.drawPixmap(290, 280, 200, 120, pixmap2)

        text3 = (
            "Еще одной ключевой концепцией является 'expected value' (ожидаемая выгода). "
            "Каждый ход в покере оценивается с точки зрения потенциальной прибыли."
        )
        rect3 = QRect(550, 110, columnWidth - 20, 150)
        painter.drawText(rect3, Qt.AlignmentFlag.AlignLeft | Qt.TextFlag.TextWordWrap, text3)
        pixmap3 = QPixmap("Images/Table.jpg")
        painter.drawPixmap(550, 280, 200, 120, pixmap3)

        painter.end()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NewspaperWindow()
    window.show()
    sys.exit(app.exec())
