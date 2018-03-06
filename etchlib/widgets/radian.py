#radian.py
import math
import random
from PyQt5.QtCore import(
    Qt,
    QRectF,
    QPointF,
    QPoint,
    pyqtSignal,
    pyqtSlot
)
from PyQt5.QtGui import(
    QFont,
    QPen,
    QBrush,
    QColor
)
from PyQt5.QtWidgets import (
    QGraphicsObject,
    QGraphicsTextItem
    )

class Spinner(QGraphicsObject):
    tickSignal = pyqtSignal(int)

    #BoundingRect = QRectF(-width/2,-height/2,width,height)
    def __init__(self,w=1000,scale=1.0,parent=None):
        super(Spinner, self).__init__()
        self.w = w
        self.rect = self.boundingRect()
        self.center = self.rect.center()
        self.radius = self.rect.width()/2
        self.currentValue = 0
        self.setAcceptHoverEvents(True)

    def onLeftClick(self,f):
        if not hasattr(self,'leftClickF'):
            self.leftClickF = []
        self.leftClickF.append(f)
        return self

    def onRightClick(self,f):
        if not hasattr(self,'rightClickF'):
            self.rightClickF = []
        self.rightClickF.append(f)
        return self

    def leftClick(self,event):
        self.currentClickPosition = event.pos()

    def rightClick(self,event):
        #self.currentClickPosition = QPointF(event.pos().x(),-event.pos().y())
        self.currentClickPosition = event.pos()

    def hoverMoveEvent(self,event):
        self.currentHoverPosition = event.pos()
        super().hoverMoveEvent(event)
        self.update()

    def mouseMoveEvent(self,event):
        self.currentMovePosition = event.pos()
        super().mouseMoveEvent(event)
        self.update()

    def mousePressEvent(self,event):
        if event.button() == Qt.LeftButton:
            self.leftClick(event)
            if hasattr(self,'leftClickF'):
                for f in self.leftClickF:
                    f(event)
        if event.button() == Qt.RightButton:
            self.rightClick(event)
            if hasattr(self,'rightClickF'):
                for f in self.rightClickF:
                    f(event)
        super().mousePressEvent(event)
        self.update()

    def valueChanged(self,value):
        self.currentValue = value
        self.update()

    def toRad(self,deg):
        return deg*math.pi/180
        
    def boundingRect(self):
        return QRectF(-self.w/2,-self.w/2,self.w,self.w)

    def movable(self,m=True):
        self.setFlag(QGraphicsObject.ItemIsMovable,m)
        return self

    def selectable(self,m=True):
        self.setFlag(QGraphicsObject.ItemIsSelectable,m)
        return self

    def paint(self, painter, option, widget):
        painter.setBrush(Qt.white)
        painter.drawEllipse(self.rect)
        painter.setPen(QPen(QColor('SlateBlue'), 1, Qt.DotLine, Qt.RoundCap, Qt.RoundJoin))
        painter.drawLine(self.center.x()-self.radius,
        				self.center.y(),
        				self.center.x()+self.radius,self.center.y())
        painter.drawLine(self.center.x(),
        				self.center.y()+self.radius,
        				self.center.x(),self.center.y()-self.radius)
        painter.setPen(QPen(QColor('BlueViolet'), 2))
        painter.drawLine(self.center.x(),
                        self.center.y(),
                        self.center.x()+(math.cos(self.currentValue)*self.radius),
                        self.center.y()-(math.sin(self.currentValue)*self.radius))
        painter.setPen(QColor('DarkBlue'))
        painter.drawLine(self.center.x(),
                        self.center.y(),
                        self.center.x()+(math.cos(self.currentValue)*self.radius),
                        self.center.y())
        painter.setPen(QPen(QColor('DarkGreen'), 1))
        painter.drawLine(self.center.x()+(math.cos(self.currentValue)*self.radius),
                         self.center.y()-(math.sin(self.currentValue)*self.radius),
                         self.center.x()+(math.cos(self.currentValue)*self.radius),
                         self.center.y()
                         )
        painter.setBrush(QBrush(QColor('SteelBlue')))
        painter.drawEllipse(QRectF(self.center.x()+(math.cos(self.currentValue)*self.radius)-20,
                         self.center.y()-(math.sin(self.currentValue)*self.radius)-10,
                         20,
                         20)
                         )

        # if hasattr(self,'currentHoverPosition'):
        #     size = self.radius * .05
        #     painter.setBrush(Qt.blue)
        #     origin_x = -self.w/2
        #     origin_y = -self.w/2
        #     print(self.currentHoverPosition)
        #     painter.drawEllipse(QRectF(math.cos(self.currentHoverPosition.x()-origin_x)*self.radius,
        #                                math.sin(self.currentHoverPosition.y()-origin_y)*self.radius,size,size))
        if hasattr(self,'currentClickPosition'):
            size = self.radius * .05
            painter.setBrush(Qt.red)
            painter.drawEllipse(QRectF(self.currentClickPosition.x()-size/2,
                                        self.currentClickPosition.y()-size/2,size,size))
