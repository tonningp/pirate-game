#!/usr/bin/env python3
from etchlib.graphicsitem import svg
from PyQt5.QtCore import(
    Qt,
    QRectF,
    QPointF,
    pyqtSignal
)
from PyQt5.QtWidgets import (
    QGraphicsTextItem
)
from PyQt5.QtGui import(
    QFont
)

class Item(svg.Item):
    def __init__(self,file,scale=1.0,parent=None):
        super(Item, self).__init__(file,scale,parent)
        self.text = QGraphicsTextItem("",self)
        self.text.setFont(QFont("Comic Sans MS", 24))
        center = self.boundingRect().center()
        center.setX(center.x()-40)
        center.setY(center.y()-250)
        self.text.setPos(center)
        self.text.setDefaultTextColor(Qt.white)
        self.text.setScale(4)
        self.text.setZValue(999)
        self.selected = False
        self.color = Qt.red
        self.points = 0
        self.onLeftClick(self.setTrue)
        self.onRightClick(self.setFalse)
        self.watch = []
        self.clicked = False

    def addPoint(self):
        self.points += 1
        self.text.setPlainText("{0}".format(self.points))

    def setTrue(self,event):
        if not self.clicked:
            self.setSelected(True)
            for w in self.watch:
                w.clicked = True
            self.clicked = True
        self.update()

    def setFalse(self,event):
        self.setSelected(False)
        self.update()

    def getPoints(self):
        return self.points

    def setColor(self,color):
        self.color = color

    def setSelected(self,value):
        self.selected = value

    def addWatch(self,b):
        self.watch.append(b)
        
    def reset(self):
        self.selected = False
        self.clicked = False 
        self.points = 0
        self.text.setPlainText("")
        for w in self.watch:
            w.clicked = False
        self.update()

    def paint(self,painter,widget,options):
        if self.selected:
            painter.setBrush(self.color)
            painter.drawEllipse(self.boundingRect())
        super(Item,self).paint(painter,widget,options)
        #if self.points:
        #   painter.drawText(self.boundingRect().center(),"{0}".format(self.points))
