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
    def __init__(self,scale=1.0,parent=None):
        super(Item, self).__init__(":/images/Treasure_chest.svg",scale,parent)
        self.text = QGraphicsTextItem("",self)
        self.text.setFont(QFont("Comic Sans MS", 24))
        center = self.boundingRect().center()

    def paint(self,painter,widget,options):
        painter.setBrush(self.color)
        painter.drawEllipse(self.boundingRect())
        super(Item,self).paint(painter,widget,options)
