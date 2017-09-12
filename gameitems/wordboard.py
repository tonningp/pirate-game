#!/usr/bin/env python3

from PyQt5.QtCore import(
    Qt,
    QRectF,
    QPointF
)

from PyQt5.QtWidgets import (
    QGraphicsObject,
    QGraphicsTextItem
    )

from PyQt5.QtGui import(
    QFont
)

class Letter(QGraphicsTextItem):
    def __init__(self,letter,parent):
        super(Letter,self).__init__(letter,parent)
        self.setFont(QFont("Helvetica [Cronyx]", 36))
        self.setToolTip(letter)

    def movable(self,m=True):
        self.setFlag(Letter.ItemIsMovable,m)
        return self

    def paint(self, painter, option, widget):
        super(Letter,self).paint(painter,option,widget)
        painter.drawRect(self.boundingRect())

class WordBoard(QGraphicsObject):
    BoundingRect = QRectF(0,0,800,300)
    def __init__(self,phrase,parent=None):
        super(WordBoard, self).__init__()
        self.letters = []
        for p in phrase:
            lastPos = QPointF(0,0)
            index = 0
            for l in phrase[p]:
                letter = Letter(l,self)
                width = letter.boundingRect().width()
                letter.movable(True)
                self.letters.append(letter)
                letter.setPos(QPointF(lastPos.x()+5,lastPos.y()))
                index += 1
                lastPos = QPointF(letter.pos().x() + width,letter.pos().y())
        self.setFlag(QGraphicsObject.ItemIsMovable,True)

    def boundingRect(self):
        return WordBoard.BoundingRect

    def paint(self, painter, option, widget):
        painter.drawRect(self.boundingRect())
