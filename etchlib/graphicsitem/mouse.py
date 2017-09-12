#!/usr/bin/env python3
import math
from PyQt5.QtCore import *
from PyQt5.QtGui import (QPainter, QColor,
QPen,QIcon,QBrush,QPixmap,QPainterPath,QImage,QFont,QFontMetrics)
from PyQt5.QtWidgets import (QWidget,QAction, QLCDNumber, QSlider, 
    QApplication,QMainWindow,QPushButton,QFrame,
    QGridLayout,QVBoxLayout, 
    QLabel,QSizePolicy,QGraphicsScene,QGraphicsView,
    QGraphicsTextItem,QGraphicsItem,QGraphicsObject,QGraphicsPixmapItem,
    QGraphicsProxyWidget,
    QMessageBox,
    QLineEdit,QFormLayout,QGroupBox,
    QRadioButton,QButtonGroup,QComboBox,QSizePolicy,
    QDialog)
from PyQt5.QtSvg import QGraphicsSvgItem,QSvgRenderer

from etchlib.dialogs import QuestionDialog




class Item(QGraphicsObject):
    Pi = math.pi
    TwoPi = 2.0 * Pi

    # Create the bounding rectangle once.
    adjust = 0.5
    BoundingRect = QRectF(-20 - adjust, -22 - adjust, 40 + adjust, 83 + adjust)
    showBoundingRect = True
    moved = pyqtSignal(object)
    name = 'mouse'
    
    def __init__(self):
        super(Item, self).__init__()
        self.angle = 0.0
        self.speed = 0.0
        self.mouseEyeDirection = 0.0
        self.resetColor()

    def resetColor(self):
        self.color = QColor(qrand() % 256, qrand() % 256, qrand() % 256)

    def boundingRect(self):
        return Item.BoundingRect
   
    def collidesWith(self,item):
        return item in self.scene().collidingItems(self)

    def inCollidingItem(self,item):
        return self.collidingItems(item)

    def getNoseInMaze(self,maze):
        return maze.mapFromItem(self,self.noseCenter())

    def isWallPixel(self,pixel):
        return self.scene().mazeimage.valid(pixel.x(),pixel.y()) \
                and self.scene().mazeimage.pixel(pixel.x(),pixel.y()) != 0

    def hitsWall(self,scene):
        nose = self.getNoseInMaze(self.scene().maze)
        point = QPoint(nose.x() * self.scene().SCALE,nose.y() * self.scene().SCALE)
        return self.isWallPixel(point)

    def shape(self):
        path = QPainterPath()
        path.addRect(-10, -20, 20, 40)
        return path;

    def noseCenter(self):
        return QPointF(-2,-22)

    def paint(self, painter, option, widget):
        # Body.
        painter.setBrush(self.color)
        painter.drawEllipse(-10, -20, 20, 40)

        # Eyes.
        painter.setBrush(Qt.white)
        painter.drawEllipse(-10, -17, 8, 8)
        painter.drawEllipse(2, -17, 8, 8)

        # Nose.
        painter.setBrush(Qt.black)
        painter.drawEllipse(QRectF(-2, -22, 4, 4))

        # Pupils.
        painter.drawEllipse(QRectF(-8.0 + self.mouseEyeDirection, -17, 4, 4))
        painter.drawEllipse(QRectF(4.0 + self.mouseEyeDirection, -17, 4, 4))

        # Ears.
        if self.scene().collidingItems(self):
            painter.setBrush(Qt.red)
        else:
            painter.setBrush(Qt.darkYellow)

        painter.drawEllipse(-17, -12, 16, 16)
        painter.drawEllipse(1, -12, 16, 16)

        # Tail.
        path = QPainterPath(QPointF(0, 20))
        path.cubicTo(-5, 22, -5, 22, 0, 25)
        path.cubicTo(5, 27, 5, 32, 0, 30)
        path.cubicTo(-5, 32, -5, 42, 0, 35)
        painter.setBrush(Qt.NoBrush)
        painter.drawPath(path)
        if self.showBoundingRect:
            painter.drawRect(self.boundingRect())
            painter.drawPath(self.shape())
        #painter.drawText(5,5,"mouse")

    def move(self,pos):
        self.setPos(pos)
        self.moved.emit(self)
        if self.scene():
            for obj in self.scene().collidingItems(self):
                if hasattr(obj,'mouseCollision') and obj.mouseCollision \
                   and not obj.questionAnswered:
                    obj.questionAnswered = True




