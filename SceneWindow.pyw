from PyQt6.QtWidgets import (
    QApplication, QDialog, QGraphicsScene, QGraphicsView, 
    QGraphicsRectItem, QPushButton, QVBoxLayout, 
    QWidget, QHBoxLayout, QGraphicsItem, QColorDialog, QGraphicsDropShadowEffect
)
from PyQt6.QtCore import Qt, QRectF
from PyQt6.QtGui import QColor, QPen

class CustomItem(QGraphicsRectItem):
    def __init__(self, rect, color, movable=False):
        super().__init__(rect)
        self.setBrush(color)
        self.setFlags(QGraphicsItem.GraphicsItemFlag.ItemIsSelectable)
        self.movable = movable
        if movable:
            self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
        else:
            self.setAcceptHoverEvents(True)

    def hoverEnterEvent(self, event):
        if not self.movable:
            QApplication.setOverrideCursor(Qt.CursorShape.OpenHandCursor)

    def hoverLeaveEvent(self, event):
        if not self.movable:
            QApplication.restoreOverrideCursor()

    def mousePressEvent(self, event):
        if not self.movable and event.button() == Qt.MouseButton.LeftButton:
            color = QColorDialog.getColor()
            if color.isValid():
                self.setBrush(color)
        super().mousePressEvent(event)


class SceneWindow(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setWindowTitle("Графическая сцена")

        mainWidget = QWidget()
        mainLayout = QHBoxLayout(mainWidget)
        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)
        self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.view.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.view.setSceneRect(0, 0, 800, 600)

        controlLayout = QVBoxLayout()
        controlLayout.addWidget(self.createButton("Изменить размер сцены", self.changeSceneSize))
        controlLayout.addWidget(self.createButton("Переместиться к элементу", self.moveToItem))
        controlLayout.addWidget(self.createButton("Повернуть элемент", self.rotateItem))
        controlLayout.addWidget(self.createButton("Изменить размер элемента", self.resizeItem))
        controlLayout.addWidget(self.createButton("Сделать элемент видимым/невидимым", self.toggleVisibility))
        controlLayout.addWidget(self.createButton("Переместить элемент", self.moveItem))
        controlLayout.addWidget(self.createButton("Запретить/разрешить перемещение", self.toggleMovable))
        controlLayout.addWidget(self.createButton("Сгруппировать/разгруппировать элементы", self.groupItems))#
        controlLayout.addWidget(self.createButton("Добавить/убрать эффект1", self.addEffect1))
        controlLayout.addWidget(self.createButton("Добавить/убрать эффект2", self.addEffect2))
        controlLayout.addStretch()
        mainLayout.addWidget(self.view)
        mainLayout.addLayout(controlLayout)
        self.setLayout(mainLayout)
        self.createItems()

    def createButton(self, text, callback):
        button = QPushButton(text)
        button.clicked.connect(callback)
        return button

    def createItems(self):
        colors = [Qt.GlobalColor.red, Qt.GlobalColor.green, Qt.GlobalColor.blue,
                  Qt.GlobalColor.yellow, Qt.GlobalColor.magenta, Qt.GlobalColor.cyan,
                  Qt.GlobalColor.gray, Qt.GlobalColor.darkRed, Qt.GlobalColor.darkGreen,
                  Qt.GlobalColor.darkBlue]

        for i in range(5):
            item = CustomItem(QRectF(50 + i * 60, 50, 50, 50), QColor(colors[i]), movable=False)
            self.scene.addItem(item)

        for i in range(5, 10):
            item = CustomItem(QRectF(50 + (i - 5) * 60, 150, 50, 50), QColor(colors[i]), movable=True)
            self.scene.addItem(item)

    def changeSceneSize(self):
        self.scene.setSceneRect(0, 0, 1200, 800)
        self.view.setSceneRect(self.scene.sceneRect())

    def moveToItem(self):
        items = self.scene.selectedItems()
        if items:
            target_item = items[0]
            self.view.centerOn(target_item)

    def rotateItem(self):
        items = self.scene.selectedItems()
        if items:
            targetItem = items[0]
            center = targetItem.boundingRect().center()
            targetItem.setTransformOriginPoint(center)
            targetItem.setRotation(targetItem.rotation() + 45)

    def resizeItem(self):
        items = self.scene.selectedItems()
        if items:
            targetItem = items[0]
            rect = targetItem.rect()
            rect.setWidth(rect.width() + 10)
            rect.setHeight(rect.height() + 10)
            targetItem.setRect(rect)

    def toggleVisibility(self):
        items = self.scene.selectedItems()
        if items:
            for item in items:
                item.setVisible(False)
        else:
            for item in self.scene.items():
                item.setVisible(True)

    def moveItem(self):
        items = self.scene.selectedItems()
        if items:
            targetItem = items[0]
            targetItem.setPos(targetItem.pos().x() + 10, targetItem.pos().y())

    def toggleMovable(self):
        items = self.scene.selectedItems()
        if items:
            target_item = items[0]
            is_movable = target_item.flags() & QGraphicsItem.GraphicsItemFlag.ItemIsMovable
            if is_movable:
                target_item.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable, False)
            else:
                target_item.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable, True)

    def groupItems(self):
        self.close()
        self.newWindow = SceneWindow()
        self.newWindow.show()

    def addEffect1(self):
        items = self.scene.selectedItems()
        if items:
            targetItem = items[0]
            if targetItem.graphicsEffect():
                targetItem.setGraphicsEffect(None)
            else:
                effect = QGraphicsDropShadowEffect()
                effect.setBlurRadius(10)
                effect.setColor(QColor(Qt.GlobalColor.black))
                targetItem.setGraphicsEffect(effect)

    def addEffect2(self):
        items = self.scene.selectedItems()
        if items:
            targetItem = items[0]
            pen = targetItem.pen() if hasattr(targetItem, 'pen') else QPen()
            if pen.width() > 1:
                targetItem.setPen(QPen(Qt.GlobalColor.transparent))
            else:
                pen.setWidth(5)
                pen.setColor(Qt.GlobalColor.red)
                targetItem.setPen(pen)

if __name__ == "__main__":
    app = QApplication([])
    window = SceneWindow()
    window.show()
    app.exec()
