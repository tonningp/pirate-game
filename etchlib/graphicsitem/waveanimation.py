#!/usr/bin/env python3
from etchlib.graphicsitem import svg
import math
from PyQt5.QtCore import(
    Qt,
    QRectF,
    QPointF,
    QObject,
    pyqtSlot
)

from PyQt5.QtGui import (
    QBrush, 
    QFont,
    QPen,
    QPainter, 
    QPainterPath,
    QPixmap
)
from PyQt5.QtWidgets import (
    QGraphicsObject,
    QGraphicsTextItem
    )

class Ship(svg.Item):
    def __init__(self,file,scale,parent=None):
        super(Ship,self).__init__(file,scale,parent)

    def moveTo(self,point):
        self.setPos(point.x()-self.boundingRect().width()/2*self.scale,point.y()-self.boundingRect().height()/1.1*self.scale)

    def paint(self, painter, option, widget):
        super(Ship,self).paint(painter,option,widget)
#        r = self.boundingRect()

class WaveAnimation(QGraphicsObject):
    width = 1200
    height = 400
    BoundingRect = QRectF(-width/2,-height/2,width,height)
    def __init__(self,parent=None):
        super(WaveAnimation, self).__init__()
        self.ship1 = Ship(":/images/Pirate-ship.svg",0.6,self)
        self.ship1.movable()
        self.r = self.boundingRect()
        self.ship1.moveTo(QPointF(self.r.left(),self.r.center().y()))
        self.wavePath = QPainterPath()
        #self.fn = math.sin
        self.fn = lambda x: 2 * math.sin(x*2)
        color = Qt.blue
        self.color = color
        self.xres = 1.67
        self.yres = 100
        self.start = 0
        self.currentTick = self.start
        lastPoint = QPointF(self.r.left(),-1*self.yres * self.fn(self.start))
        self.period = 720
        self.currentTick = 0
        self.factor = 1
        for d in range(self.start,self.period):
            self.wavePath.moveTo(lastPoint)
            nextPoint = QPointF(self.r.left() + self.xres * d,-1*self.yres * self.fn(d*math.pi/180.0))
            self.wavePath.lineTo(nextPoint)
            lastPoint = nextPoint

    def boundingRect(self):
        return WaveAnimation.BoundingRect

    def movable(self,m=True):
        self.setFlag(WaveAnimation.ItemIsMovable,m)
        return self

    @pyqtSlot(int)
    def updateTick(self,spin):

   #     if direction == 1:
   #         mult = 1
   #     else:
   #         mult = -1
        #self.ship1.moveTo(QPointF(self.r.left() + self.xres * self.factor*spin*15,-1*self.yres * self.fn(self.factor*spin*15*math.pi/180.0)))
        self.ship1.moveTo(QPointF(self.r.left() + self.xres * spin*15+5,-1*self.yres * self.fn((spin*15+5)*math.pi/180.0)))
   #     self.currentTick += mult * direction
   #     if self.currentTick > 720:
   #         self.currentTick = 0
        if spin >= 23:
            if self.factor == 1:
                self.factor = 2
            else:
                self.factor = 1
        self.update()

    def paint(self, painter, option, widget):
        r = self.boundingRect()
        painter.setPen(QPen(Qt.blue,15))
        #painter.drawRect(r)
        #painter.drawLine(QPointF(r.left(),r.center().y()),QPointF(r.right(),r.center().y()))
        painter.drawPath(self.wavePath)
