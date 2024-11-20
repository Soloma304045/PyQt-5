import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt6.QtGui import QIcon, QGuiApplication
from PyQt6.QtCore import Qt
from PaintWindow import PaintWindow # type: ignore
from NewspaperWindow import NewspaperWindow # type: ignore
from SceneWindow import SceneWindow # type: ignore

class MainWindow(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.setWindowTitle("Чайдаков Иван ИТД-21")
        self.setWindowIcon(QIcon("Images/Pepe.jpg"))

        screen = QGuiApplication.primaryScreen()
        siz = screen.size()
        window_width, window_height = 300, 200
        self.setGeometry(
            (siz.width() - window_width) // 2,
            (siz.height() - window_height) // 2,
            window_width,
            window_height
        )

        label = QLabel('''
            <center>
                <h1>Лабораторная работа №5</h1><br>
                <b>Работа с графикой. Графическая сцена.</b><br>
                Выполнил студент группы <span style="color: red;">ИТД-21
                <h2>Чайдаков Иван Миронович</h2></span>
            </center>
        ''')
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        button1 = QPushButton("Картина", self)
        button1.setToolTip("Перерисовка известной картины")
        button1.clicked.connect(self.openPaint) 

        button2 = QPushButton("Газета", self)
        button2.setToolTip("Газетная статья")
        button2.clicked.connect(self.openNews) 

        button3 = QPushButton("Сцена", self)
        button3.setToolTip("Графическая сцена")
        button3.clicked.connect(self.openScene) 

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)
        self.setLayout(layout)

    def openPaint(self):
        self.paintWindow = PaintWindow(self)
        self.paintWindow.show()

    def openNews(self):
        self.newsWindow = NewspaperWindow(self)
        self.newsWindow.show()

    def openScene(self):
        self.sceneWindow = SceneWindow(self)
        self.sceneWindow.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
