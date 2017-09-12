#!/usr/bin/env python3
import math

from PyQt5.QtCore import *
from PyQt5.QtGui import (
        QPainter, 
        QColor,
        qRgb,
        QPen,
        QIcon,
        QBrush,
        QPixmap,
        QPainterPath,
        QImage,
        QFont,
        QPolygon,
        QPolygonF,
        QFontMetrics
        )
from PyQt5.QtWidgets import (
        QGraphicsObject,
        QGraphicsItem
)
from etchlib.defaults import colors
class Item(QGraphicsObject):
    """
http://www.redblobgames.com/grids/hexagons

    """
    defaultBrushColor = QColor(colors['Moccasin']) 
    enterBrushColor = QColor(colors['LightSeaGreen']) 
    selectedBrush = QColor(colors['LightBlue']) 
    originBrush = QColor(colors['LightCoral']) 
    ADJUST = 0.085
    hoverEnter = pyqtSignal(object)
    hoverLeave = pyqtSignal(object)
    changeOrigin = pyqtSignal(object)

    def __init__(self,
            oid,
            grid,
            orient='pointy',
            cubeline=True,
            outline=False,
            parent=None):
        super(Item, self).__init__(parent)
        self.oid = oid
        self.grid = grid
        self.cubeline=cubeline
        self.outline = outline
        Item.BoundingRect = grid.block()
        self.points_method = getattr(self,orient+'HexCorner')
        self.size = self.boundingRect().width()/2
        Item.polygon = QPolygonF(self.points())
        #self.setFlag(QGraphicsObject.ItemIsMovable,True)
        #self.setFlag(QGraphicsObject.ItemSendsScenePositionChanges,True)
        self.setFlag(QGraphicsObject.ItemIsSelectable,True)
        self.setAcceptHoverEvents(True)
        self.pressed = False
        self.currentPolyBrush = Item.defaultBrushColor
        self.origin = None

    def __call__(self):
        return QPolygonF(self.polygon)

    def setOrigin(self,origin):
        self.origin = origin

    def isOrigin(self):
        return self.origin == self

    def boundingRect(self):
        return Item.BoundingRect
   
    def center(self):
        return Item.BoundingRect.center()

    def points(self):
        return [self.points_method(self.boundingRect().center(),self.size,i)
                             for i in range(6)]

    def getAngle(self,i):
        angle_deg = 60 * i   + 30
        return math.pi / 180 * angle_deg
    
    def height(self):
        return self.size * 2.0

    def width(self):
        return math.sqrt(3)/2.0 * self.height()

    def pointyHexCorner(self,center, size, i):
        angle_rad = self.getAngle(i)
        x = round(center.x() + size * math.cos(angle_rad))
        y = round(center.y() + size * math.sin(angle_rad))
        return QPointF(x,y)

    def flatHexCorner(self,center, size, i):
        angle_rad = self.getAngle(i)
        x = round(center.x() + size * math.sin(angle_rad))
        y = round(center.y() + size * math.cos(angle_rad))
        return QPointF(x,y)

    def itemChange(self,change,value):
        if change == QGraphicsItem.ItemPositionChange and self.scene():
            self.scene().update()
        return super(Item,self).itemChange(change,value)
    
    def hoverEnterEvent(self,event):
        self.currentPolyBrush = Item.enterBrushColor
        self.update()
        self.hoverEnter.emit(self)
        return super(Item,self).hoverEnterEvent(event)

    def hoverLeaveEvent(self,event):
        self.currentPolyBrush = Item.defaultBrushColor
        self.update()
        self.hoverLeave.emit(self)
        return super(Item,self).hoverLeaveEvent(event)

    def mouseDoubleClickEvent(self,event):
        self.changeOrigin.emit(self)

    def mousePressEvent(self,event):
        self.pressed = True
        if event.button() == Qt.RightButton:
            self.currentPolyBrush = QColor(colors['MedAquamarine'])
        self.update()
        return super(Item,self).mousePressEvent(event)

    def mouseReleaseEvent(self,event):
        self.pressed = False
        self.update()
        return super(Item,self).mouseReleaseEvent(event)

    def shape(self):
        path = QPainterPath()
        path.addPolygon(Item.polygon)
        return path;

    def coords(self):
        return (self.col - self.origin.col,self.row - self.origin.row)

    def isOdd(self,row):
        return row % 2

    def setToGrid(self,col,row):
        self.col = col
        self.row = row
        rect = self.grid.boundingRect()
        adjustWidth = Item.ADJUST*self.width()

        if self.isOdd(row):
            start = \
            QPointF(rect.left()+self.width()+adjustWidth,rect.top()+self.height())
        else:
            start = \
            QPointF(rect.left()+self.width()/2+adjustWidth,rect.top()+self.height())

        delta = QPointF(col*self.width(),row*3*self.height()/4)
        pos  = \
        self.mapToItem(self.grid,start+delta)
        #print("{},{}".format(pos.x(),pos.y()))
        self.setPos(self.mapToScene(pos))

    def drawPoints(self,qp):
        qp.setPen(Qt.red)
        for p in self.points():
            qp.drawPoint(p.x(), p.y())

    def printPoints(self):
        for p in self.points():
            print(p)

    def drawPos(self,painter):
        painter.setPen(Qt.black)
        painter.setFont(QFont("Helvetica",5,QFont.Bold))
        width = self.boundingRect().width()
        height = self.boundingRect().height()
        start = self.center() \
                - QPointF(width/2 - (.10 * width),0.20*height) #self.boundingRect().height()/2)
        painter.drawText(start,"({0:.2f},{1:.2f})".format(self.pos().x(),self.pos().y()))
        painter.drawText(start-QPointF(0,.10*height),"({0:.2f},{1:.2f})".format(self.center().x(),self.center().y()))
        painter.setPen(Qt.black)
        painter.setFont(QFont("Helvetica",5,QFont.Bold))
        painter.drawText(self.center(),str(self.oid))

    def paint(self, painter, option, widget):
        if self.outline:
            painter.setPen(QPen(Qt.red,1,Qt.DotLine))
            painter.drawRect(self.boundingRect())
        if self.isSelected():
            painter.setBrush(self.selectedBrush)
        elif self.isOrigin():
            painter.setBrush(self.originBrush)
        else:
            painter.setBrush(self.currentPolyBrush)
        painter.setPen(Qt.blue)
        painter.drawPolygon(Item.polygon)
        #painter.drawEllipse(self.center(),1,1)
        if self.cubeline:
            if self.isSelected() or self.isOrigin():
                painter.setPen(QPen(Qt.black,1,Qt.DotLine))
            else:
                painter.setPen(QPen(Qt.gray,1,Qt.DotLine))
            painter.drawLine(self.points()[1],self.center())
            painter.drawLine(self.points()[3],self.center())
            painter.drawLine(self.points()[5],self.center())



# Notes:
# http://www.redblobgames.com/grids/hexagons/
