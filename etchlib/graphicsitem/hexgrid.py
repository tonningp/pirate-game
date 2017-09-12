#!/usr/bin/env python3
import math

from PyQt5.QtCore import *
from PyQt5.QtGui import (
        QPainter, 
        QColor,
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

class Item(QGraphicsObject):

    changeOrigin = pyqtSignal(object)

    def __init__(self,drawGrid=False,BoundingRect=QRectF(-600,-600,600,600),gridWidth=50,parent=None):
        super(Item, self).__init__(parent)
        self.drawGrid = drawGrid
        Item.BoundingRect = BoundingRect
        Item.gridWidth = gridWidth
        Item.Block = QRectF(-gridWidth,-gridWidth,gridWidth,gridWidth)
        self.tiles = []
        self.origin = None
        """
        self.setFlag(QGraphicsObject.ItemIsMovable,True)
        self.setFlag(QGraphicsObject.ItemIsSelectable,True)
        self.setFlag(QGraphicsObject.ItemSendsScenePositionChanges,True)
        """
   
    def addTile(self,tile):
        self.tiles.append(tile)
        self.scene().addItem(tile)
        return self

    def block(self):
        return Item.Block

    def boundingRect(self):
        return Item.BoundingRect

    def center(self):
        return Item.BoundingRect.center()

    def itemChange(self,change,value):
        if change == QGraphicsItem.ItemPositionChange and self.scene():
            self.scene().update()
        return super(Item,self).itemChange(change,value)
    
    def mousePressEvent(self,event):
        self.pressed = True
        self.update()
        return super(Item,self).mousePressEvent(event)

    def mouseReleaseEvent(self,event):
        self.pressed = False
        return super(Item,self).mouseReleaseEvent(event)

    def setOrigin(self,origin):
        self.origin = origin
        self.changeOrigin.emit(self.origin)
        return self

    def getOrigin(self,origin):
        return self.origin

    def drawGrid(self,painter):
        #start = QPointF(self.center().x() -
        #        self.center().x()/2,self.center().y() - self.center().y()/2)
        gridWidth = self.tiles[0].width()
        gridHeight = self.tiles[0].height()
        start = QPointF(self.boundingRect().left(),self.boundingRect().top())
        left = start.x()
        top = start.x()
        rows = Item.BoundingRect.height()/(gridHeight/4)
        cols = Item.BoundingRect.width()/(gridWidth/4)
        right = self.boundingRect().right()
        bottom = self.boundingRect().bottom()
        #print('rows='+str(Item.rows))
        #print('cols='+str(Item.rows))
        for row in range(int(rows)):
            line =\
                QLineF(QPointF(left,top+gridHeight/4*row),QPointF(0,top+gridHeight/4*row))
            if row % 4 == 0:
                painter.setPen(QPen(Qt.black,0.5,Qt.DashLine))
            else:
                painter.setPen(QPen(Qt.black,0.5,Qt.DotLine))
            painter.drawLine(line)
        for col in range(int(cols)):
            line =\
                QLineF(QPointF(left+gridWidth/4*col,top),QPointF(left+gridWidth/4*col,bottom))
            if col % 4 == 0:
                painter.setPen(QPen(Qt.black,0.5,Qt.DashLine))
            else:
                painter.setPen(QPen(Qt.black,0.5,Qt.DotLine))
            painter.drawLine(line)

    def paint(self, painter, option, widget):
        if self.drawGrid:
            painter.setPen(QPen(Qt.black,1,Qt.DotLine))
            painter.drawRect(self.boundingRect())
            if len(self.tiles):
                self.drawGrid(painter)
